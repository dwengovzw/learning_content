---
hruid: g_matrix_vb3
version: 3
language: en
title: "Example LED matrix 3"
description: "Example LED matrix 3"
keywords: ["oefeningen", "led-matrix"]
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
## LED matrix

EXERCISE 3

Program 2 eyes that look back and forth (left - right - left - right - ...).

Solution:  

![blockly](@learning-object/matrix_m3/en/3)

***

<div class="alert alert-box alert-success">
To create the illusion of movement, you can use a loop to turn on and off different LED patterns in a specific order.
</div>