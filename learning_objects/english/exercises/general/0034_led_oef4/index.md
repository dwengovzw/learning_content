---
hruid: g_led_oef4
version: 3
language: en
title: "Oefening Led 4"
description: "oefening Led 4"
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
teacher_exclusive: false
---
## Led

EXERCISE 4

Write a program that does the following:

1. Turn on LEDs 0 and 7.
2. Wait 100 ms. Turn on LEDs 1 and 6.
3. Wait 100 ms. Turn off LEDs 0 and 7. Turn on LEDs 2 and 5.
4. Wait 100 ms. Turn off LEDs 1 and 6. Turn on LEDs 3 and 4.
5. Wait 100 ms. Turn off LEDs 2 and 5. Turn on LEDs 0 and 7.
6. Wait 100 ms. Turn off LEDs 3 and 4.

*Test this on an actual Dwenguino board if it works in the simulator.*