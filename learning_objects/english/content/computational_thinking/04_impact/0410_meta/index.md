---

hruid: m_ct04_10
version: 3
language: en
title: "Pregnancy test"
description: "Pregnancy test"
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
A pregnancy test can easily be performed at home. You can find them in non-digital and digital form. Unravel the functioning of a digital pregnancy test. Compare this functioning with that of a non-digital pregnancy test.  
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Which components does a digital pregnancy test consist of?
        <ul>
            <li>A strip to bring into contact with urine. A specific substance on that strip with which the urine may or may not react based on the presence of pregnancy hormones.
            <li>Inside the device there is a paper strip on which a control line appears if the test was performed correctly and a second line appears if there is a reaction with the urine sample.
            <li>A sensor that detects whether or not a reaction has taken place. What kind of sensor is that? (color sensor)
            <li>A microcontroller that displays the result on the display.
            <li>A display on which the result of the test appears (via text or via a symbol).</li>
        </ul>
    <li>What happens during such a test? What is the role of the computer in this?
    <li>What is the input and what is the output of the digital test?
    <li>What are the differences between the digital and the non-digital version of a pregnancy test?</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern recognition**<br>
<ul>
    <li>Input – processing – output
    <li>The use of a non-digital and a digital test proceeds in almost the same way.
    <li>In both cases, the input is a urine sample and the (ultimate) output is a message.
    <li>Both tests contain a paper strip on which a control line appears. In the digital test this is located inside the device. In both cases, the urine sample may or may not react with a specific substance present in the measuring device. If this reaction takes place, a second line appears on the paper strip.
    <li>The microcontroller receives input from the sensor. For this, the color sensor measures whether the second line is colored or not. The sensor thus inputs to the microcontroller whether the test is positive or not. The microcontroller will process this input and pass on which message should appear as output on the display.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>The digital value, a sequence of zeros and ones, that the sensor returns to the microcontroller is an abstraction of the result on the paper strip.
    <li>The result of a pregnancy test is often represented in an abstract way by a symbol: one or two lines, a plus or minus sign, etc.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic thinking**<br>
<ul>
    <li>Performing the test itself follows the step-by-step plan described in the manual.
    <li>Algorithm for the non-digital test:<br>
    IF the urine reacts with the substance<br>
    THEN 2 lines<br>
    ELSE 1 line
    <li>Algorithm for the digital test:<br>
    IF sensor value is 1<br>
    THEN show 'PREGNANT' on the screen<br>
    ELSE show 'NOT PREGNANT' on the screen</li>
</ul>
</algorithms>
<implementation>
**Program**<br>
This is an activity in which no programming is required.
</implementation>
