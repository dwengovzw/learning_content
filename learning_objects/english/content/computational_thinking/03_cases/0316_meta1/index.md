---

hruid: m_ct03_16a
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
New York. What is the straight-line distance from Times Square to the Empire State Building, expressed in miles?
</div>
</context>
<decomposition>
**Decomposition**
<ul>
    <li>Enlist the help of a computer <span style="color: yellowgreen">→ use a route planner, e.g., Google Maps.</span>
    <li>Indicate Times Square and the Empire State Building.</li>

![image](https://user-images.githubusercontent.com/48352335/206757334-ebdad093-2ee7-493c-9d53-2c14c598115c.png)

</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
In the route planner, streets, squares, parks ... are represented in a certain way. Recognizing what streets, parks ... are is a form of pattern recognition.
</patternRecognition>
<abstraction>
**Abstraction**<br>
The street map of New York is an abstraction of the city. 
The building and the square are abstracted as a point on the map.
</abstraction>
<algorithms>

</algorithms>
<implementation>
**Program**<br>
Have the computer determine the solution using Google Maps functionality: 'measure distance'.<br>
![image](https://user-images.githubusercontent.com/48352335/206757540-f5205128-03b3-46e4-adac-09efecb53a39.png)
</implementation>
