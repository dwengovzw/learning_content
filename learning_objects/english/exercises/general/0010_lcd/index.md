---
hruid: g_lcd
version: 3
language: en
title: "Explanation LCD"
description: "Explanation LCD"
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# dwenguinoBlockly
## LCD screen

### Type
- Output
- Actuator

### Functionality
The LCD screen can display text. This can be used to communicate a message.<br>
The dwenguino's LCD screen can display up to 32 characters, such as letters or numbers, spread over two lines. You can show 16 characters per line. 

> The brightness of the screen is adjustable. You can adjust this yourself by turning the yellow screw (see figure) with a screwdriver, while the LCD screen is on.

***

### In real life

![](embed/dwenguino_lcd.png "Picture of LCD screen")

### In the simulator

![](embed/lcd.png "Picture of LCD screen")

The blocks to control the LCD screen can be found in the category ![](embed/cat_dwenguino.png "dwenguino category").

<div class="alert alert-box alert-success">
For more information about the LCD screen, you can consult the student sheets of the <em>Social Robot</em>.
</div>