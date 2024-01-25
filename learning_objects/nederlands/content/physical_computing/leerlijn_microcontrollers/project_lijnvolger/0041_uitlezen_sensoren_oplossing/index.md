---
hruid: leerlijn_project_lijnvolger_uitlezen_sensoren_oplossing
version: 1
language: nl
title: "Uitlezen sensoren"
description: "Hoe kan ik de grondsensoren op de lijvolger uitlezen."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "grondsensor"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Uitlezen sensoren (oplossing)

Op de Dwenguino kan je de data eenvoudig doorsturen door twee lijnen code toe te voegen.

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="sensoren_uitlezen.cpp">

    #include <Dwenguino.h>

    // Definieer het aantal sensoren
    #define AANTAL_SENSOREN 6

    // Sla op op welke pinnen de sensoren zijn aangesloten.
    unsigned char sensorPinnen[AANTAL_SENSOREN] = {A0, A1, A2, A3, A4, A5};
    // Maak een array om de waarden van de sensoren in op te slaan.
    int sensorWaarden[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};

    void leesSensorWaarden(){
    // Overloop elke sensor, lees die uit en sla de waarde op.
    for (unsigned char i = 0 ; i < AANTAL_SENSOREN ; ++i){
        sensorWaarden[i] = analogRead(sensorPinnen[i]);
    }
    }

    void setup()
    {
    initDwenguino(); 
    // Initialiseer de Bluetooth communicatie.
    Serial1.begin(9600);
    }

    void loop()
    {
    // Lees elke halve seconde de waarden van de sensoren.
    leesSensorWaarden();
    // Stuur de waarde door in csv formaat.
    Serial1.println(
        String(sensorValues[0]) + ";" + 
        String(sensorValues[1]) + ";" + 
        String(sensorValues[2]) + ";" + 
        String(sensorValues[3]) + ";" + 
        String(sensorValues[4]) + ";" + 
        String(sensorValues[5]));
    delay(500);
    }
</code>
    </pre>
</div>

Het Python programma om de waarden te lezen en af te drukken is identiek aan het voorbeeld eerder in dit leerpad.

<pre>
<code class="lang-python">

    # Importeer de pyserial bibliotheek
    import serial

    # Configureer de seriële poort
    # Deze instelling hangt af van je computer
    serial_port = 'COM4'  
    # Stel de baud rate in. Deze moet dezelfde zijn als in je Dwenguino programma.
    baud_rate = 9600      

    # Initialize serial connection
    ser = serial.Serial(serial_port, baud_rate)

    # Blijf lezen van de seriële poort en print de ontvangen gegevens
    while True:
        print('Wachten op gegevens...')
        line = ser.readline().decode('utf-8').strip()
        print(line)

</code>
</pre>