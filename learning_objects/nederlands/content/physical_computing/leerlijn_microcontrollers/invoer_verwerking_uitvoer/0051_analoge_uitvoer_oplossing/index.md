---
hruid: leerlijn_invoer_verwerking_uitvoer_analoge_uitvoer_oplossing
version: 1
language: nl
title: "Analoge uitvoer (oplossing)"
description: "Leer hoe je een analoge schrijft naar van een pin van de µC."
keywords: ["invoer", "verwerking", "uitvoer", "microcontroller", "µC", "arduino", "dwenguino", "analogWrite"]
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

# Analoge uitvoer (oplossing)

Hieronder zie je de oplossing voor de opdracht waarbij de leerlingen LED 13 moeten dimmen. Merk op dat de delay tijd hier zo gekozen is dat het wisselen tussen aan en uit niet meer zichtbaar is voor het menselijke oog (100Hz). Je kan de leerlingen laten experimenteren met deze delay tijd. Zo kunnen ze achterhalen vanaf welke frequentie het oog het flikkeren kan zien.

```arduino
#include <Wire.h>;
#include <Dwenguino.h>;

void setup()
{
    initDwenguino();
    pinMode(13, OUTPUT);
}

void loop()
{
    digitalWrite(13, HIGH);
    delay(5);
    digitalWrite(13, LOW);
    delay(5);
}
```

Je kan de leerlingen ook laten experimenteren met de verhouding tussen aan en uit. Op die manier kunnen ze de led dimmen tot verschillende lichtsterktes. Om dit te doen zorg je ervoor dat de duur van de **periode** gelijk blijft (bv. 10 ms) maar de tijd dat het signaal hoog (de **duty cycle**) is groter of kleinder wordt. Hieronder zie je een voorbeeld van een led die 20% gedimd wordt.

```arduino
#include <Wire.h>;
#include <Dwenguino.h>;

void setup()
{
    initDwenguino();
    pinMode(13, OUTPUT);
}

void loop()
{
    digitalWrite(13, HIGH);
    delay(8);
    digitalWrite(13, LOW);
    delay(2);
}
```