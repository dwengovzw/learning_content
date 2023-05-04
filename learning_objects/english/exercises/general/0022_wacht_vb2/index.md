---
hruid: g_wacht_vb2
version: 3
language: en
title: "Voorbeeld Wacht 2"
description: "Voorbeeld Wacht 2"
keywords: ["oefeningen", "wacht"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
## Wacht

OPGAVE 2

Maak een reclamebord voor de UGent en dwengo. De namen moeten afwisselend verschijnen in een interval van 5 seconden. Zorg er ook voor dat de namen gecentreerd zijn (één regel op het lcd-scherm kan een maximum van 16 karakters tonen).

Oplossing:

![blockly](@learning-object/wacht_m2/nl/3)