---
content_type: text/markdown
copyright: CC BY dwengo
description: How do I represent a graph on the computer and how can I find the Eulerian
  path in that graph?
estimated_time: 50
hruid: org-dwengo-waisda-soc-netwerken-graaf-zelf-programmeren
keywords:
- grafen
- Euleriaans pad
- koningsbergen
- voorstellingen
- python
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
title: Programming yourself
version: 1
---
# Programming graphs yourself

By now you know how to represent a graph on the computer and what an Eulerian path is in that graph. In the next notebook you will get hands-on with different graphs. You will represent them using their adjacency list, check whether they contain an Eulerian path, and you will find such a path using Fleury's algorithm. Be sure to watch the video about Fleury's algorithm first to understand how it works.

![](@youtube/https://www.youtube.com/embed/R9FA5VkfHrw?si=d64v4-WPlQvYVEFp "video")


[![](images/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=waisda_sociale_netwerken_euler_en "Notebook transfer learning")


<div class="dwengo-content sideinfo">
<h2 class="title">Graphs and AI</h2>
<div class="content">
The connection between graphs and AI systems may not be entirely clear yet. Still, graphs are often used in AI systems because they are a good way to structure information. For example, we can represent information and the relationships between them with a <strong>knowledge graph</strong> (<strong>knowledge graph</strong> in English). <br>
For example, we can represent all the information on Wikipedia with such a knowledge graph. The articles are then the nodes of the graph, and the edges of the graph are the hyperlinks between the articles. <br>
You can also represent information from social networks using a graph, the <strong>social graph</strong>. In a social graph, the nodes are, for example, people. If two people are friends, there is an edge in the graph that connects them. 
</div>
</div>