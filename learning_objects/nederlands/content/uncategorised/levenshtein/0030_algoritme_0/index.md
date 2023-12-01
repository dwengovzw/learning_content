---
hruid: org_dewengo_levenshtein_algorithm
version: 1
language: nl
title: "Het algoritme (1)"
description: "Een algoritme om de Levenshtein afstand te bepalen."
keywords: ["taaltechnologie", "taal", "afstand", "levenshtein", "algoritme"]
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
estimated_time: 2
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Een algoritme (1)

Om de Levenshtein afstand altijd op een correcte manier te kunnen berekenen, moeten we een **stappenplan** opstellen. Zo'n **stappenplan** noemen we een **algoritme**. Bij het opstellen van zo'n stappenplan moeten we er rekening mee houden dat we het stappenplan willen kunnen laten uitvoeren door een computer. Omdat we hier een manier bedenken op het probleem op te lossen met de computer doen we aan **computationeel denken**.

## Onze gegevens voorstellen

Om ons algoritme uit te kunnen voeren met de computer, moeten we onze gegevens op een manier voorstellen die de computer begrijpt. In dit geval doen we dat aan de hand van een tabel. Hieronder zie je een voorbeeld van hoe die tabel eruitziet als we de afstand willen zoeken tussen het woord PLAAT en het woord KAST.

<img src="./img/levenshtein_example_base_grid.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen">
