---

hruid: m_ct03_36c
version: 3
language: en
title: "Pythagoras - route planner"
description: "Calculate the straight-line distance in New York"
keywords: ["Pythagoras", "route planner", "distance", "triangle"]
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
New York. What is the straight-line distance from Times Square to the Empire State Building, expressed in kilometers?<br>

![Map and GPS New York](newyork.png) </context> <decomposition>
**Decomposition**<br>

<ul>
    <li>Summarize the problem in a diagram.</li>
    <li>Identify the given data and mark it on the diagram (the lengths of the two legs according to the route planner).</li>
    <li>The problem can be solved using the Pythagorean theorem. Determine which formula is needed: calculate the hypotenuse from the two legs.</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>New York's street grid shows a rectangular pattern.</li>
    <li>The depicted triangle is a right triangle; the straight-line distance is the hypotenuse.</li>
    <li>The problem is similar to previously solved Pythagoras exercises: calculate the hypotenuse from two known legs.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
<ul>
    <li>The map and streets are an abstraction of reality. Intersections and buildings are projected as sides of a right triangle, where the desired distance corresponds to the hypotenuse.</li>
</ul>
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
<ul>
    <li>Ask the user for the lengths of the two legs.</li>
    <li>Calculate the hypotenuse using the formula: c = √(a² + b²).</li>
    <li>Display the result in kilometers.</li>
</ul>
</algorithms>
<implementation>
**Program in Python**<br>
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
import math<br><br>
# input<br>
a = float(input("Length of the first leg in km: "))<br>
b = float(input("Length of the second leg in km: "))<br><br>
# processing<br>
c = math.sqrt(a**2 + b**2)<br><br>
# output<br>
print("The straight-line distance is: ", c, "km")
</p></div>
</implementation>
