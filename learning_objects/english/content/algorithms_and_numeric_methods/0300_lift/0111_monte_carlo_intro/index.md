---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Using statistical methods, we can quickly find the correct solution with
  a high probability.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 2
hruid: org-dwengo-elevator-riddle-monte-carlo
keywords:
- grafen
- algoritme
- computationeel denken
- clustering
- datastructuur
- monte carlo
- python
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
title: Statistical methods
version: 1
---
# Monte Carlo

Our first solution to the problem utilized a brute force algorithm. These kinds of algorithms try out all possible combinations and then select the best one. Despite the fact that computers these days can perform a large number of calculations very quickly, for many problems it remains impossible to solve them using brute force. This is also the case with the graph cut problem. For such issues, computer scientists often look for alternative algorithms. These alternative algorithms sacrifice the certainty of obtaining an exact solution in exchange for a faster algorithm. These algorithms are called **heuristics**.

A type of **heuristic** that can be applied to various problems is **Monte Carlo algorithms**. The name for this sort of algorithms is inspired by the eponymous district in the city-state of Monaco. In that district lies the famous Monte Carlo Casino where many people enjoy gambling their money away. Monte Carlo algorithms got their name because they, just like the gambler in a casino, wager what a correct solution might be. The likelihood that the algorithm will guess correctly is small, but by making multiple guesses in succession and remembering the best solution, these algorithms can still yield good results.