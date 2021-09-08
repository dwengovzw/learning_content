---
hruid: LED_Oef2-v1
version: 3
language: nl
title: LED Oefening 2
description: LED Oefening 2
keywords: [StartToDwenguino, LED]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [10, 11, 12, 13, 14]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', 
    'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso'
]
teacher_exclusive: false
---

## 3.2 Opdracht LED

Schrijf een programma dat het volgende doet:

1. LEDs 0 en 7 gaan aan.
2. Wacht 100 ms. LEDs 1 en 6 gaan aan.
3. Wacht 100 ms. LEDs 0 en 7 gaan uit. LEDs 2 en 5 gaan aan.
4. Wacht 100 ms. LEDs 1 en 6 gaan uit. LEDs 3 en 4 gaan aan.
5. Wacht 100 ms. LEDs 2 en 5 gaan uit. LEDs 0 en 7 gaan aan.
6. Wacht 100 ms. LEDs 3 en 4 gaan uit.

*Test dit ook eens uit op een echte Dwenguino als dit werkt in de simulator.*