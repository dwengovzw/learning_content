---

hruid: m_ct03_36b
version: 3
language: en
title: "Pythagoras - Hypotenuse with Function"
description: "Pythagoras - Hypotenuse using a function"
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
![Triangle1](pyth1.png)<br>
<br>
**Problem Statement**<br>
Automate the calculation of the hypotenuse of a right triangle when the lengths of the legs are known. Ask the user for the necessary input.
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li><p style="color: Gray">Create an algorithm to calculate the hypotenuse using the Pythagorean theorem.</p></li>
    <li><p style="color: Gray">Implement the algorithm on a computer (software choice, e.g., Python).</p></li>
    <li><p style="color: Gray">Ensure the user can enter the lengths of the triangle's legs.</p></li>
    <li><p style="color: Gray">Choose an appropriate datatype for the sides (int or float).</p></li>
    <li><p style="color: Gray">Ensure the output is displayed correctly after processing.</p></li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li><p style="color: Gray">Input → Processing → Output</p></li>
    <li>If the same calculation needs to be repeated frequently, it is useful to encapsulate it in a function.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li><p style="color: Gray">Only the fact that the triangle is right-angled and the lengths of its legs matter.</p></li>
    <li>By encapsulating the calculation in a user-defined function, you can reuse it multiple times without worrying about the details.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
<p style="color: Gray">The program contains (in this order) instructions to:</p>
<ol>
    <li><p style="color: Gray">ask the user for input;</p></li>
    <li><p style="color: Gray">process the input to calculate the hypotenuse using the function;</p></li>
    <li><p style="color: Gray">display the length of the hypotenuse on the screen.</p></li>
</ol>
</algorithms>
<implementation>
**Python Program**
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
import math<br>
def pythagoras(a, b):<br>
&nbsp;&nbsp;&nbsp;&nbsp;"""Calculate hypotenuse from given legs."""<br>
&nbsp;&nbsp;&nbsp;&nbsp;return math.sqrt(a**2 + b**2)<br><br>
# input<br>
leg1 = float(input("Length of the first leg: "))<br>
leg2 = float(input("Length of the second leg: "))<br><br>
# processing<br>
hypotenuse = pythagoras(leg1, leg2)<br><br>
# output<br>
print("The length of the hypotenuse is: ", hypotenuse)
</p>
</div>
</implementation>
