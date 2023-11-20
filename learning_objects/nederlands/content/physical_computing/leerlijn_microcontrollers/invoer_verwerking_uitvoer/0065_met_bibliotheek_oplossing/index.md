---
hruid: leerlijn_invoer_verwerking_uitvoer_bibliotheek_oplossing
version: 1
language: nl
title: "Met een bibliotheek (oplossing)"
description: "Een component aansturen aan de hand van een bibliotheek."
keywords: ["invoer", "verwerking", "uitvoer", "microcontroller", "µC", "arduino", "dwenguino", "bibliotheek", "library"]
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

# Gebruik maken van een bibliotheek

In onderstaande code staat in de commentaar aangegeven welke lijnen te maken hebben met de bibliotheek.

```arduino
    #include <Wire.h>
    #include <Dwenguino.h>
    #include <LiquidCrystal.h>

    /* Met deze lijn importeer je de bibliotheek NewPing.
     * Deze bevat de nodige variabelen en functies om te spreken met de sonar-sensor. */
    #include <NewPing.h>

    #define TRIGGER_PIN 11
    #define ECHO_PIN 12
    #define MAX_DISTANCE 200

    /* Met deze code definieer je het sonar object en sla
     * je die op in de variabele sonar.
     * Deze zal je gebruiken om op een abstracte manier
     * te communiceren met de sensor. 
     * Hier stel je ook al in met welke pinnen de sensor verbonden is
     * en wat de maximale afstand is dat die mag/kan meten.*/
    NewPing sonar = NewPing(
        TRIGGER_PIN,
        ECHO_PIN,
        MAX_DISTANCE);
    int afstand;

    void setup(){
        initDwenguino();
        pinMode(13, OUTPUT);
    }

    void loop(){
        /* Met deze lijn roep je de  ping_cm() functie op van het sonar object.
         * In deze functie zal de bibliotheek de juiste signalen sturen naar de
         * sensor zodat die een waarde kan lezen. */
        afstand = sonar.ping_cm();
        if (afstand > 0 && afstand < 100){
            digitalWrite(13, HIGH);
        } else {
            digitalWrite(13, LOW);
        }
        delay(100);
    }
```