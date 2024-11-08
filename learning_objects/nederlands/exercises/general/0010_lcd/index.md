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
# dwenguinoBlockly
## Lcd-scherm

### Type
- Uitvoer
- Actuator

### Werking
Het lcd-scherm kan tekst weergeven. Hiermee kan bijvoorbeeld een boodschap worden meegedeeld.<br>
Op het lcd-scherm van de dwenguino passen maximaal 32 karakters, zoals letters of cijfers, verspreid over twee regels. Je kan dus 16 karakters per regel tonen. 

> De helderheid van het scherm is aanpasbaar. Je kan dit zelf regelen door aan de gele schroef te draaien (zie figuur) met een schroevendraaier, terwijl het lcd-scherm aanstaat.

***

### In het echt

![](embed/dwenguino_lcd.png "Afbeelding lcd-scherm")

### In de simulator

![](embed/lcd.png "lcd-scherm")

De blokken om het lcd-scherm aan te sturen vind je terug in de categorie ![](embed/cat_dwenguino.png "categorie dwenguino").

<div class="alert alert-box alert-success">
Voor meer informatie over het lcd-scherm kan je terecht in de leerlingenfiches van de <em>Sociale Robot</em>.
</div>