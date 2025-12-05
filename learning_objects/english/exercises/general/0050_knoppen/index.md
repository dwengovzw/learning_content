---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Explanation of Buttons
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: g_knoppen
keywords:
- oefeningen
- knoppen
language: en
licence: dwengo
return_value:
  callback_schema:
    att: test
    att2: test2
  callback_url: callback-url-example
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
target_ages:
- 10
- 11
- 12
teacher_exclusive: false
title: Explanation of Buttons
version: 3
---
# dwenguinoBlockly
## Buttons

### Type
- Input

### How it works
On the dwenguino you will find five push buttons. The outer buttons are named NORTH, SOUTH, EAST, WEST, just like in geography. The middle button is called CENTER.

You can click a button with your mouse. If you click it, the button is pressed. When you release the button again, it is no longer pressed.  

***

### In real life

![](embed/knoppen.png "buttons")

### In the simulator

![](embed/knoppen_sim.png "buttons simulator")

The blocks needed to use the buttons can be found under the category ![](embed/cat_dwenguino.png "dwenguino category").

*** 

Of course you want the drawing robot to start drawing only when you say so. Therefore, you will introduce an extra start condition here as in the example below:

![blockly](@learning-object/knoppen_m/nl/3)