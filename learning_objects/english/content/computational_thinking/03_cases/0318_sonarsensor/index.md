---
available: true
content_type: text/markdown
copyright: dwengo
description: Sonar sensor
difficulty: 3
estimated_time: 1
hruid: ct03_18
language: en
licence: dwengo
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
target_ages:
- 12
- 13
- 14
teacher_exclusive: true
title: Sonar sensor (1)
version: 3
---
# How the sonar sensor works

A sonar sensor measures the distance to an object. To do this, it uses ultrasonic sounds that are reflected by objects. By measuring the time between sending and receiving the sound signal, you can use a formula to calculate the distance to the object very precisely. In this case study, your students reflect on how the sonar sensor works based on the principles of computational thinking.

**Target group:** First stage A and B stream

**Subject:** ...

**Prior knowledge:**<br>
* The students know the concept of speed
* Optionally, the students know that speed is a ratio of distance to duration

A possible course of the case study is as follows:<br><br>

*Phase 1: lesson about echolocation*<br>
<ul>
    <li>Bats detect prey and obstacles via echolocation. The bat emits a sound signal. It is reflected by the object, after which the bat picks it up again.
    <li>Scientists were inspired by this to design an electronic component that can automatically determine the distance to an object.</li>
</ul>

*Phase 2: the sonar works exactly like that*<br>
<ul>
    <li>You explain to the students that the sonar works according to the principle of echolocation.
    <li>If students understand that, then through pattern recognition they should be able to conclude that the sonar will have to emit and receive an (ultrasonic) sound signal.
    <li>The students fill in the diagram with the basic concepts.</li>
</ul>

*Phase 3: formula*<br>
<ul>
    <li>The speed of sound is about 340 meters per second.
    <li>Calculate the distance for a given time interval from transmission to receiving the signal again. The students use the correct units for time and distance.
    <li>The students devise a formula to calculate the distance, which could be programmed into the processing unit of the digital system.
    <li>The students further complete the diagram with the basic concepts.</li>
</ul>

![ct-schema](@learning-object/m_ct03_18/en/3)