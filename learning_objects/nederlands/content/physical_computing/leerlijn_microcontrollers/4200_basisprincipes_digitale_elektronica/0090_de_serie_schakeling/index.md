---
hruid: leerlijn_invoer_basisprincipes_serie
version: 1
language: nl
title: "Serieschakeling"
description: "Je leert wat een serieschakeling is en wat het effect is op de stroom, spanning en weerstand."
keywords: ["digitale elektronica", "serie", "basisprincipes", "microcontroller", "µC", "arduino", "dwenguino"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Serieschakeling

In een serieschakeling verbinden we de uitvoer van de ene component met de invoer van een andere. Op die manier krijgen we een ketting van aaneengeschakelde componenten. Hieronder zie je een voorbeeld van n weerstanden in serie.

<img src="img/serie.svg" alt="Voorbeeld van een serieschakeling" title="Voorbeeld van een serieschakeling"></img>

**Het effect van de serieschakeling op de stroom:**

In een serieschakeling is de stroom overal hetzelfde.

\\[I_T = I_1 = I_2 = … = I_n\\]

**Het effect van de serieschakeling op de spanning:**

De spanning in een serieschakeling zal zich verdelen over de componenten. Hoeveel de spanning zakt over een component staat in verhouding met de weerstand van die component.

\\[U_T = U_1 + U_2 + … + U_n\\]

**Het effect van de serieschakeling op de weerstand:**

De totale weerstand van een reeks in serie geschakelde weerstanden is de som van die weerstanden.

\\[R_T = R_1 + R_2 + … + R_n\\]
