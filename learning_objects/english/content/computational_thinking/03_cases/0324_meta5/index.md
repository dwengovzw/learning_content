---

hruid: m_ct03_24e
version: 3
language: en
title: "Social Robot"
description: "Social Robot"
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
Translate the desired actions into a program in the simulator.<br>
For example, the student chose: <br>
<ul>
    <li>If someone comes closer than 30 cm, the robot waves both hands and must wink.</li>
    <li>Otherwise, it does not wave and its eyes remain wide open.</li>
    <li>If someone claps their hands, the message ‘Hello! How are you?’ appears.</li>
</ul>
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Split per action</li>
    <li>Determine the input elements for each action</li>
    <li>Determine the output elements for each action</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>Choice structure is similar for the different 'if-then' actions</li>
    <li>Sending eye open signal is analogous to closing the eyes</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>Waving hands = control servomotors</li>
    <li>Eyes = LED matrices</li>
    <li>Clapping hands = detect sound (note: detect all sounds!)</li>
    <li>Simulation is an abstraction of what the robot will do in reality</li>
    <li>...</li>
</ul>
</abstraction>
<algorithms>
**Algorithm**<br>
IF someone comes closer than 30 cm<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN robot waves both hands and winks <br>
ELSE does not wave and eyes remain wide open <br>
IF someone claps hands<br>
&nbsp;&nbsp;&nbsp;&nbsp;THEN display message ‘Hello! How are you?’<br>
</algorithms>
<implementation>
**Program**<br>
Place a screenshot of the Blockly code here.
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
code
</p>
</div>
</implementation>
