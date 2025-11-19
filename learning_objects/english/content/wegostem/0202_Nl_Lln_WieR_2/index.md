---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: History and construction of robots
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: wgs_watiseenrobot2
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
- http://ilearn.ilabt.imec.be/vocab/curr1/s-informatie-verwerven
target_ages:
- 10
- 11
- 12
teacher_exclusive: false
title: What is a robot? Part 2
version: 3
---
# What is a robot?

*What is a robot made of?* 

A robot consists of hardware (its body, with wiring, processing unit, and batteries) and software (the program that controls it).  

![](embed/hardsoftware.png "Hardware and Software")

The ‘body’ of a robot contains mechanical parts that can be made of many materials: wheels, an arm, a head, ...  
The robot has sensors (inputs) to ‘feel’ and actuators (outputs) to ‘act’. A robot can be equipped with distance sensors, ground sensors, touch sensors, light sensors, or sound sensors.  
Examples of actuators are an LCD screen, a buzzer, and a servo motor. Your computer also has inputs and outputs. The keyboard and the mouse are examples of inputs; the screen is an output. 

Crucial is the processing unit with which your robot makes ‘decisions’. For this you can use, for example, a processor (as in a computer) or a microcontroller (as on the dwenguino). 

![](embed/Dwenguinobordje.png "Processing unit")

The wiring ensures that the processing unit, the sensors, and the actuators are connected to each other. How the robot controls its actuators depends on the information it gathers via its sensors and on how the processing unit is programmed. The batteries in the robot supply the motors with the required energy. 

A robot can only perform a specific task if its processing unit is programmed for it. That task is not necessarily fixed: you can reprogram the processing unit so that the robot performs a different task each time. Moreover, that task can depend on the information the microcontroller receives via the inputs, but if the program on the microcontroller does nothing with it, this information has no effect.  
Curious what your drawing robot can do? You will program it to make a drawing over and over again.