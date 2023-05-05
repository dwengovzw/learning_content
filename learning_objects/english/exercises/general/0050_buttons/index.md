---
hruid: g_knoppen
version: 3
language: en
title: "Explanation Buttons"
description: "Explanation Buttons"
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# dwenguinoBlockly

## Buttons

### Type
- Input

### Functioning
On the Dwenguino board, you can find five push buttons. The outer buttons are named NORTH, SOUTH, EAST, and WEST, similar to geography. The center button is named MIDDLE.

You can click on a button with your mouse. When you click it, the button is pressed down. When you release the button, it is no longer pressed.

***

### In real life

![](embed/knoppen.png "buttons")

### In the simulator

![](embed/knoppen_sim.png "buttons simulator")

You can find the blocks needed to use the buttons under the category ![](embed/cat_dwenguino.png "dwenguino category").

***

Of course, you want the drawing robot to start drawing only when you tell it to. That's why you'll introduce an additional start condition like in the example below:

![blockly](@learning-object/knoppen_m/en/3)