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
hruid: stem5_8
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
title: The Leslie matrix
version: 3
---
# Modeling the life cycle of a beetle with the Leslie matrix

In the previous modules, we focused on the number of box tree moth caterpillars over time, treating a caterpillar as an unchanging entity. In this chapter, we will also take into account the life stage an insect may be in. To do this, we will consider the beetle, which goes through three different life stages:

- the beetle comes into the world in the form of an egg;
- a larva hatches from the egg;
- the larva pupates into a beetle.

![Beetle](embed/kever.jpg "https://commons.wikimedia.org/wiki/File:Chrysomelidae_-_Chrysolina_americana.JPG")<br>
Source: [https://commons.wikimedia.org/wiki/File:Chrysomelidae_-_Chrysolina_americana.JPG](https://commons.wikimedia.org/wiki/File:Chrysomelidae_-_Chrysolina_americana.JPG)

For a biologist, it's interesting to know how many eggs, larvae, and beetles there are at different points in time. In this chapter, you will learn that these population sizes can be modeled using the **Leslie matrix**.

## Transitions between life stages

In beetles, the transition from one life stage to another is not straightforward. Empirically, it has been observed that as many as 95% of the eggs are eaten or never hatch. If there are initially 1000 eggs, only about 50 remain after a month! The chance that the larva then becomes a beetle is much higher: as many as 75% of the larvae pupate into a beetle. Once emerged, the beetle lays about 100 eggs in a month.

This sequence of life stages leads to a cycle. This cycle can be cast into a graph that describes the transition between states at a given point in time:

![Graph](embed/graph.png "https://www.wisfaq.nl/pagina.asp?nummer=1883")

Based on the values of the nodes in the graph, the next state can be computed. To simplify this process, you will use matrices.

## The Leslie matrix

To perform matrix multiplication, set the state at time \(0\) equal to a vector \(v_0\) that contains the number of eggs, larvae, and beetles. For example, consider:

\[v_0 = \begin{bmatrix} 1000 \\ 100 \\ 60 \end{bmatrix}\]

To determine the state \(v_{1}\) at time \(1\), use the **Leslie matrix** \(L\) that describes the population growth. In the above example, it looks as follows:

\[L = \begin{bmatrix} 0 & 0 & 100 \\ 0.05 & 0 & 0 \\ 0 & 0.75 & 0 \end{bmatrix}\]

Starting from the state \(v_0\), \(v_{1}\) can be computed as follows:

\[v_{1} = L v_0 = \begin{bmatrix} 0 & 0 & 100 \\ 0.05 & 0 & 0 \\ 0 & 0.75 & 0 \end{bmatrix} \begin{bmatrix} 1000 \\ 100 \\ 60 \end{bmatrix} = \begin{bmatrix} 6000 \\ 50 \\ 75 \end{bmatrix}\]

Going one step further, we find:

\[v_{2} = L v_{1} = \begin{bmatrix} 0 & 0 & 100 \\ 0.05 & 0 & 0 \\ 0 & 0.75 & 0 \end{bmatrix} \begin{bmatrix} 6000 \\ 50 \\ 75 \end{bmatrix} = \begin{bmatrix} 7500 \\ 300 \\ 37.5 \end{bmatrix}\]

Note that this last expression can also be written as follows:

\[v_{2} = L v_{1} = L L v_{0} = L^2 v_{0}\]

To compute the number of eggs, larvae, and beetles at time step \(t\), it suffices to compute the \(t^\text{th}\) power of the matrix \(L\) and multiply it by \(v_0\):

\[v_{t} = L^t v_{0}\]

## Interactive notebook

Now you will work with an interactive online notebook in which you will use Python to perform matrix calculations and visualize the population growth.

[![](embed/knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=6030_en "Leslie matrix")