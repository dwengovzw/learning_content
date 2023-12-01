---
hruid: org_dewengo_levenshtein_algorithm_3
version: 1
language: nl
title: "Het algoritme (3)"
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

# Een algoritme (3)

Om de rest van de tabel in te vullen, maken we gebruik van de informatie die we al hebben. Zo moeten we onze redenering niet voor elk vakje helemaal opnieuw uitvoeren. We bestuderen hier eerst het geval om van P naar K te gaan. We kunnen dat op drie manieren doen:

1. We laten P weg en voegen K toe.
2. We voegen K toe en laten P weg.
3. We vervangen P door K.

<table>
    <tr>
        <td style="min-width:450px"><img src="img/levenshtein_example_step3.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
        <td>Om van het lege woord naar het lege woord te gaan moeten we niets doen. De kost is hier dus 0.</td>
    </tr>
    <tr>
        <td><img src="img/levenshtein_example_step4a.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
        <td>Om van het lege woord naar KAST te gaan moeten we telkens een letter toevoegen. De kost om een letter toe te voegen is 1.</td>
    </tr>
    <tr>
        <td><img src="img/levenshtein_example_step4b.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
        <td>Om van het woord PL naar het lege woord te gaan moeten we PL weglaten. De kost is hier dus 2.</td>
    </tr>
    <tr>
        <td><img src="img/levenshtein_example_step2.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
        <td>Met die redenering kunnen we dus de tweede rij en de tweede kolom van de tabel invullen.</td>
    </tr>
</table>


We hebben nu een **gegevensvoorstelling** (ofwel een **datastructuur**) waarin we de gegevens van ons probleem zullen opslaan. Nu hebben we nog een **stappenplan** (ofwel een **algoritme**) nodig om deze **datastructuur** in te vullen.