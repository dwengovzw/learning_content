---
hruid: g_sound
version: 3
language: nl
title: "Uitleg Geluidssensor"
description: "Uitleg Geluidssensor"
keywords: ["oefeningen", "geluidssensor"]
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
# DwenguinoBlockly
## Geluidssensor

### Type
- Invoer
- Digitale sensor

### Werking
Gebruik deze sensor om geluid te detecteren. Bij geluid geeft de sensor 1 terug indien er geluid is en 0 bij stilte. Idealiter wordt deze sensor gebruikt in een stille omgeving.

### Werking in de simulator
In de simulator is een knop voorzien om geluid te simuleren. De knop indrukken simuleert geluid.

***

### In het echt

![](embed/geluidssensor.png "geluidssensor")

### In de simulator

![](embed/sim_geluidssensor.png "geluidssensor simulator")

De nodige blokken voor het aansturen van de geluidssensor vind je terug oner de categorie ![](embed/cat_uitvoer.png "categorie uitvoer")