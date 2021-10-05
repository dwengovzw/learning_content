---
hruid: UitlegAlsDan-v1
version: 3
language: nl
title: "Uitleg als-dan"
description: "Uitleg als-dan"
keywords: ["WeGoSTEM"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [10, 11, 12, 13, 14]
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

# 7. Controlestructuren: als-dan

Net als met de lus kan je met het *‘als-dan’-blok* een structuur inbouwen om het verloop van de code te veranderen.

In het *‘als-dan’-blok* wordt nagegaan of een bepaalde voorwaarde (conditie) waar of niet waar (vals) is. Als de voorwaarde waar is, dan wordt de code in het ‘dan’-gedeelte uitgevoerd. Als de voorwaarde vals is, dan wordt de code in het ‘dan’-gedeelte niet uitgevoerd.

Op het Dwenguino-bord staan er ook *knoppen*.

Hieronder zie je een voorbeeld van het gebruik van het *‘als-dan’-blok*. Bij de opstart van het programma brandt led 13. Deze code gaat na of de NOORD-knop, dus de bovenste knop, is ingedrukt. Zodra de NOORD-knop wordt ingedrukt, dooft led 13 (linksboven op het Dwenguino-bord).

![alt](https://scholen.dwengo.org/static/alsdancode.png "Afb. alsdan")