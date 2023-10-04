---
hruid: org-dwengo-elevator-riddle-monte-carlo-karger-python-1
version: 1
language: nl
title: "Karger in Python (decompositie)"
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---
# Monte Carlo

## Algoritme van Karger: implementatie in Python

Om ons algoritme in Python te implementeren, denken we eerst nog eens goed na over hoe we het probleem in deelproblemen kunnen opsplitsen (decompositie). Wij hebben hiervoor voor de volgende opdeling gekozen:
- Het gokken van een knip.
    - Kiezen van twee willekeurige knopen.
    - Samenvoegen van deze knopen in de graaf tot één knoop met de labels van de twee samengevoegde knopen.
    - De bogen die vertrekken uit de twee knopen samenvoegen.
- Meerdere keren een knip gokken en de kleinste onthouden.



