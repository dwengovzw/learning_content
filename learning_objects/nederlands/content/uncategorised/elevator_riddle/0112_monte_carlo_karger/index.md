---
hruid: org-dwengo-elevator-riddle-monte-carlo-karger
version: 1
language: nl
title: "Algoritme van Karger"
description: "Het algoritme van Karger gebruikt de Monte Carlo methode om tot een oplosing te komen."
keywords: ["grafen", "algoritme", "computationeel denken", "clustering", "datastructuur", "monte carlo", "python", "karger"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---

# Algoritme van Karger

Voor het bepalen van de minimale knip van een graaf bestaat ook een Monte Carlo algoritme. Dit wordt het algoritme van Karger genoemd (naar de uitvinder David Karger). Hieronder leggen we stap voor stap uit hoe dit algoritme werkt.

Het algoritme van Karger zal de graaf die in stukken geknipt moet worden, reduceren tot een graaf met maar twee knopen. De kost om die graaf in twee te knippen is dan de som van alle bogen die die twee knopen verbinden. Deze som is wat het algoritme gokt dat de minimale kost is. Deze procedure wordt een aantal keer herhaald waarna de beste gok gekozen wordt als finaal resultaat. Hieronder zie je een voorbeeld van hoe de graaf gereduceerd kan worden.

|  |  |
| - | - |
| We starten met de volledige graaf. | ![Karger stap 1](embed/karger1.png "Stap 1") |
|  |  |
| We kiezen een willekeurige boog en de twee knopen die aan die boog grenzen. | ![Karger stap 2](embed/karger2.png "Stap 2.") |
|  |  |


