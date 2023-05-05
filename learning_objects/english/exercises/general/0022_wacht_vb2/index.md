---
hruid: g_wacht_vb2
version: 3
language: en
title: "Voorbeeld Wacht 2"
description: "Voorbeeld Wacht 2"
keywords: ["oefeningen", "wacht"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [10, 11, 12]
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
## Delay

EXERCISE 2

Create a billboard for UGent and dwengo. The names should alternate on the LCD screen with an interval of 5 seconds. Also, make sure that the names are centered (one line on the LCD screen can display a maximum of 16 characters).

Solution:

![blockly](@learning-object/wacht_m2/en/3)