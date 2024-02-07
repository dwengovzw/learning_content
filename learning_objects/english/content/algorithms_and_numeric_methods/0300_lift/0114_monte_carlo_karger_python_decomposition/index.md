---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Karger's algorithm uses the Monte Carlo method to find a solution.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: org-dwengo-elevator-riddle-monte-carlo-karger-python-1
keywords:
- grafen
- algoritme
- computationeel denken
- clustering
- datastructuur
- monte carlo
- python
- karger
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
title: Karger in Python (decomposition)
version: 1
---
# Monte Carlo

## Karger's Algorithm: Implementation in Python

To implement our algorithm in Python, we first think carefully about how we can decompose the problem into subproblems (decomposition). We have chosen the following division:
- Guessing a cut.
    - Selecting two random nodes.
    - Merging these nodes in the graph into one node with the labels of the two merged nodes.
    - Merging the edges that originate from the two nodes.
- Guessing a cut several times and remembering the smallest one.