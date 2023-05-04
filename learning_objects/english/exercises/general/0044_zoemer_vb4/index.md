---
hruid: g_zoemer_vb4
version: 3
language: en
title: "Voorbeeld Zoemer 4"
description: "Voorbeeld Zoemer 4"
keywords: ["oefeningen", "zoemer"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
## Zoemer

OPGAVE 4

Schrijf een programma zodat je de dwenguino kunt gebruiken als een pentatonisch (5 tonen) instrument. Dit kan je doen door aan elk van de 5 knoppen (NOORD - OOST - ZUID - WEST - MIDDEN) een noot te binden. Een standaard pentatoniek is *Do (C), Re (D), Mi (E), Fa (F), Sol (G)*.

Oplossing:

![blockly](@learning-object/zoemer_m4/nl/3)  

<div class="alert alert-box alert-success">
Zoals je misschien merkt, is het niet zo eenvoudig om zoemertonen te binden aan de knoppen. De meest efficiënte manier om dit te doen wordt hierna uitgelegd.
</div>