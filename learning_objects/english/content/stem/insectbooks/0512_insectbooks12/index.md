---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Differential equations
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: stem5_12
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
title: Differential equations
version: 3
---
# Ladybugs and aphid infestations: a dynamic view of the world with differential equations

We have already established that in practice time is experienced as continuous, making discrete growth models insufficient for long. Therefore, scientists often describe reality with a more powerful model: the differential equation. The solution of such a differential equation is not a number but a function that describes the system over time. Differential equations are usually only introduced after a solid mathematical foundation. In this learning object, we give a first introduction to differential equations, with the goal of describing a population of aphids and ladybugs.

## Biological control with ladybugs

Where caterpillars are true monsters that eat plant leaves and thereby damage crops, aphids are more refined. With their needle-shaped mouthparts, they suck the sap of a plant directly from the vascular tissue. This sap contains mainly sugars and relatively few amino acids that the aphids also need. Therefore, the aphids excrete most of the sap again, stripped of most amino acids; this substance is called honeydew. Although honeydew is an important food source for ants and wasps, it can also attract harmful fungi. Moreover, through the vascular tissue, aphids not only remove the plant’s valuable sugars, but also dangerous plant viruses that can spread further in this way. Therefore, aphids are very troublesome pests for many types of crops, such as potatoes, beans, and roses.

![Aphid](embed/bladluis.jpg "https://commons.wikimedia.org/wiki/File:Aphids_May_2010-2.jpg")<br>
Source: [https://commons.wikimedia.org/wiki/File:Aphids_May_2010-2.jpg](https://commons.wikimedia.org/wiki/File:Aphids_May_2010-2.jpg)

Because aphids are so harmful, various chemical pesticides exist. However, this treatment can cause harmful substances to end up in crops and soil, which are bad for people and nature. Therefore, biological control is also often applied: aphids are, after all, tasty food for many other insects and birds. The ladybug in particular is a real killing machine for aphids. Larvae alone eat about 400 aphids, while an adult ladybug can devour as many as 5000 aphids. One can therefore buy ladybug larvae to bring an aphid infestation under control.

![Ladybug](embed/lieveheersbeestje.jpg "https://commons.wikimedia.org/wiki/File:Ladybug.jpg")<br>
Source: [https://commons.wikimedia.org/wiki/File:Ladybug.jpg](https://commons.wikimedia.org/wiki/File:Ladybug.jpg)

When ladybugs are introduced into the environment, they will continue to reproduce. A ladybug can lay as many as 50 eggs in a day, which first become larvae, and after about 20 days pupate into new ladybugs. This means that the population will grow as long as there is sufficient food. When at some point too few aphids remain, the number of ladybugs will decrease again.

To model the effects of biological control, you therefore need a more complex model than the models discussed earlier. You will need to model two states: the number of aphids and the number of ladybugs.

## Population size as a differential equation

In this module, you will use the concept of derivatives to describe the change in the population size of aphids and ladybugs, where one population size has a direct impact on the other. For this, you will use an equation in which both a function and its derivative appear; this is called a differential equation.

Characteristic of differential equations is that the derivative of a function, denoted as \\(\dot{y}\\), can be written as a function of the original function \\(y\\) at a specific moment in time \\(t\\):

\\[\dot{y} = f(y, t)\\]

Specifically targeting the aphid problem, you can describe the growth of the aphid population size as follows:

\\[\dot{y} = ry \left(1 - \frac{y}{K}\right)\\]

Here \\(r = a - 1\\) denotes the growth rate and \\(K\\) the carrying capacity (both strictly positive constants), and \\(y\\) denotes the population size. \\(\dot{y}\\) is then the derivative of \\(y\\), which tells you something about the change in population size:

- when \\(\dot{y} > 0\\), the population size will increase;
- when \\(\dot{y} < 0\\), the population size will decrease;
- when \\(\dot{y} = 0\\), there will be no change and the population size remains constant.

It is therefore important to note that \\(\dot{y}\\) describes the change (growth/decline) of the population size, and not the population size itself!

You can ask yourself when the system is in equilibrium, and the population size thus remains constant. In that case, you must solve the following equation:

\\[\dot{y} = 0 \iff ry \left(1 - \frac{y}{K}\right) = 0 \iff ry = 0 \lor 1 - \frac{y}{K} = 0 \iff y = 0 \lor y = K\\]

In the first case there are no aphids; in the second case the carrying capacity \\(K\\) is reached (see earlier).

The aim now is to be able to describe the evolution of the population size over time. To do this, you can use the Euler method, which allows you to compute a numerical solution of a differential equation with initial conditions. Recall that you can approximate the derivative of a function as follows:

\\[f'(t) \approx \frac{f(t + \Delta t) - f(t)}{\Delta t}\\]

with \\(\Delta t\\) as small as possible. You then find that:

\\[f(t + \Delta t) \approx f(t) + \Delta t \cdot f'(t)\\]

In the case under consideration, \\(y = f(t)\\) denotes the population size, and \\(\dot{y} = f'(t)\\) the change of this quantity. In the interactive notebook, you will use this latter formula to make step-by-step new estimates for the function \\(f\\).

## Interactive notebook

Get started now with an interactive notebook, in which you will use Python to map out the interaction between the population sizes of aphids and ladybugs.

[![](embed/knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=6050_en "Dynamic model")