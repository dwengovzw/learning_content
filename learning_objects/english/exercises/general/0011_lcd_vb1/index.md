---
hruid: g_lcd_vb1
version: 3
language: en
title: "Voorbeeld Lcd 1"
description: "Voorbeeld Lcd 1"
keywords: ["oefeningen", "lcd", "lcd-scherm"]
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
## Lcd-screen

EXERCISE 1

Display 'Welcome robot' on the LCD screen.

Solution:

![blockly](@learning-object/lcd_m1/en/3)

<div class="alert alert-box alert-success">
You can change the text 'Welcome robot' in the blue block.<br><br>
The two zeros below are also important:<br>
<ul><li><em>on row 0</em>: the text appears on the first row.</li></ul>
<ul><li><em>starting from column 0</em>: the text starts from the first character.</li></ul>
</div>