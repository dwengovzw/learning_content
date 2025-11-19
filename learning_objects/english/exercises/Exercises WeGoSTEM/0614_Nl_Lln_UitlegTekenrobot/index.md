---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Drawing robot explanation
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: wgs_Motoren
keywords:
- WeGoSTEM
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
title: Explanation of the drawing robot
version: 3
---
# Controlling the drawing robot

The WeGoSTEM drawing robot has *two motors* and *two arms*. Each arm is connected to one of the motors. When these motors turn, the arms of the drawing robot move. Each motor can turn *to the right* and *to the left* and can be set to *different speeds*.

You control a motor with a *'motor' block*: 

![](embed/dcmotor.png "Fig. Drawing robot")

With this block you control the speed and the direction of rotation of the motor.


![](embed/positiemotorentekenrobot.jpg "Fig. Drawing robot")

The motors are located at the positions of the lower red dots.
The two motors are numbered: the left motor is motor number 1 and the right motor is motor number 2. This corresponds to the number you see next to the text “number” on the *'motor' block*. 

With the *'motor' block* you can set not only the motor's number but also its speed. *That speed is determined by a number between -255 and 255*. With a positive value the motor turns in one direction, with a negative value in the other direction.