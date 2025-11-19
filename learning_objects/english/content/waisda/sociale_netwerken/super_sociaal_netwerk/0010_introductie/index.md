---
content_type: text/markdown
copyright: CC BY dwengo
description: Learn how to extract information from a social network.
estimated_time: 10
hruid: org-dwengo-waisda-sociale-netwerken-super-sociaal-netwerk-introductie
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
title: Introduction
version: 1
---
# Social networks

We share quite a lot of our personal information on social networks. You may not realize it, but the owners of these social networks use your information to make money. They can do this, for example, by showing you personalized advertisements or by selling insights about the users to other companies. To analyze their users' information, social media platforms use various data analysis techniques. These techniques, for instance, look for friend groups or identify which people have a lot of influence within the network.  

## The social graph

A social graph, or *social graph*, is a way to represent data about the users in a social network. Each node in such a graph represents a person. Between two nodes there is a connection (an edge) if those two people are friends with each other. Below you can see an example of a social graph.

!["Example of a social graph."](img/voorbeeld_sociale_graaf.svg)

In the rest of this activity, you will see how you can learn things from this graph.

<div class="dwengo-content assignment">
<h2 class="title">Assignment</h2>
<div class="content">
Try to answer the following questions.
<ul>
<li>Which friend groups can you extract from the graph?</li>
<li>Which people in this network are highly influential? A person is influential when their posts can be read by many people.</li>
<li>Which people are farthest apart? </li>
</ul>
</div>
</div>




<div class="dwengo-content sideinfo">
<h2 class="title">Unsupervised learning</h2>
<div class="content">
Unsupervised or <em>unsupervised</em> learning is an AI technique that computer scientists use to try to extract new information from data, such as finding friend groups in a social graph. In contrast to supervised (<em>supervised</em>) learning, unsupervised learning does not operate based on labeled examples. So you do not have a training set to train a model.  
</div>
</div>