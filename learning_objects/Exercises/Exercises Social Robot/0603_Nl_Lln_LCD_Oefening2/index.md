---
hruid: SR_LCDOef2-v1
version: 3
language: nl
title: "Oefening Lcd 2"
description: "Oefening Lcd 2"
keywords: ["StartToDwenguino", "lcd", "lcd-scherm"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [12, 13, 14]
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', 
    'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso'
]
teacher_exclusive: false
---

### Oefening lcd-scherm

OPGAVE 2

Zorg ervoor dat 'Welkom' en 'robot' op aparte lijnen verschijnen.

Om de tekst in 2 rijen te splitsen, heb je een tweede *'lcd-scherm'-blok* nodig.
Verander je bij 'op rij:' de 0 in een 1, dan komt je tekst op de tweede lijn.