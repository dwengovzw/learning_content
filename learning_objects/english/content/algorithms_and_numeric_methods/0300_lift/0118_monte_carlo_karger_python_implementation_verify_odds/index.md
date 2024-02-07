---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: The Karger's algorithm uses the Monte Carlo method to arrive at a solution.
difficulty: 5
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: org-dwengo-elevator-riddle-monte-carlo-karger-python-5
keywords:
- grafen
- algoritme
- computationeel denken
- clustering
- datastructuur
- monte carlo
- python
- karger
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
title: Karger in Python (chance of correct guess)
version: 1
---
# Monte Carlo

## Karger's Algorithm: Probability of Correct Guess

Since we know the answer for our graph, we can calculate the probability of having a correct answer after \\(n\\) guesses.


```python

# Determine the probability of getting a correct answer using the minCutRepeat function for n = 8
def determineProbabilityOfCorrectAnswerForNumberOfGuesses(n):
    correct_count = 0
    for i in range(1000):
        mincutcost, labels = repeatGuessMinCutCost(edges_matrix, n)
        if mincutcost == 12:
            correct_count += 1
    return correct_count / 1000


probs = []
for tries in range(2, 20):
    probs.append(determineProbabilityOfCorrectAnswerForNumberOfGuesses(tries))
 
print(probs)
 
plt.plot(range(2, 20), probs)
plt.show()

```

The graph below shows the probability of a correct guess for each \\(n\\) from 2 to 20.

![Probability of correct guess for our graph.](embed/prob_correct_for_n_tries.png "Probability of correct guess for our graph.")