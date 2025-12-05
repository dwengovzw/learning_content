---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Algorithmic thinking
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct08_05
keywords:
- ''
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
- 12
- 13
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: true
title: Algorithmic thinking
version: 3
---
# Algorithmic thinking

*Students devise a systematic way to solve the (sub)problem. That systematic way is a set of sequential, unambiguous steps in the required order.*

**Example**<br>
In the automation of a drawbridge, a possible algorithm looks as follows:

* If the sensor on the bridge detects an incoming boat, then:

    - the traffic lights on the roadway for through traffic (cars, cyclists, etc.) must be set to red;
    - 'x' minutes must be waited to allow traffic on the bridge to clear;
    - the barriers must close;
    - the bridge's motor may start to raise the bridge;
    - the motor must stop when the bridge is up;
    - the signal for the boat must be set to 'may proceed'.
    
* When the boat is through and the sensor detects the outgoing boat, then:
    -  ...