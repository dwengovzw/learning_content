---
hruid: g_led_vb3
version: 3
language: en
title: "Example LED 3"
description: "Example LED 3"
keywords: ["oefeningen", "led"]
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
## LED

EXERCISE 3

Let all LEDs blink for half a second in numerical order. This means that LED 0 lights up first and goes off when LED 1 lights up, LED 1 goes off when LED 2 lights up, ...

Solution:

![blockly](@learning-object/led_m3/en/3)