---

hruid: m_ct03_24c
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
Realize a social robot based on your own design.
</context>
<decomposition>
**Decomposition**<br>
Students break down the assignment into the different phases/steps they must go through in the create-realize-evaluate process.
<ul>
    <li>(Create a plan)</li>
    <li>Sketch of the design 'Robot body and actions' that meets the criteria and desired actions</li>
    <li>Technical information: sensors and actuators</li>
    <li>Transfer drawing to the chosen medium</li>
    <li>Program action(s) in the simulator based on the written algorithm</li>
    <li>Test the program in the simulator, evaluate and adjust</li>
    <li>Test actions using the hardware</li>
    <li>Assemble components on the robot body</li>
    <li>Test and evaluate the complete system</li>
    <li>(Optimize)</li>
</ul>

![schetsontwerp](schetsontwerp.png) </decomposition> <patternRecognition>

</patternRecognition>
<abstraction>
**Abstraction**<br>
Angle or speed of a servo motor is abstracted to an integer from -255 to 255.
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
Represent the robot's action(s) in an algorithm (This can be written in pseudocode, described in a sentence ...)<br>
![schetsalgoritme](schetsalgoritme.png)<br>
The decomposition provides the step-by-step plan to follow.
</algorithms>
<implementation>
**Program**<br>
Place a screenshot of the Blockly code here.
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
text
</p></div>
</implementation>
