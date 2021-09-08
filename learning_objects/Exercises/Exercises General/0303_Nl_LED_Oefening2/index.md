---
hruid: LED Oefening 2-v1.0.1
version: 1
language: nl
title: LED Oefening 2
description: LED Oefening 2
keywords: [voorbeeld, voorbeeld2]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [4, 3]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
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