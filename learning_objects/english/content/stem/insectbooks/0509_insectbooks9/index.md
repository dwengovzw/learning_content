---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: The Leslie matrix
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: stem5_9
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
title: The Leslie matrix
version: 3
---
# Modeling the life cycle of a beetle with the Leslie matrix

In this learning object, students will become familiar with the Leslie matrix, which makes it possible to calculate the number of individuals in a specific life stage of a population. This matrix is introduced using the beetle’s life stages: the egg, the larva, and the adult beetle. This sequence of life stages leads to a cycle, which can be cast into a graph:

![Graph](embed/graph.png "https://www.wisfaq.nl/pagina.asp?nummer=1883")

Based on the values of the nodes in the graph, the next state can be computed. To simplify this process, students will use matrices.

## The Leslie matrix

To perform matrix multiplication, the state at time \(0\) is set equal to a vector \(v_0\), which contains the number of eggs, larvae, and beetles. The following example is used:

\[v_0 = \begin{bmatrix} 1000 \\ 100 \\ 60 \end{bmatrix}\]

To determine the state \(v_{1}\) at time \(1\), the Leslie matrix \(L\) is used. In the example above it looks as follows:

\[L = \begin{bmatrix} 0 & 0 & 100 \\ 0.05 & 0 & 0 \\ 0 & 0.75 & 0 \end{bmatrix}\]

Starting from the state \(v_0\), \(v_{1}\) can be computed as follows:

\[v_{1} = L v_0 = \begin{bmatrix} 0 & 0 & 100 \\ 0.05 & 0 & 0 \\ 0 & 0.75 & 0 \end{bmatrix} \begin{bmatrix} 1000 \\ 100 \\ 60 \end{bmatrix} = \begin{bmatrix} 6000 \\ 50 \\ 75 \end{bmatrix}\]

## Matrices in Python

The learning object first provides an introduction to matrices, which can be worked with using the `NumPy` library. Several examples are given, and students are asked to do a few simple calculations by hand first. The following is explained:

- How matrices can be defined

- How matrix multiplications can be performed

- That NumPy makes it possible to multiply a matrix on the right by a row matrix, even though this calculation is not mathematically allowed

- How powers of a matrix can be computed using the function `linalg.matrix_power`

On this basis, the necessary calculations are made regarding the population size of the beetles. In addition, among other things, students are asked to generate a graph for which the requisite data must be provided.

## Mortality tables

As a second example, we work with mortality and reproduction figures for women. Women are grouped by age, in periods of ten years.

To calculate the probability that a randomly selected woman moves from one phase to the next, a mortality table with official data for Belgium is used. Students are asked to consult it and, based on the data (per year), compute the survival probabilities (after ten years) and enter these into the Leslie matrix.

In addition, fictitious data are provided that contain the expected number of daughters a woman has in a given life stage. By entering these into the Leslie matrix as well, the number of women in a particular stage can be determined over ten-year periods.

## Writing to CSV files

Students are asked to write the calculated data for the next 20 generations of women to a CSV file. The `Pandas` library is used to write the data.

## Python

This notebook, like the others, uses Python to perform calculations and generate plots. As a teacher it is important to know:

