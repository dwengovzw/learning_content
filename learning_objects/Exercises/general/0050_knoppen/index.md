---
hruid: g_knoppen
version: 3
language: nl
title: "Uitleg Knoppen"
description: "Uitleg Knoppen"
keywords: ["oefeningen", "knoppen"]
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
## Knoppen

### Type
- Invoer

### Werking
Op de Dwenguino vind je vijf drukknoppen. De buitenste knoppen kregen de namen NOORD, ZUID, OOST, WEST, net als in aardrijkskunde. De middelste knop heet MIDDEN.

Je kan op een knop klikken met je muis. Als je erop klikt, is de knop ingedrukt. Als je de knop weer loslaat, is hij niet meer ingedrukt.  

***

### In het echt

![](embed/knoppen.png "knoppen")

### In de simulator

![](embed/knoppen_sim.png "knoppen simulator")

De blokken die nodig zijn om de knoppen te gebruiken, vind je onder de categorie ![](embed/cat_dwenguino.png "categorie dwenguino").

*** 

Je wilt uiteraard dat de tekenrobot pas begint te tekenen wanneer jij dit zegt. Daarom ga je hier een extra startconditie invoeren zoals in onderstaand voorbeeld:

![blockly](@learning-object/knoppen_m/nl/3)