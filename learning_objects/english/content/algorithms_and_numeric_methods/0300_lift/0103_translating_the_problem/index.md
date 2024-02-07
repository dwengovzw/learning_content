---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Now that we have chosen a data structure, we can formulate the problem
  in a different way.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 5
hruid: org-dwengo-elevator-riddle-analyzing-3
keywords:
- grafen
- algoritme
- computationeel denken
- clustering
- datastructuur
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
title: Translate the problem
version: 1
---
# Reframing the Problem

Now that we have an **abstract representation** of the movements between different floors, we can restate the problem in terms of that:

> How do you cut a graph into two equal pieces such that the sum of the number of edges you cut is as small as possible?

|  |  |
| - | - |
| Here you see an example of how we can cut the graph into two equal pieces. The red line represents the line along which we cut the graph. Every edge that crosses the line is cut. The total cost of the cut is then the sum of the weights of all the edges that we cut.  | ![Cut in the graph.](embed/verplaatsingen_chaos_cut.png "Graph cut.") |
|  |  |
| In this image, you see the edges that are being cut, represented by a dashed line. This collection of edges is called a cut. The total cost of this cut is the sum of the weights on the dashed lines. 3 + 5 + 4 + 2 + 6 + 4 = 24 | ![Cut in the graph.](embed/verplaatsingen_chaos_cut_finished.png "Graph cut.") |
|  |  |

To solve our problem, we're looking for a cut of the graph with a minimal cost.

Our problem is not yet solved; in fact, we still have to start working on it. So far, by using abstraction and pattern recognition, we have transformed the problem into a structure with which a computer can easily deal. This is the essence of computational thinking. We transform a problem so that it becomes easier to think about, as well as to solve with a computer.