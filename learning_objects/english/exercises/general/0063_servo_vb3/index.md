---
hruid: g_servo_vb3
version: 3
language: en
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
## Servomotor (black)

EXERCISE 3

Write a program for a black servo motor so that the motor rotates continuously.

Solution:  

![blockly](@learning-object/servo_m3/nl/3)

***

<div class="alert alert-box alert-success">
In contrast to the blue servo motor, here you have to set the speed of the servo motor instead of an angle. If a black servo motor has to stop rotating, set the speed to 0.
</div>