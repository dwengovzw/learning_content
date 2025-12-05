---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: 'Storm-resistant network: Creating an abstraction'
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct05_06
keywords:
- ''
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
- 12
- 13
- 14
teacher_exclusive: true
title: 'Storm-resilient network: Creating an abstraction'
version: 3
---
# Example 6:  Making abstraction
Source: [the online platform of the Belgian Bebras contest](https://bebras.ugent.be/)<br>
Text: Zoltán Molnár, HU, Zsuzsa Pluhár, HU<br>
Images: Ivo Blöchliger, CH<br>
Translation: Kris Coolsaet 

## Storm-resistant network (Bebras 2014-HU-02) 

The mobile phone company Beaver Telecom wants to place cell towers on Windy Island.<br>
The coverage area of a tower is a circle centered around it. Two towers are said to be *connected* if their coverage areas overlap. Two towers can *communicate* if there exists a chain of intermediate towers such that each tower is connected to the next.<br>
Because of the strong wind on the island, it occasionally happens that a tower breaks. If any one tower stops functioning somewhere, we still want every two of the remaining towers to be able to communicate with each other.

Which of the arrangements below should we use for this?

![Storm-resistant network](embed/bebrasabstractie.png "Bebras Abstraction")