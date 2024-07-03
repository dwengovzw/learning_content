---
hruid: leerlijn_microcontrollers_microcontroller_naar_plc_ladder_5
version: 1
language: nl
title: "Ladder logica: latch"
description: "Wat is Ladder logica?"
keywords: ["microcontroller", "plc", "automatisatie", "programmable logic controller", "µC", "ladder"]
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
estimated_time: 15
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Ladder: latch 

Een latch is een circuit dat twee stabiele uitvoertoestanden heeft. Deze uitvoertoestand stuurt dan bijvoorbeeld een machine aan. Het volgende ladder diagram toont de logica van een latch circuit.

| Ladder diagram van het latch circuit |
|:---:|
| ![Voorbeeld van een ladder diagram van het latch circuit.](images/latch.svg "Voorbeeld van een ladder diagram van het latch circuit.") | 


Merk op dat de uitvoer van de lijn hier ook gebruikt wordt als een invoerelement van de lijn. Dit maakt het mogelijk om de uitvoer vast te houden op een bepaalde waarde. 

Deze logica kan je gebruiken om een apparaat aan of uit te zetten. Wil je bijvoorbeeld een lamp laten branden door op de ene knop te drukken en die af zetten door op een andere knop te drukken, dan kan je dit circuit gebruiken. Schakel daarvoor twee knoppen aan aan de PLC. Deze knoppen laten alletwee geen stroom door wanneer ze niet ingedrukt zijn (normaal open). Ze geven op dat moment dus de logisch waarde 0 terug. Door deze knoppen te verbinden met de invoerpinnen \\(A\\) en \\(B\\) van de PLC, kan je ervoor zorgen dat de lamp gaat branden wanneer je de knop op invoer \\(B\\) indrukt en uitgaat wanneer je de knop op invoer \\(A\\) indrukt. Bekijk onderstaand ladder diagram. Probeer de verschillende toestanden van de knoppen uit. Wanneer gaat de lamp aan en wanneer gaat die uit.

| Ladder diagram van het latch circuit voor het aansturen van een lamp |
|:---:|
| ![Voorbeeld van een ladder diagram van het latch circuit.](images/latch_lamp.svg "Voorbeeld van een ladder diagram van het latch circuit.") | 

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Schrijf een microcontrollerprogramma dat de logica van het latch circuit implementeerd.
        <img src="images/latch_lamp.svg">
    </div>
</div>