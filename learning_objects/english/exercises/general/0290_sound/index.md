---
hruid: g_sound
version: 3
language: en
title: "Explanation Geluidssensor"
description: "Explanation Geluidssensor"
keywords: ["oefeningen", "geluidssensor"]
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
## Sound Sensor

### Type
- Input
- Digital sensor

### Operation
Use this sensor to detect sound. The sensor returns 1 when there is sound and 0 when it's silent. Ideally, this sensor should be used in a quiet environment.

### Working in the simulator
In the simulator, a button is provided to simulate sound. Pressing the button simulates sound. Programming of the sound sensor is similar to the programming of the sonar sensor.

***

### In real life

![](embed/geluidssensor.png "sound sensor")

### In the simulator

![](embed/sim_geluidssensor.png "sound sensor simulator")

You can find the necessary blocks for controlling the sound sensor under the category ![](embed/cat_output.png "output category").