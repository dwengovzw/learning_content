---
content_type: text/markdown
copyright: CC BY dwengo
description: Learn how to extract information from a social network.
estimated_time: 10
hruid: org-dwengo-waisda-sociale-netwerken-super-sociaal-netwerk-vriendengroepen
keywords:
- Sociale netwerken
- grafen
- AI
- Unsupervised learning
- clusters
- vriendengroepen
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
title: Friend groups
version: 1
---
# Friend groups

Groups of people who are strongly connected to each other are often friend groups. Between these groups there are also regularly one or more connections. For example, you have friends at school, but also friends in your sports club or youth organization. You are then the link between the friend group at school, the one in the sports club, and the one in the youth organization. 

## Community detection

Methods to find friend groups in graphs are called techniques for *community detection*. There are several techniques for this. One method was devised by the Belgian mathematician Vincent Daniel Blondel at UCL. That is why it is also called the **Louvain method**. This method will compute the *modularity* of the graph where each node is its own community. The algorithm then merges nodes into communities in such a way that the modularity of the graph increases. The algorithm keeps repeating this until the modularity no longer increases.