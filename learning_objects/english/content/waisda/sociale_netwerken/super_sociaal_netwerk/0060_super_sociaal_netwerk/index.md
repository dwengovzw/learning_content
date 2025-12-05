---
content_type: text/markdown
copyright: CC BY dwengo
description: Learn how to extract information from a social network.
estimated_time: 10
hruid: org-dwengo-waisda-sociale-netwerken-super-sociaal-netwerk-notebook
keywords:
- Sociale netwerken
- grafen
- AI
- Unsupervised learning
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
title: Super social network
version: 1
---
# The super social network

In the following notebook, you will explore a "super" social network yourself. The network contains an overview of all superheroes who have ever been part of a Marvel comic. In the network, there is a link between two characters when they have appeared together in a comic. If those characters appear together in multiple comics, that link receives a stronger weight. Below you can see an example of what a simple version of the super social network might look like.

!["Example super social network"](img/voorbeeld_sociale_graaf_min_dist.svg)

The nodes of this graph represent the superheroes. When there is an edge between two heroes, they appear together in a comic one or more times. The number next to the edge indicates in how many comics they appear together. 

<div class="dwengo-content assignment">
<h2 class="title">Assignment</h2>
<div class="content">
Look at the image of the super social network. Think about how you would detect communities in this graph. Which properties will you take into account?
</div>
</div>

Now get started yourself with the social network of the Marvel superheroes and discover what information you can extract from the network.

[![](img/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=waisda_sociale_netwerken_super_sociaal_netwerk_en "Notebook transfer learning")