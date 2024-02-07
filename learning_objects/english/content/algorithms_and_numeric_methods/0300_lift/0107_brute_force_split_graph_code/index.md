---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Based on the pseudocode, we can easily write an algorithm in Python.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 8
hruid: org-dwengo-elevator-riddle-brute-force-4
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
title: 'Step 1: Code'
version: 1
---
# Brute Force

## Implementation in python

Below you can see the translation of the pseudocode into Python.

```python
# This function generates all possible combinations of k elements from a row of n elements
def generate_all_possible_choices(k, n):

    # If k == 0 then no more elements should be chosen
    if k == 0:
        return [[2 for _ in range(n)]]

        # If k == n then all elements have to be chosen
    if k == n:
        return [[1 for _ in range(n)]]

        # If k > n then there is no possible selection, this case cannot occur in the algorithm
    if k > n:
        return []
    else:
        # Create a list to store all possible selections in
        selections = []
        # Assign the first floor in the row to elevator 1.
        # Combine this with all possible ways to choose k-1 elements from n-1 elements
        selections.extend(
            [[1] +
                selection for selection in generate_all_possible_choices(k-1, n-1)]
        )
        # Assign the first floor in the row to elevator 2.
        # Combine this with all possible ways to choose k from n-1 elements
        selections.extend(
            [[2] +
                selection for selection in generate_all_possible_choices(k, n-1)]
        )
        return selections
```

Note that the function generate_all_possible_choices calls itself. Such an algorithm is called a recursive algorithm by computer scientists. Recursive algorithms are often useful in problems where a certain pattern repeats itself.

When we execute our algorithm with the values four and eight, we get all possible divisions of the vertices of the graph into two equal groups. Below you can see the output of the function generate_all_possible_choices(4, 8).

[[1, 1, 1, 1, 2, 2, 2, 2], [1, 1, 1, 2, 1, 2, 2, 2], [1, 1, 1, 2, 2, 1, 2, 2], [1, 1, 1, 2, 2, 2, 1, 2], [1, 1, 1, 2, 2, 2, 2, 1], [1, 1, 2, 1, 1, 2, 2, 2], [1, 1, 2, 1, 2, 1, 2, 2], [1, 1, 2, 1, 2, 2, 1, 2], [1, 1, 2, 1, 2, 2, 2, 1], [1, 1, 2, 2, 1, 1, 2, 2], [1, 1, 2, 2, 1, 2, 1, 2], [1, 1, 2, 2, 1, 2, 2, 1], [1, 1, 2, 2, 2, 1, 1, 2], [1, 1, 2, 2, 2, 1, 2, 1], [1, 1, 2, 2, 2, 2, 1, 1], [1, 2, 1, 1, 1, 2, 2, 2], [1, 2, 1, 1, 2, 1, 2, 2], [1, 2, 1, 1, 2, 2, 1, 2], [1, 2, 1, 1, 2, 2, 2, 1], [1, 2, 1, 2, 1, 1, 2, 2], [1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 2, 1], [1, 2, 1, 2, 2, 1, 1, 2], [1, 2, 1, 2, 2, 1, 2, 1], [1, 2, 1, 2, 2, 2, 1, 1], [1, 2, 2, 1, 1, 1, 2, 2], [1, 2, 2, 1, 1, 2, 1, 2], [1, 2, 2, 1, 1, 2, 2, 1], [1, 2, 2, 1, 2, 1, 1, 2], [1, 2, 2, 1, 2, 1, 2, 1], [1, 2, 2, 1, 2, 2, 1, 1], [1, 2, 2, 2, 1, 1, 1, 2], [1, 2, 2, 2, 1, 1, 2, 1], [1, 2, 2, 2, 1, 2, 1, 1], [1, 2, 2, 2, 2, 1, 1, 1], [2, 1, 1, 1, 1, 2, 2, 2], [2, 1, 1, 1, 2, 1, 2, 2], [2, 1, 1, 1, 2, 2, 1, 2], [2, 1, 1, 1, 2, 2, 2, 1], [2, 1, 1, 2, 1, 1, 2, 2], [2, 1, 1, 2, 1, 2, 1, 2], [2, 1, 1, 2, 1, 2, 2, 1], [2, 1, 1, 2, 2, 1, 1, 2], [2, 1, 1, 2, 2, 1, 2, 1], [2, 1, 1, 2, 2, 2, 1, 1], [2, 1, 2, 1, 1, 1, 2, 2], [2, 1, 2, 1, 1, 2, 1, 2], [2, 1, 2, 1, 1, 2, 2, 1], [2, 1, 2, 1, 2, 1, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1], [2, 1, 2, 1, 2, 2, 1, 1], [2, 1, 2, 2, 1, 1, 1, 2], [2, 1, 2, 2, 1, 1, 2, 1], [2, 1, 2, 2, 1, 2, 1, 1], [2, 1, 2, 2, 2, 1, 1, 1], [2, 2, 1, 1, 1, 1, 2, 2], [2, 2, 1, 1, 1, 2, 1, 2], [2, 2, 1, 1, 1, 2, 2, 1], [2, 2, 1, 1, 2, 1, 1, 2], [2, 2, 1, 1, 2, 1, 2, 1], [2, 2, 1, 1, 2, 2, 1, 1], [2, 2, 1, 2, 1, 1, 1, 2], [2, 2, 1, 2, 1, 1, 2, 1], [2, 2, 1, 2, 1, 2, 1, 1], [2, 2, 1, 2, 2, 1, 1, 1], [2, 2, 2, 1, 1, 1, 1, 2], [2, 2, 2, 1, 1, 1, 2, 1], [2, 2, 2, 1, 1, 2, 1, 1], [2, 2, 2, 1, 2, 1, 1, 1], [2, 2, 2, 2, 1, 1, 1, 1]]