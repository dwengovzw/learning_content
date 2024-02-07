---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: As a first solution method, we can apply the brute force technique.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 2
hruid: org-dwengo-elevator-riddle-brute-force-1
keywords:
- grafen
- algoritme
- computationeel denken
- clustering
- datastructuur
- brute force
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
title: Brute force
version: 1
---
# Brute Force

As the first method of solution, we can apply the brute force technique. This is a well-known technique in the field of computer science. It consists of trying out all possibilities and then checking which was the best.
More specifically, we can break down the brute force technique into several subproblems (**decomposition**).
1. Generating all possible ways to divide the graph into two graphs with an equal number of nodes.
2. For a given division of the graph, calculate what the **cost** is of the **cut** needed to arrive at that division.
3. Find the **cut** with the lowest **cost**.