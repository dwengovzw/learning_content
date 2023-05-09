---
hruid: sr3_elektronica1
version: 3
language: en
title: "Motherboard"
description: "Motherboard"
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
## The motherboard
You will be using the Dwenguino and its accompanying expansion board. When cutting out the recesses, you will need to provide space for this!

<div class="alert alert-box alert-danger">
Note that the USB port of the Dwenguino must be accessible for comfortable connection of the USB cable.
</div>

### Wiring and assembly

Before attaching the components to the body of the robot, it is wise to first connect the wiring between the Dwenguino and the other components. This prevents there from being too little space left to connect the wires after the components have been attached.

The image below shows which components are present on the Dwenguino and which actuators can be connected directly to it.

![](embed/assemblage1.png "Dwenguino")

*The contrast of the LCD screen can be adjusted. You can power the Dwenguino via the USB cable or an adapter.*

On the *extension connector*, you can connect the expansion board (see image). This is specifically tailored for the social robot. With this, you can connect all other sensors and actuators.

![](embed/pcb.png "Expansion board")