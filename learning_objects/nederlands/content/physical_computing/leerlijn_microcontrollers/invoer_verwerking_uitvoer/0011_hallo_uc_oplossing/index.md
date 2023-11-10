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

Hieronder kan je een voorbeeldoplossing zien voor de opdracht. Merk op dat er zeker variaties op deze oplossing mogelijk zijn.

```arduino
#include <Wire.h>
#include <Dwenguino.h>
#include <LiquidCrystal.h>
#include <NewPing.h>

#define TRIGGER_PIN 11
#define ECHO_PIN 12
#define MAX_DISTANCE 200

NewPing sonar(
    TRIGGER_PIN, 
    ECHO_PIN, 
    MAX_DISTANCE);
int afstand;

void setup(){
    initDwenguino();
    pinMode(13, OUTPUT);
}

void loop(){
    afstand = sonar.ping_cm();
    if (afstand > 0 && afstand < 100){
        digitalWrite(13, HIGH);
    } else {
        digitalWrite(13, LOW);
    }
    delay(100);
}
```