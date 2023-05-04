---
hruid: g_servo_vb1
version: 3
language: en
title: "Voorbeeld Servomotor 1"
description: "Voorbeeld Servomotor 1"
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
## Servomotor (blauw)

OPGAVE 1

Laat de handen van de robot zwaaien. Hiervoor werd er reeds een blok voorzien.

Oplossing:  

![blockly](@learning-object/servo_m1/nl/3)

Je robot kan nu zwaaien met zijn armen.

<div class="alert alert-box alert-danger">
Vergeet niet om de servomotor als component toe te voegen in de simulator! Voor de volledigheid verander je deze ook best van uiterlijk voor een accuratere simulatie.
</div>