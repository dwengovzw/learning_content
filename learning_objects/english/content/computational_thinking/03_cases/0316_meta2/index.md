---

hruid: m_ct03_16b
version: 3
language: en
title: "Route Planner"
description: "Route Planner"
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
New York. What is the straight-line distance from Times Square to the Empire State Building, expressed in miles? 
</div>
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Enlist the help of a computer → use a route planner, e.g., Google Maps.</li>
    <li>Indicate Times Square and the Empire State Building.</li>
    <li>Mark what is known on the figure.</li>
    <li>Find the lengths of the two sides of the right triangle in the given route.</li>
    <li>Apply the Pythagorean theorem.</li>
</ul>

![image](https://user-images.githubusercontent.com/48352335/206760776-a6f57eda-9706-4571-926d-5dcabc4bdd5e.png)

![image](https://user-images.githubusercontent.com/48352335/206760809-189326b9-00cc-43b9-be6b-924847648eb6.png)

![image](https://user-images.githubusercontent.com/48352335/206760823-a837820a-2010-4cb1-95c5-6818671f4867.png)

</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>The street map shows a pattern: the streets form a rectangular grid.<br>
    The straight-line distance can therefore be determined as the hypotenuse of a right triangle.<br><br>
    Recognizing that the problem is related to a previously solved problem: this exercise is of the type where the hypotenuse is calculated when the two sides are known.</li>
    <li>In the route planner, streets, squares, parks ... are represented in a certain way. Recognizing what streets, parks ... are is a form of pattern recognition.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
The street map of New York is an abstraction of the city. 
The building and the square are abstracted as a point on the map.
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
Calculate the square root of the sum of the squares of the right triangle’s sides.
</algorithms>
<implementation>
**Program**<br>
The use of the computer is limited to using the route planner. No programming is done.
</implementation>
