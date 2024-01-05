---
hruid: org_dewengo_levenshtein_algorithm_4
version: 1
language: nl
title: "Het algoritme (4)"
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

# Een algoritme (4)

Hieronder zie je nog een voorbeeld van hoe we een volgende vakje kunnen invullen.
<div class="dwengo_content table_container">
    <table>
        <tr>
            <td style="width:375px;min-width:250px"><img src="img/levenshtein_example_step9a.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td style="min-width:250px">Manier 1: De kost om van PL naar KA te gaan kennen we (= 2). Daar tellen we de kost bij op om A te verwijderen uit PLA (= 1). Voor dit geval dus 3 in totaal.</td>
        </tr>
        <tr>
            <td><img src="img/levenshtein_example_step9b.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td>Manier 2: De kost om van PLA naar K te gaan kennen we (= 3). Daar tellen we de kost bij om A toe te voegen (= 1). Voor dit geval dus 4 in totaal.</td>
        </tr>
        <tr>
            <td><img src="img/levenshtein_example_step9c.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td>Manier 3: De kost om van PL naar K te gaan kennen we (= 2). Daar tellen we de kost bij om A in A te veranderen (= 0). Voor dit geval dus 2 in totaal.</td>
        </tr>
    </table>
</div>

We willen de minimale kost bepalen dus nemen we nu het minimum van deze drie gevallen en vullen die waarde permanent in in onze tabel.

<div class="dwengo_content table_container">
    <table>
        <tr>
            <td><img src="img/levenshtein_example_step10a.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td><img src="img/levenshtein_example_step10b.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td><img src="img/levenshtein_example_step10c.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
        </tr>
    </table>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Probeer de rest van de tabel aan te vullen aan de hand van de regels uit het algoritme.
    </div>
</div>


