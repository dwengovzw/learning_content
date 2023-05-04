---
hruid: g_servo_vb3
version: 3
language: nl
title: "Voorbeeld Servomotor 3"
description: "Voorbeeld Servomotor 3"
keywords: ["oefeningen", "servomotor"]
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
## Servomotor (zwart)

OPGAVE 3

Schrijf een programma voor een zwarte servomotor zodat de motor continu draait.

Oplossing:  

![blockly](@learning-object/servo_m3/nl/3)

<div class="alert alert-box alert-success">
In tegenstelling tot de blauwe servomotor, moet je hier de snelheid van de servomotor instellen i.p.v. een hoek. Als een zwarte servomotor moet stoppen met draaien, stel je dus de snelheid in op 0.
</div>