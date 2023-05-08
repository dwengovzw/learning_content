---
hruid: g_sonar
version: 3
language: en
title: "Explanation Sonar"
description: "Uitleg Sonar"
keywords: ["oefeningen", "sonar"]
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
## Sonar Sensor

### Type
- Input
- Digital sensor

### Operation
The sensor sends out an ultrasonic sound signal. If an object is within range, the ultrasonic sound wave will bounce off that object. You can compare its operation to the echolocation used by bats. By measuring the time between sending the sound signal and receiving the reflected beam, the sensor can accurately determine the distance to the object.

The distance is returned in cm. The range of the sonar sensor is 200 cm.

### Operation in the simulator
In the simulator, a slider is provided to simulate the distance between the sensor and an object. The number on the slider simulates the distance to the object in cm.

***

### In real life

![](embed/sonar.png "Sonar Sensor")

### In the simulator

![](embed/Sonarsim.png "Sonar Sensor simulator")

You can find the blocks for programming the sonar sensor under the category ![](embed/cat_output.png "output category").

<div class="alert alert-box alert-success">
For more information about the sonar sensor, you can consult the student sheets of the <em>Social Robot</em>.
</div>