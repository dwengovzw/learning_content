---
hruid: Uitleg als-dan-v1.0.00
version: 1
language: nl
title: Uitleg als-dan
description: Uitleg als-dan
keywords: [voorbeeld, voorbeeld2]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [4, 3]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
---

# 7. Controlestructuren: als-dan

Net als met de lus kan je met het *‘als-dan’-blok* een structuur inbouwen om het verloop van de code te veranderen.

In het ‘als-dan’-blok wordt nagegaan of een bepaalde voorwaarde (conditie) waar of niet waar (vals) is. Als de voorwaarde waar is, dan wordt de code in het ‘dan’-gedeelte uitgevoerd. Als de voorwaarde vals is, dan wordt de code in het ‘dan’-gedeelte niet uitgevoerd.

Op het Dwenguino-bord staan er ook *knoppen*.

Hieronder zie je een voorbeeld van het gebruik van het ‘als-dan’-blok. Bij de opstart van het programma brandt LED 13. Deze code gaat na of de NOORD-knop, dus de bovenste knop, is ingedrukt. Zodra de NOORD-knop wordt ingedrukt, dooft LED 13 (linksboven op het Dwenguino-bord).

![alt](https://scholen.dwengo.org/static/alsdancode.png "Afb. alsdan")