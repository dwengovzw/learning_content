---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Apples and pears
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct03_14
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
title: Apples and pears
version: 3
---
# Distinguishing apples from pears

**Class discussion on object recognition by an AI system.**

Object recognition is an application of artificial intelligence that is very common nowadays. With machine learning techniques, a computer can, for example, recognize animal and plant species or human faces. 

In class, you can discuss with the students how a computer looks at photos and how one could program a computer to distinguish apples from pears based on rules.

**Target group:** all grades - all pathways

**Subjects:** 
* Mathematics 
* STEM 
* Computer science 
* Media literacy

**Prerequisites:** Students know that numbers can be ordered.

<div class="alert alert-box alert-warning">
<strong>Distinguishing apples and pears - class discussion</strong><br>
<ul>
    <li>How do we distinguish apples and pears? Which features do we take into account?</li>
    <li>Would a computer do that in the same way?</li>
    <li>A computer generally cannot feel or see. How could a computer see? (If it has a camera, it can see.) <em>Computer vision</em> will play a role.</em></li>
    <li>How can we provide those apples and pears to the computer?</li>
    <li>How does a computer look at an image?</li>
    <li>Which features of apples and pears are meaningful for a computer?</li>
</ul>
</div>

The considerations and conclusions from the class discussion can be summarized in a diagram.

![ct-schema](@learning-object/m_ct03_14/en/3)

It goes without saying that the solution to the problem is much more complex in reality. The shape of some pears strongly resembles that of an apple; other features, such as the texture of the skin, can then be decisive. Using a deep neural network can yield better results than programming based on rules. 

![CNN looks for features of objects in order to recognize them.](embed/kenmerkenappelpeer.png)