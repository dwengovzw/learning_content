---
hruid: org_dewengo_levenshtein_applications
version: 1
language: nl
title: "Toepassingen"
description: "Welke toepassingen heeft de levenshtein afstand?"
keywords: ["taaltechnologie", "taal", "afstand", "levenshtein", "algoritme", "toepassingen"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16]
difficulty: 1
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Toepassingen van de Levenshteinafstand

Het zoeken van de afstand tussen twee woorden is een basistechniek die in heel wat toepassingen gebruikt kan worden. Denk bijvoorbeeld aan de genetica. In dit vakgebied is het vaak nodig om gelijkenissen te zoeken in DNA sequenties. Een DNA sequentie wordt voorgesteld door een opeenvolging van base paren. Zo'n basenpaar bestaat uit nucleobasen. Er komen vier verschillende nucleobasen voor in een DNA sequentie: cytosine (C), guanine (G), adenine (A) en thymine (T). Op de computer stellen we een DNA sequentie dus gewoonlijk voor als een opeenvolging van de letters C, G, A en T. Bijvoorbeeld:

```python
# Hier verwijst de variable dna_sequentie naar een stukje van een DNA sequentie.
dna_sequentie = "CGGTCACGATCTGACTCTCGCTATTAGTTTCTTACATGCTTTAGTCTCAC"
```


Een andere veelgebruikte toepassing van de Levenshteinafstand is de spellingscontrole in een tekstverwerker. Deze zal voor elk woord dat je typt kijken of het voorkomt in een woordenlijst. Als het niet voorkomt in de lijst, dan zal het systeem op zoek gaan naar de woorden in de woordenlijst die dicht bij het woord liggen dat je geschreven hebt. Deze woorden zal het suggereren als correctie. Hiervoor wordt de Levenshteinafstand gebruikt.
