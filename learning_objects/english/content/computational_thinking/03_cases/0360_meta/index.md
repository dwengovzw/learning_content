---

hruid: m_ct03_60
version: 3
language: en
title: "Pregnancy Test"
description: "Pregnancy Test"
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
---

<context>
**Problem Statement**<br>
A pregnancy test can be easily performed at home. They exist in non-digital and digital forms. Unravel how a digital pregnancy test works and compare it with a non-digital test.
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>What components make up a digital pregnancy test?
        <ul>
            <li>A stick to be in contact with urine, with a substance that reacts based on the presence of pregnancy hormones.</li>
            <li>Inside the device, a paper strip shows a control line if the test is correctly performed and a second line appears if the urine reacts.</li>
            <li>A sensor detects whether a reaction has occurred (color sensor).</li>
            <li>A microcontroller that displays the result.</li>
            <li>A display showing the test result (text or symbol).</li>
        </ul>
    </li>
    <li>What happens during the test and what is the role of the computer?</li>
    <li>What is the input and output of the digital test?</li>
    <li>What are the differences between the digital and non-digital tests?</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>Input → processing → output.</li>
    <li>The procedure for non-digital and digital tests is almost identical.</li>
    <li>In both, the input is a urine sample and the output is a message.</li>
    <li>Both tests have a paper strip showing a control line. In digital tests, the strip is inside the device. In both, the urine may or may not react with the substance. If a reaction occurs, a second line appears.</li>
    <li>The microcontroller receives input from the sensor. The color sensor measures if the second line is colored. This input tells the microcontroller whether the test is positive or not, which it then processes and outputs the corresponding message on the display.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>The digital value, a sequence of zeros and ones from the sensor to the microcontroller, is an abstraction of the paper strip result.</li>
    <li>The test result is often represented abstractly by a symbol: one or two lines, plus or minus, etc.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
<ul>
    <li>The test is performed according to the steps in the manual.</li>
    <li>Non-digital test algorithm:<br>
    IF urine reacts with the substance<br>
    THEN display 2 lines<br>
    ELSE display 1 line</li>
    <li>Digital test algorithm:<br>
    IF sensor value = 1<br>
    THEN show 'PREGNANT' on the screen<br>
    ELSE show 'NOT PREGNANT' on the screen</li>
</ul>
</algorithms>
<implementation>
**Program**<br>
This is an activity without programming.
</implementation>
