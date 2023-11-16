---
hruid: leerlijn_invoer_verwerking_uitvoer_bibliotheek
version: 1
language: nl
title: "Met een bibliotheek"
description: "Een component aansturen aan de hand van een bibliotheek."
keywords: ["invoer", "verwerking", "uitvoer", "microcontroller", "µC", "arduino", "dwenguino", "bibliotheek", "library"]
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
estimated_time: 20
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Gebruik maken van een bibliotheek

Vaak hebben sensoren en actuatoren hun eigen complexe elektronica die al een deel van de verwerking doen (bv. sonar sensor of servo motor). Elk van deze componenten heeft een eigen “taal” waarmee het met de microcontroller spreekt. Om in de correcte “taal” te kunnen spreken met de component, gebruik je op de microcontroller meestal een bibliotheek. Deze bibliotheek zal dan signalen genereren die de component begrijpt.

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        <p>
        Eerder in dit leerpad schreef je een programma om led 13 aan en uit te zetten op basis van de gedetecteerde afstand. Bekijk die code opnieuw. Deze maakt gebruik van een bibliotheek om waarden van de sonar-sensor te lezen. Op welke lijnen in die code wordt er verwezen naar die bibliotheek?
        </p>
    </div>
</div>