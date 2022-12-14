---
hruid: sr_WachtVB1
version: 3
language: nl
title: "Voorbeeld Wacht 1"
description: "Voorbeeld Wacht 1"
keywords: ["StartToDwenguino", "wacht"]
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

### Voorbeeld Wacht

OPGAVE 1

Schrijf een programma dat het volgende doet:

* Laat "Hallo mensen" op het lcd-scherm verschijnen gedurende 1 seconde (1000 ms).
* Laat "Ik ben Dwenguino" op het lcd-scherm verschijnen voor 2 seconden (2000 ms).

Oplossing:

![blockly](@learning-object/SRM_Wacht1/nl/3)

Het *'wacht'-blok* dat **na** een bepaalde instructie staat, geeft weer hoelang de computer moet **wachten** vooraleer deze met de volgende instructie mag beginnen.

Het probleem dat zich nu voordoet, is dat "Ik ben Dwenguino" op het scherm blijft staan. *Denk even na over wat dit zou veroorzaken.*

*Test deze voorbeelden ook zelf uit in de simulator!*
