---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Before we can solve a problem with the computer, we use computational
  thinking to translate the problem into a form that the computer understands.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 5
hruid: org-dwengo-elevator-riddle-analyzing-1
keywords:
- grafen
- algoritme
- computationeel denken
- clustering
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
title: Problem Analysis
version: 1
---
# Problem Analysis

In the first phase, we try to eliminate all the unnecessary information that is not needed to solve the problem. By making this abstraction, we can focus on the information that is relevant to solving the problem. For this, we look at the question:

> On which floors must each of the private elevators stop to ensure that as few people as possible need to take the stairs?

The question only concerns private elevators; therefore, the information about the common elevator is not relevant. The question also assumes that there are already two private elevators that stop at their own four floors each. Hence, we no longer need to worry about how these elevators should be installed or what strategy we should use to deploy the elevators efficiently. The essence of the issue is the division of the floors into two groups. To do this, we base our decision on historical elevator usage.

When dividing the floors into two groups, certain movements will inevitably have to be made using the stairs. Our goal is to minimize these movements. To achieve this, we base our plan on the table of movements.

| From floor | To floor |
| ----------- | ----------- |
| 4      | 8, 10, 10, 8, 6, 6        |
| 5   | 8, 8, 9, 9, 11, 11, 11, 9, 8         |
| 6   | 10, 8, 10, 4         |
| 7   | 10, 10, 11, 11, 11, 5, 11, 5, 9, 9, 5, 10, 10         |
| 8   | 5, 5, 4, 6, 4, 6, 5, 10, 10         |
| 9   | 5, 5, 11, 11, 7, 11, 7, 5         |
| 10   | 6, 8, 8, 7, 6, 7, 6         |
| 11   | 7, 5         |

The order in which the movements take place is not important to us. We just want to look at how many movements there are between each floor. We can draw up a table for this:

|  | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** |
| ----------- | ----------- |----------- | ----------- |----------- | ----------- |----------- | ----------- |----------- |
| **4** | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| **5** | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 3 | 
| **6** | 1 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 
| **7** | 0 | **3** | 0 | 0 | 0 | 2 | 4 | 4 | 
| **8** | 2 | 3 | 2 | 0 | 0 | 0 | 2 | 0 | 
| **9** | 0 | 3 | 0 | 2 | 0 | 0 | 0 | 3 | 
| **10** | 0 | 0 | 3 | 2 | 2 | 0 | 0 | 0 |
| **11** | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |

The table shows the number of moves from the floor in the first column to floor 0 in the first row of the table. For example, the cell in bold at coordinate (row 7, column 5) represents the number of moves between floors seven and five (= 3).
Note that these movements also indicate direction. For example, there are two movements from floor seven to floor nine, but also two movements from floor nine to seven. The direction of the movement is not important to us, only the number of movements. We omit this unnecessary information to simplify the problem (**abstraction**). So we can transform our table into an upper triangular matrix by adding the movements between the same floors. Then we get the following table:

|  | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** |
| ----------- | ----------- |----------- | ----------- |----------- | ----------- |----------- | ----------- |----------- |
| **4** | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| **5** | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 3 | 
| **6** | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 
| **7** | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 4 | 
| **8** | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 
| **9** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 
| **10** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **11** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |