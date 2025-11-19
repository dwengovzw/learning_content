---
content_type: text/markdown
copyright: CC BY dwengo
description: Learn which layers a neural network consists of and what these layers
  are for.
estimated_time: 10
hruid: org-dwengo-waisda-beelden-emoties-deel2-input-layer
keywords:
- lagen
- AI
- neurale netwerken
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
title: The input layer
version: 1
---
# The input layer (InputLayer)

This layer is the simplest layer in the network. This layer will pass the data it receives on to the rest of the network. It will therefore pass the input image one-to-one to the next layer in the network. Below you can visually see what the input layer does

![Input layer image](img/invoerlaag.png)

<div class="dwengo-content sideinfo">
<h2 class="title">What is a layer?</h2>
<div class="content">
<p>
You can think of a layer as an <strong>operation</strong> that <strong>transforms a certain input into a certain output</strong>. How the input is transformed is not fixed. You can apply any operation to the input. The only requirement is that this operation is <strong>differentiable</strong>. This is because otherwise we cannot train the network with <strong>gradient descent</strong>.
</p>
<p>
For the input layer, the operation is to take a copy of the input.
</p>
</div>
</div>