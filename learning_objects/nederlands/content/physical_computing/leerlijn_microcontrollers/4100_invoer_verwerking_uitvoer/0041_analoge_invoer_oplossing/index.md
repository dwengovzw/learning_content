---
hruid: leerlijn_invoer_verwerking_uitvoer_analoge_invoer_oplossing
version: 1
language: nl
title: "Analoge invoer (oplossing)"
description: "Leer hoe je een analoge waarde leest van een pin van de µC."
keywords: ["invoer", "verwerking", "uitvoer", "microcontroller", "µC", "arduino", "dwenguino", "analogRead"]
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
teacher_exclusive: true
---

# Analoge invoer (oplossing)

We gebruiken in dit geval een `unsigned int` en geen `unsigned char` omdat de analoge waarde die we lezen tussen 0 en 1023 ligt. Het datatype `unsigned char` bestaat maar uit 8 bits. Bijgevolg kun je er maar waarden van 0 tot 255 mee voorstellen. Een `unsigned int` bestaat uit 16 bits. Je kan er dus getallen van 0 tot 65536 in opslaan. Dit is meer dan voldoende voor onze analoge waarde.
