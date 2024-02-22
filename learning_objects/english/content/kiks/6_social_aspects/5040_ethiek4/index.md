---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Threshold value
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: kiks_ethiek4
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
title: Threshold Value
version: 3
---
# Threshold Value

The KIKS neural network examines patches on a given micrograph to determine whether they contain a stomata or not. The network determines a percentage that reflects how confident the network is that a stomata is visible. During the development of the neural network, the network architect establishes a threshold value. If the determined percentage exceeds this threshold value, then the patch belongs to the class 'stomata', otherwise, it does not.

Adjusting the threshold value affects the number of false positives and false negatives. The threshold value used by the model determines how 'strict' the model is. 
- With a high threshold value, fewer stomata will be detected, but there will also be fewer false positives. There will, however, be more false negatives.
- With a low threshold value, more stomata will be detected, but there will also be more false positives. There will be fewer false negatives.

![ivy threshold](https://user-images.githubusercontent.com/48352335/219100751-29a97452-4495-49ea-8157-3c4dcfcc9aa9.png)

An important consideration when choosing a threshold value is the balance between ***precision*** and ***recall***.

- Precision: the percentage of stomata found that are actually stomata.
- Recall: the percentage of stomata in an image that were actually found.

It is clear that a low threshold value will result in low precision (more points are considered as stomata, so more incorrect points; there are then more **false positives**), but a high recall (more stomata will also be found). Conversely, a high threshold value will result in high precision, but low recall (there will be more **false negatives**).

The chosen threshold value is literally a matter of life and death in the case of a deep neural network in the field of medical imaging, such as a system for recognizing malignant tumors.