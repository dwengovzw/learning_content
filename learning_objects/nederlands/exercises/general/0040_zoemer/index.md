---
hruid: g_zoemer
version: 3
language: nl
title: "Uitleg Zoemer"
description: "Uitleg Zoemer"
keywords: ["oefeningen", "zoemer"]
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# dwenguinoBlockly
## Zoemer

### Type
- Uitvoer
- Actuator

### Werking 
Boven het lcd-scherm kan je een een ronde, zwarte component zien. Dit is de zoemer of buzzer. Hiermee kan je geluiden afspelen. 

Geluid is een golf van luchtdruk veroorzaakt door een trillend object zoals bijvoorbeeld een instrument of luidspreker. De hoeveelheid trillingen per seconde (de frequentie) bepaalt de toonhoogte. Wanneer het aantal trillingen per seconde tussen de 20 en 20 000 ligt, dan kan je dit als mens horen. Voor trillingen per seconde gebruiken we de eenheid Hertz, afgekort Hz. De mens kan dus trillingen horen tussen de 20 Hz en 20 000 Hz.

Om geluid te kunnen afspelen is de dwenguino voorzien van een eenvoudige buzzer die je een gekozen frequentie kunt laten afspelen.

***

### In het echt

![](embed/zoemer.png "Zoemer")

### In de simulator

![](embed/buzzer_on_board.png "buzzer")

De blokken die je nodig hebt om de buzzer te besturen, vind je onder de categorie ![](embed/cat_dwenguino.png "categorie dwenguino").

<div class="alert alert-box alert-success">
Voor meer informatie over de zoemer kan je terecht in de leerlingenfiches van de <em>Sociale Robot</em>
</div>