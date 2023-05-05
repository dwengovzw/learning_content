---
hruid: g_servo_vb1
version: 3
language: en
title: "Example Servo motor 1"
description: "Example Servo motor 1"
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
## Servo motor (blue)

EXERCISE 1

Make the robot's hands wave. For this, a block has already been provided.

Solution:

![blockly](@learning-object/servo_m1/en/3)

Your robot can now wave its arms.

<div class="alert alert-box alert-danger">
Don't forget to add the servo motor as a component in the simulator! For completeness, you should also change its appearance for a more accurate simulation.
</div>