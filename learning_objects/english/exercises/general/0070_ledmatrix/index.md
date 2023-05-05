---
hruid: g_matrix
version: 3
language: en
title: "Explanation LED matrix"
description: "Explanation LED matrix"
keywords: ["oefeningen", "led-matrix"]
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
## LED Matrix

### Type
- Output
- Actuator

### Operation
The LED Matrix is a square 8x8 matrix with 64 LEDs in a fixed color (red). The matrix is ideal for lighting up certain patterns, such as an eye or a mouth of the robot or another symbol. You can also connect the matrices together (maximum of 4), if you want to use multiple matrices at the same time. You can program which LEDs should light up at the same time.

***

### In real life

![](embed/ledmatrix.png "led-matrix")

### In the simulator

![](embed/led_matrix.png "led-matrix simulator")

The blocks you need to program the LED matrices can be found under the category ![](embed/cat_uitvoer.png "output category").

<div class="alert alert-box alert-success">
For more information about the LED Matrix, you can consult the student sheets of the <em>Social Robot</em>.
</div>