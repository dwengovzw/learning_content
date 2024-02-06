---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: 'If no English text is found in the input, return the input.


  Bias'
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: kiks_ethiek1
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
title: Bias
version: 3
---
# Bias

Bias occurs when the data are not representative. For example, if only green apples are given as examples to a deep learning system, the model will not recognize red apples. Or if, during training, only pictures of dogs under a clear blue sky are provided, then the deep learning model may not classify a dog in the rain as belonging to the 'dog' category.

If the data used are colored by an existing bias in society, such as stereotypes, this will also be passed on to the ML system.
Therefore, it must be ensured that the model does not become discriminatory towards certain population groups. For example, if only female nurses are put in the dataset, men may not be classified as nurses.

However, a model is tested before it is put into use. The test data, however, can contain the same bias as the training data.