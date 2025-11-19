---
content_type: text/markdown
copyright: CC BY dwengo
description: What is the Eulerian path.
estimated_time: 5
hruid: org-dwengo-waisda-soc-netwerken-euleriaans-pad-opl
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
teacher_exclusive: true
title: Eulerian path (solution)
version: 1
---
# Eulerian path (solution)


<div class="dwengo-content assignment">
<h2 class="title">Assignment</h2>
<div class="content">
Count the number of edges that depart from each node (= the degree of the node) of the graph of Königsberg. Is it possible to find an Eulerian path in the graph?

<img src="images/koningsbergen_graph.svg"></img>

<strong>None of the nodes has an even degree. Therefore, it is impossible to find an Eulerian path in the graph.</strong>
</div>
</div>



<div class="dwengo-content assignment">
<h2 class="title">Assignment</h2>
<div class="content">
Look back at the following drawings. Which of these drawings can you draw without lifting your pen and which cannot?

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
    <td colspan=2><strong>Solution: </strong>There are two nodes with an odd degree. The rest of the nodes have an even degree. Consequently, an Eulerian path in the graph is possible.</td>
  </tr>
  <tr>
    <td>2</td>
    <td><img src="images/euler2_graph.svg" alt="Euler Graph 2"></td>
  </tr>
  <tr>
    <td colspan=2><strong>Solution: </strong>All nodes in the graph have an even degree. Consequently, an Eulerian path in the graph is possible.</td>
  </tr>
  <tr>
    <td>3</td>
    <td><img src="images/euler3_graph.svg" alt="Euler Graph 3"></td>
  </tr>
  <tr>
    <td colspan=2><strong>Solution: </strong>All nodes in the graph have an even degree. Consequently, an Eulerian path in the graph is possible.</td>
  </tr>
  <tr>
    <td>4</td>
    <td><img src="images/euler4_graph.svg" alt="Euler Graph 4"></td>
  </tr>
  <tr>
    <td colspan=2><strong>Solution: </strong>There are more than two nodes in the graph with an odd degree. Consequently, an Eulerian path in the graph is not possible.</td>
  </tr>
</table>
</div>
</div>