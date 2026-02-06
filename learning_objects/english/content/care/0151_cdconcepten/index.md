---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: AI in Healthcare
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: aiz_ctconcepten
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
title: AI in Healthcare
version: 3
---
# Project 'AI in Healthcare' 
## Computational thinking

In the ‘AI in Healthcare’ project, you will address that bigger picture. You will represent data in a suitable way to help a healthcare provider make a diagnosis or determine a treatment. So you are looking for a solution to a problem that helps a human.

The creative process in which you think about how to deploy the computer for problems like these is the essence of computational thinking.<br> 
Sometimes you may want a computer to perform a certain task, but there is no suitable system yet. Computational thinking then includes, among other things: being aware of the limitations of the computer system at your disposal, knowing the capabilities of the software and hardware to be used, thinking about why existing systems are inadequate, and designing new systems.<br> 
In Chapter 3, you saw, for example, that there are different kinds of graphs. An adequate representation of a problem requires that the graph visualizes aspects relevant to the problem. If you cannot achieve that with one of the known types of graphs, then you look for a type of graph that is suitable, or it may be necessary to devise a new type of graph.<br> 
In Chapter 4, you were presented with examples of how a specific type of graph, the decision tree, is used in healthcare. The binary decision tree is an abstract representation of the strategy to follow in solving the problem in question. To solve the problem, you must traverse the decision tree from root to leaf; the decision tree visualizes the algorithm to follow: start at the root, answer the successive yes–no questions until you arrive at the leaf that gives you the decision.<br> 
In Chapter 7, you will work with Python to automatically generate a decision tree starting from labeled data. First, you do this using a guided example. Afterwards, you will work with other datasets. It is important to recognize the patterns in the guided example so that you can adapt the known solution to the example’s problem efficiently and quickly arrive at the solution to the new problem. 

## Central problem of 'AI in Healthcare' 

"Represent labeled data from the healthcare sector in a way that is suitable for making decisions regarding a diagnosis or a treatment." 

Simple decision trees can be created manually, but if there are many factors to consider, that takes a lot of time. It is then useful to use a computer. Chapter 6 looks specifically at how the computer can be used for this. Chapter 8 shows how, by implementing the method found in the computer, you automatically generate a decision tree to arrive at a solution to the central problem. 

> To obtain a decision tree that is useful for a healthcare provider, you will need to use sufficient data on which to base the decision tree. That will therefore have to be done with a computer. 

Below it is explained how the four basic concepts of computational thinking came into play. 

You start with pattern recognition and abstraction: 

<ul><li>In the examples of Chapter 4, you see that the data are generally represented with a directed, rooted graph, usually binary.</li></ul> 
<ul><li>How the data are represented shows a pattern. The data are abstracted in the same way each time, namely by using a (binary) decision tree.<br>The construction of such a binary decision tree also exhibits certain patterns.</li></ul> 
<ul><li>From the examples in Chapter 4, you infer that a decision tree starts from a root and a yes–no question that produces a separation of the data into two sets that show as little dispersion across the categories as possible. Using an iterative process, the nodes and the next yes–no questions are determined. The leaves of the decision tree give the possible decisions.</li></ul> 

Decomposition of this problem (and decomposition of the subproblems): 

<ul><li>In the examples of Chapter 4, look for a pattern in how the data are represented there.</li></ul> 
<ul><li>From which elements is a decision tree built?<br>- A decision tree is a model for the desired solution. It is an <strong>abstract</strong> representation; its form is a graph.<br>- From which elements is such a graph composed?</li></ul> 
<ul><li>How does such a decision tree work?<br>- A decision tree starts from a root and a yes–no question that produces a separation of the data into two sets that show as little dispersion across the categories as possible. Using an iterative process, the nodes and the next yes–no questions are determined. The leaves of the decision tree give the possible decisions.</li></ul> 
<ul><li>To have a computer construct a binary decision tree, a computer program is needed. You will therefore have to work with concepts the computer understands, such as numbers and logical expressions. The computer program is written based on an algorithm.</li></ul> 
<ul><li>Which computations lead to the correct split?<br>- At each split, you aim for as little dispersion across the categories as possible. To make the computer recognize the degree of dispersion, you will represent the degree of dispersion with a number. The Gini index is used as a measure of dispersion. How do you represent that with a number?</li></ul> 

> The Gini index is used as a measure for dispersion. 

<ul><li>With which <strong>algorithm</strong> can a binary decision tree be constructed?<br>- The algorithm will have to determine the root for a binary decision tree, choose the correct nodes, and establish the appropriate yes–no questions.<br>- This happens via an iterative process. The same pattern repeats at each split.<br>- How does a computer make yes–no questions? This will be done by means of mathematical expressions that are checked to see whether they are true or not true.</li></ul> 

> These mathematical expressions will be built using the comparison operators > and <. 

<ul><li>The implementation of the algorithm in the computer.</li></ul> 
<ul><li>In what format are the data supplied to the computer?<br>- Do the data meet this format?<br>- If not, how can you preprocess the data?</li></ul> 

> You will use a CSV file; CSV stands for 'comma separated values'. 

You notice that the basic concepts are intertwined.<br>
Figure 5.1 summarizes how the four basic concepts of computational thinking set you on your way to tackling the central problem of constructing decision trees. 

> The box ‘algorithm’ has not yet been filled in because the algorithm still has to be developed in Chapter 6. Figure 6.31 provides the completed diagram. 

![](embed/4kotjesDTalgor.png "Fig 5.1")
<figure>
    <figcaption align = "center"><b>Basic concepts of computational thinking applied to the problem of constructing a binary decision tree.</b></figcaption>
</figure>