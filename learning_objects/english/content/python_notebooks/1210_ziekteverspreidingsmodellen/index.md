---
available: true
content_type: text/markdown
copyright: dwengo
description: Epidemic
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: pn_epidemie1
keywords:
- voorbeeld
- voorbeeld2
language: en
licence: dwengo
return_value:
  callback_schema:
    att: test
    att2: test2
  callback_url: callback-url-example
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-digitale-media-en-toepassingen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
- http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-kansrekenen-statistiek
- http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek
- http://ilearn.ilabt.imec.be/vocab/curr1/s-stem-onderzoek
target_ages:
- 16
- 17
- 18
title: Disease spread models
version: 3
---
# Disease Spread Models

During an outbreak of an infectious disease, it's important to understand how this disease may spread in the coming days and weeks. This will help to plan the optimal use of resources and personnel to halt the propagation of the disease. Moreover, before we implement these measures, we need to know how they can affect the course of the disease, so that the most efficient and cost-effective measures can be implemented first.

To answer these and other important questions, *disease spread models* are often used. These models are based on mathematical equations that describe how an infectious disease spreads over time and/or space. They can be used to answer relevant questions, such as:

* Without intervention, will the disease die out or spread uncontrollably?
* How many people need to be vaccinated to stop the spread?
* How does the behavior of humans or animals affect the spread of diseases?
* What effect will different quarantine measures have?

Since the course over time is crucial in the case of disease spread, nearly all disease spread models are *dynamic* in nature. They model a change over time.
In this project, we will study a commonly used type of disease spread model: the SIR model.

With each wave of the COVID-19 pandemic, the number of infections or the number of hospital admissions at a given time experience exponential growth. In this project, you will learn to determine an exponential function through regression that reflects that trend in the data.