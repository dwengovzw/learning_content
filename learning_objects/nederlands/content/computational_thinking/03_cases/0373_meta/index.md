---
hruid: m_ct03_73
version: 3
language: nl
title: "Huidmondjes"
description: "Huidmondjes"
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
**Probleemstelling**<br>
Automatiseer het tellen van huidmondjes op microscopische foto’s (project 'KIKS').
</context>
<decomposition>
**Decompositie**<br>
<ul>
    <li>Hoe 'kijkt' een computer naar foto’s?</li>
    <li>Hoe geef ik de foto’s aan de computer?</li>
    <li>Hoe zien de microscopische foto's in de dataset eruit?</li>
    <li>Welk AI-systeem is geschikt voor classificatie (staat er een huidmondje op de foto of niet)?</li>
    <li>Hoe moet de trainingsset eruitzien?</li>
    <li>Hoe krijg ik een geschikte dataset?</li>
    <li>Welke bias zit er in de dataset?</li>
    <li>Hoe goed moet het AI-systeem presteren?</li>
    <li>Hoe kunnen de gedetecteerde huidmondjes worden geteld?</li>
</ul>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
<ul>
    <li>Objectherkenning wordt vaak gedaan met diepe convolutionele neurale netwerken, die hiervoor worden getraind met gelabelde voorbeelden.</li>
    <li>Het gaat hier om een probleem van binaire classificatie: huidmondje of geen huidmondje. Het AI-systeem moet kenmerken van huidmondjes herkennen. Er worden gelabelde foto's van een deel van een bladoppervlak met huidmondje of zonder huidmondje aan het systeem gegeven.</li>
    <li>Bias in de dataset (patroon):
        <ul>
            <li>alle huidmondjes hebben een afmeting van ongeveer 125 x 125 pixels;</li>
            <li>de foto's hebben een grijsgroene kleur.</li>
        </ul>
    </li>
    <li>Om de dataset op te stellen en om de getedecteerde huidmondjes te clusteren, wordt eenzelfde techniek gebruikt: *sliding window*.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
<ul>
    <li>Een kleurenfoto is voor de computer een driedimensionaal rooster van getallen. Een digitale foto bestaat uit pixels, waarbij de kleur van elke pixel wordt weergegeven door drie getallen (de RGB-code). Dus om huidmondjes te herkennen, moet de computer bepaalde patronen herkennen in tabellen van getallen.</li>
</ul>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
Er zijn meerdere algoritmen nodig.<br>
Voor de training:
<ul>
    <li>een algoritme om de microscopische foto's op te delen in vierkantjes met huidmondjes erop en zonder huidmondjes erop;</li>
    <li>een algoritme om het neurale netwerk te trainen.</li>
</ul>
Voor het tellen van huidmondjes:
<ul>
    <li>een algoritme om de aangeboden foto op te delen in vierkantjes van 125 x 125 pixels (deze vierkantjes worden aangeboden aan het neurale netwerk);</li>
    <li>een algoritme om meermaals gedetecteerde huidmondjes te clusteren;</li> 
    <li>een algoritme om de huidmondjes te tellen. </li>
</ul>
</algorithms>
<implementation>
**Programma**<br>
Voor de programma’s, zie het <a href="https://dwengo.org/kiks">KIKS-project</a>.
</implementation>

