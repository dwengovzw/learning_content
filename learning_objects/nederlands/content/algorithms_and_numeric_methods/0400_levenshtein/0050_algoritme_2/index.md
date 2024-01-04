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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Een algoritme (3)

Om de rest van de tabel in te vullen, maken we gebruik van de informatie die we al hebben. Zo moeten we onze redenering niet voor elk vakje helemaal opnieuw uitvoeren. We bestuderen hier eerst het geval om van P naar K te gaan. We kunnen dat op drie manieren doen:

1. We voegen K toe en laten P weg.
2. We laten P weg en voegen K toe.
3. We vervangen P door K.

<div class="dwengo_content table_container">
    <table>
        <tr>
            <td style="width:375px;min-width:250px"><img src="img/levenshtein_example_step3.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td style="min-width:250px">De afstand om van P naar K te gaan schrijven we in het oranje vakje (2, 2). Hieronder bekijken we de drie manieren om dat te doen.</td>
        </tr>
        <tr>
            <td><img src="img/levenshtein_example_step4a.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td>Manier 1: K toevoegen en P verwijderen. We kennen de kost al om K toe te voegen. Deze staat in het vakje boven het huidige vakje. Daar tellen we de kost bij op op P te verwijderen (= 1).</td>
        </tr>
        <tr>
            <td><img src="img/levenshtein_example_step4b.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td>Manier 1: De totale kost is in dit geval dus 2.</td>
        </tr>
        <tr>
            <td><img src="img/levenshtein_example_step5a.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td>Manier 2: P weglaten en K toevoegen. Daarvoor kijken we naar de kost om P weg te laten. Die staat in het vakje links van het huidige vakje. Deze kost is 1. Daar tellen we de kost bij om K toe te voegen (= 1)</td>
        </tr>
        <tr>
            <td><img src="img/levenshtein_example_step5b.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td>Manier 2: De totale kost is in dit geval ook 2.</td>
        </tr>
        <tr>
            <td><img src="img/levenshtein_example_step6a.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td>Manier 3: Hier kijken we naar de kost om van het lege woord naar het lege woord te gaan. Daarbij tellen we de kost om P te vervangen door K. In dit geval is die kost 1 omdat P en K verschillende letters zijn.</td>
        </tr>
        <tr>
            <td><img src="img/levenshtein_example_step6b.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td>Manier 3: De totale kost is hier dus 1</td>
        </tr>
    </table>
</div>

We willen de minimale kost bepalen dus nemen we nu het minimum van deze drie gevallen en vullen die waarde permanent in in onze tabel.
<div class="dwengo_content table_container">
    <table>
        <tr>
            <td><img src="img/levenshtein_example_step7a.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td><img src="img/levenshtein_example_step7b.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td><img src="img/levenshtein_example_step7c.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
        </tr>
    </table>
</div>


Op deze manier kunnen we de rest van de tabel invullen.