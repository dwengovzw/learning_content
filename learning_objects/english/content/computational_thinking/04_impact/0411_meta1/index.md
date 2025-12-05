---

hruid: m_ct04_11a
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
How does a tap work that you can operate without touching it?
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>What must the device do?
        <ul>
            <li>When the device is activated: water flows from the tap.
            <li>After some time, the water must stop flowing.
            <li>Is the tap set to a specific flow rate or a specific duration?</li>
        </ul>
    <li>Identify components: type of sensor, microcontroller
    <li>What is the input? (Distance of hand to sensor)
    <li>What is the output? (Tap opens)</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern recognition**<br>
<ul>
    <li>All devices that are activated without being touched work with a sensor that detects something: distance to an object, movement, light, interruption of an infrared beam, etc. They are therefore controlled by similar computer programs. Examples include an automatic soap or towel dispenser, but also automatic sliding doors.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>The sensor determines the distance to an object. No distinction is made as to whether it is a hand or not.
    <li>The tap opens when the hand is close enough to the sensor. “Close enough” is an abstraction of the distance threshold you choose when programming the microcontroller.
    <li>When programming, you can abstract the calculated distance by using a variable.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic thinking**<br>
<ul>
    <li>IF something is close to the sensor<br>
        THEN the tap runs<br>
        ELSE the tap does not run
    <li>More abstract:<br>
        IF something is close to the sensor<br>
        THEN the device is activated<br>
        ELSE the device is not active
    </li>
</ul>
</algorithms>
<implementation>
**Program**<br>
This activity can be done without a computer.
If you choose to program, have your students complete the additional assignment. (see next section)
</implementation>
