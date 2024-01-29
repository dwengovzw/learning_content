---
hruid: leerlijn_project_lijnvolger_pid_oplossing
version: 1
language: nl
title: "PID regeling (oplossing)"
description: "Hoe programmeer ik een pid regeling."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "pid"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16]
difficulty: 1
estimated_time: 15
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# PID regeling (oplossing)

Hieronder zie je de volledige applicatie met P regeling.

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
            
    #include <Dwenguino.h>
#include <DwenguinoMotor.h>

// Tel iteraties van de hoofdlus
long iters = 0;

// Definieer het aantal sensoren
#define AANTAL_SENSOREN 6
// Sla op op welke pinnen de sensoren zijn aangesloten.
unsigned char sensorPinnen[AANTAL_SENSOREN] = {A0, A1, A2, A3, A4, A5};
// Maak een array om de waarden van de sensoren in op te slaan.
float sensorWaarden[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};
float sensorKalibratieHoog[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};
float sensorKalibratieLaag[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};

// Maak voor elke motor een object en stel de juiste pinnen in.
DCMotor dcMotor1(MOTOR_1_0, MOTOR_1_1);
DCMotor dcMotor2(MOTOR_2_0, MOTOR_2_1);

// Parameters voor PID regeling
float proportie = 0;
float Kp = 15;
float integraal = 0;
float Ki = 0;
float derivative = 0;
float vorigeFout =  0;
float Kd = 0;
int basisMotorSnelheid = 65;

void printStringsToLCD(String lijn1, String lijn2){
    dwenguinoLCD.clear();
    dwenguinoLCD.setCursor(0,0);
    dwenguinoLCD.print(lijn1);
    dwenguinoLCD.setCursor(0,1);
    dwenguinoLCD.print(lijn2);
}

// Sla een referentiewaarde op voor het huidige oppervlak.
void kalibreerReferentiepunt(float* kalibratieReferentiePunten){
    // Lees een eerste sensorwaarde voor elke sensor
    for (unsigned char i = 0 ; i < AANTAL_SENSOREN ; ++i){
        kalibratieReferentiePunten[i] = (float)analogRead(sensorPinnen[i]);
    }
    // Lees meerdere waarden tot op de E knop wordt gedrukt.
    // Bereken exponentieel gemiddelde.
    while (digitalRead(SW_E) == HIGH){
        for (unsigned char i = 0 ; i < AANTAL_SENSOREN ; ++i){
            kalibratieReferentiePunten[i] = (float)analogRead(sensorPinnen[i]) * 0.95 + kalibratieReferentiePunten[i] * 0.05;
        }
    }
    delay(500); // Debounce
}

// Start de kalibratieprocedure
void kalibreer(){
    printStringsToLCD("Naar zwart", "E -> Ga verder");
    while (digitalRead(SW_E) == HIGH){
        // Wacht tot de oost knop wordt ingedrukt.
    }
    delay(500); // Debounce knop

    printStringsToLCD("Zwart kalibreren", "E -> Ga verder");
    // Kalibreer waarde zwart
    kalibreerReferentiepunt(sensorKalibratieHoog);

    printStringsToLCD("Naar wit", "E -> Ga verder");
    while (digitalRead(SW_E) == HIGH){
        // Wacht tot de oost knop wordt ingedrukt.
    }
    delay(500); // Debounce

    printStringsToLCD("Wit kalibreren", "E -> Ga verder");
    // Kalibreer waarde wit
    kalibreerReferentiepunt(sensorKalibratieLaag);

    // Stuur data naar  computer
    Serial1.println("TOP: " + String(sensorKalibratieHoog[0]) + ";"  + String(sensorKalibratieHoog[1]) + ";"  + String(sensorKalibratieHoog[2]) + ";"  + String(sensorKalibratieHoog[3]) + ";"  + String(sensorKalibratieHoog[4]) + ";"  + String(sensorKalibratieHoog[5]));
    Serial1.println("BOTTOM: " + String(sensorKalibratieLaag[0]) + ";"  + String(sensorKalibratieLaag[1]) + ";"  + String(sensorKalibratieLaag[2]) + ";"  + String(sensorKalibratieLaag[3]) + ";"  + String(sensorKalibratieLaag[4]) + ";"  + String(sensorKalibratieLaag[5]));
    printStringsToLCD("Kalibratie Klaar", "E -> START!");
    while (digitalRead(SW_E) == HIGH){
        // Wacht tot de oost knop wordt ingedrukt.
    }
    printStringsToLCD("GO!", "");
}

