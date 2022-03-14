---
hruid: STD_KnoppenVB3-v1
version: 3
language: nl
title: "Voorbeeld Knoppen 3"
description: "Knoppen Voorbeeld"
keywords: ["StartToDwenguino", "knoppen"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [10, 11, 12]
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
teacher_exclusive: true
---
### Voorbeeld knoppen

OPGAVE 3

Wanneer het programma opstart verschijnt er "Hallo" op het lcd-scherm. Als je op de NOORD-knop drukt moet deze tekst verdwijnen en gaat led 0 branden. Als je op de ZUID-knop drukt gaat led 0 uit en verschijnt er opnieuw tekst op het lcd-scherm.

Oplossing:

![blockly](@learning-object/KNOPSTD3-v1/nl/3)

*Test deze voorbeelden ook zelf uit in de simulator!*