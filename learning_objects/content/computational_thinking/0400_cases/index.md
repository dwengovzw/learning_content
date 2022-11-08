---
hruid: ct_cases-v1
version: 1
language: nl
title: "CT schema test"
description: "CT schema test"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Dwengo
licence: cc by
content_type: text/ct-schema
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

<context>
![Face](ct_face.png)
<div style="position:absolute;right:0px;width:40%;height:100px;margin-top:-100px;margin-right:20px">Kan een computer dier- en plantensoorten herkennen?</div>
</context>
<decomposition>
Dit probleem kunnen we bijvoorbeeld opsplitsen in twee belangrijke subtaken (**decompositie**):
1. Representatie
2. Classificatie
</decomposition>
<patternRecognition>
Het herkennen van objecten komt voor in tal van contexten. Vaak worden dus gelijkaardige oplossingen toegepast (denk bijvoorbeeld aan de populariteit van AI (diepe neurale netwerken) voor beeldherkenning). (**patroonherkenning**)
</patternRecognition>
<abstraction>
![Een afbeelding bestaat uit pixels. Deze pixels komen overeen met een keurenwaarde voor de rood, groen en blauwcomponenten. Deze waarden zijn gewoon getallen.](appels_en_peren.png)
Hoe stellen we planten en dieren voor aan de computer? (**abstractie**)
</abstraction>
<algorithms>
Op basis van die getallen kunnen we een **algoritme** opstellen waarmee een computer appels en peren kan onderscheiden.
![Grafiek die classificatie illustreert door op de x-as de hoogte van het stuk fruit te plotten en op de y-as de omtrek. Zo kan je een lijn tekenen die de appels en peren van elkaar scheidt.](appels_en_peren_grafiek.png)
</algorithms>
<implementation>
Implementatie is hier niet van toepassing, dit is een unplugged voorbeeld.
</implementation>






