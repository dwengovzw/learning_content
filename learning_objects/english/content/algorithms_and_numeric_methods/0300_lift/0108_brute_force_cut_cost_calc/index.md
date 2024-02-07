---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Now that we know all the possible ways to split the graph in two, we
  must calculate the cut cost for each partition.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 5
hruid: org-dwengo-elevator-riddle-brute-force-5
keywords:
- grafen
- algoritme
- computationeel denken
- clustering
- datastructuur
- brute force
- python
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
title: 'Step 2: Calculate the cost of the cut'
version: 1
---
# Brute Force

## Calculate the cost of the cut

Now that we have all possible partitions of the graph, it's simple to calculate the cost of such a partition. We simply iterate over all the edges in the graph. If they have been assigned to the same elevator, we do nothing. If they have been assigned to different elevators, we add the cost of that edge to the total cost of the cut. Below you can see an example of a partition of the graph with also the location where the graph will be cut into two.

 ![Example of a graph labeling.](embed/verplaatsingen_chaos_labeled.png "Example of a graph labeling.")

 The following Python code calculates the cut cost for a particular partition. We do this using the edge matrix that we have previously set up.

```python
edges_matrix = np.array([
    [0, 0, 3, 0, 4, 0, 2, 0],
    [0, 0, 0, 3, 6, 6, 0, 4],
    [0, 0, 0, 0, 3, 0, 5, 0],
    [0, 0, 0, 0, 0, 4, 6, 5],
    [0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]])


# Calculate the cost to cut a certain distribution of the graph into two
def cut_cost(floor_distribution):
    # The cost is the sum of all edges connecting the two parts of the graph, starting at 0.
    cost = 0
    # Iterate over each possible combination of departure and destination floor.
    for departure_floor in range(len(floor_distribution)):
        for destination_floor in range(len(floor_distribution)):
            # If the departure and destination floor are not assigned to the same elevator, 
            # then add the cost of the edge to the total cost.
            if floor_distribution[departure_floor] != floor_distribution[destination_floor]:
                cost += edges_matrix[departure_floor][destination_floor]
    return cost # Return the total cost
```