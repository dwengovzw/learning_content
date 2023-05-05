---
hruid: g_zoemer_oef4
version: 3
language: en
title: "Oefening Zoemer 4"
description: "Oefening Zoemer 4"
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
teacher_exclusive: false
---
## Buzzer

TASK 4

Write a program so that you can use the Dwenguino as a pentatonic (5-tone) instrument. You can do this by assigning a note to each of the 5 buttons (NORTH - EAST - SOUTH - WEST - MIDDLE). A standard pentatonic scale is *Do (C), Re (D), Mi (E), Fa (F), Sol (G)*.

***

<div class="alert alert-box alert-success">
As you may notice, it's not so easy to bind buzzer tones to the buttons. The most efficient way to do this is explained below.
</div>