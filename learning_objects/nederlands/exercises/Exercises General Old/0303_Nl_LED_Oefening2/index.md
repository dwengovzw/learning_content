---
hruid: led_Oef2
version: 3
language: nl
title: "led Oefening 2"
description: "led Oefening 2"
keywords: ["StartTodwenguino", "led"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

## 3.2 leds

Schrijf een programma dat het volgende doet:

1. leds 0 en 7 gaan aan.
2. Wacht 100 ms. leds 1 en 6 gaan aan.
3. Wacht 100 ms. leds 0 en 7 gaan uit. leds 2 en 5 gaan aan.
4. Wacht 100 ms. leds 1 en 6 gaan uit. leds 3 en 4 gaan aan.
5. Wacht 100 ms. leds 2 en 5 gaan uit. leds 0 en 7 gaan aan.
6. Wacht 100 ms. leds 3 en 4 gaan uit.

*Test dit ook eens uit op een echte dwenguino als dit werkt in de simulator.*