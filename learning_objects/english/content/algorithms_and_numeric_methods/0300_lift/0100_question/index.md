---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Problem statement.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 5
hruid: org-dwengo-elevator-riddle-question
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
title: Elevator problem
version: 1
---
# The Challenge
The offices of Dwengo are located on the fourth to the eleventh floor of an office building. There is a shared elevator for all the companies in this building. However, this elevator can only be used to move to and from the entrance and not for movement between floors. Below you can see a drawing of what the office building looks like.

![A drawing of an office building where Dwengo has six floors connected by a private elevator](embed/M026_Kantoorgebouw.svg)

The employees of Dwengo can move between their own floors using a private elevator. Because the number of employees has increased significantly in recent years, the elevator is often overloaded. To solve this, Dwengo has decided to install an additional private elevator. To use this efficiently, they decide to ensure that the two elevators serve their own collection of floors where they stop. For example, one elevator only stops at the even floors and the other elevator only at the odd floors. Note that as a result, it is no longer possible to move between even and odd floors using the elevator. These people must take the stairs.

As there are not an equal number of movements between the different floors, Dwengo wants to choose the division in such a way that as few people as possible have to take the stairs. Below you will find an overview of the movements that take place on an average day.

| From Floor | To Floor |