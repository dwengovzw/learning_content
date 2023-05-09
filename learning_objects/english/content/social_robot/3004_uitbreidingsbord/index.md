---
hruid: sr3_elektronica2
version: 3
language: en
title: "Expansion board"
description: "Expansion board"
keywords: ["Sociale Robot", "AI Op School", "STEM", "Computationeel denken", "Grafisch programmeren"]
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
estimated_time: 20
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-technologie-en-technieken'
]
teacher_exclusive: false
---
# Building the physical robot
## The expansion board

An additional advantage of using an expansion board is that the connectors are labeled with the specific sensors or actuators they are intended for.

![](embed/pcb-inkscape.png "Expansion board figure")

<div class="alert alert-box alert-danger">
Be careful when connecting or disconnecting the expansion board and the Dwenguino. The pins bend very easily, which can result in a poor connection between the expansion board and the Dwenguino.
</div>

### Wiring and assembly
When plugging in your pins, it is important to connect the correct components to each other. The sensors and actuators have symbols such as '+', '-', and 'GND' at their connectors, and it is important to connect these to the corresponding pin on the expansion board.

You can easily do this with [these cards](embed/leerlingenfiches.pdf "cards").

Once the wiring is in order, you can mount the electronics on the body of the robot.

If you have difficulty attaching certain items to the body, you can also consult the cards for help with the attachments. There we show you how to quickly attach something with the help of accessories.