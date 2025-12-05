---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Logistic growth
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: stem5_4
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
title: Logistic growth
version: 3
---
# Modeling a caterpillar outbreak with logistic growth

Earlier you looked at the exponential growth model to represent a population of caterpillars. You observed that you must eventually hit a limit: a garden does not have unlimited carrying capacity! In this module you therefore look at logistic growth. This model has a surprising property: it can be chaotic, making it completely unpredictable for certain values!

## Logistic growth

**You are looking for a rule that takes the carrying capacity of the system into account.** It is expected that when the population size is small, and there are therefore many plants per caterpillar, unimpeded growth is possible. When the number of caterpillars approaches the carrying capacity \\(K\\), growth must stop. The following rule can be used for this:

\\[u_t = \left[1 + (a - 1) \left(1 - \frac{u_{t - 1}}{K}\right)\right] u_{t - 1} = \left[1 + r \left(1 - \frac{u_{t - 1}}{K}\right)\right] u_{t - 1}\\]

This is the recursive rule of a geometric sequence, where \\(a\\) represents the growth factor and \\(r\\) the growth rate. The same holds here: if you know \\(u_0\\), you can compute each term of the sequence step by step.

From the function rule you can see that if \\(u_{t - 1}\\) is small, the part between parentheses is approximately equal to \\(1\\). You then approximately obtain exponential growth again:

\\[u_t = \left[1 + r \left(1 - \frac{u_{t - 1}}{K}\right)\right] u_{t - 1} \approx (1 + r) \cdot u_{t - 1} = a \cdot u_{t - 1}\\]

Recall that \\(a\\) represents the growth factor here. When \\(u_{t - 1}\\) is approximately equal to \\(K\\), the part between parentheses is approximately equal to \\(0\\), and the population size in the next step will be more or less equal:

\\[u_t = \left[1 + r \left(1 - \frac{u_{t - 1}}{K}\right)\right] u_{t - 1} \approx u_{t - 1}\\]

The population size thus stabilizes.

A model in which the population grows according to the proposed recursive rule is called a **logistic model**!

## Interactive notebook

Now you will get to work with an interactive online notebook, in which you will use Python to visualize this model.

[![](embed/knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=6020_en "Logistic")