void leesSensorWaarden(){
    // Overloop elke sensor, lees die uit en sla de waarde op.
    for (unsigned char i = 0 ; i < AANTAL_SENSOREN ; ++i){
        sensorWaarden[i] = analogRead(sensorPinnen[i]);
        // Zorg ervoor dat de gemeten waarde nooit hoger is dan de hoge kalibratiewaarde
        if (sensorWaarden[i] > sensorKalibratieHoog[i]){
            sensorWaarden[i] = sensorKalibratieHoog[i];
        }
        // Zorg ervoor dat de gemeten waarde nooit lager is dan de lage kalibratiewaarde
        if (sensorWaarden[i] < sensorKalibratieLaag[i]){
            sensorWaarden[i] = sensorKalibratieLaag[i];
        }
        // Normaliseer
        // Trek de lage kalibratiewaarde af van de meting
        sensorWaarden[i] -= sensorKalibratieLaag[i];
        // Deel door het verschil van de hoge en lage kalibratiewaarde
        sensorWaarden[i] = (float)sensorWaarden[i]/(float)(sensorKalibratieHoog[i] - sensorKalibratieLaag[i]);
    }
}

float berekenFout(){
    float fout = 0; // Veronderstel fout = 0
    float afwijking[AANTAL_SENSOREN] = {-3.0, -2.0, -1.0, 1.0, 2.0, 3.0};
    // Overloop de sensoren, vermenigvuldig de gemeten waarde met de overeenkomstige afwijking en tel op.
    for (char i = 0 ; i < AANTAL_SENSOREN ; ++i){
        fout += afwijking[i] * sensorWaarden[i];
    }
    return fout;
}

void setup()
{
    initDwenguino();
    Serial1.begin(9600);
    kalibreer();
}

void loop()
{
    // Lees elke halve seconde de waarden van de sensoren.
    leesSensorWaarden();

    float meetFout = berekenFout();

    proportie = meetFout;
    integraal = integraal + meetFout;
    derivative = meetFout - vorigeFout;
    vorigeFout = meetFout;

    // Bereken het nieuwe snelheidsverschil
    float snelheidsVerschil = Kp * proportie + Ki * integraal + Kd * derivative;
    // Stel de snelheid van de motoren in
    int snelheidMotor1 = basisMotorSnelheid - (int)snelheidsVerschil;
    int snelheidMotor2 = basisMotorSnelheid + (int)snelheidsVerschil;
    dcMotor1.setSpeed(snelheidMotor1);
    dcMotor2.setSpeed(snelheidMotor2);

    // Stuur om de 100 iteraties telemetrie door.
    if (iters % 100){
        // Stuur de waarde door in csv formaat.
        Serial1.println(
            String(snelheidsVerschil) + ";" +
            String(Kp * proportie) + ";" +
            String(Ki * integraal) + ";" +
            String(Kd * derivative) + ";" +
            String(meetFout) + ";" +
            String(0));
    }
}


</code>
    </pre>
</div>


Wanneer de waarde van \\(\mathrm{K_p}\\) hoger wordt, begint de robot te oscilleren. Er wordt telkens te veel gecompenseerd voor de gemaakte fout. Wanneer de op dat moment \\(\mathrm{K_p}\\) nog verhogen zal de robot voorbij de lijn draaien waardoor deze niet meer in staat zal zijn om de lijn te volgen.

TODO: filmpje oscillatie en overshoot.