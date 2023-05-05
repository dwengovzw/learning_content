---
hruid: g_led
version: 3
language: en
title: "Explanation LED"
description: "Explanation LED"
keywords: ["oefeningen", "led"]
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# DwenguinoBlockly
## LED

### Type
- Output
- Actuator

### Functioning
On the bottom left of the dwenguino board, you will find eight LEDs:

![](embed/leds.png "leds")

These LEDs are *LED 0*, *LED 1*, ..., *LED 7*, from right to left. The first LED is thus *LED 0*. In computer science, it is often convention to start counting from 0. You may have noticed this convention with the LCD screen as well.

On the top left there is another LED: *LED 13*.
This last LED has some special functionalities and therefore has a special name.

You can turn the LEDs on or off using the blocks provided for this purpose. You can find them under the category ![](embed/cat_dwenguino.png "dwenguino category").