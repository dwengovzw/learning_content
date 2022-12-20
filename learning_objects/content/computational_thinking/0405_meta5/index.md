---
hruid: m_ct_cases5d
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
Zet de gewenste acties om tot een programma in de simulator.<br>
De leerling heeft bv. gekozen: <br>
  Als iemand dichter dan 30cm komt, dan zwaait de robot met beide handjes en moet hij knipogen. <br>
  Anders zwaait hij niet en zijn zijn ogen wijd open. <br>
  Als iemand in de handen klapt, dan verschijnt de boodschap ‘Hallo! Hoe gaat het?’
</context>
<decomposition>
**Decompositie**:<br>
<ul><li>opsplitsen per actie </li></ul>
<ul><li>per actie de invoerelementen bepalen</li></ul>
<ul><li>per actie de uitvoerelementen bepalen</li></ul>
</decomposition>
<patternRecognition>
**Patroonherkenning**:<br>
<ul><li>keuzestructuur is voor de verschillende ‘als, dan’ acties gelijklopend</li></ul>
<ul><li> oogje open sturen, is gelijklopend met oogje dichtknijpen</li></ul>
</patternRecognition>
<abstraction>
**Abstractie:**<br>
<ul><li>Handjes zwaaien= servomotoren aansturen</li></ul>
<ul><li>Oogjes = ledmatrices</li></ul>
<ul><li>….</li></ul>
<ul><li>In de handen klappen = geluid waarnemen (let op alle geluid waarnemen!)</li></ul>
<ul><li>Simulatie is abstractie van wat de robot in de werkelijkheid zal doen</li></ul>
</abstraction>
<algorithms>
**Algoritme:**<br>
ALS iemand dichter dan 30 cm komt<br>
DAN robot zwaait met beide handjes en knipoogt <br>
ANDERS zwaait hij niet en ogen wijd open <br>
ALS iemand in de handen klapt<br>
DAN verschijnt de boodschap ‘Hallo! Hoe gaat het?’<br>
</algorithms>
<implementation>
Plaats hier een screenshot van de Blockly-code.
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
code
</p></div>
</implementation>
