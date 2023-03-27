---
hruid: g_matrix
version: 3
language: nl
title: "Uitleg Led-matrix"
description: "Uitleg Led-matrix"
keywords: ["oefeningen", "led-matrix"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# dwenguinoBlockly
## Led-matrix

### Type
- Uitvoer
- Actuator

### Werking
De led-matrix is een vierkante 8x8 matrix met 64 leds in een vaste kleur (rood). De matrix is ideaal om bepaalde patronen te laten oplichten, zoals een oog of een mond van de robot of een ander symbool. Je kan de matrices ook met elkaar verbinden (maximaal 4) als je meerdere matrices tegelijk wil gebruiken. Je kan programmeren welke leds er tegelijk moeten oplichten.

***

### In het echt

![](embed/ledmatrix.png "led-matrix")

### In de simulator

![](embed/led_matrix.png "led-matrix simulator")

De blokken die je nodig hebt voor het programmeren van de led-matrices vind je terug onder de categorie ![](embed/cat_uitvoer.png "categorie uitvoer").

<div class="alert alert-box alert-success">
Voor meer informatie over de led-matrix kan je terecht in de leerlingenfiches van de <em>Sociale Robot</em>
</div>