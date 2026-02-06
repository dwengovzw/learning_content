---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Algorithms
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: aiz_algoritmes
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
title: Algorithms
version: 3
---
# Algorithms
## Divide-and-conquer algorithm

The algorithm you will use in Chapter 6 to construct a decision tree for a specific application is a divide-and-conquer algorithm. The idea of divide and conquer is that to solve a problem, you transform the problem into an identical problem that is smaller. Then you tackle that smaller problem in the same way by also transforming it into a (nearly) identical problem that is even smaller. If you keep doing this, the problem you actually have to solve becomes so small that the solution is obvious. 

> Over the centuries, people have devised effective algorithms that provide answers to specific problems, such as sorting and searching algorithms. These algorithms exhibit certain characteristics, e.g., divide and conquer and greedy.<br>Through pattern recognition, one can determine whether an existing algorithm is suitable for a new problem to be solved.

With a divide-and-conquer algorithm, you make a problem simpler at each step. 

*Example*<br> 
Suppose you want to look up a medical term in a dictionary, e.g., meningitis. In a dictionary, the words are arranged alphabetically. 

<ul><li>You open the dictionary in the middle.</li></ul> 
<ul><li>Are the words that start with an 'm' in the first or second half? Take the correct half.</li></ul> 
<ul><li>Split that half in two again.</li></ul> 
<ul><li>Are the words that start with an 'm' in the first or second half? Again, take the correct half.</li></ul> 
<ul><li>Repeat this method until you reach the words starting with an 'm'.</li></ul> 

There are also mathematical applications. Euclid’s algorithm is a divide-and-conquer algorithm to determine the greatest common divisor of two natural numbers.<br> 
And there are also practical applications. To pair matching socks after washing, you can first sort them by color before matching them (Stock, 2017).

## Greedy algorithm
The algorithm you will use in Chapter 6 to construct a decision tree has another special characteristic. It is a greedy algorithm. At each step in building the decision tree, it will choose the split that is as optimal as possible at that moment, but it does not take into account the steps that follow. The strategy used is one of ‘take what you can get now’ (Fack, 2007). The algorithm is effective, but not always the most efficient. 

> A greedy algorithm is also called an eager algorithm.