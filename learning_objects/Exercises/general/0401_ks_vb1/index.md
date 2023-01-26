---
hruid: g_ks_vb1
version: 3
language: nl
title: "Voorbeeld Keuzestructuur 1"
description: "Voorbeeld Keuzestructuur 1"
keywords: ["oefeningen", "keuzestructuur"]
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
teacher_exclusive: true
---
## Keuzestructuur: Als - Dan - Anders

OPGAVE 1.1

Schrijf een programma dat ervoor zorgt dat de tekst "auw" verschijnt op het lcd-scherm wanneer je de NOORD-knop indrukt.

![blockly](@learning-object/conditional_m1a/nl/3)

***

OPGAVE 1.2

Het is niet de bedoeling dat de tekst "auw" blijft staan wanneer je de knop loslaat. Vul het programma aan zodat de tekst op het lcd-scherm verdwijnt wanneer je de knop niet langer indrukt.

![blockly](@learning-object/conditional_m1b/nl/3)
