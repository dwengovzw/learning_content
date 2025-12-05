---

hruid: m_ct03_62
version: 3
language: en
title: "SIR"
description: "SIR"
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
![COVID-19 Measures](covid19maatregelen.png)<br>
*Outdoor plan March 5, 2021*.<br>Image © NCCN, Brussels, Belgium.
<div style="position:absolute;right:0px;width:40%;height:100px;margin-top:-100px;margin-right:20px">
Can we estimate the effect of COVID-19 measures before implementing them?
</div>
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Model for disease spread</li>
    <li>Represent human interactions</li>
    <li>Simulate the spread using the model</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
The spread of plague, cholera, COVID-19, etc., behaves similarly. We distinguish: susceptible individuals, infected individuals, and resistant individuals.<br><br>
Interactions between people can be represented similarly to connections between cities (roads), i.e., using a graph.
</patternRecognition>
<abstraction>
**Abstraction**<br>
We abstractly represent human interactions with a graph.
    ![Social Network](sociaalnetwerk.png)
The changes in the numbers of susceptible, infected, and resistant individuals are abstractly represented with differential equations.  
![System of differential equations epidemic](differentiaalvergelijkingenepidemie.png)
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
<ol>
    <li>Define the SIR model with a system of differential equations (as shown on the left)</li>
    <li>Choose the composition of the initial population</li>
    <li>Choose the infection rate</li>
    <li>Choose the recovery rate</li>
    <li>Choose a time interval</li>
    <li>Solve the system numerically</li>
</ol>
</algorithms>
<implementation>
**Program**<br>
See the notebooks in the learning path 'Epidemic'.
</implementation>
