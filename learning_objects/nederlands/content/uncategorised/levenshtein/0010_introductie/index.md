---
hruid: org_dewengo_levenshtein_intro
version: 1
language: nl
title: "De Levenshtein afstand"
description: "Wat is de Levenshtein afstand?"
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

# De Levenshtein afstand

De **Levenshtein afstand** is een metriek om de afstand tussen twee woorden of zinnen te bepalen. Om de afstand tussen twee woorden te bepalen, tel je het aantal letters dat je moet toevoegen, verwijderen of vervangen om het ene woord om te vormen in het andere. Hieronder zie je voorbeelden van deze operaties.

<table>
    <tr>
        <th>Woord 1</th>
        <th>Woord 2</th>
        <th>Operatie</th>
        <th>Afstand</th>
    </tr>
    <tr>
        <td>STAL</td>
        <td>STAAL</td>
        <td>A toevoegen</td>
        <td>1</td>
    </tr>
    <tr>
        <td>TREK</td>
        <td>TROK</td>
        <td>E vervangen door O</td>
        <td>1</td>
    </tr>
    <tr>
        <td>VIEREN</td>
        <td>VIER</td>
        <td>E en N weglaten</td>
        <td>2</td>
    </tr>
    <tr>
        <td>STAM</td>
        <td>STAM</td>
        <td>Geen</td>
        <td>0</td>
    </tr>
</table>

Voor korte en eenvoudige woorden kan je dit makkelijk met de hand doen. Voor langere woorden of zinnen is het voor een mens al een heel stuk moeilijker om te zien welke operaties je moet uitvoeren om het ene woord om te zetten in het andere.
