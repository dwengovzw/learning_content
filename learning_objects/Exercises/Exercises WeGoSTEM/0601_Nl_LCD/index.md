---
hruid: wgs_lcd
version: 3
language: nl
title: "Uitleg Lcd"
description: "Uitleg Lcd"
keywords: ["StartToDwenguino", "lcd", "lcd-scherm"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

## Lcd-scherm

Het lcd-scherm kan je gebruiken om tekst te tonen. Dit kan bijvoorbeeld handig zijn voor het uitlezen van de waarden die de sensoren meten.

Op het lcd-scherm van de Dwenguino passen maximaal 32 karakters, bijvoorbeeld letters of cijfers, verspreid over twee regels. Je kan dus 16 karakters per regel tonen. De helderheid en de achtergrondverlichting van het scherm zijn ook aanpasbaar, maar deze worden hier niet verder behandeld.

![](embed/Afb1.png "Afbeelding lcd")