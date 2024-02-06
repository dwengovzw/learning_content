---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Overfitting
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 20
hruid: kiks_overfitting
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
teacher_exclusive: false
title: Overfitting
version: 3
---
# Overfitting
When a network becomes too fixated on the training data, it will perform worse on unseen data. The network then essentially memorizes the training data by heart. This is called **overfitting**. When the network is still able to learn, by adding more layers for example, it is referred to as **underfitting**.

![over- and underfitting](embed/overunderfit.png "Balance between over- and underfitting") 

On the left of the image, there is a case of underfitting, while the right graph illustrates overfitting.

In the following notebook, you will learn how to take this into account.

[![](embed/Knop.png "Button")](https://kiks.ilabt.imec.be/jupyterhub/?id=1713 "Overfitting")