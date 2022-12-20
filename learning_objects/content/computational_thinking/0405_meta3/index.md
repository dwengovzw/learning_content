---
hruid: m_ct_cases5c
version: 3
language: nl
title: "Sociale robot"
description: "Sociale robot"
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
Ontwerp en realiseer een sociale robot.
</context>
<decomposition>
Leerlingen kunnen de opdracht opsplitsen in de verschillende fasen/stappen die ze moeten doorlopen in het creëer-realiseer-evalueer proces (**decompositie**):
<ul><li>(Planning opmaken)</li></ul>
<ul><li>Bepalen van het ontwerpidee</li></ul>
<ul><li>Vastleggen criteria/gewenste acties)</li></ul>
<ul><li>Acties programmeren in de simulator</li></ul>
<ul><li>Acties testen a.h.v. de hardware </li></ul>
<ul><li>‘Lichaam robot’ ontwerpen (tekening)</li></ul>
<ul><li>‘Lichaam en acties robot’ aanapssen aan de criteria en beperkingen (bv. aanwezige hardware)</li></ul>
<ul><li>Tekening overbrengen op de gekozen drager</li></ul>
<ul><li>Onderdelen monteren</li></ul>
<ul><li>Geheel testen en evalueren</li></ul>
<ul><li>(Optimaliseren)</li></ul>
![schetsontwerp](https://user-images.githubusercontent.com/48352335/208729461-0752ca6f-5302-4abd-bfdc-30e94a763e7b.png)
</decomposition>
<patternRecognition>
Acties die meermaals terugkeren, en complexer acties, kunnen vervat worden in een zelfgedefinieerde functie. (**patroonherkenning**)
</patternRecognition>
<abstraction>
Een actie die uit meerdere deelacties bestaat, kan **geabstraheerd** worden in een (overkoepelende) actie.
</abstraction>
<algorithms>
Uit de decompositie volgt het stappenplan dat meegeeft hoe tewerk te gaan. (**algoritme**)
</algorithms>
<implementation>
Tekst
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
tekst
</p></div>
</implementation>
