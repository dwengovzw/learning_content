---
content_type: text/markdown
copyright: CC BY dwengo
description: Learn how to extract information from a social network.
estimated_time: 10
hruid: org-dwengo-waisda-sociale-netwerken-super-sociaal-netwerk-verst-van-elkaar
keywords:
- Sociale netwerken
- grafen
- AI
- Unsupervised learning
- diameter graaf
- dijkstra
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
title: Maximum distance
version: 1
---
# The maximum distance between two arbitrary people

The maximum distance between two arbitrary people in the network gives us information about how "spread out" the network is. A network with many nodes but a short maximum distance will be strongly cohesive. A network with few nodes but a large maximum distance is less cohesive. Parts of a network that are strongly cohesive often correspond to friend groups.

## The minimum distance between two people

To find the maximum distance between two arbitrary people, we must first find the minimum distance between every pair of people in the network. Below you can see the minimum path between Alexi and Jules. There are 3 arcs on this path. The minimum distance is therefore 3.

!["Minimum-distance path between Alexi and Jules"](img/voorbeeld_sociale_graaf_min_dist.svg)


We search for this distance between each pair of people in the network. There are 10 people, and each of these 10 people can be connected to 9 other people. So there are 90 possible pairs. Since the minimum distance between the pair (person1, person2) and (person2, person1) is the same, we only need to determine the distance between 45 pairs. 

## Dijkstra's algorithm

To determine the minimum distance between two nodes in a graph, we can use Dijkstra's algorithm. This algorithm is also used, for example, in a route planner to determine the shortest route between two places. Watch the following video to learn how the algorithm works.

![](@youtube/https://www.youtube.com/embed/O83LGOGicZ8?si=li_3kOd7z7HQyMA- "video")


By applying Dijkstra's algorithm to each pair of nodes in our social graph, we know the minimum distance between every two nodes. The pair of nodes with the highest minimum distance tells us how spread out the network is.