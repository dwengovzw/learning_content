---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Processing in the project
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: aiz_etstemzorg
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
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: true
title: Processing in the project
version: 3
---
# STEM
# STEM attainment targets and the '*AI in Healthcare*' project 

*Attainment targets - STEM concepts* 

In hospitals, patients are increasingly monitored automatically, resulting in large quantities of digital data. Electronic patient records contain a wealth of data. From this big data, a lot of information can be extracted (information).<br>
Much available data on COVID-19 makes it possible to monitor the pandemic and simulate the effects of possible measures (cause and effect - systems and models).<br>
Learning systems look for patterns in data and, based on that, e.g., construct a decision tree to make a diagnosis based on certain data of the patient concerned. Radiologists can rely on AI systems to, e.g., detect subtle effects of medication on tumors; these systems also work with pattern recognition (patterns - systems).<br>
Societal needs can accelerate developments in the field of technology (stability and change).<br>
Automated EWS systems can profoundly influence day-to-day operations in the hospital and lead to adjustments (changes) in their operation.<br>
The rule-based system used to automatically generate decision trees is based on the data provided. Insufficient or poor-quality data lead to a decision tree that is not effective. Decision trees that are too large are not usable in practice; such decision trees will be pruned; too much pruning can reduce accuracy. Students realize that the AI system they use to automatically generate decision trees has a major advantage, namely the transparency with which a developed model arrives at its predictions. Students also realize, on the other hand, that the AI system used has limitations: it is, e.g., not suitable when many parameters have to be taken into account; a learning system is better suited for that, but the disadvantage is that transparency is lost (ratio and quantity). 

Because students know the advantages and limitations of certain AI systems, they can argue why in a particular case it is, e.g., better to choose a decision tree rather than a learning system. 

Students work with a dataset to gain insight into a medical problem: which parameters are important for (the evolution of) that medical problem? A decision tree offers a solution to that problem. Once that decision tree has been established, students have at their disposal a system that allows them to enter the values of the parameters for a new patient and, e.g., predict which diagnosis those parameters translate into or how a medical situation will evolve.<br>
To arrive at a decision tree, students will first have to become familiar with the concepts that will be applied concretely. The need for these concepts will emerge when tackling subproblems: the structure of such a decision tree with nodes and edges, the successive questions asked at the nodes, the minimal spread of the parameters across the different categories that constitute the outcome of the tree, the Gini index, and how to ensure that all this can be implemented in a computer program.<br>
They will learn concepts from computer science, such as a divide-and-conquer algorithm and abstraction, and be confronted with the fact that computers work with numbers, which means they will have to work with data types. They will work with mathematical concepts, such as graphs, sets, parabolas, relationships between quantities, the 'p' and 'q' from probability theory, and possibly logical expressions.<br>
The algorithm that the students design and first apply manually is then implemented on the computer. To that end, they write a program in Python that automates the entire process. They use the built-in functions of existing Python modules for this, allowing them to see that collaboration between computer science and mathematics can lead to great applications for the healthcare sector. The students arrive at a program they wrote themselves by adapting existing programs and combining them.<br>
It is important to discuss with the students that the input of healthcare providers and patients is also required, so that one arrives at usable and ethically acceptable applications. Being usable and ethically acceptable are, in addition to effectiveness, criteria that should certainly be taken into account in the design. The students can test a generated decision tree with previously unseen data and assess the size of the tree for usability. 

Students recognize that a decision tree can be used in a medical context to provide better care, e.g., obtaining a diagnosis more quickly or having no doubt about the remedy to follow. Students recognize that there is an interplay between the growing presence of AI systems on the one hand, and society—including economic interests and how ethical aspects are handled—on the other.