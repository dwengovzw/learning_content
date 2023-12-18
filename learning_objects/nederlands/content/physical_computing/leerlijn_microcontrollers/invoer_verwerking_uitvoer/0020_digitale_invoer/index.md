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

# Een digitale waarde lezen

De pinnen van de µC kunnen gebruikt worden om een hoge (5V) of lage (0V) spanning op een pin te meten. Bijgevolg zal je in je programma de waarde van een pin altijd inlezen als een logische 1 of een logische 0. Hieronder zie je hoe je met de Arduino bibliotheek de waarde van een digitale pin kan inlezen.

```cpp
unsigned char waardePin12 = digitalRead(12);
```
- `waardePin12` is hier de variabele waarin we de waarde van de pin opslaan.
- `unsigned char` is het type van de variabele. Getallen van dit type hebben een **waarde tussen 0 en 255**. 
- `digitalRead(12)` is een functie uit de Arduino bibliotheek die de waarde op pin 12 zal lezen.