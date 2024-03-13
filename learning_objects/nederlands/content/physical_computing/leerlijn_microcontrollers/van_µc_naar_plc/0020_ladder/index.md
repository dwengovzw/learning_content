---
hruid: leerlijn_microcontrollers_microcontroller_naar_plc_ladder
version: 1
language: nl
title: "Ladder logica (1)"
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

# Ladder logica (1)

Om fouten in de productielijn te vermijden is de methode waarmee je de PLC programmeert specifiek gericht op controletoepassingen. Daardoor is het programmeren  van een PLC een stuk eenvoudiger dan het programmeren van een µC. Je kan ladder logica zien als een extra abstractielaag bovenop de C++ code. Net zoals de grafische blokken in de Dwengo simulator een abstractie zijn van de tekstuele code. Hieronder zie je een voorbeeld van een ladder diagram. Deze zal een uitvoer activeren wanneer twee schakelaars ingedrukt worden.

<img src="./images/sample.svg" alt="Voorbeeld van een ladder diagram" title="Voorbeeld van een ladder diagram">

