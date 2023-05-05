---
hruid: g_knoppen_vb1
version: 3
language: en
title: "Example Buttons 1"
description: "Example Buttons 1"
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

EXERCISE 1.1

When the program starts, if the NORTH button is pressed, the first LED (LED 0) will turn on.

Solution:

![blockly](@learning-object/knoppen_m1a/en/3)

***

EXERCISE 1.2

It is not intended for LED 0 to remain on when you release the button. Make sure the LED turns off when you release the button.

Solution:

![blockly](@learning-object/knoppen_m1b/en/3)

***

<div class="alert alert-box alert-success">
To use the buttons, you will always need a selection structure. Buttons are always used to control something.
</div>

