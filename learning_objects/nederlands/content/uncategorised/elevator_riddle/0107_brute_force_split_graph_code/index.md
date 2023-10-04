---
hruid: org-dwengo-elevator-riddle-brute-force-4
version: 1
language: nl
title: "Stap 1: Code"
description: "Op basis van de pseudocode kunnen we gemakkelijk een algoritme in Python schrijven."
keywords: ["grafen", "algoritme", "computationeel denken", "clustering", "datastructuur", "brute force", "python"]
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
estimated_time: 8
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---
# Brute kracht

## Implementatie in python

Hieronder zie je de vertaling van de pseudocode naar Python.

```python
# Deze functie genereert alle mogelijke combinaties van k elementen uit een rij van n elementen
def genereer_alle_mogelijke_keuzes(k, n):

    # Als k == 0 dan mogen er geen elementen meer worden gekozen
    if k == 0:
        return [[2 for _ in range(n)]]

        # Als k == n dan moeten alle elementen worden gekozen
    if k == n:
        return [[1 for _ in range(n)]]

        # Als k > n dan is er geen mogelijke selectie, dit geval kan niet voorkomen in het algoritme
    if k > n:
        return []
    else:
        # Maak een lijst om alle mogelijke selecties in op te slaan
        selections = []
        # Ken het eerste verdiep in de rij toe aan lift 1.
        # Combineer dit met alle mogelijke manieren om k-1 elementen te kiezen uit n-1 elementen
        selections.extend(
            [[1] +
                selection for selection in genereer_alle_mogelijke_keuzes(k-1, n-1)]
        )
        # Ken het eerste verdiep in de rij toe aan lift 2.
        # Combineer dit met alle mogelijke manieren om k uit n-1 elementen te kiezen
        selections.extend(
            [[2] +
                selection for selection in genereer_alle_mogelijke_keuzes(k, n-1)]
        )
        return selections
```

Merk op dat de functie genereer_alle_mogelijke_keuzes zichzelf aanroept. Een dergelijk algoritme noemen informaticawetenschappers een recursief algoritme. Recursieve algoritmes zijn vaak nuttig bij problemen waar een bepaald patroon zich herhaalt.

Wanneer we ons algoritme uitvoeren met de waarden vier en acht, krijgen we alle mogelijke verdelingen van de knopen van de graaf in twee gelijke groepen. Hieronder zie je de uitvoer van de functie genereer_alle_mogelijke_keuzes(4, 8).

[[1, 1, 1, 1, 2, 2, 2, 2], [1, 1, 1, 2, 1, 2, 2, 2], [1, 1, 1, 2, 2, 1, 2, 2], [1, 1, 1, 2, 2, 2, 1, 2], [1, 1, 1, 2, 2, 2, 2, 1], [1, 1, 2, 1, 1, 2, 2, 2], [1, 1, 2, 1, 2, 1, 2, 2], [1, 1, 2, 1, 2, 2, 1, 2], [1, 1, 2, 1, 2, 2, 2, 1], [1, 1, 2, 2, 1, 1, 2, 2], [1, 1, 2, 2, 1, 2, 1, 2], [1, 1, 2, 2, 1, 2, 2, 1], [1, 1, 2, 2, 2, 1, 1, 2], [1, 1, 2, 2, 2, 1, 2, 1], [1, 1, 2, 2, 2, 2, 1, 1], [1, 2, 1, 1, 1, 2, 2, 2], [1, 2, 1, 1, 2, 1, 2, 2], [1, 2, 1, 1, 2, 2, 1, 2], [1, 2, 1, 1, 2, 2, 2, 1], [1, 2, 1, 2, 1, 1, 2, 2], [1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 2, 1], [1, 2, 1, 2, 2, 1, 1, 2], [1, 2, 1, 2, 2, 1, 2, 1], [1, 2, 1, 2, 2, 2, 1, 1], [1, 2, 2, 1, 1, 1, 2, 2], [1, 2, 2, 1, 1, 2, 1, 2], [1, 2, 2, 1, 1, 2, 2, 1], [1, 2, 2, 1, 2, 1, 1, 2], [1, 2, 2, 1, 2, 1, 2, 1], [1, 2, 2, 1, 2, 2, 1, 1], [1, 2, 2, 2, 1, 1, 1, 2], [1, 2, 2, 2, 1, 1, 2, 1], [1, 2, 2, 2, 1, 2, 1, 1], [1, 2, 2, 2, 2, 1, 1, 1], [2, 1, 1, 1, 1, 2, 2, 2], [2, 1, 1, 1, 2, 1, 2, 2], [2, 1, 1, 1, 2, 2, 1, 2], [2, 1, 1, 1, 2, 2, 2, 1], [2, 1, 1, 2, 1, 1, 2, 2], [2, 1, 1, 2, 1, 2, 1, 2], [2, 1, 1, 2, 1, 2, 2, 1], [2, 1, 1, 2, 2, 1, 1, 2], [2, 1, 1, 2, 2, 1, 2, 1], [2, 1, 1, 2, 2, 2, 1, 1], [2, 1, 2, 1, 1, 1, 2, 2], [2, 1, 2, 1, 1, 2, 1, 2], [2, 1, 2, 1, 1, 2, 2, 1], [2, 1, 2, 1, 2, 1, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1], [2, 1, 2, 1, 2, 2, 1, 1], [2, 1, 2, 2, 1, 1, 1, 2], [2, 1, 2, 2, 1, 1, 2, 1], [2, 1, 2, 2, 1, 2, 1, 1], [2, 1, 2, 2, 2, 1, 1, 1], [2, 2, 1, 1, 1, 1, 2, 2], [2, 2, 1, 1, 1, 2, 1, 2], [2, 2, 1, 1, 1, 2, 2, 1], [2, 2, 1, 1, 2, 1, 1, 2], [2, 2, 1, 1, 2, 1, 2, 1], [2, 2, 1, 1, 2, 2, 1, 1], [2, 2, 1, 2, 1, 1, 1, 2], [2, 2, 1, 2, 1, 1, 2, 1], [2, 2, 1, 2, 1, 2, 1, 1], [2, 2, 1, 2, 2, 1, 1, 1], [2, 2, 2, 1, 1, 1, 1, 2], [2, 2, 2, 1, 1, 1, 2, 1], [2, 2, 2, 1, 1, 2, 1, 1], [2, 2, 2, 1, 2, 1, 1, 1], [2, 2, 2, 2, 1, 1, 1, 1]]
