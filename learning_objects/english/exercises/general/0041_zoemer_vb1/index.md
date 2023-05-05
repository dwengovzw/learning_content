---
hruid: g_zoemer_vb1
version: 3
language: en
title: "Voorbeeld Zoemer 1"
description: "Voorbeeld Zoemer 1"
keywords: ["oefeningen", "zoemer"]
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
## Buzzer

EXERCISE 1

Write a program so that the buzzer plays a tone with a frequency of 262 Hz in intervals of 1 second on and 1 second off.

Solution:

![blockly](@learning-object/zoemer/en/3)