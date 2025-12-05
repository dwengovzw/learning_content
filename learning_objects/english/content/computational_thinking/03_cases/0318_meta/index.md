---

hruid: m_ct03_18
version: 3
language: en
title: "Sonar Sensor"
description: "Sonar Sensor"
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
**Problem Statement**<br>
Reflect on the operation of the sonar sensor from the principles of computational thinking. (1)
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>What is echolocation?
    <li>What is the speed at which the signal travels?
    <li>What is the relationship between speed, distance, and time?
        <ul>
            <li>What does this mean for the distance between the sonar and the object?
            <li>How can you calculate that distance?
            <li>In which unit is the distance expressed?
        </ul>
    </li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>Operation of sonar according to the principle of echolocation: sending out and receiving a sound signal.
    <li>The sonar sensor is an input element.
    <li>The measured time is processed by the computing unit into a distance in cm.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>Formula to convert the measured time into distance in meters: x = 340 * (∆t/2), with x the distance in meters and ∆t the measured time in seconds between sending and receiving the sound signal.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
<ul>
    <li>Calculate the distance from the measured time.
    <li>The distance is given by the sonar in cm, so the distance in meters is multiplied by 100.
    <li>Thus: distance = 340 * (time interval / 2) * 100, with distance in centimeters and time in seconds.</li>
</ul>
</algorithms>
<implementation>
**Program**<br>
No programming is done in this activity.
</implementation>
