---
hruid: g_lcd
version: 3
language: nl
title: "Uitleg Lcd"
description: "Uitleg Lcd"
keywords: ["oefeningen", "lcd", "lcd-scherm"]
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
# DwenguinoBlockly
## Lcd-scherm

Het lcd-scherm kan tekst weergeven. Hiermee kan bijvoorbeeld een boodschap worden meegedeeld.<br>
Op het lcd-scherm van de Dwenguino passen maximaal 32 karakters, zoals letters of cijfers, verspreid over twee regels. Je kan dus 16 karakters per regel tonen. 

> De helderheid van het scherm is aanpasbaar. Je kan dit zelf regelen door aan de gele schroef te draaien (zie figuur) met een schroevendraaier terwijl het lcd-scherm aanstaat.

![](embed/dwenguino_lcd.png "Afbeelding lcd")