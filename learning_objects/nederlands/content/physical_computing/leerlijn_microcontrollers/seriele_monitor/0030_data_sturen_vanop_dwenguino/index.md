---
hruid: leerlijn_microcontrollers_seriele_monitor_data_sturen
version: 1
language: nl
title: "Gegevens sturen vanop de Dwenguino"
description: "Hoe stuur je gegevens over een seriële connectie vanop de Dwenguino?"
keywords: ["seriële communicatie", "seriële monitor", "dwenguino", "robot", "project", "µC", "pid", "controletheorie"]
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
teacher_exclusive: false
---

# Sturen vanop de Dwenguino

Hieronder zie je een voorbeeldprogramma die de waarden van een sinusgolf doorstuurt over de seriële verbinding.

<div class="dwengo-content dwengo-code-simulator">
<pre>
<code class="language-arduino">

    #include <Wire.h>
    #include <Dwenguino.h>
    #include <LiquidCrystal.h>

    // We gaan de teller elke halve seconde met één verhogen.
    int teller = 0;

    void setup()
    {
    initDwenguino();
    // Stel de baud rate in van de connectie.
    // Dit legt vast hoe snel de Dwenguino gegevens zal sturen.
    Serial.begin(9600);
    while (!Serial) {
        ; // Wacht tot er op de computer verbinding wordt gemaakt.
    }
    }


    void loop()
    {
        // Druk de waarde van de teller af op het lcd-scherm.
        dwenguinoLCD.setCursor(0,0);
        dwenguinoLCD.print(String(teller));

        // Stuur de sinus van de waarde van teller door naar de Dwenguino.
        Serial.println(sin(teller));

        // Wacht een halve seconde
        delay(500);

        // Maak het lcd-scherm leeg
        dwenguinoLCD.clear();

        // Verhoog teller met 1.
        teller++;
    }
</code>
</pre>

Je kan het programma openen in de Dwengo simulator, compileren en overzetten naar de Dwenguino. Op die manier kan je straks waarden lezen via de seriële monitor.