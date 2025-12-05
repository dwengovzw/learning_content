---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: The chaos explained
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: stem5_7
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
title: The chaos explained
version: 3
---
# The chaos explained

## Transitions between population sizes

In this learning object, the apparent randomness for certain values of the growth factor $a$ is examined closely. To that end, a new graph is introduced that shows the transitions from \\(u_{t - 1}\\) to \\(u_t\\), together with the first bisector and the equilibrium point. This graph is provided via a function that can be reused to explore the impact of the parameters \\(u_0\\), \\(a\\), and \\(K\\):

- What happens for different values of \\(a > 1\\)?

- What impact does the starting value \\(u_0=\\) have? What happens if \\(u_0 = K\\)?

Based on the given tasks, students will observe that a period of two, a period of four, or chaotic behavior is obtained.

## The bifurcation diagram

Code is provided to generate a bifurcation diagram, where the logistic equation is applied for a large number of steps, for all values of \\(a\\) from \\(0\\) to \\(4\\) with increments of \\(0{,}01\\). Typically, all integer values from 1 up to and including \\(K - 1\\) are plotted, but to account for large values of \\(K\\) (which significantly affect execution time) it is decided to draw 100 random numbers between \\(1\\) and \\(K - 1\\) with replacement. From the result, the following can be concluded:

- for $0 < a < 1$ there is no growth, the population dies out;

- for $1 \le a < 3$ there is convergence to $K$;

- for $3 \le a < 4$ you first observe a split (a bifurcation) into two, indicating a periodic sequence with period two. For higher values you observe a periodic sequence of four, eventually transitioning to a chaotic regime.

Currently, the code for this plot is provided, with the request that students use it to create a second plot with different properties. The teacher can also choose not to provide the sample code and make this a (programming) assignment.

## Saving plots

Students are asked to save a generated bifurcation diagram to a PDF file. For this, the `Matplotlib` library will be used.

## Python

This notebook, like the others, uses Python to perform calculations and generate plots. As a teacher, it is important to know:

- which [syntax](https://www.w3schools.com/python/python_syntax.asp) Python uses;

- how [functions](https://www.w3schools.com/python/python_functions.asp) are defined;

- how [lists](https://www.w3schools.com/python/python_lists.asp) can be used;

- how [for-loops](https://www.w3schools.com/python/python_for_loops.asp) work;

- how the [NumPy library](https://www.w3resource.com/numpy/array-creation/arange.php) makes it possible to generate a list of numbers and to generate random numbers within a given range;

- how the [Matplotlib library](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py) makes it possible to generate plots and save them to a local file.

To make it easier for the teacher to understand what is happening, the necessary comments have been provided. All functions have also been provided with a description that includes the function’s behavior, the parameters used as input, and the parameters returned as output. When a teacher wants to consult this description, it suffices to call `help(<function_name>)`.

## Minimum goals

### WD_06 Mathematics

#### General minimum goals

All considered tracks

<span style="color: yellowgreen">MD 06.19 Students describe real-world phenomena using mathematical concepts from the third grade.</span><br>
In this notebook, the growth of the population sizes of the box tree moth is discussed in detail, using a logistic growth model.

<span style="color: yellowgreen">MD 06.21 Students use ICT to perform calculations and create graphical representations.</span><br>
The notebook calculates the population size after about a hundred generations, for various values of the growth factor \\(a\\) and starting values \\(u\\). This makes it possible to generate a bifurcation diagram that illustrates the impact of the growth factor on the final population size.

#### Natural sciences B+S

Latin-Sciences; Sciences-Mathematics

#### Natural sciences B+S'

Greek-Mathematics; Latin-Mathematics

<span style="color: yellowgreen">MD 06.46 Students analyze the interaction between science, technology, mathematics, and society based on societal challenges.</span><br>
This minimum goal can be incorporated into this module at the teacher’s initiative.

### WD_07 Computer science

#### Computer science

Economics-Mathematics; Greek-Mathematics; Latin-Mathematics; Sciences-Mathematics

#### Computer science S''

Business-supporting computer science

#### Computer and communication sciences B+S

Computer and communication sciences

#### Technological sciences and Engineering B+S

Technological sciences and Engineering

#### Business sciences S (GO!)

Business sciences (GO!)

<span style="color: yellowgreen">SMD 07.01.01 Students program self-designed solutions to concrete problems.</span><br>
A structured programming language is used, namely Python. A bounded repetition is covered. The notebook uses variables, data types, data structures, operators, functions, and software libraries. The necessary comments are provided so that students understand what the different code fragments do.

#### Biotechnological and chemical STEM sciences B+S

Biotechnological and chemical STEM sciences

#### Mechatronics B+S

Mechatronics

<span style="color: yellowgreen">SMD 07.02.01 Students program self-designed solutions to concrete problems.</span><br>
A structured programming language is used, namely Python. A bounded repetition is covered. The notebook uses variables, data types, data structures, operators, functions, and software libraries. The necessary comments are provided so that students understand what the different code fragments do.