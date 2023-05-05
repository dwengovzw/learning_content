---
hruid: g_led_vb4
version: 3
language: en
title: "Voorbeeld Led 4"
description: "Voorbeeld Led 4"
keywords: ["Oefeningen", "led"]
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
## Led

TASK 4

Write a program that does the following:

1. Leds 0 and 7 turn on.
2. Wait 100 ms. Leds 1 and 6 turn on.
3. Wait 100 ms. Leds 0 and 7 turn off. Leds 2 and 5 turn on.
4. Wait 100 ms. Leds 1 and 6 turn off. Leds 3 and 4 turn on.
5. Wait 100 ms. Leds 2 and 5 turn off. Leds 0 and 7 turn on.
6. Wait 100 ms. Leds 3 and 4 turn off.

*Try this out on an actual Dwenguino board if it works in the simulator.*

Solution:

![blockly](@learning-object/led_m4/en/3)