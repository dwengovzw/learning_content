---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Deep neural network architecture
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: kiks_opbouwdiepneuraalnetwerk
keywords:
- AI
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
title: Deep neural network architecture
version: 3
---
# Construction of a Deep Neural Network

To be able to count stomata, the computer first has to recognize them. It must be able to determine from different parts of a picture whether there is a stoma on it or not.
The computer thus has to solve a *classification problem*, where it is necessary for it to recognize a specific object. The AI system will need to incorporate an *object recognition* system. For this, a convolutional neural network is highly suitable.

In this notebook, you will become acquainted step by step with the construction of a *deep neural network* that provides a solution for this classification problem. When developing a neural network, the architect of the system makes multiple choices and also sets the values of some parameters. These choices determine the architecture of the network and how the network's training proceeds.

[![](embed/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=1701_en "Deep neural network")