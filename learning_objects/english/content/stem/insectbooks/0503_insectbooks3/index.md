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
hruid: stem5_3
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
title: Exponential growth
version: 3
---
# Modeling a caterpillar outbreak using exponential growth

## Situation depending on the growth factor \\(a\\)

The number \\(a\\) represents the average number of offspring per caterpillar. We work with averages, so decimal numbers are allowed, but negative numbers do not make sense.

- If \\(a < 1\\), then each caterpillar produces less than one caterpillar per generation. At each time step the population becomes smaller and smaller until it eventually dies out. This is an exponential **decrease**.
- If \\(a > 1\\), then each caterpillar will give rise to more than one new caterpillar in the next generation. The population will grow. This is an exponential **increase**.
- In the edge case where \\(a = 1\\), the population size is **stable**: the birth of new caterpillars compensates for mortality.

In the case of the caterpillar of the box tree moth, \\(a > 1\\), since these caterpillars are a pest.

The formula is the recursive formula of a geometric sequence. The number \\(a\\) is nothing more than the equivalent of the **growth factor** in an exponential function (continuous model instead of discrete). So this is **exponential growth**. 

## The parameters in the mathematical model

In the notebook, the graph of a geometric sequence is plotted using the general formula. The index \\(t\\) here plays the role of the **variable**. For certain values of \\(t\\), the population size is calculated and returned.

The geometric sequence is determined by the general formula with two **parameters**: the growth factor \\(a\\) and the initial value \\(u_0\\). By adjusting the parameters, you can experiment with the model. Students can investigate the effect of the parameters on the model:

- What is the effect of a larger initial value?
- What is the effect of a larger growth factor?
- What is the effect of a growth factor less than 1?

## Carrying capacity

In the notebook, the graph is drawn of a geometric sequence that models the evolution of the caterpillar population size. **The graph makes the problem much clearer.**

The infestation grows very rapidly, which is alarming. Looking further ahead in time, you find the following: the population size continues to grow without any hindrance; after 70 generations there are more than 971.000.000.000.000 caterpillars. There are not enough boxwood hedges in the world to support such populations!

In practice, every ecosystem has a certain **carrying capacity**, the amounts of food, water and space available to support a given population. Our caterpillar population is limited by the number of plants available as food. The carrying capacity is often denoted by the letter \\(K\\). A value \\(K = 1000 \\) would mean that a garden has enough boxwoods to feed 1,000 caterpillars, but no more.

In the next learning object, the model is adapted to take this carrying capacity into account.

## COVID-19 infections

As an illustration, data are read from a CSV file that describes the number of infections and deaths due to COVID-19 in Belgium in the first weeks of the lockdown in March 2020. Using several graphs, the danger of unbounded growth is illustrated. The `Pandas` library is used to read the data.

