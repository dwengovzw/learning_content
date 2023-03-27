---
hruid: pc_micro_bouwstenen
version: 3
language: nl
title: "Bouwstenen"
description: "Bouwstenen"
keywords: ["Microcontroller"]
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# Microcontroller

## Bouwstenen van een microcontroller
![](@youtube/https://www.youtube.com/embed/Tj78BgXAhMQ "De bouwstenen van een microcontroller")

De behandelde onderdelen van de microcontroller vormen een hele boterham. Het is normaal dat dit wat overweldigend overkomt.

![](embed/microcontroller.png "schematische microcontroller")

Op dit moment is het voldoende om te beseffen dat je in dit project code zal schrijven voor een microcontroller, en *niet* voor een klassieke computer met snelle processor en geheugen van meerdere gigabytes.

De microcontroller die je zal gebruiken, de AT90USB646, kan tot 16 miljoen instructies per seconde (MIPS) uitvoeren en is voorzien van 64 KB programmageheugen en 4 KB datageheugen.<br>
De microcontroller heeft bovendien een 8-bit architectuur, wat impliceert dat de registers en bus 8 bit breed zijn. Bij het schrijven van code hou je dit best in gedachten en gebruik je waar mogelijk 8-bit datatypes. 

<div class="alert alert-box alert-success">
Het optellen van twee 8-bit getallen kan in één kloktik gebeuren, terwijl het optellen van twee floating point getallen meer dan 100 kloktikken in beslag neemt! <br><br>

Aan jullie de uitdaging om deze beperkte computerkracht efficient te benutten.
</div>