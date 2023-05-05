---
hruid: g_lcd_vb2
version: 3
language: en
title: "Voorbeeld Lcd 2"
description: "Voorbeeld Lcd 2"
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
## LCD screen

EXERCISE 2

Make sure that 'Welcome' and 'robot' appear on separate lines.

Solution:

![blockly](@learning-object/lcd_m2/en/3)

<div class="alert alert-box alert-success">
To split the text over two lines, you need a second <em>'lcd screen'-block</em>.<br>
Change the 0 in 'on row:' to 1, and the text will appear on the second line.
</div>