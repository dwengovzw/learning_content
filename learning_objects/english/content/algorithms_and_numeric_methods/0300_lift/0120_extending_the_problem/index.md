---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: We can expand the problem and take into account the distance that individuals
  have to travel.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 5
hruid: org-dwengo-elevator-riddle-extending-the-problem
keywords:
- grafen
- algoritme
- computationeel denken
- clustering
- python
- spectrale clustering
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
title: Expansion
version: 1
---
# Extension: Taking into account the number of floors traversed by stairs

In the previous solutions, we only looked at which movements had to be done by stairs. However, we did not consider how many floors were in such a movement. We can easily adjust our solution to this by multiplying the number of movements between two floors by a cost to move between those floors.
In that case, we obtain the following arc matrix.

|  | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** |
| - | - |- | - |- | - |- | - |- |
| **4** | 0 | 0 | 2x2 | 0 | 2x4 | 0 | 2x8 | 0 |
| **5** | 0 | 0 | 0 | 0 | 3x3 | 3x4 | 0 | 3x6 | 
| **6** | 1x2 | 0 | 0 | 0 | 1x2 | 0 | 2x4 | 0 | 
| **7** | 0 | 3x2 | 0 | 0 | 0 | 2x2 | 4x3 | 4x4 | 
| **8** | 2x4 | 3x3 | 2x2 | 0 | 0 | 0 | 2x2 | 0 | 
| **9** | 0 | 3x4 | 0 | 2x2 | 0 | 0 | 0 | 3x2 | 
| **10** | 0 | 0 | 3x4 | 2x3 | 2x2 | 0 | 0 | 0 |
| **11** | 0 | 1x6 | 0 | 1x4 | 0 | 0 | 0 | 0 |

Then we obtain the following arc matrix:

|  | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** |
| - | - |- | - |- | - |- | - |- |
| **4** | 0 | 0 | 4 | 0 | 8 | 0 | 16 | 0 |
| **5** | 0 | 0 | 0 | 0 | 9 | 12 | 0 | 18 | 
| **6** | 2 | 0 | 0 | 0 | 2 | 0 | 8 | 0 | 
| **7** | 0 | 6 | 0 | 0 | 0 | 4 | 12 | 16 | 
| **8** | 8 | 9 | 4 | 0 | 0 | 0 | 4 | 0 | 
| **9** | 0 | 12 | 0 | 4 | 0 | 0 | 0 | 6 | 
| **10** | 0 | 0 | 12 | 6 | 4 | 0 | 0 | 0 |
| **11** | 0 | 6 | 0 | 4 | 0 | 0 | 0 | 0 |

Coincidentally, the minimum cut in this case is equal: 
The minimum cost is: 36
The distribution of the floors across the elevators is: [1, 2, 1, 2, 1, 2, 1, 2]

Other techniques yield the same result. This is, for example, the spectral embedding:

![Result of spectral embedding.](embed/spectral_embedding_weighted_floors.png "Result of spectral embedding")