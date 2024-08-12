---
hruid: leerlijn_invoer_basisprincipes_parallel
version: 1
language: nl
title: "Parallelschakeling"
description: "Je leert wat een parallelschakeling is en wat het effect is op de stroom, spanning en weerstand."
keywords: ["digitale elektronica", "parallel", "basisprincipes", "microcontroller", "µC", "arduino", "dwenguino"]
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

# Parallelschakeling

In een parallelschakeling verbinden we de invoer van een reeks componenten met elkaar en verbinden we ook de uitvoer van de componenten met elkaar. Hieronder zie je een voorbeeld van n weerstanden in parallel.

<img src="img/parallel.svg" alt="Voorbeeld van een parallelschakeling" title="Voorbeeld van een parallelschakeling"></img>

**Het effect van de parallelschakeling op de stroom:**

De stroom zal zich in een parallelschakeling verdelen over de componenten. Hoeveel stroom er door elke component gaat is omgekeerd evenredig aan de weerstand van die component.

\\[I_T = I_1 + I_2 + … + I_n\\]

**Het effect van de parallelschakeling op de spanning:**

In een parallelschakeling is de spanning over elke component gelijk.

\\[U_T = U_1 = U_2 = … = U_n\\]

**Het effect van de parallelschakeling op de weerstand:**

In een parallelschakeling is de totale weerstand gelijk aan het inverse van de som van de inversen van de individuele weerstanden.

\\[R_T = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2} + … + \frac{1}{R_n}}\\]
