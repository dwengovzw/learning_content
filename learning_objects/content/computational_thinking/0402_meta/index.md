---
hruid: m_cd_cases2
version: 3
language: nl
title: "Kleerhanger"
description: "Kleerhanger"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
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
Maak drie kleerhangers voor volwassenen, twee voor kinderen en vier voor baby’s.
</context>
<decomposition>
Dit probleem kunnen we bijvoorbeeld opsplitsen in subtaken (**decompositie**):
<ul><li>Welke materialen</li></ul>
<ul><li>Welke software? <span style="color: green">→ geparameteriseerd CAD-ontwerp</span></li></ul>
<ul><li>Welke machine? <span style="color: green">→ CNC-machine</span></li></ul>
<ul><li>Welke afmetingen zijn geschikt?</li></ul>
<ul><li>Welke kromming is geschikt?</li></ul>
<ul><li>...</li></ul>
</decomposition>
<patternRecognition>
Het ontwerp van een kleerhanger is onafhankelijk van de maat. (**patroonherkenning**)
</patternRecognition>
<abstraction>
CAD-tekening is **abstractie** van de drie soorten van kapstok. 
</abstraction>
<algorithms>
**algoritme** <br>
    Aanpassen van bepaalde parameters in de software.
</algorithms>
<implementation>
Geen implementatie. Dit is (voorlopig) een unplugged voorbeeld.
</implementation>

