---
hruid: g_sonar_oef2
version: 3
language: en
title: "Oefening Sonar-sensor 2"
description: "Oefening Sonar-sensor 2"
keywords: ["oefeningen", "sonar-sensor"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
## Sonar Sensor

TASK 2

Write a program that depending on the value, returns the message "value < 20 cm" or "value > 20 cm".

You should use a conditional structure.

***

When programming the social robot, you can link other actions to these conditions. For example, you can wave the arms or blink the eyes when someone is between 0 and 50 cm away from the robot.

<div class="alert alert-box alert-danger">
The sonar sensor has a range of 200 cm. When nothing is within this range, the sonar sensor returns a value of 0. This means that when there is nothing visible within 2 m, the sensor interprets this as if there is something right in front of the sensor.<br><br>

Therefore, always program <em>"Distance greater than 0"</em> as a condition for the shortest distance, so that there are no problems here.
</div>