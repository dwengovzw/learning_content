---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Bias at KIKS
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: kiks_ethiek2
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
- 16
- 17
- 18
teacher_exclusive: true
title: Bias in KIKS
version: 3
---
# Bias in KIKS

The KIKS model also contains a bias. The photos of the training set are taken in such a way that the stomata approximately fit in a box of **120 X 120 pixels**.
These examples are prints of leaves taken with transparent nail polish. This means that the model will perform best on images
of stomata of similar size in a similar, **greenish-gray color**.

![example training set](embed/vierkantjespositievestomatavoorbeelden.png "Examples of stomata from the training set") 
<figure>
    <figcaption align = "center">Examples of stomata from the training set.</figcaption>
</figure> 

This also means that if you submit a microphoto to the network with stomata that are too small or with many different colors, the network might not properly detect the stomata in that photo.
