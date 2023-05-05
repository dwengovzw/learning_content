---
hruid: g_zoemer_vb3
version: 3
language: en
title: "Voorbeeld Zoemer 3"
description: "Voorbeeld Zoemer 3"
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

EXERCISE 3

Write a program so that the buzzer plays *Frère Jacques*. You will first need to look up the score of the song and the frequencies of the notes.

Solution:

![blockly](@learning-object/zoemer_m3/en/3)

<div class="alert alert-box alert-success">
As you can see, this is a quite long program. Fortunately, there are some places where you can shorten it using a <strong>bounded loop</strong>. This will be explained further in the next section.
</div>