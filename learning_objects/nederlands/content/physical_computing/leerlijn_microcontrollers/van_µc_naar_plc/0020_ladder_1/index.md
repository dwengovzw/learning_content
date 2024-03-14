---
hruid: leerlijn_microcontrollers_microcontroller_naar_plc_ladder
version: 1
language: nl
title: "Ladder logica"
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Ladder logica

Om fouten in de productielijn te vermijden is de methode waarmee je de PLC programmeert specifiek gericht op controletoepassingen. Daardoor is het programmeren  van een PLC een stuk eenvoudiger dan het programmeren van een µC. Je kan ladder logica zien als een extra abstractielaag bovenop de C++ code. Net zoals de grafische blokken in de Dwengo simulator een abstractie zijn van de tekstuele code. Hieronder zie je een voorbeeld van een ladder diagram. Deze zal een uitvoer (Q) activeren wanneer twee schakelaars (A en B) ingedrukt worden.

![Voorbeeld van een ladder diagram.](images/sample.png "Voorbeeld van een ladder diagram.")


Een ladder diagram heeft altijd dezelfde structuur. Links heb je een verticale lijn, deze stelt een draad met positieve spanning voor. Rechts heb je ook een verticale lijn, deze stelt een draad men neutrale spanning voor. Tussen de twee spanningslijnen heb je horizontale verbindingen (rungs in het engels). Deze geven een bepaalde logische schakeling weer.

