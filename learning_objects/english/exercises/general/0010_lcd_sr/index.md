---
hruid: g_lcd_sr
version: 3
language: en
title: "Uitleg Lcd"
description: "Uitleg Lcd"
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
The LCD screen can display text, which can be used to convey a message.<br>
The dwenguino LCD screen can display a maximum of 32 characters, such as letters or numbers, spread over two lines. Therefore, you can display 16 characters per line.

> The brightness of the screen is adjustable. You can adjust this yourself by turning the yellow screw (see figure) with a screwdriver while the LCD screen is on.

***

### In real life

![](embed/dwenguino_lcd.png "LCD screen image")

### In the simulator

![](embed/lcd.png "LCD screen")

You can find the blocks to control the LCD screen in the category ![](embed/cat_output.png "output category").

<div class="alert alert-box alert-success">
For more information on the LCD screen, you can consult the student sheets of the <em>Social Robot</em>.
</div>