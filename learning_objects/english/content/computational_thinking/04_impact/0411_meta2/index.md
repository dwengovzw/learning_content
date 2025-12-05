---

hruid: m_ct04_11b
version: 3
language: en
title: "Automatic tap"
description: "Automatic tap"
keywords: [""]
educational_goals: [
    {source: Source, id: id},
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/ct-schema
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
    '[http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen](http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen)'
]
teacher_exclusive: true
-----------------------

<context>
**Problem statement**<br>
**EXTRA** Design a device that activates when your hand is less than 10 cm away from it, but without touching it.
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Exploring the problem:
        <ul>
            <li>choose which device you will design, for example an LCD screen on which “Hello there” appears when your hand comes close enough to the device.
            <li>choose a suitable sensor: with which types of sensors can you determine a distance? How does this work?
            <li>find out how you can make the message disappear after a certain amount of time.</li>
        </ul>
    <li>What do you need? How can you realize this?
        <ul>
            <li>Microcontroller platform with LCD screen
            <li>Motion sensor (PIR sensor) or distance sensor (sonar sensor or infrared sensor)</li>
        </ul>
    </li>
    <li>Approach:
        <ul>
            <li>How do you connect the sensor to the platform?
            <li>Write a program to control the microcontroller. (What is the input? What is the output? Which unit do you use for the distance?)</li>
        </ul>
    </li>
</ul>
</decomposition>
<patternRecognition>
**Pattern recognition**<br>
<ul>
    <li>In the toilets of restaurants, hotels, schools, etc., taps, soap dispensers and towel dispensers often work in the same way; they are activated via a sensor, without being touched.
    <li>Automatic sliding doors also work in a similar way.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>The sensor determines the distance to an object. No distinction is made as to whether it is a hand or not.
    <li>In the program, you can abstract the calculated distance by using a variable.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic thinking**<br>
<ul>
    <li>IF distance from sensor to object < 10 cm<br>
        THEN the text “Hello there” appears on the LCD screen<br>
        ELSE empty LCD screen</li>
    <li>This instruction must be repeated continuously to check whether there is a hand nearby and whether it has moved away again, because then the message must disappear.</li>
</ul>
</algorithms>
<implementation>
**Program**<br>
You can program the Dwenguino textually or in a block-based programming environment with a simulator.
You can therefore optionally limit this assignment to the simulator; in that case, work in the “Social robot” scenario.
</implementation>
