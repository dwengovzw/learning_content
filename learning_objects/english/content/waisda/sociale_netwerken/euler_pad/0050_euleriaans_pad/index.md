---
content_type: text/markdown
copyright: CC BY dwengo
description: What is the Eulerian path.
estimated_time: 10
hruid: org-dwengo-waisda-soc-netwerken-euleriaans-pad
keywords:
- grafen
- Euleriaans pad
- koningsbergen
language: en
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
- http://ilearn.ilabt.imec.be/vocab/tref1/ict
target_ages:
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: false
title: Eulerian path
version: 1
---
# Eulerian path

Leonhard Euler solved the Seven Bridges of Königsberg problem in 1736. Euler stated that a *walk* in the graph in which you cross each edge exactly once is only possible if:

 **Every vertex in the graph has an even number of edges, or there are exactly two vertices with an odd number of edges**.

Euler based his theorem on two observations:
1. If you have a graph in which every vertex has an even number of edges, you can never get stuck at a vertex other than the one where you started. This follows directly from the even number of edges of each vertex. If you arrive via one edge, there is always another to depart by. Otherwise, the number of edges would not be even.
2. If you have a graph with two vertices with an odd number of edges, you must start at one of the vertices and end at the other. For the other vertices, observation 1 applies, so you cannot get stuck.



<div class="dwengo-content assignment">
<h2 class="title">Assignment</h2>
<div class="content">
Count the number of edges leaving each vertex (= the degree of the vertex) of the Königsberg graph. Is it possible to find an Eulerian path in the graph?

<img src="images/koningsbergen_graph.svg"></img>
</div>
</div>



<div class="dwengo-content assignment">
<h2 class="title">Assignment</h2>
<div class="content">
Look back at the following drawings. Which of these drawings can you draw without lifting your ballpoint pen, and which cannot?

<table>
  <tr>
    <th>Image Number</th>
    <th>Image</th>
  </tr>
  <tr>
    <td>1</td>
    <td><img src="images/euler1_graph.svg" alt="Euler Graph 1"></td>
  </tr>
  <tr>
    <td>2</td>
    <td><img src="images/euler2_graph.svg" alt="Euler Graph 2"></td>
  </tr>
  <tr>
    <td>3</td>
    <td><img src="images/euler3_graph.svg" alt="Euler Graph 3"></td>
  </tr>
  <tr>
    <td>4</td>
    <td><img src="images/euler4_graph.svg" alt="Euler Graph 4"></td>
  </tr>
</table>
</div>
</div>