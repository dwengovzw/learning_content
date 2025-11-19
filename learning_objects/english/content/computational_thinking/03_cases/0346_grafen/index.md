---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Graph applications
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct03_46
keywords:
- ''
language: en
licence: dwengo
return_value:
  callback_schema:
    att: test
    att2: test2
  callback_url: callback-url-example
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
target_ages:
- 12
- 13
- 14
teacher_exclusive: true
title: Applications of graphs (2,3)
version: 3
---
# Applications of graphs

**A graph as a data structure in two problems with different contexts.** 

Here you look at some applications of graphs: how a route planner works and fingerprint matching. These examples are part of a lesson series on graph theory.

**Target group:** Students in the 2nd and 3rd stage, transfer finality and dual finality (tracks yet to be determined).

**Subject:** /

**Prior knowledge:** The students already know some types of graphs (simple graph, directed graph, path, walk, cycle).

**Goal:** Students realize that you can sometimes arrive at a solution faster if you abstract the data to a graph. In these examples, a new type of graph is needed.

### How a route planner works

You know the distances in km between certain municipalities along major roads and as-the-crow-flies: Ghent, Lokeren, Sint-Niklaas, Dendermonde, Willebroek, Mechelen. Determine the shortest route between Ghent and Mechelen via these roads? How can a computer help with that?  
![image](https://user-images.githubusercontent.com/48352335/213927739-9b9c0801-bdb0-4692-af36-eafa8f172864.png)
![image](https://user-images.githubusercontent.com/48352335/213927749-83781385-10f4-43f4-9d28-10bfc20d3700.png)

![ct-schema](@learning-object/m_ct03_46a/nl/3)

This example is an introduction to Dijkstra's algorithm and how it is applied in practice. 

### Matching fingerprints

![ct-schema](@learning-object/m_ct03_46b/nl/3)



For more information, see the learning path ['Graphs'](https://www.dwengo.org/learning-path.html?hruid=aiz2_grafen&language=nl&te=true&source_page=%2Fcare%2F&source_title=%20AI%20in%20de%20Zorg#aiz_sprouts;nl;3) in the project [AI in Healthcare](https://www.dwengo.org/care/) or at [Python in the Math Lesson](https://www.dwengo.org/math_with_python/).