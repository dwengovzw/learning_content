---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: MNIST
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: kiks_mnist
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
title: MNIST
version: 3
---
# MNIST
The MNIST dataset consists of 70,000 images of handwritten digits, each 28 x 28 pixels in grayscale.

![](embed/drie.jpg "A three from the MNIST dataset")
<figure>
    <figcaption align = "center">A three from the MNIST dataset.</figcaption>
</figure>

Of the images in the MNIST dataset, 60,000 are used to **train** a neural network and 10,000 to **test** it.
The final neural network aims to recognize handwritten digits it has not seen before.

In a first notebook, you work with a **feedforward neural network**.<br>
In a second notebook, you work with a **convolutional neural network**; here you use a training and test set as well as a **validation set**.<br>
You can compare the structure and performance of these networks with each other. By adjusting the parameters in these networks, you gain insights into the influence of these parameters on training and performance.

[![](embed/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=1810_en "MNIST")