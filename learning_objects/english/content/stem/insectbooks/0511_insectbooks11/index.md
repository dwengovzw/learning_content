---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: The finite difference method
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: stem5_11
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
title: The finite difference method
version: 3
---
# The finite difference method

In this learning object, the finite difference method is explained, which uses the difference quotient to estimate the derivative of a function at a given value:

\\[f'(t) = \frac{\text{d}f(t)}{\text{d}t} \approx \frac{f(t + \Delta t) - f(t)}{\Delta t}\\]

A concrete example is given for the function \\(f\\) with definition \\(f(t) = t sin (t)\\), although other examples are of course also possible.

## The impact of the time interval \\(\Delta t\\)

A function `plot_afgeleide` is provided that makes it possible to plot the derivative of the function \\(f\\) in a graph, together with an estimate of the function values based on the finite difference method. This Python function takes the time interval \\(\Delta t\\) as input, which makes it possible to experiment with different values for this parameter; this allows the student to investigate the impact of a larger/smaller time interval.

As an extension, the teacher can have alternative functions investigated, or ask students to find a time interval \\(\Delta t\\) for which the deviation from the actual values does not exceed a given threshold. It can also be requested to provide a single plot in which the obtained results are plotted for different values of the time interval, with an accompanying legend.

## Python

This notebook, like the others, uses Python to perform calculations and generate plots. As a teacher, it is important to know:

- which [syntax](https://www.w3schools.com/python/python_syntax.asp) Python uses;

- how [functions](https://www.w3schools.com/python/python_functions.asp) are defined;

- how [for loops](https://www.w3schools.com/python/python_for_loops.asp) work;

- how the [NumPy library](https://www.w3resource.com/numpy/array-creation/arange.php) makes it possible to generate a list of numbers;

- how the [Matplotlib library](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py) makes it possible to generate plots.

To make it easier for the teacher to understand what is happening, the necessary comments have been provided. All functions were also provided with a description containing the operation of the function, the parameters used as input, and the parameters returned as output. When a teacher wants to consult this description, it suffices to call `help(<functie_naam>)`.

## Minimum objectives

### WD_06 Mathematics

#### General minimum objectives

All considered tracks

<span style="color: yellowgreen">MD 06.03 Students interpret the derivative as the limit of a difference quotient and as the slope of the tangent line to the graph.</span><br>
The finite difference method is covered, with the difference quotient discussed.

<span style="color: yellowgreen">MD 06.04 Students graphically relate a function and its derivative.</span><br>
Students observe that the function values increase when the derivative is positive, and decrease when it is negative.

<span style="color: yellowgreen">MD 06.21 Students use ICT to perform calculations and create graphical representations.</span><br>
The notebook computes the estimated derivative for different values of \\(t\\), and allows generating plots that illustrate the impact of the variable \\(\Delta t\\).

#### Mathematics B+S

Business-supporting computer science

<span style="color: yellowgreen">06.05.06 Students relate the graph of a function to its characteristics.</span><br>
In the notebook, the graph of a function is plotted, with periodicity identified. The link between the function’s rise and fall and its derivative is discussed.

#### Mathematics B+S'

Biotechnological and Chemical STEM Sciences; Information and Communication Sciences; Mechatronics

<span style="color: yellowgreen">06.04.06 Students relate the graph of a function to its characteristics.</span><br>
In the notebook, the graph of a function is plotted, with periodicity identified. The link between the function’s rise and fall and its derivative is discussed.

#### Mathematics B+S''

Economics-Mathematics; Greek-Mathematics; Latin-Mathematics; Technological Sciences and Engineering; Sciences-Mathematics

<span style="color: yellowgreen">SMD 06.08.07 Students relate the graph of a function to its characteristics.</span><br>
In the notebook, the graph of a function is plotted, with periodicity identified. The link between the function’s rise and fall and its derivative is discussed.

### WD_07 Computer Science

#### Computer Science

Economics-Mathematics; Greek-Mathematics; Latin-Mathematics; Sciences-Mathematics

#### Computer Science S''

Business-supporting computer science

#### Information and Communication Sciences B+S

Information and Communication Sciences

#### Technological Sciences and Engineering B+S

Technological Sciences and Engineering

#### Business Sciences S (GO!)

Business Sciences (GO!)

<span style="color: yellowgreen">SMD 07.01.01 Students program self-designed solutions to concrete problems.</span><br>
A structured programming language is used, namely Python. Bounded iteration is covered. The notebook uses variables, data types, data structures, operators, functions, and software libraries. The necessary comments are provided so that students understand what the different code fragments do.

#### Biotechnological and Chemical STEM Sciences B+S

Biotechnological and Chemical STEM Sciences

#### Mechatronics B+S

Mechatronics

<span style="color: yellowgreen">SMD 07.02.01 Students program self-designed solutions to concrete problems.</span><br>
A structured programming language is used, namely Python. Bounded iteration is covered. The notebook uses variables, data types, data structures, operators, functions, and software libraries. The necessary comments are provided so that students understand what the different code fragments do.