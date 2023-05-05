---
hruid: g_zoemer_oef3
version: 3
language: en
title: "Exercise Buzzer 3"
description: "Exercise Buzzer 3"
keywords: ["oefening", "zoemer"]
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

EXERCISE 3

Write a program that plays the tune "Brother John" on the buzzer. To do this, you will first need to look up the score of the song and the frequencies of the notes.

***

<div class="alert alert-box alert-success">
As you can see, this will be a fairly long program. Fortunately, there are a few places where you can shorten it using a <strong>bounded loop</strong>. This will be explained further in the next section.
</div>