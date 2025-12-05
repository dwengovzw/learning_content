---

hruid: m_ct03_36d
version: 3
language: en
title: "Pythagoras - fixed values"
description: "Automate Pythagoras calculation with fixed sides"
keywords: ["Pythagoras", "triangle", "hypotenuse", "Python"]
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
![Triangle1](pyth1.png)<br>
<br>
**Problem statement**<br>
Automatically calculate the hypotenuse of a right triangle when the legs are known, using fixed values in the program.
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Create an algorithm to calculate the hypotenuse using the Pythagorean theorem.</li>
    <li>The input is now fixed values in the program instead of user input.</li>
    <li>Choose the appropriate datatype for the sides (float or int).</li>
    <li>Display the output neatly.</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>The process remains Input → Processing → Output, even though the input is predefined.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>It is only important that the triangle is right-angled and the values of the legs are known.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
<ul>
    <li>Use the fixed values of the triangle legs.</li>
    <li>Calculate the hypotenuse with the formula c = √(a² + b²).</li>
    <li>Display the result on the screen.</li>
</ul>
</algorithms>
<implementation>
**Program in Python**
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
import math<br><br>
# fixed values for the triangle legs<br>
rhz1 = 3  # length of the first leg<br>
rhz2 = 4  # length of the second leg<br><br>
# calculate hypotenuse<br>
schz = math.sqrt(rhz1**2 + rhz2**2)<br><br>
# output<br>
print("The length of the hypotenuse is: ", schz)
</p>
</div>
</implementation>
