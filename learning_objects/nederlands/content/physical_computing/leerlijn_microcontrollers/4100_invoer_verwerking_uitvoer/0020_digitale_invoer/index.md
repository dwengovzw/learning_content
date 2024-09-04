---
hruid: leerlijn_invoer_verwerking_uitvoer_digitale_invoer
version: 1
language: nl
title: "Digitale invoer"
description: "Leer hoe je een digitale waarde leest van een pin van de µC."
keywords: ["invoer", "verwerking", "uitvoer", "microcontroller", "µC", "arduino", "dwenguino", "digitalRead"]
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

# Digitale invoer - Een digitale waarde lezen

De pinnen van de µC kunnen gebruikt worden om een hoge (5 V) of lage (0 V) spanning op een pin te meten. Bijgevolg zal je in een programma de waarde van een pin altijd inlezen als een logische 1 of een logische 0. Hieronder zie je hoe je met de Arduino-bibliotheek de waarde van een digitale pin kan inlezen.

```cpp
unsigned char waardePin12 = digitalRead(12);
```
- `waardePin12` is hier de variabele waarin de waarde van de pin wordt opgeslagen.
- `unsigned char` is het type van de variabele. Getallen van dit type hebben een gehele **waarde tussen 0 en 255** (met inbegrip van 0 en 255). 
- `digitalRead()` is een functie uit de Arduino-bibliotheek die de waarde op een digitale pin leest. Die pin moet je wel meegeven. `digitalRead(12)` bv. leest de waarde op pin 12.
