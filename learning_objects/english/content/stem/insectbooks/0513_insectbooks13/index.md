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
hruid: stem5_13
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
title: Differential equations
version: 3
---
# Ladybugs and aphid infestations: a dynamic world model with differential equations

We have already established that time is experienced as continuous in practice, for which discrete growth models do not suffice for long. Therefore we introduce the differential equation, whose solution is a function that describes the system over time. In this learning object we give a first introduction to differential equations, with the goal of describing a population of aphids and ladybugs.

## Population size as a differential equation

Specifically geared towards the aphid problem, the growth of the aphid population size is described as follows:

\[\dot{y} = ry \left(1 - \frac{y}{K}\right)\]

Here, \(r = a - 1\) denotes the growth rate and \(K\) the carrying capacity, and \(y\) denotes the population size. \(\dot{y}\) is the derivative of \(y\), which tells students something about the change in population size:

- when \(\dot{y} > 0\), the population size will increase;
- when \(\dot{y} < 0\), the population size will decrease;
- when \(\dot{y} = 0\), there will be no change and the population size remains constant.

It is important that students realize that \(\dot{y}\) describes the change (growth/decline) of the population size, and not the population size itself!

## Equilibrium values and dynamics

Equilibrium is reached when \(\dot{y} = 0\). To determine the equilibrium value, students must solve the following equation:

\[\dot{y} = 0 \iff ry \left(1 - \frac{y}{K}\right) = 0 \iff ry = 0 \lor 1 - \frac{y}{K} = 0 \iff y = 0 \lor y = K\]

In the first case there are no aphids; in the second case the carrying capacity \(K\) is reached.

To describe the evolution of the population size over time, students will use Euler’s method. The derivative of a function is approximated as follows:

