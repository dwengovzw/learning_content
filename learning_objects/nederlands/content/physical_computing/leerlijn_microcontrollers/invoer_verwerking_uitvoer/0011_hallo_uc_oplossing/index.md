---
hruid: leerlijn_invoer_verwerking_uitvoer_hallo_uc_opl
version: 1
language: nl
title: "Hallo µC (oplossing)"
description: "Beschrijving van wat er aan bod komt in het leerpad over invoer, verwerking en uitvoer."
keywords: ["invoer", "verwerking", "uitvoer", "microcontroller", "µC", "arduino", "dwenguino"]
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

# Hallo µC (oplossing)

De fiches voor deze opdracht kan je vinden in de leerpaden *Fiches Dwenguino* of *Fiches Arduino*. Het leerpad dat je kiest is afhankelijk van de hardware die je gebruikt. Op de fiches staat telkens informatie over hoe je een component kan aansluiten en programmeren.

Hieronder kan je een voorbeeldoplossing zien voor de opdracht. Merk op dat er zeker variaties op deze oplossing mogelijk zijn. In de commentaar is uitleg voorzien bij de code.

### Oplossing Dwenguino

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

    // Eerst importeren we een aantal bibliotheken.
    #include <Wire.h>       // Basisfuncties communicatie
    #include <Dwenguino.h>  // Basisfuncties Dwenguino
    #include <NewPing.h>    // Bibliotheek van de sonarsensor

    // Definities 
    #define TRIGGER_PIN 11
    #define ECHO_PIN 12
    #define MAX_DISTANCE 200

    // Sonar object om afstand te meten.
    NewPing sonar = NewPing(
        TRIGGER_PIN,
        ECHO_PIN,
        MAX_DISTANCE);
    // Variabele om de afstand in op te slaan.
    int afstand;

    // Zet klaar -> een keer bij start programma.
    void setup(){
        initDwenguino();
        pinMode(13, OUTPUT);
    }

    // Herhaal blijft herhalen tot je stroom uittrekt.
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


<br>

### Oplossing Arduino

<div class="dwengo-content">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

    // Eerst importeren we een aantal bibliotheken.
    #include <Wire.h>       // Basisfuncties communicatie
    #include <NewPing.h>    // Bibliotheek van de sonarsensor

    // Definities 
    #define TRIGGER_PIN 11
    #define ECHO_PIN 12
    #define MAX_DISTANCE 200

    // Sonar object om afstand te meten.
    NewPing sonar = NewPing(
        TRIGGER_PIN,
        ECHO_PIN,
        MAX_DISTANCE);
    // Variabele om de afstand in op te slaan.
    int afstand;

    // Zet klaar -> een keer bij start programma.
    void setup(){
        pinMode(13, OUTPUT);
    }

    // Herhaal blijft herhalen tot je stroom uittrekt.
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