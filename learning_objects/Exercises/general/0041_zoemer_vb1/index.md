---
hruid: g_zoemer_vb1
version: 3
language: nl
title: "Voorbeeld Zoemer 1"
description: "Voorbeeld Zoemer 1"
keywords: ["oefeningen", "zoemer"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
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
## Zoemer

OPGAVE 1  

Schrijf een programma zodat de buzzer een toon met frequentie 262 Hz afspeelt in intervallen van 1 seconde aan en 1 seconde uit.


Oplossing:

![blockly](@learning-object/zoemer_m1/nl/3)

*Test dit ook eens uit op een echte Dwenguino als dit werkt in de simulator.*