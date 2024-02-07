---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: The Karger algorithm uses the Monte Carlo method to arrive at a solution.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: org-dwengo-elevator-riddle-monte-carlo-karger
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
title: Karger's Algorithm
version: 1
---
# Monte Carlo

## Karger's Algorithm

For determining the minimum cut of a graph, there is also a Monte Carlo algorithm. This is called Karger's algorithm (after the inventor David Karger). Below, we explain step by step how this algorithm works.

Karger's algorithm will reduce the graph that needs to be cut into pieces to a graph with just two nodes. The cost of cutting this graph into two is then the sum of all edges that connect these two nodes. This sum is what the algorithm guesses to be the minimum cost. This procedure is repeated a number of times after which the best guess is chosen as the final result. Below you can see an example of how the graph can be reduced.

|  | <div style="min-width:450px"></div> |
| - | -- |
| We start with the full graph. | ![Karger step 1](embed/karger1.png "Step 1") |
|  |  |
| We choose a random edge and the two nodes that are adjacent to that edge. | ![Karger step 2](embed/karger2.png "Step 2.") |
|  |  |
| We merge the two nodes by eliminating the edge that connects them. All other edges that originated from one of the two nodes now originate from the combined node. | ![Karger step 3](embed/karger3.png "Step 3.") |
|  |  |
| If there are multiple edges running between the same nodes, we replace these edges with a single edge. The weight of this edge is equal to the sum of the weights of the edges we are replacing. For example, between node (4, 8) and node (6) there are two edges with weight 3. We replace these with one edge with weight 6. | ![Karger step 4](embed/karger4.png "Step 4.") |
|  |  |
| Then we choose a random edge again. | ![Karger step 5](embed/karger6.png "Step 5.") |
|  |  |
| We merge the adjacent nodes of this edge again. | ![Karger step 6](embed/karger7.png "Step 6.") |
|  |  |
| And we again reduce double edges between the same two nodes. | ![Karger step 7](embed/karger8.png "Step 7.") |
|  |  |
| We keep repeating this until only 2 nodes remain. Edge selection. | ![Karger step 8](embed/karger9.png "Step 8.") |
|  |  |
| Merging nodes. | ![Karger step 9](embed/karger10.png "Step 9.") |
|  |  |
| Reducing edges. | ![Karger step 10](embed/karger11.png "Step 10.") |
|  |  |
| Edge selection. | ![Karger step 11](embed/karger12.png "Step 11.") |
|  |  |
| Merging nodes and reducing edges. | ![Karger step 12](embed/karger13.png "Step 12.") |
|  |  |
| Edge selection. | ![Karger step 13](embed/karger14.png "Step 13.") |
|  |  |
| Merging nodes and reducing edges. | ![Karger step 14](embed/karger15.png "Step 14.") |
|  |  |
| Edge selection. | ![Karger step 15](embed/karger16.png "Step 15.") |
|  |  |
| Merging nodes and reducing edges. | ![Karger step 16](embed/karger17.png "Step 16.") |


After this reduction, our guess for the minimum cut is the weight of the edge between the two remaining nodes. In this case, it's 22. **Note that this algorithm does not ensure that the distribution of nodes in the two parts of the cut is equal.** In our case, there are 6 nodes in one graph and two nodes in the other.