---
content_type: text/markdown
copyright: CC BY dwengo
description: What is batch normalization?
estimated_time: 10
hruid: org-dwengo-waisda-beelden-emoties-deel2-batchnorm
keywords:
- lagen
- AI
- neurale netwerken
- batch normalisatie
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
title: Batch normalization
version: 1
---
# Batch normalization

Batch normalization will normalize the input of the layer. That means the layer will transform the input values to values between, for example, -1 and 1. For one image a layer may receive an input with values between 0 and 1000, and for another image an input between -10 and 0.01. This variation makes it harder for the network to learn. To avoid this, you will convert each input to a similar range.

You can perform such a normalization by subtracting the mean from the value and then dividing by the standard deviation.

1. Compute the mean

\\[\mu = \frac{1}{m} \sum_{i=1}^{m}{x_i}\\]

2. Compute the variance

\\[\sigma^2 = \frac{1}{m} \sum_{i=1}^{m}{(x_i - \mu)^2}\\]

3. Normalize the value

\\[\hat{x}_i = \frac{x_i - \mu}{\sqrt{\sigma^2}}\\]


Batch normalization will make the training process more stable, ensure that the model converges faster, and make it less sensitive to variations in the input.

<div class="dwengo-content assignment">
<h2 class="title">Assignment</h2>
<div class="content">
Apply batch normalization to the following data.
<ul>
    <li>\(x_{1} = 5\), \(x_{2} = 3\), \(x_{3} = 2\), \(x_{4} = 1\), \(x_{5} = 9\)</li>
    <li>\(x_{1} = -2\), \(x_{2} = 4\), \(x_{3} = -3\), \(x_{4} = -1\), \(x_{5} = 2\), \(x_{6} = 0\)</li>
    <li>\(x_{1} = 1\), \(x_{2} = 1\), \(x_{3} = 1\), \(x_{4} = 1\)</li>
</ul>
</div>
</div>