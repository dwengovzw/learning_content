---
hruid: sr_LCDVB1
version: 3
language: nl
title: "Voorbeeld Lcd 1"
description: "Voorbeeld Lcd 1"
keywords: ["StartTodwenguino", "lcd", "lcd-scherm"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

### Voorbeeld lcd-scherm

OPGAVE 1

Laat 'Welkom robot' op het lcd-scherm verschijnen.

Oplossing:

![blockly](@learning-object/SRM_LED1/nl/3)

De tekst 'Welkom robot' kan je aanpassen. De twee nullen betekenen: eerste lijn, eerste karakter.

*Test deze voorbeelden ook zelf uit in de simulator! Als je de werking wat te pakken hebt, kan je zelf aan de slag.*