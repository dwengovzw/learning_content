---
hruid: leerlijn_project_lijnvolger_kalibratie_oplossing
version: 1
language: nl
title: "Kalibratie (oplossing)"
description: "Hoe kan ik de grondsensoren kalibreren."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "grondsensor", "kalibratie", "calibratie"]
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

# Kalibratie (oplossing)

Hieronder zie je de code voor de lijnvolger. Deze zal eerst de kalibratieprocedure doorlopen en daarna de genormaliseerde sensorwaarden doorsturen naar de computer.



<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="lees_sensoren_en_kalibreer.cpp">

    #include <Dwenguino.h>

    // Definieer het aantal sensoren
    #define AANTAL_SENSOREN 6
    // Sla op op welke pinnen de sensoren zijn aangesloten.
    unsigned char sensorPinnen[AANTAL_SENSOREN] = {A0, A1, A2, A3, A4, A5};
    // Maak een array om de waarden van de sensoren in op te slaan.
    int sensorWaarden[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};
    float sensorKalibratieHoog[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};
    float sensorKalibratieLaag[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};

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
    delay(500);
    }

</code>
    </pre>
</div>


Aan de Python code kan je een eenvoudige conditie toevoegen die controleert wat er met het pakket moet gebeuren.

<pre>
<code class="lang-python">

    # Importeer de pyserial bibliotheek.
    import serial
    # Importeer de matplotlib bibliotheek.
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    # Configureer de seriële poort.
    # Deze instelling hangt af van je computer.
    serial_port = 'COM4'  
    # Stel de baud rate in. Deze moet dezelfde zijn als in je Dwenguino programma.
    baud_rate = 9600     

    # Het huidige tijdstip.
    tijdstip = 0
    # Sla het tijdstip op van een meting.
    tijdstippen = [] 
    # Sla de gemeten waarden op.
    sensorWaarden = []

    # Initialize serial connection.
    ser = serial.Serial(serial_port, baud_rate)

    # Deze functie zet een string in csv formaat om naar een lijst met getallen.
    def parse_data_pakket(pakket):
        data = pakket.strip().split(';')
        return [float(getal) for getal in data]

    def update_plot(frame):
        fig.clear()
        # Plot de gemeten waarden.
        for i in range(0, len(sensorWaarden[0])):
            # Selecteer telkens de i-de waarde van elke meting.
            plt.plot(tijdstippen, [meting[i] for meting in sensorWaarden], label='Waarde sensor ' + str(i))
        plt.xlabel('Tijd')
        plt.ylabel('Gemeten waarde')
        plt.legend()
        plt.title('Verloop van de sensorwaarden doorheen de tijd.')
        
        return plt

    # Maak een figuur aan.
    fig = plt.figure()
    animatie = animation.FuncAnimation(fig, update_plot, interval=1000)

    # Blijf lezen van de seriële poort en print de ontvangen gegevens
    while True:
        print('Wachten op gegevens...')
        line = ser.readline().decode('utf-8').strip() # Lees een lijn van de seriële poort.
        
        if line.startswith('TOP') or line.startswith('BOTTOM'):
            print(line)
        else:
            tijdstippen.append(tijdstip) # Sla het tijdstip op.
            sensorWaarden.append(parse_data_pakket(line)) # Sla de gemeten waarden op.
            tijdstip += 1 # Verhoog het tijdstip met 1.
            
            plt.pause(0.001) # Pauzeer even om de plot te updaten.
    

</code>
</pre>


In je Python programma krijg je dan het volgende resultaat:

<pre>
<code class="lang-bash">

    Wachten op gegevens...
    TOP: 958.00;1003.00;1007.00;1006.00;991.00;931.95
    Wachten op gegevens...
    BOTTOM: 46.00;711.05;729.00;373.00;450.95;66.95

</code>
</pre>