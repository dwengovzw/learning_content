---
content_type: text/markdown
copyright: CC BY dwengo
description: What is max pooling?
estimated_time: 8
hruid: org-dwengo-waisda-beelden-emoties-deel2-maxpool
keywords:
- lagen
- AI
- neurale netwerken
- max pooling
language: en
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
- http://ilearn.ilabt.imec.be/vocab/tref1/ict
target_ages:
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: false
title: Max pooling
version: 1
---
# Max pooling

The max pooling operation will combine pixels in an image into a single number, the maximum of all pixels in the *pool*. Below you can see an example of such a max pooling operation with a size of 2x2 pixels.

!["Example of max pooling"](img/maxpooling.jpg)

You apply max pooling for various reasons. The most important ones are listed below.

- **Reducing the size of the image**: Max pooling will reduce the size of the image while preserving the most important information. This makes the model simpler, allowing you to train and evaluate it faster.
- **More robust to small shifts**: By applying max pooling, you make your model more robust to small shifts in the input image. 
- **Suppresses noise**: Because max pooling always takes the maximum value within a neighborhood, small differences (noise) in that region will be ignored. This gives us a network that can handle noise in images better.
- **Limits overfitting**: By simplifying the model, you reduce the chance that the model memorizes the training set.