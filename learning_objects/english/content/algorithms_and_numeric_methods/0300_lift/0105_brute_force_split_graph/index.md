---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: How do we split our graph into two parts?
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: org-dwengo-elevator-riddle-brute-force-2
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
title: 'Step 1: Split the graph'
version: 1
---
# Brute Force

## All possible ways to split the graph into two equal parts

Our graph consists of eight nodes (the floors). We can divide these in two by choosing four nodes and assigning them to elevator 1. The remaining four nodes we assign to elevator 2.  
We can calculate the number of choices of four items from eight options using our knowledge of combinatorics \\(\mathrm{C}^4_8 = 70\\).

To generate all 70 combinations, we can devise a simple algorithm.

We start with no division. We have not yet chosen any floors to assign to elevator 1:

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| x | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

For the first floor on the list, we have two options, either we assign it to elevator 1 or not. In the case that we do not choose this floor for elevator 1, it is automatically assigned to elevator 2. That gives the following options for the first choice:


|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 1 | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 2 | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

We can now examine these two cases in detail.

#### Case 1: The first floor on the list was assigned to elevator 1.

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 1 | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

In this case, there are still seven floors that we need to assign to an elevator. Of these, we can still assign three more to elevator 1. There are \\(\mathrm{C}^3_7 = 35\\) possibilities for the remaining seven floors. To distribute these over the elevators we can make a choice again for the first of the seven remaining floors, giving us the following two possibilities.


|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 1 | 1 | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 1 | 2 | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

#### Case 2: The first floor on the list was assigned to elevator 2.

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 2 | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

In this case, we are allowed to choose four more of the remaining floors to assign to elevator 1. There are \\(\mathrm{C}^4_7 = 35\\) more possibilities for the remaining seven floors. Here again, we can continue the algorithm by making a selection for the second floor on the list.

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 2 | 1 | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 2 | 2 | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

#### Generalizing Case 1 and Case 2

If we look closely at the two cases described above, we see a pattern emerging (**pattern recognition**).
- We make a choice each time for the first not-yet-assigned floor in the list. 
- If we assign that floor to elevator 1, then we reduce the number of times we can still assign to elevator 1 by 1, and assign that quantity from the remaining floors to elevator 1.
- If we do not assign that floor to elevator 1, then we can still assign just as many from the remaining floors to elevator 1.