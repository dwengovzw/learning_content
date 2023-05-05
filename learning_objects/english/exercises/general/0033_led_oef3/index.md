---
hruid: g_led_oef3
version: 3
language: en
title: "Oefening Led 3"
description: "Oefening Led 3"
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

EXERCISE 3

Make all LEDs flicker for half a second in numerical order. This means that LED 0 should turn on and then turn off when LED 1 turns on, LED 1 turns off when LED 2 turns on, and so on.