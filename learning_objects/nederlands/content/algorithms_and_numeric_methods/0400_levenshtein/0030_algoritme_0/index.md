---
hruid: org_dewengo_levenshtein_algorithm
version: 1
language: nl
title: "Het algoritme (1)"
description: "Een algoritme om de Levenshteinafstand te bepalen."
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
estimated_time: 8
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Een algoritme (1)

Om de Levenshteinafstand altijd op een correcte manier te kunnen berekenen, moeten we een **stappenplan** opstellen. Zo'n **stappenplan** is een **algoritme**. Bij het opstellen van zo'n stappenplan moeten we er rekening mee houden dat we het stappenplan willen kunnen laten uitvoeren door een computer. Omdat we hier een manier bedenken op het probleem op te lossen met behulp van de computer doen we aan **computationeel denken**.

## Onze gegevens voorstellen

Om ons algoritme te kunnen uitvoeren met de computer, moeten we de gegevens op een manier voorstellen die de computer begrijpt. In dit geval doen we dat aan de hand van een tabel. Hieronder zie je een voorbeeld van hoe die tabel eruitziet als we de kortste afstand willen zoeken tussen het woord PLAAT en het woord KAST. (Ter verduidelijking verwijzen we soms naar een vakje in de tabel aan de hand van een coördinaat. Deze stelt x- en y-waarde voor van de positie van het vakje waarbij de positieve x-as naar rechts gaat en de positieve y-as naar beneden. Dit is een courante manier om een assenstelsel voor te stellen op de computer.)

<div class="dwengo_content table_container">
    <table>
        <tr>
            <td style="width:375px;min-width:250px"><img src="img/levenshtein_example_base_grid.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td style="min-width:250px">Zoals je kan zien op de afbeelding, staat het woord waarvan we vertrekken in de eerste kolom. Het woord waar we naartoe willen zetten we in de eerste rij. Het vakje linksboven (coördinaat (0, 0)) heeft geen betekenis. Merk op dat we telkens ook een <strong>leeg vakje</strong> voor het woord plaatsen (coördinaten (1, 0) en (0, 1)). Dit leeg vakje stelt het lege woord voor. In de overige vakjes vullen we in wat de afstand is tussen de prefix van het woord dat links staat naar de prefix van het woord dat rechts staat. Hieronder zie je daar twee voorbeelden van.</td>
        </tr>
        <tr>
            <td><img src="img/levenshtein_example_example_point1.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td>De waarde die we in het oranje vakje (3, 4) zullen schrijven, is de afstand tussen PLA en KA.</td>
        </tr>
        <tr>
            <td><img src="img/levenshtein_example_example_point2.svg" alt="Tabel om afstand tussen woord voor te stellen" title="tabel om afstand tussen woord voor te stellen"></td>
            <td>De waarde die we in het oranje vakje (4, 2) zullen schrijven is de afstand tussen P en KAS.</td>
        </tr>
    </table>
</div>


We hebben nu een **gegevensvoorstelling** (ofwel een **datastructuur**) waarin we de gegevens van het probleem zullen opslaan. Nu hebben we nog een **stappenplan** (ofwel een **algoritme**) nodig om deze **datastructuur** in te vullen.