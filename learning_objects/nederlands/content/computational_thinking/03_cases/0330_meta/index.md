---
hruid: m_ct03_30
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
Dit probleem kunnen we opsplitsen in deelproblemen (**decompositie**):
<ul>
    <li>Welke materialen?</li>
    <li>Welke software? <span style="color: yellowgreen">→ geparametriseerd CAD-ontwerp</span></li>
    <li>Welke parameters zijn nodig?</li>
    <li>Welke machine wordt er ingezet? <span style="color: yellowgreen">→ CNC-machine</span></li>
    <li>Welke afmetingen zijn geschikt?</li>
    <li>Welke kromming is geschikt?</li>
    <li>...</li>
</ul>
</decomposition>
<patternRecognition>
De vorm van een kleerhanger is onafhankelijk van de maat. (**patroonherkenning**)
</patternRecognition>
<abstraction>
De geparametriseerde CAD-tekening is een **abstractie** van de drie maten kleerhangers.<br>
Eigenlijk wordt een kleerhanger voorgesteld d.m.v. de waarden van de gekozen parameters. (**abstractie**)  
</abstraction>
<algorithms>
**algoritme** <br>
Om van de ene maat naar een andere maat over te gaan, dien je bepaalde parameters in de software aan te passen. De computer zorgt voor het nodige rekenwerk en het ontwerp wordt automatisch aangepast.
</algorithms>
<implementation>
Geen implementatie. Dit is (voorlopig) een unplugged voorbeeld.
</implementation>

