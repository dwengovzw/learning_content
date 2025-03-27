---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: ML
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: un_ai3
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
- 15
- 16
- 17
- 18
teacher_exclusive: true
title: Machine learning
version: 3
---
# Machine learning

Machine learning (ML) is a popular and successful part of artificial intelligence (AI). In *machine learning*, the approach is mainly empirical but based on solid mathematics, using principles from mathematical statistics (Chollet, 2018).

AI systems are developed by humans. They incorporate parameters whose values are not yet fixed.<br>
During training, the system learns. This means that it searches for the optimal values for the unfixed parameters using a learning algorithm.<br>
After training, these values are determined, giving an ML model, or an ML system that is ready for use.

**A machine learning system acquires knowledge from data using learning algorithms with the intention of predicting outcomes related to new data.**

- The new data must be similar to the data provided.
- These predictions are made with a particular level of certainty. ML models will therefore never be one hundred percent accurate.

<div class="alert alert-box alert-success">
    Learning algorithms are algorithms in which the ML system itself gradually makes adjustments to the parameters during the learning process, to achieve better performance over time.
</div>

> An ML system therefore does not make its decisions based on pre-programmed and detailed instructions.

The decisions of an ML model are called *predictions*.

### Regression and classification

<div class="alert alert-box alert-success">
    Predicting based on tendencies is a <b>regression problem</b>.<br> 
    Predicting a class is a <b>classification problem</b>. <br>
    <b>Predicting</b> means, for example, that future figures are generated from past tendencies (regression) or that an object is classified into a certain category (called a class) (classification).
</div>

> Instead of categories, in this context, we often speak of classes.
 
> **Concrete examples of regression:** <br>
> - predicting the price of an apartment using the prices of apartments that have already been sold;<br>
> - deducing the future sea levels in Ostend using sea levels from the past few decades. <br>

> **Concrete examples of classification:** <br>
> - determining whether an email is spam; <br>
> - being able to say whether a photo includes stomata.

![Regression](embed/regressie.png "Regression") 
<figure>
    <figcaption align = "center">Regression.</figcaption>
</figure> 

![Classification](embed/classificatie.png "Classification") 
<figure>
    <figcaption align = "center">Classification.</figcaption>
</figure>
