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
hruid: stem5_5
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
title: Logistic growth
version: 3
---
# Modeling a caterpillar outbreak using logistic growth

In the previous learning object, students established that the population size keeps increasing without any constraint when exponential growth with growth factor $a > 1$ is considered. However, we wish to take into account the carrying capacity of the ecosystem in which the population occurs; this determines the maximum population size that can be supported based on the amounts of food, water, and space available to sustain the population.

## Logistic growth

In this learning object, we introduce logistic growth, which takes into account the growth factor $a$ and the carrying capacity $K$:

\\[u_t = \left[1 + (a - 1) \left(1 - \frac{u_{t - 1}}{K}\right)\right] u_{t - 1} = \left[1 + r \left(1 - \frac{u_{t - 1}}{K}\right)\right] u_{t - 1}\\]

Students can investigate the effect of the parameters on this model:

- What is the effect of a larger carrying capacity?
- What is the effect of a larger population size?
- What happens when the population size is at some point larger than the carrying capacity?

## Creating graphs

In this learning object, students are asked to generate various graphs. A fixed template is used:

- The necessary libraries (Matplotlib and NumPy) are imported

- The necessary calculations are performed to generate the data to be plotted

- A new figure is created

- The previously generated data are plotted

- The axes are labeled

- A title is provided

- The graph is shown

Teachers can add their own accents here. For instance, various color palettes can be used, different series can be combined in the same graph with the help of a legend, and so on.

## Chaos theory

Throughout the learning object, students will discover that a certain randomness arises when certain values for the growth factor $a$ are used. This refers to chaos theory, which states that small differences in the initial conditions of a system can lead to large differences in the outcome. To frame this chaotic behavior, a separate learning object is provided.

## Python

This notebook, like the others, uses Python to perform calculations and generate graphs. As a teacher it is important to know:

- which [syntax](https://www.w3schools.com/python/python_syntax.asp) Python uses;

- how [functions](https://www.w3schools.com/python/python_functions.asp) are defined;

- how [lists](https://www.w3schools.com/python/python_lists.asp) can be used;

- how [for-loops](https://www.w3schools.com/python/python_for_loops.asp) work;

- how the [NumPy library](https://www.w3resource.com/numpy/array-creation/arange.php) makes it possible to generate a list of numbers, and to execute functions that use the values in this list as input arguments;

- how the [Matplotlib library](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py) makes it possible to generate graphs.

To make it easier for the teacher to understand what is happening, the necessary comments were provided. All functions were also provided with a description containing the function’s behavior, the parameters used as input, and the parameters returned as output. When a teacher wants to consult this description, it is sufficient to call `help(<function_name>)`.

## Minimum goals

### WD_06 Mathematics

#### General minimum goals

All considered tracks

<span style="color: yellowgreen">MD 06.19 Students describe phenomena from reality using mathematical concepts from the third grade.</span><br>
In this notebook, the growth of the population sizes of the box tree moth is discussed in detail, using a logistic growth model.

<span style="color: yellowgreen">MD 06.20 Students solve problems by mathematizing and demathematizing and by using heuristics.</span><br>
Among other things, the notebook asks to determine when the number of box tree moths is in equilibrium.<br>
Suggestions from the curriculum of Catholic Education Flanders: *Examples of heuristics that may be covered: explicating the given and the asked, reformulating the problem or splitting it into subproblems, making a sketch or drawing, examining special cases, temporarily dropping one of the conditions, working from back to front, writing down all possibilities and then eliminating them. Demathematizing can be done through a full-sentence answer. Checking whether an answer could be realistic is also part of this step of the solution process.*

<span style="color: yellowgreen">MD 06.21 Students use ICT to perform calculations and create graphical representations.</span><br>
The notebook calculates the population size at different moments in time and makes it possible to generate graphs that illustrate the population’s growth.

#### Natural Sciences B+S

Latin-Sciences; Sciences-Mathematics

#### Natural Sciences B+S'

Greek-Mathematics; Latin-Mathematics

<span style="color: yellowgreen">MD 06.46 Students analyze the interaction between sciences, technology, mathematics and society based on societal challenges.</span><br>
This minimum goal can be addressed in this module at the teacher’s initiative.

#### Mathematics B+S

Business-supporting computer science

<span style="color: yellowgreen">06.05.06 Students explain the relationship between the graph of a function and its characteristics.</span><br>
In the notebook, various graphs are generated that show the population size over time. Students observe that the population size stabilizes for certain values of \\(a\\).

<span style="color: yellowgreen">06.05.07 Students solve equations and inequalities graphically.</span><br>
Students determine when the population size is in equilibrium.

#### Mathematics B+S'

Biotechnological and Chemical STEM Sciences; Computer and Communication Sciences; Mechatronics

<span style="color: yellowgreen">06.04.06 Students explain the relationship between the graph of a function and its characteristics.</span><br>
In the notebook, various graphs are generated that show the population size over time. Students observe that the population size stabilizes for certain values of \\(a\\).

<span style="color: yellowgreen">06.04.07 Students solve equations and inequalities graphically.</span><br>
Students determine when the population size is in equilibrium.

#### Mathematics B+S''

Economics-Mathematics; Greek-Mathematics; Latin-Mathematics; Technological Sciences and Engineering; Sciences-Mathematics

<span style="color: yellowgreen">SMD 06.08.07 Students explain the relationship between the graph of a function and its characteristics.</span><br>
In the notebook, various graphs are generated that show the population size over time. Students observe that the population size stabilizes for certain values of \\(a\\).

<span style="color: yellowgreen">SMD 06.08.13 Students solve simple polynomial equations, rational equations, irrational equations, exponential equations, logarithmic equations and trigonometric equations algebraically.</span><br>
Students determine when the population size is in equilibrium.

### WD_07 Computer Science

#### Computer Science

Economics-Mathematics; Greek-Mathematics; Latin-Mathematics; Sciences-Mathematics

#### Computer Science S''

Business-supporting computer science

#### Computer and Communication Sciences B+S

Computer and Communication Sciences

#### Technological Sciences and Engineering B+S

Technological Sciences and Engineering

#### Business Sciences S (GO!)

Business Sciences (GO!)

<span style="color: yellowgreen">SMD 07.01.01 Students program self-designed solutions for concrete problems.</span><br>
A structured programming language is used, namely Python. A bounded loop is covered. The notebook uses variables, data types, data structures, operators, functions and software libraries. The necessary comments are provided so that students understand what the different code fragments do.

#### Biotechnological and Chemical STEM Sciences B+S

Biotechnological and Chemical STEM Sciences

#### Mechatronics B+S

Mechatronics

<span style="color: yellowgreen">SMD 07.02.01 Students program self-designed solutions for concrete problems.</span><br>
A structured programming language is used, namely Python. A bounded loop is covered. The notebook uses variables, data types, data structures, operators, functions and software libraries. The necessary comments are provided so that students understand what the different code fragments do.