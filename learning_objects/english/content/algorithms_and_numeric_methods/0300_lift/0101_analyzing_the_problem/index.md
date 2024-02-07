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