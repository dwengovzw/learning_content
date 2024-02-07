---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: When we want to process data with a computer, we need to represent it
  in a data structure.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 3
hruid: org-dwengo-elevator-riddle-analyzing-2
keywords:
- grafen
- algoritme
- computationeel denken
- clustering
- datastructuur
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
- 16
- 17
- 18
teacher_exclusive: false
title: Choosing a Data Structure
version: 1
---
# Choosing a Data Structure

Representing the problem with a known data structure allows us to use all the algorithmic techniques that exist for that data structure. Therefore, choosing an appropriate data structure can make it easier to solve the problem.

|  | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** |
| ----------- | ----------- |----------- | ----------- |----------- | ----------- |----------- | ----------- |----------- |
| **4** | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| **5** | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 3 | 
| **6** | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 
| **7** | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 4 | 
| **8** | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 
| **9** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 
| **10** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **11** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |


If you already have some knowledge of computer science, this type of matrix may look familiar to you. After all, this matrix has the same structure as the arc matrix or adjacency matrix of a graph (**pattern recognition**). We can therefore also represent this matrix graphically as a graph (Figure 1). A graph is a collection of nodes (= the circles), which are connected by arcs (= the lines between the circles). A knot represents a floor. An arc represents the number of moves between the two adjacent nodes/floors.

| ![Graphical representation of the graph with movements between the floors.](embed/verplaatsingen_chaos_with_labels.png "Graphical representation of graph with movements between floors.") | 
| ---- |
| **Figure 1**: Represents movements between floors as a graph. |