---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Exponential growth
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: stem5_2
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
title: Exponential growth
version: 3
---
# Modeling a caterpillar outbreak according to exponential growth

Many insects want to produce as many offspring as possible. In one generation, box tree moth caterpillars pupate into box tree moths, which in turn lay new eggs on a hedge. From these eggs, new caterpillars hatch and the cycle starts again. However, the life of an insect is not without danger. At any point in the cycle, eggs, caterpillars, pupae, and moths can die due to predation by birds, pesticides, starvation, or other hazards. On average, however, you can assume that each caterpillar gives rise to a certain number of new caterpillars in the next generation. This assumption forms the basis of exponential growth.

## Exponential growth

When you may assume that a caterpillar on average gives rise to \\(a > 0\\) new caterpillars, you obtain the following expression:

\\[u_t = a \cdot u_{t - 1}\\]

This equation is nothing more than the recursive definition of a sequence, whereby, based on a given element, you can easily determine the next element by multiplying by \\(a\\). This parameter \\(a\\) is called the growth factor.

### Exercise 1

- Describe the situation depending on the value of \\(a\\). What happens, for example, if \\(a < 1\\)?
- The box tree moth caterpillars constitute a pest. Which values of \\(a\\) fit this situation?
- Explain why you are dealing with exponential growth here.

## Exponential model

With a growth factor \\(a = 1.6\\), each caterpillar on average leads to just over one and a half new caterpillars per generation. Consider a modest initial population of five caterpillars. Use the following exercise to set up a mathematical model for the evolution of population size.

### Exercise 2

- Set \\(a = 1.6\\) and \\(u_0 = 5\\). Then determine the number of caterpillars at \\(t = 1\\), \\(t = 2\\), \\(t = 3\\) and \\(t = 4\\).
- Formulate the general rule for the sequence with this exponential growth.

The general rule now represents the exponential growth model!

## Interactive notebook

Now get started with an interactive online notebook. In the notebook, you will use Python to perform calculations and to present the model graphically.

[![](embed/knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=6010_en "Expon")

## Beyond the insects

Now look at the following graph, which shows the number of transistors on a computer chip as a function of time. Note that a logarithmic axis is used, and that you are indeed dealing with exponential growth!

![Moore](embed/moore.png "https://commons.wikimedia.org/wiki/File:Moore%27s_Law_Transistor_Count_1970-2020.png")<br/>
Source: [https://commons.wikimedia.org/wiki/File:Moore%27s_Law_Transistor_Count_1970-2020.png](https://commons.wikimedia.org/wiki/File:Moore%27s_Law_Transistor_Count_1970-2020.png)

Various computer scientists argue that Moore’s law cannot continue, because developers will sooner or later encounter physical limits. **Infinite growth is almost always impossible: at some point you have to run into the system’s limits.** Nevertheless, an exponential model often provides an excellent description of the beginning of the growth.