Students who finish this learning object early, or who show a strong interest in this topic, can follow [this related learning object](https://www.dwengo.org/learning-path.html?hruid=maths_epidemie&language=nl&te=true&source_page=%2F&source_title=%20Ga%20aan%20de%20slag%20met%20uniek%20lesmateriaal%20over%20AI%20en%20STEM!#pn_expogroei;nl;3).

## The logarithmic axis

As a final example of exponential growth, Moore’s law is discussed. To illustrate this, a graph with a logarithmic axis is used; the use of such an axis is discussed using concrete examples in Python.

## Python

This notebook, like the others, uses Python to perform calculations and generate graphs. As a teacher it is important to know:

- which [syntax](https://www.w3schools.com/python/python_syntax.asp) Python uses;

- how [functions](https://www.w3schools.com/python/python_functions.asp) are defined;

- how [lists](https://www.w3schools.com/python/python_lists.asp) can be used;

- how [for loops](https://www.w3schools.com/python/python_for_loops.asp) work;

- how [while loops](https://www.w3schools.com/python/python_while_loops.asp) work;

- how the [NumPy library](https://www.w3resource.com/numpy/array-creation/arange.php) makes it possible to generate a list of numbers, and to execute functions that use the values in this list as input arguments;

- how the [Matplotlib library](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py) makes it possible to generate graphs;

- how the [Pandas library](https://pythonbasics.org/read-csv-with-pandas/) makes it possible to read CSV files into a dataframe that contains data in tabular form.

To make it easier for the teacher to understand what is happening, the necessary comments were provided. All functions were also provided with a description including the function’s behavior, the parameters used as input, and the parameters returned as output. When a teacher wants to consult this description, it suffices to call `help(<function_name>)`.

## Minimum attainment targets

### WD_06 Mathematics

#### General minimum objectives

All considered streams

<span style="color: yellowgreen">MD 06.06 Students use models for exponential growth.</span><br>
In this notebook, the growth of the population sizes of the box tree moth is discussed in detail, using an exponential growth model.<br>
Clarification from the curriculum of Catholic Education Flanders: *This objective includes on the one hand modeling (formulating the rule from a verbal description) and on the other hand answering questions using the model, for example determining the value at a given time or determining the time for a given value. Although "exponential growth" suggests an increase, you can also describe decreasing processes.*

<span style="color: yellowgreen">MD 06.12 Students use arithmetic and geometric sequences to describe patterns.</span><br>
This concerns a geometric sequence, where initially the recursive rule is used. For the model, the formula of the exponential function, the formula for the general term is used.

<span style="color: yellowgreen">MD 06.19 Students describe real-world phenomena using mathematical concepts from the third stage.</span><br>
In this notebook, the growth of the population sizes of the box tree moth is discussed in detail, using an exponential growth model.

<span style="color: yellowgreen">MD 06.20 Students solve problems by mathematizing and de-mathematizing and by using heuristics.</span><br>
In the notebook, among other things, it is asked to determine when the number of box tree moths first exceeds a given value.<br>
Tips from the curriculum of Catholic Education Flanders: *Examples of heuristics that may be covered: making the given and the asked explicit, reformulating the problem or breaking it down into subproblems, making a sketch or drawing, investigating special cases, temporarily dropping one of the conditions, working backward, writing down all possibilities and then eliminating. De-mathematizing can be done via a sentence-form answer. Checking whether an answer could be realistic is also part of this step of the solution process.*

<span style="color: yellowgreen">MD 06.21 Students use ICT to perform calculations and create graphical representations.</span><br>
The notebook computes the population size at different times, and allows the generation of graphs that illustrate the growth of the population.

#### Natural sciences B+S

Latin-Sciences; Sciences-Mathematics

#### Natural sciences B+S'

Greek-Mathematics; Latin-Mathematics

<span style="color: yellowgreen">MD 06.46 Students analyze the interaction between science, technology, mathematics, and society based on societal challenges.</span><br>
This minimum objective can be incorporated into this module at the initiative of the teacher.

#### Mathematics B+S

Business-supporting information sciences

<span style="color: yellowgreen">06.05.06 Students relate a function’s graph to its characteristics.</span><br>
In the notebook, various graphs are generated that show the population size over time. Students observe that the population size continues to increase if \\(a > 1\\). It is also explained how the logarithmic axis can be used in a graph.

#### Mathematics B+S'

Biotechnological and chemical STEM sciences; Computer and communication sciences; Mechatronics

<span style="color: yellowgreen">06.04.06 Students relate a function’s graph to its characteristics.</span><br>
In the notebook, various graphs are generated that show the population size over time. Students observe that the population size continues to increase if \\(a > 1\\). It is also explained how the logarithmic axis can be used in a graph.

#### Mathematics B+S''

Economics-Mathematics; Greek-Mathematics; Latin-Mathematics; Technological sciences and Engineering; Sciences-Mathematics

<span style="color: yellowgreen">SMD 06.08.07 Students relate a function’s graph to its characteristics.</span><br>
In the notebook, various graphs are generated that show the population size over time. Students observe that the population size continues to increase if \\(a > 1\\). It is also explained how the logarithmic axis can be used in a graph.

<span style="color: yellowgreen">SMD 06.08.09 Students solve equations and inequalities graphically.</span><br>
Students calculate the population size at a given point in time, and using a while loop they check when the population size will first exceed a given value.

### WD_07 Information sciences

#### Information sciences

Economics-Mathematics; Greek-Mathematics; Latin-Mathematics; Sciences-Mathematics

#### Information sciences S''

Business-supporting information sciences

#### Computer and communication sciences B+S

Computer and communication sciences

#### Technological sciences and Engineering B+S

Technological sciences and Engineering

#### Business sciences S (GO!)

Business sciences (GO!)

<span style="color: yellowgreen">SMD 07.01.01 Students program self-designed solutions to concrete problems.</span><br>
A structured programming language is used, namely Python. A bounded loop is covered. The notebook uses variables, data types, data structures, operators, functions, and software libraries. The necessary comments are provided so that students understand what the various code fragments do.

#### Biotechnological and chemical STEM sciences B+S

Biotechnological and chemical STEM sciences

#### Mechatronics B+S

Mechatronics

<span style="color: yellowgreen">SMD 07.02.01 Students program self-designed solutions to concrete problems.</span><br>
A structured programming language is used, namely Python. A bounded loop is covered. The notebook uses variables, data types, data structures, operators, functions, and software libraries. The necessary comments are provided so that students understand what the various code fragments do.