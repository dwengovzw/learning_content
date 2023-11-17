---
hruid: leerlijn_basis_programmeren_basisstructuur
version: 1
language: nl
title: "Basisstructuur"
description: "Basisstructuur van het programma: de setup en loop functies."
keywords: ["programmeren", "setup", "loop", "microcontroller", "µC", "arduino", "dwenguino"]
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
teacher_exclusive: false
---

# Basisstructuur

Om de basisstructuur van een µC-programma uit te leggen, kijken we terug naar ons eerste programma uit het leerpad over invoer, verwerking en uitvoer. Dit programma zorgde ervoor dat led 13 ging branden wanneer de sonarsensor beweging detecteerde. Hieronder zie je die code opnieuw weergegeven. In de commentaar staan de verschillende onderdelen van de code aangeduid.


<div class="dwengo-content code-simulator">
<pre>
<code class="language-arduino dwengo-code-simulator">

    /*
        ONDERDEEL 1: Het koppelen van bibliotheken.
    */
    #include <Wire.h>
    #include <Dwenguino.h>
    #include <LiquidCrystal.h>
    #include <NewPing.h>

    /*
        ONDERDEEL 2: Definiëren van constanten en globale variabelen.
    */
    #define TRIGGER_PIN 11
    #define ECHO_PIN 12
    #define MAX_DISTANCE 200

    NewPing sonar(
        TRIGGER_PIN, 
        ECHO_PIN, 
        MAX_DISTANCE);
    int afstand;

    /*
        ONDERDEEL 3: De setup() functie, 
        deze functie wordt één keer opgeroepen bij de start van je programma.
    */

    void setup(){
        initDwenguino();
        pinMode(13, OUTPUT);
    }

    /*
        ONDERDEEL 4: De loop() functie, 
        deze functie wordt telkens opnieuw opgeroepen 
        tot wanneer het programma stopt.
    */
    void loop(){
        afstand = sonar.ping_cm();
        if (afstand > 0 && afstand < 100){
            digitalWrite(13, HIGH);
        } else {
            digitalWrite(13, LOW);
        }
        delay(100);
    }
</code>
</pre>
</div>


