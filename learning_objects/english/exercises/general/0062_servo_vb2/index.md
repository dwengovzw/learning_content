---
hruid: g_servo_vb2
version: 3
language: en
title: "Voorbeeld Servomotor 2"
description: "Voorbeeld Servomotor 2"
keywords: ["oefeningen", "servomotor"]
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
teacher_exclusive: true
---
## Servo Motor (Blue)

TASK 2

Program both hands so that they can move up and down in intervals of 1 second.

Don't be fooled! This is not the same as the previous exercise. Instead of using the pre-programmed function for waving, you are now programming both hands separately. So you can move both hands independently of each other or choose to keep the hand in a certain position.

Solution:

![blockly](@learning-object/servo_m2/nl/3)

You are now able to do a lot of other actions! Your robot can shake hands with someone, cover its eyes...

<div class="alert alert-box alert-success">
This requires some knowledge about angles and degrees. It is an extra challenge that you can give to your students if you notice that they find the basic blocks too easy.
</div>

<div class="alert alert-box alert-danger">
Note that in the simulator, you are limited in rotating and placing the servo motors. When building a robot, it is important to remember that the simulator is only a tool for building a real robot.

When testing servo motors, it is advisable to mainly consider the physical robot. The orientation of the servo motor plays a big role!
</div>