---
hruid: g_zoemer
version: 3
language: en
title: "Explanation Buzzer"
description: "Explanation Buzzer"
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# dwenguinoBlockly
## Buzzer

### Type
- Output
- Actuator

### Operation
Above the LCD screen, you can see a round, black component. This is the buzzer. With it, you can play sounds.

Sound is a wave of air pressure caused by a vibrating object such as an instrument or speaker. The number of vibrations per second (the frequency) determines the pitch. When the number of vibrations per second is between 20 and 20,000, humans can hear it. We use the unit Hertz, abbreviated Hz, for vibrations per second. The human ear can hear vibrations between 20 Hz and 20,000 Hz.

To be able to play sound, the Dwenguino is equipped with a simple buzzer that you can play with a chosen frequency.

***

### In real life

![](embed/zoemer.png "Buzzer")

### In the simulator

![](embed/buzzer_on_board.png "Buzzer")

You can find the blocks you need to control the buzzer under the category ![](embed/cat_dwenguino.png "Dwenguino category").

<div class="alert alert-box alert-success">
For more information about the buzzer, you can consult the student sheets of the <em>Social Robot</em>
</div>