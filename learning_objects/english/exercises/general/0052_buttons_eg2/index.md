---
hruid: g_knoppen_vb2
version: 3
language: en
title: "Example Buttons 2"
description: "Example Buttons 2"
keywords: ["oefeningen", "knoppen"]
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
## Buttons

EXERCISE 2

Make sure the program meets the following conditions:

- When you're not doing anything, the LCD screen should display: "Press the SOUTH button?"
- When you press the SOUTH button, "Thank you" will appear on the LCD screen.
- When you press the NORTH button, "This is not what I asked!" will appear on the LCD screen.

Solution:

![blockly](@learning-object/knoppen_m2/nl/3)