\[f'(t) \approx \frac{f(t + \Delta t) - f(t)}{\Delta t}\]

In the case considered, \(y = f(t)\) denotes the population size, and \(\dot{y} = f'(t)\) the change of this quantity. In the interactive notebook this last formula will be used to make step-by-step new estimates for the function \(f\).

## Aphids and ladybugs

After a first practical example of the use of differential equations, an example of a system of differential equations is given. Two variables are considered: the population size of aphids and the population size of ladybugs. These populations interact with each other, because the ladybugs (the predators) eat aphids (the prey). The following general form is used to represent this:

$$\dot{\mathbf{y}} = f(\mathbf{y}, t)$$

It is important to emphasize to students that $\mathbf{y}$ and $\mathbf{\dot{y}}$ are written in bold because they are vectors. Here $\mathbf{y} = (y_1, y_2)$, with $y_1$ and $y_2$ the respective population sizes of the aphids and the ladybugs. Analogously, $\mathbf{\dot{y}} = (\dot{y_1}, \dot{y_2})$, with $\dot{y_1}$ and $\dot{y_2}$ the respective growth rates of both populations.

Two examples of systems are given in the notebook. For instance, we find the following system that describes the growth of the populations:

$$
\begin{cases}
    \dot{y_1} = (a - 1) y_1 \left(1 - \frac{y_1}{K}\right) - 0.0012 y_1 y_2 \\
    \dot{y_2} = -0.4 y_2 + 0.0005 y_1 y_2
\end{cases}
$$

This system is called a Lotka–Volterra equation, which is often used in ecology to describe a dynamic biological system in which both a prey (the aphid) and a predator (the ladybug) occur. The system consists of two equations, each with two terms:

- The change in the aphid population over time $\dot{y_1}$

    - $(a - 1) y_1 \left(1 - \frac{y_1}{K}\right)$ describes the logistic growth of the aphid population, determined by the current population size $y_1$, the growth factor $a$, and the carrying capacity $K$.
    - $-0.0012 y_1 y_2$ describes predation by the ladybugs on the aphids. This predation is proportional to both the number of aphids and the number of ladybugs: the more aphids there are, the more can be caught, and the more ladybugs there are, the more they can catch. Note that the model assumes these two effects are independent and can be multiplied.

- The change in the ladybug population over time $\dot{y_2}$

    - $-0.4 y_2$ describes the net mortality of ladybugs: each day, 40% of the ladybugs die from old age or external factors.
    - $+0.0005 y_1 y_2$ again describes predation by the ladybugs on the aphids. Here it provides a positive contribution: the aphids serve as food that the ladybugs use to grow and reproduce. Here too, the model assumes these two effects are independent and can be multiplied.

The above requires some explanation, which can be given in class. Afterwards, students can get to work with the provided code, which makes it possible to evaluate the impact of the different parameters by means of graphs.

In targeted assignments, students are asked, among other things, to determine when both systems are in equilibrium. This equilibrium is first determined mathematically, and then verified using Python code that makes it possible to generate a phase diagram of the Lotka–Volterra model. In this diagram, the population sizes of the predators and the prey are plotted, and a periodic behavior is observed.

## Python

This notebook, like the others, uses Python to perform calculations and generate graphs. As a teacher, it is important to know:

- what [syntax](https://www.w3schools.com/python/python_syntax.asp) Python uses;

- how [functions](https://www.w3schools.com/python/python_functions.asp) are defined;

- how [lists](https://www.w3schools.com/python/python_lists.asp) can be used;

- how [for-loops](https://www.w3schools.com/python/python_for_loops.asp) work;

- how the [NumPy library](https://www.w3resource.com/numpy/array-creation/arange.php) makes it possible to generate a list of numbers, and to execute functions that use the values in this list as input arguments;

- how the [Matplotlib library](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py) makes it possible to generate graphs.

To make it easier for the teacher to understand what is happening, the necessary comments were provided. All functions were also provided with a description containing the function’s behavior, the parameters used as input, and the parameters returned as output. When a teacher wants to consult this description, it suffices to call `help(<functie_naam>)`.

## Minimum objectives

### WD_06 Mathematics

#### General minimum objectives

All studied programs

<span style="color: yellowgreen">MD 06.03 Students interpret the derivative as the limit of a difference quotient and as the slope of the tangent line to the graph.</span><br>
Euler’s method is covered, which uses the difference quotient.

<span style="color: yellowgreen">MD 06.21 Students use ICT to perform computations and create graphical representations.</span><br>
The notebook computes the estimated derivative for different values \\(t\\), and allows graphs to be generated that illustrate, among other things, the impact of the variable \\(\Delta t\\). The resulting population sizes are plotted over time, and a phase diagram of the Lotka–Volterra model is generated.

#### Mathematics B+S''

Economics–Mathematics; Greek–Mathematics; Latin–Mathematics; Technological Sciences and Engineering; Sciences–Mathematics

<span style="color: yellowgreen">SMD 06.08.13 Students solve simple polynomial equations, rational equations, irrational equations, exponential equations, logarithmic equations, and trigonometric equations algebraically.</span><br>
Using a system of equations, it is determined when the population sizes of predators and prey are in equilibrium.

### WD_07 Computer Science

#### Computer Science

Economics–Mathematics; Greek–Mathematics; Latin–Mathematics; Sciences–Mathematics

#### Computer Science S''

Business-supporting Computer Science

#### Computer and Communication Sciences B+S

Computer and Communication Sciences

#### Technological Sciences and Engineering B+S

Technological Sciences and Engineering

#### Business Sciences S (GO!)

Business Sciences (GO!)

<span style="color: yellowgreen">SMD 07.01.01 Students program self-designed solutions to concrete problems.</span><br>
A structured programming language is used, namely Python. A bounded iteration is covered. The notebook uses variables, data types, data structures, operators, functions and software libraries. The necessary comments are provided so that students understand what the different code fragments do.

#### Biotechnological and Chemical STEM Sciences B+S

Biotechnological and Chemical STEM Sciences

#### Mechatronics B+S

Mechatronics

<span style="color: yellowgreen">SMD 07.02.01 Students program self-designed solutions for concrete problems.</span><br>
A structured programming language is used, namely Python. A bounded iteration is covered. The notebook uses variables, data types, data structures, operators, functions and software libraries. The necessary comments are provided so that students understand what the different code fragments do.