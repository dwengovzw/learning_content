---
content_type: text/markdown
copyright: CC BY dwengo
description: What is the convolution operation?
estimated_time: 20
hruid: org-dwengo-waisda-beelden-emoties-deel2-conv2d
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
title: The convolution
version: 1
---
# Convolutional layers

## The convolution operation

When you apply a **convolution** to an image, you will strengthen or weaken certain **properties of that image**. For example, you can make the image sharper or enhance the edges in the image. The effect of the convolution is determined by the **filter** you have chosen. Below you can try different filters. What is the effect of each of these filters?

<iframe src="https://dwengo.org/convolutie" title="Example of a convolution" width="720px" height="800px"></iframe>

The convolution will slide the **filter** (= grid of numbers) across the image from left to right and from top to bottom. At each position of the grid, a pixel value of the output image is computed. Watch the video below to understand how you can apply a convolution to an image.

TODO: insert video about convolutions.

Using Python you can apply convolutions to an image. Through the following notebook you will learn how to do that.

[![](img/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=1712_en "Basic")

## The convolutional layer

A convolutional layer will transform an input image by applying a convolution to it. The layer will not do that with a fixed **filter** but will **learn a filter itself** during the training process. This allows the neural network to extract from the image the properties that are relevant to the task. 

<div class="dwengo-content sideinfo">
<h2 class="title">When do you use convolutions?</h2>
<div class="content">
<p>Convolutions are especially useful for data where there is a relationship between neighboring values. The convolution will combine neighboring values into a new value.</p>
<p>For images, for example, we combine regions of 3x3 pixels into 1 new value. This value then represents a property of this region. For example, whether an edge is visible in the region or not.</p>
<p>
Besides images, convolutions can be used for: audio, financial time series, ECG signals, sensor data, ... Convolutions are not useful for data without local relationships such as a table with customer data or medical data in a patient record.
</p>
</div>
</div>