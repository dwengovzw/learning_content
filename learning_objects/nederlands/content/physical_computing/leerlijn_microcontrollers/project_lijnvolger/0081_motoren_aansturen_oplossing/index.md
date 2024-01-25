---
hruid: leerlijn_project_lijnvolger_motoren_aansturen_oplossing
version: 1
language: nl
title: "Motoren aansturen (oplossing)"
description: "Hoe stuur ik dc-motoren aan."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "motoren", "dc-motor"]
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Motoren aansturen (oplossing)

Hieronder zie je oplossing van de opdracht om de lijvolger rechtdoor te laten rijden. Merk op het het mogelijk is dat de motoren met deze code niet in de juiste richting draaien. In dat geval kan je een van de snelheden negatief maken of de draadjes van de motor omdraaien.

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

    #include <Dwenguino.h>
    #include <DwenguinoMotor.h>

    // Definieer het aantal sensoren
    #define AANTAL_SENSOREN 6
    // Sla op op welke pinnen de sensoren zijn aangesloten.
    unsigned char sensorPinnen[AANTAL_SENSOREN] = {A0, A1, A2, A3, A4, A5};
    // Maak een array om de waarden van de sensoren in op te slaan.
    int sensorWaarden[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};
    float sensorKalibratieHoog[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};
    float sensorKalibratieLaag[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};

    // Maak voor elke motor een object en stel de juiste pinnen in.
    DCMotor dcMotor1(MOTOR_1_0, MOTOR_1_1);
    DCMotor dcMotor2(MOTOR_2_0, MOTOR_2_1);

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
        printStringsToLCD("Kalibratie is", "voltooid!");
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
        for (char i = 0 ; i <= AANTAL_SENSOREN ; ++i){
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
        // Stuur de waarde door in csv formaat.
        Serial1.println(
            String(sensorWaarden[0]) + ";" +
            String(sensorWaarden[1]) + ";" +
            String(sensorWaarden[2]) + ";" +
            String(sensorWaarden[3]) + ";" +
            String(sensorWaarden[4]) + ";" +
            String(sensorWaarden[5]));

        // Laat de robot vooruit rijden
        dcMotor1.setSpeed(100);
        dcMotor2.setSpeed(100);

        delay(500);
    }

</code>
    </pre>
</div>