- which [syntax](https://www.w3schools.com/python/python_syntax.asp) Python uses;

- how [functions](https://www.w3schools.com/python/python_functions.asp) are defined;

- how [lists](https://www.w3schools.com/python/python_lists.asp) can be used;

- how [for-loops](https://www.w3schools.com/python/python_for_loops.asp) work;

- how the [NumPy library](https://www.w3resource.com/numpy/array-creation/arange.php) makes it possible to generate a list of numbers, define matrices, perform matrix multiplications and exponentiation, and reshape matrices;

- how the [Matplotlib library](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py) makes it possible to generate plots;

- how the [Pandas library](https://pythonbasics.org/read-csv-with-pandas/) makes it possible to write data from a dataframe, which contains the data in tabular form, to a CSV file.

To make it easier for the teacher to understand what is happening, the necessary comments have been provided. All functions have also been provided with a description including the function’s behavior, the parameters used as input, and the parameters returned as output. When a teacher wants to consult this description, it suffices to call `help(<function_name>)`.

## Minimum objectives

### WD_06 Mathematics

#### General minimum objectives

All considered tracks

<span style="color: yellowgreen">MD 06.19 Students describe phenomena from reality using mathematical concepts from the third grade.</span><br>
In this notebook, the growth of the population sizes of the beetle (in the form of eggs, larvae, and beetles) is discussed in detail, using the Leslie matrix.

<span style="color: yellowgreen">MD 06.20 Students solve problems by mathematizing and demathematizing and by using heuristics.</span><br>
In the notebook, among other things, students are asked to determine when the number of newborn girls first exceeds a given value.<br>
Guidelines from the curriculum of Catholic Education Flanders: Examples of heuristics that may be covered: making the given and the asked explicit, reformulating the problem or dividing it into subproblems, making a sketch or drawing, investigating special cases, temporarily dropping one of the conditions, working backward, writing down all possibilities and then eliminating. Demathematizing can be done via an answer sentence. Checking whether an answer can be realistic is also part of this step of the solution process.

<span style="color: yellowgreen">MD 06.21 Students use ICT to perform calculations and create graphical representations.</span><br>
The notebook computes the population size after a number of time steps for the different life stages of the beetle. This makes it possible to generate a graph that illustrates the number of individuals in each life stage.

#### Natural sciences B+S

Latin-Sciences; Sciences-Mathematics

#### Natural sciences B+S'

Greek-Mathematics; Latin-Mathematics

<span style="color: yellowgreen">MD 06.46 Students analyze the interaction between sciences, technology, mathematics, and society based on societal challenges.</span><br>
This minimum objective can be included in this module at the teacher’s initiative.

#### Mathematics B+S

Business-supporting computer science

<span style="color: yellowgreen">06.05.01 Students perform operations with matrices: addition, scalar multiplication, matrix multiplication, raising to a power, and transposition.</span><br>
Multiplications of the Leslie matrix with a column vector are applied to determine the state in the next time step, and raising the Leslie matrix to a power is applied to determine the state further in time.

<span style="color: yellowgreen">06.05.02 Students use matrix models to describe evolutions.</span><br>
The Leslie matrix is used to describe the evolution of the number of eggs, larvae, and beetles over time. The link is made with the matrix representation of a graph.

#### Mathematics B+S'

Biotechnological and chemical STEM sciences; Computer and communication sciences; Mechatronics

<span style="color: yellowgreen">06.04.01 Students perform operations with matrices: addition, scalar multiplication, matrix multiplication, raising to a power, and transposition.</span><br>
Multiplications of the Leslie matrix with a column vector are applied to determine the state in the next time step, and raising the Leslie matrix to a power is applied to determine the state further in time.

<span style="color: yellowgreen">06.04.02 Students use matrix models to describe evolutions.</span><br>
The Leslie matrix is used to describe the evolution of the number of eggs, larvae, and beetles over time. The link is made with the matrix representation of a graph.

#### Mathematics B+S''

Economics-Mathematics; Greek-Mathematics; Latin-Mathematics; Technological sciences and Engineering; Sciences-Mathematics

<span style="color: yellowgreen">06.08.01 Students perform operations with matrices: addition, scalar multiplication, matrix multiplication, raising to a power, and transposition.</span><br>
Multiplications of the Leslie matrix with a column vector are applied to determine the state in the next time step, and raising the Leslie matrix to a power is applied to determine the state further in time.

<span style="color: yellowgreen">06.08.02 Students use matrix models to describe evolutions.</span><br>
The Leslie matrix is used to describe the evolution of the number of eggs, larvae, and beetles over time. The link is made with the matrix representation of a graph.

### WD_07 Computer Science

#### Computer Science

Economics-Mathematics; Greek-Mathematics; Latin-Mathematics; Sciences-Mathematics

#### Computer Science S''

Business-supporting computer science

#### Computer and communication sciences B+S

Computer and communication sciences

#### Technological sciences and Engineering B+S

Technological sciences and Engineering

#### Business Sciences S (GO!)

Business Sciences (GO!)

<span style="color: yellowgreen">SMD 07.01.01 Students program self-designed solutions to concrete problems.</span><br>
A structured programming language is used, namely Python. A bounded loop is addressed. The notebook uses variables, data types, data structures, operators, functions, and software libraries. The necessary comments are provided so that students understand what the different code fragments do.

#### Biotechnological and chemical STEM sciences B+S

Biotechnological and chemical STEM sciences

#### Mechatronics B+S

Mechatronics

<span style="color: yellowgreen">SMD 07.02.01 Students program self-designed solutions to concrete problems.</span><br>
A structured programming language is used, namely Python. A bounded loop is addressed. The notebook uses variables, data types, data structures, operators, functions, and software libraries. The necessary comments are provided so that students understand what the different code fragments do.