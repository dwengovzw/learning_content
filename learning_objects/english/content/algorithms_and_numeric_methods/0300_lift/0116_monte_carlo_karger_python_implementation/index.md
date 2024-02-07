---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: The Karger algorithm uses the Monte Carlo method to arrive at a solution.
difficulty: 10
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: org-dwengo-elevator-riddle-monte-carlo-karger-python-3
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
title: Karger in Python (implementation)
version: 1
---
# Monte Carlo

## Karger's Algorithm: Implementation

To choose two random nodes, we use the following function. We choose to always return the nodes sorted from small to large. This will make it easier to merge the rows and columns of the matrix.

```python

def chooseRandomPairInOrder(max):
    p1 = np.random.randint(0, max)
    p2 = np.random.randint(0, max)
    while p1 == p2:
        p2 = np.random.randint(0, max)
    if p2 > p1:
        return [p1, p2]
    else:
        return [p2, p1]

```

We use the following function to merge the rows and columns of the matrix. We do this using the next function:


```python

# Choose two random nodes and merge them.
def chooseAndMerge(edges_matrix, node_labels):
    random_pair_nodes = chooseRandomPairInOrder(len(edges_matrix))

    # If there is no edge between the two nodes, then choose a new pair of nodes.
    while (edges_matrix[random_pair_nodes[0]][random_pair_nodes[1]] == 0):
        random_pair_nodes = chooseRandomPairInOrder(len(edges_matrix))

    # Add rows of random_pair_nodes
    edges_matrix[random_pair_nodes[0]] += edges_matrix[random_pair_nodes[1]]
    edges_matrix = np.delete(edges_matrix, random_pair_nodes[1], axis=0)

    # Add columns of random_pair_nodes
    edges_matrix[:, random_pair_nodes[0]] += edges_matrix[:, random_pair_nodes[1]]
    edges_matrix = np.delete(edges_matrix, random_pair_nodes[1], axis=1)

    # Update edge labels
    # Add the label of the second node to the first node
    node_labels[random_pair_nodes[0]].extend(node_labels[random_pair_nodes[1]])

     # Remove the second node
    node_labels.pop(random_pair_nodes[1])
    if (len(edges_matrix) > 2):
        return chooseAndMerge(edges_matrix, node_labels)
    else:
        return edges_matrix, node_labels

```

The next function guesses what the cut cost might be. Note that we keep the values of the edges and the labels of the nodes in two separate variables here. This makes it easier to adjust the two independently. 
This function keeps calling itself until the graph has only two nodes left. We call this recursion (think back to the algorithm to generate all possible combinations of 4 nodes).

```python

def guessTheCutCost(edges_matrix):
    node_labels = [[x] for x in range(len(edges_matrix))]
    reduced_graph, reduced_nodes = chooseAndMerge(edges_matrix, node_labels)
     # Return the sum of the edges between the two remaining nodes and the labels of the edges that were contracted
    return reduced_graph[0][1] + reduced_graph[1][0], reduced_nodes

```

We now have code to guess a button. We now repeat this guess a number of times and take the best guess as the solution.

```python

# Repeat guessTheCutCost n times and remember the best solution
def repeatGuessTheCutCost(edges_matrix, n=8):
    current_minimum_cut_cost = 100000 # Choose an arbitrarily large minimum cost to start with.
    labels_of_minimum_cut = []
    for i in range(n):
        mincutcost, labels = guessTheCutCost(edges_matrix.copy())
        # Only remember the solution if it is better than the current minimum.
        if mincutcost < current_minimum_cut_cost:
            current_minimum_cut_cost = mincutcost
            labels_of_minimum_cut = labels
    return current_minimum_cut_cost, labels_of_minimum_cut


minimum_cut_cost, labels = repeatGuessTheCutCost(edges_matrix, 8)
print("The minimal cut is: ", minimum_cut_cost)
print("The labels of the nodes are: ", labels)

```

If we execute this code we get the following result:

The minimal cut is:  9
The labels of the nodes are:  [[0], [1, 5, 2, 4, 6, 3, 7]] 

**Note**: You need to add an offset of 4 to get to the label of the original node.