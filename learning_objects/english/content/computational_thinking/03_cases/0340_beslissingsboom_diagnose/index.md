---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Decision tree
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct03_40
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
- 12
- 13
- 14
teacher_exclusive: true
title: Decision tree for medical diagnosis (2,3)
version: 3
---
# Decision tree for medical diagnosis

*In the project 'AI in de Zorg', students and the teacher look for a way to help healthcare providers make a diagnosis or determine a treatment. They can rely on patient data provided in a CSV file. These data are labeled and include, for example, patient characteristics, symptoms, and a condition.*  

**Challenge: Represent labeled data from the healthcare sector in a way that is suitable for making decisions regarding a diagnosis or a treatment.**

**Target group**: 2nd stage - transfer finality; 3rd stage - dual finality

**Subject:**
* Mathematics
* STEM 

**Prior knowledge:**
* Students can order real numbers.
* Students know quadratic functions.
* Students have seen examples of decision trees.

A possible progression of the case study is as follows:<br><br>

*Phase 1: introduction to decision trees and their structure*<br>
<ol>
    <li>You provide examples of real-life decision trees, or students look them up themselves.
    <li>Pattern recognition: students recognize the structure from the various examples. It is a directed graph with arcs and nodes.
    <li>Students realize that you can generate a decision tree based on a dispersion parameter and yes-no questions.
    <li>Students fill in the diagram with the basic concepts.</li>
</ol>

*Phase 2: mathematics*<br>
<ol>
    <li>Students complete an assignment about the dispersion parameter.
    <li>Students choose the dispersion parameter based on several criteria. Which best reflects reality? Which is feasible given your prior knowledge?
    <li>Students derive a formula for the Gini index.
    <li>Exercises show that you can represent yes-no questions with logical expressions (inequalities).</li>
</ol>

*Phase 3: algorithm*<br>
<ol>
    <li>Students write down the algorithm (in words).
    <li>Students test the algorithm (manually or plugged in, both are possible) on a small dataset.</li>
</ol>

*Phase 4: Python*<br>
<ol>
    <li>Students implement the algorithm in Python on a real-life dataset. They use an existing Python module to write a program for this.
    <li>Students need to preprocess the dataset (clean the data and make it numerical if necessary).
    <li>Students further complete the diagram with the basic concepts.</li>
</ol>
 
![ct-schema](@learning-object/m_ct03_40/en/3)

For the elaboration of this project, see the project 'AI in de Zorg'.