---

hruid: m_ct03_46a
version: 3
language: en
title: "How a Route Planner Works"
description: "Functioning of a route planner"
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
You know the distances in km between certain towns along major roads and as the crow flies: Ghent, Lokeren, Sint-Niklaas, Dendermonde, Willebroek, Mechelen. Determine the shortest route between Ghent and Mechelen via these roads. How can a computer help with this?  
</context>
<decomposition>
**Decomposition**<br>
<ul>
    <li>Which roads are possible? To see this, it is best to look at a graphical representation, here we choose a graph.
        <ul>
            <li>A new type of graph is needed: a weighted graph.</li>
        </ul>
    </li>
    <li>From which parts are the roads composed? In other words, which towns are passed through?</li>
    <li>Total distance is the sum of the distances between the chosen towns.</li>
    <li>A computer can calculate the distances of all possible routes and select the shortest one.</li>
</ul>
</decomposition>
<patternRecognition>
**Pattern Recognition**<br>
<ul>
    <li>The roads between towns form a network. A network can be represented using a graph. Think, for example, of a social network graph.</li>
    <li>Here there is an additional complexity: the length of the roads, which also needs to be represented.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstraction**<br>
A graph is used as an abstract representation of the possible roads between towns.<br>
The given table should be converted into a weighted graph: the towns are the nodes and the roads between them are the edges, each edge assigned a weight equal to the distance.
</abstraction>
<algorithms>
**Algorithmic Thinking**<br>
<ul>
    <li>Dijkstra’s algorithm</li>
    <li>A* algorithm because not all roads need to be considered, e.g., roads through towns that are out of the way are unnecessary to check.</li>
</ul>
Describe the algorithm in words (and optionally implement it in code).  
</algorithms>
<implementation>
**Program**<br>
<ul>
    <li>Python script for Dijkstra’s algorithm</li>
    <li>Python script for the A* algorithm</li>
</ul>
See the notebooks in the learning path ‘Graphs’ for details.
</implementation>
