---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Modeling a caterpillar outbreak
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: stem5_0
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
title: Modeling a caterpillar outbreak
version: 3
---
# Modeling a caterpillar outbreak

## Ecologists model

**Ecologists study how living organisms interact with other living organisms and with their environment.**<br>

One of the most fundamental questions they try to answer is how a population of animals, plants, bacteria, or humans changes over time. Does it grow? Decline? Stagnate? Does the population go up and down? Can it suddenly implode? 

Ecologists answer these kinds of questions using **growth models**: mathematical equations that represent the (expected) growth over time. 

## Meet the box tree moth

Many insects are beneficial, but they are often a pest when they devour plants. For example, the larva of the box tree moth (*Cydalima perspectalis*) is a nightmare for any gardener with a neat boxwood hedge. The box tree moth is an invasive species in Europe with a large economic cost. You can read more on the [ILVO website](https://ilvo.vlaanderen.be/nl/dossiers/buxusmot).

![Box tree moth](embed/buxusmot.jpg "https://commons.wikimedia.org/wiki/File:Raupe_des_Buchsbaumz%C3%BCnsler,_Cydalima_perspectalis_11.JPG")<br/>
Source: böhringer friedrich, CC BY-SA 2.5 <https://creativecommons.org/licenses/by-sa/2.5>, via Wikimedia Commons

Because this caterpillar is so harmful, ecologists and crop protection specialists are very interested in monitoring and modeling population growth. **Mathematical models help them estimate whether the population stays within an acceptable size or when it threatens to get out of hand and control is needed.**

## A mathematical model

<div class="alert alert-box alert-success">
The goal is to obtain a sequence that represents the population size over time:<br>
<align="center"><em><b>u<sub>0</sub>, u<sub>1</sub>, u<sub>2</sub>, ..., u<sub>t-1</sub>, u<sub>t</sub>, ...</b></em>

Where:<br>
-  <em>u<sub>0</sub></em> is the initial population size: the number of caterpillars at the start of the measurements.
-  <em>u<sub>t</sub></em> represents the population size at generation or time <em>t</em>.
-  <em>t</em> takes the values <em>0, 1, 2, 3, ...</em>.

<strong>Suppose that <em>u<sub>t-1</sub></em>, the number of caterpillars at time <em>t-1</em>, is known.<br> What, then, is <em>u<sub>t</sub></em>? In other words, how many caterpillars are there at time <em>t</em>?</strong>
</div>

So you look for an equation that tells you the population size at time *t*, given the number of caterpillars at time *t-1*. 

**A mathematical model is always a simplification of reality.** Here you will model a caterpillar population in non-overlapping generations.

To begin with, you make three **assumptions** for such an equation:

- The equation is *deterministic*: the same number at time *t-1* always results in the same number at time *t*. Random fluctuations are not taken into account.

- The population size can be represented by real numbers instead of natural numbers. In reality there are no (living) 'half' caterpillars; for those who are not entirely comfortable with fractions of caterpillars, you can also think of *u<sub>t</sub>* as the biomass of caterpillars, the total mass of caterpillars at time *t*. For substantial population sizes, for example, you can work with a unit of 100 or 1000, allowing the counts to be expressed by decimal numbers.

- *Time* ticks *discretely*: the population size is viewed as a sequence of perfectly separated generations. A model gives the population sizes at times *0, 1, 2, 3, ...*. For instance, it makes no sense to look at time *2.4*. There is nothing between generations!

<div class="alert alert-box alert-success">
You can therefore see a discrete model as a kind of clock that keeps ticking. At each step the same rule is applied to a variable to go from the current generation to the next.
</div>

Depending on how you make the rule concrete, you obtain a different model. In the later parts of this learning path you will relax each of the above assumptions to obtain more realistic models.

You start with two discrete models:

- Exponential growth, where the population either goes extinct or keeps growing without restraint.
- Logistic growth, where the population does have a limit and can exhibit much richer behavior.

<div class="alert alert-box alert-success">
A mathematical model is always a simplification of reality.

A mathematical model helps to better understand the real situation.
</div>