---
hruid: leerlijn_invoer_verwerking_uitvoer_digitale_uitvoer
version: 1
language: nl
title: "Digitale uitvoer"
description: "Leer hoe je een digitale waarde schrijft naar een pin van de µC."
keywords: ["invoer", "verwerking", "uitvoer", "microcontroller", "µC", "arduino", "dwenguino", "digitalWrite"]
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
estimated_time: 3
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Digitale uitvoer

Naar digitale pinnen kan je ook een waarde schrijven (1 of 0). Zo stel je het spanningsniveau op de pin in op 5V of 0V. Hieronder zie je hoe je met de Arduino bibliotheek de waarde 1 (=HIGH) naar pin 12 kan schrijven.

```cpp
digitalWrite(12, HIGH)
```

Merk op dat de waarde `HIGH` een constante is die gedefinieerd wordt in de Arduino bibliotheek. De waarde van deze constante is gelijk aan 1.
