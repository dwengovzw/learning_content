---
hruid: org-dwengo-elevator-riddle-monte-carlo-karger-python-5
version: 1
language: nl
title: "Karger in Python (kans op juiste gok)"
description: "Het algoritme van Karger gebruikt de Monte Carlo methode om tot een oplosing te komen."
keywords: ["grafen", "algoritme", "computationeel denken", "clustering", "datastructuur", "monte carlo", "python", "karger"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
difficulty: 5
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---
# Monte Carlo

## Algoritme van Karger: kans op juiste gok

Omdat we het antwoord kennen voor onze graaf, kunnen we de kans berekenen dat we een correct antwoord hebben na \\(n\\) keer gokken. 


```python

# Determine the probability of getting a correct answer using the minCutRepeat function for n = 8
def bepaalKansOpCorrectAntwoordVoorAantalGokken(n):
    aantal_correct = 0
    for i in range(1000):
        mincutcost, labels = herhaalGokDeKnipKost(bogen_matrix, n)
        if mincutcost == 12:
            aantal_correct += 1
    return aantal_correct/1000


probs = []
for tries in range(2, 20):
    probs.append(bepaalKansOpCorrectAntwoordVoorAantalGokken(tries))
 
print(probs)
 
plt.plot(range(2, 20), probs)
plt.show()

```

Op de grafiek hieronder zie je de kans op een correcte gok voor elke \\(n\\) van 2 tot 20.

![Kans op correcte gok voor onze graaf.](embed/prob_correct_for_n_tries.png "Kans op correcte gok voor onze graaf.")