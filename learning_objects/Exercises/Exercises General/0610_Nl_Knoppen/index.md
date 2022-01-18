---
hruid: STD_Knoppen-v1
version: 3
language: nl
title: "Uitleg Knoppen"
description: "Uitleg Knoppen"
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# WIP
## Knoppen

Op de Dwenguino vind je vijf drukknoppen. De buitenste knoppen kregen de namen NOORD, ZUID, OOST, WEST, net als in aardrijkskunde. De middelste knop heet MIDDEN.

Je kan op een knop klikken met je muis. Als je erop klikt, is de knop ingedrukt. Als je de knop weer loslaat, is hij niet meer ingedrukt.  

![](embed/Knoppen.png "Voorbeeld Knoppen")

Je wilt uiteraard dat de tekenrobot pas begint te tekenen wanneer jij dit wilt. Daarom ga je hier een extra startconditie invoeren zoals in onderstaand voorbeeld:

![blockly](@learning-object/KNOP-v1/nl/3)