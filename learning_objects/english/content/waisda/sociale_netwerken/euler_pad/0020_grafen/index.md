---
content_type: text/markdown
copyright: CC BY dwengo
description: What are graphs and what do our drawings have to do with them?
estimated_time: 5
hruid: org-dwengo-waisda-soc-netwerken-graphs-netwerk-grafen
keywords:
- grafen
- Euleriaans pad
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
title: Grafen
version: 1
---
# Graphs

Did you manage? Were you able to make all the drawings without lifting your ballpoint pen? Or did some figures not work out for you? For many drawings it can be very difficult to find a solution by simply trying out possibilities. Yet there is a trick that can help you find the solution more easily. This trick comes from graph theory. 


<div class="dwengo-content sideinfo">
<h2 class="title">What is a graph?</h2>
<div class="content">
A graph is a structure that consists of <strong>nodes</strong> and any connections between those nodes, the <strong>edges</strong>.
</div>
</div>

Here you see an example of a graph with **two nodes** and **one edge** between them.

![](img/simple_twonode.svg)

The drawings we tried to make can also be represented as graphs. In the following table you see the drawing on the left and the representation as a graph on the right.

| Drawing | Graph |
|-|:-:|
| ![](img/euler1.svg) | ![](img/euler1_graph.svg) |
| ![](img/euler2.svg) | ![](img/euler2_graph.svg) |
| ![](img/euler3.svg) | ![](img/euler3_graph.svg) |
| ![](img/euler4.svg) | ![](img/euler4_graph.svg) |


Our initial problem, in which we want to make a drawing without lifting our ballpoint pen, can thus be translated into a graph problem. We formulate this problem as follows. Does there exist a *walk* in the graph in which you traverse each edge exactly once?

<div class="dwengo-content sideinfo">
    <h2 class="title">Isomorphism</h2>
    <div class="content">
        Unlike our drawings, the positions of the nodes of the graph are not important. You can draw the nodes of the graph anywhere as long as they remain connected via edges to the same nodes. These different versions of the graph are <strong>isomorphic</strong>. Below you can see, for example, a number of possible graph representations for the house.
        <table>
            <tr><td><img src="img/euler1_graph.svg"></img></td></tr>
            <tr><td><img src="img/euler1_graph_var2.svg"></img></td></tr>
            <tr><td><img src="img/euler1_graph_var3.svg"></img></td></tr>
            <tr><td><img src="img/euler1_graph_var4.svg"></img></td></tr>
        </table>
    </div>
</div>


<div class="dwengo-content sideinfo">
<h2 class="title">The Mercedes challenge</h2>
<div class="content">
<table>
<tr>
<td><img src="img/Mercedes-Benz_free_logo.svg"></td>
<td><p>The Mercedes challenge is a puzzle that went viral on TikTok. The challenge is said to have started at a Mercedes dealership in Dubai. There, a large Mercedes logo was drawn on the floor. Visitors to the dealership were challenged to walk along all the lines of the logo without walking over the same line twice. When they succeeded, they won a car. </p></td>
</tr>
</table>

<p>Go find a video of the <em>Mercedes Challenge</em> yourself. Can you manage to walk over the lines of the logo in the correct way?</p>
</div>
</div>


**Why is it useful to represent our drawings as graphs?**


A graph is an abstract representation that we can use for many problems. That is why many clever mathematicians and computer scientists have already thought about the properties of those graphs. We can use their knowledge to solve our drawing problem.

You might not expect it, but our drawing problem closely matches the problem of the Seven Bridges of Königsberg.