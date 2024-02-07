---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: We can now calculate the cut cost for any partition of the graph. Now
  we look for the cut with the minimal cost.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 5
hruid: org-dwengo-elevator-riddle-brute-force-6
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
title: 'Step 3: Find the minimal cut cost'
version: 1
---
# Brute Force
## Finding the cut with the lowest cost

This last step is the simplest. For this, we iterate over the list of all possible choices to distribute the elevators across the floors and calculate the cost of that choice. In the list of costs, we look for the minimal cost. Below is an example of such an assignment of the nodes to a group. We also see which cut this assignment then yields.

 ![Example of a labeling of the graph.](embed/verplaatsingen_chaos_labeled.png "Example of a labeling of the graph.")

 The following Python code computes the cut cost for a particular distribution. For this, we use the arc matrix which we have previously established.

```python
 # Generate all possible distributions of the floors over the elevators
all_possible_choices = generate_all_possible_choices(4, 8)

# Calculate the cost of each possible distribution
cut_costs = [cut_cost(choice) for choice in all_possible_choices] 

# Choose an arbitrarily high cost to start with
minimal_cost = 100000 
index_minimal_cost = 0

for i, val in enumerate(cut_costs):
    # If the cost of the current distribution is less than the minimal cost so far.
    if cut_costs[i] < minimal_cost:
        # Take the current distribution as the new minimal cost.
        index_minimal_cost = i
        minimal_cost = cut_costs[i]
               
print("The minimal cost is: ", minimal_cost)
print("The distribution of the floors over the elevators is: ", all_possible_choices[index_minimal_cost])
```

Running this code gives us the following result:

The minimal cost is: 12
The distribution of the floors over the elevators is: [1, 2, 1, 2, 1, 2, 1, 2]

The optimal distribution is thus to have elevator 1 stop on the even floors and elevator 2 on the odd floors. In this case, an average of 12 people per day will have to take the stairs. Note that there is another distribution with minimal cost. This is the opposite distribution [2, 1, 2, 1, 2, 1, 2, 1].