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
Automatiseer het tellen van huidmondjes op microscopische foto’s (KIKS).
</context>
<decomposition>
Subtaken (**decompositie**):<br>
1. Hoe kijkt een computer naar foto’s?
2. Hoe geef ik de foto’s aan de computer?
3. Classificatie (Staat er een huidmondje op de foto of niet?)
4. Hoe ziet de trainingsset eruit?
5. Hoe bekom ik een dataset?
6. Bias in de dataset.
7. Hoe goed moet het AI-systeem presteren?
</decomposition>
<patternRecognition>
Objectherkenning wordt al veel gedaan a.d.h.v. een AI-sytemen. Veelgebruikt zijn de diepe convolutionele neurale netwerken. (**patroonherkenning**)<br>
Het AI-systeem zal kenmerken van huidmondjes moeten herkennen.<br>
Bias in de dataset (**patroon**): <br>
1. Alle huidmondjes hebben een afmeting van ongeveer 125x125 pixels
2. De foto’s zijn grijsachtig van kleur
</patternRecognition>
<abstraction>
Een kleurenfoto wordt aan de computer gegeven in de vorm van een driedimensionaal rooster van getallen. Een digitale foto bestaat uit pixels waarbij de kleur van elke pixel wordt weergegeven door de RGB-code, niets anders dan drie getallen. (**abstractie**)
</abstraction>
<algorithms>
Er zijn meerdere **algoritmes** nodig. <br>
Voor de dataset:
<ol>
    <li>Een algoritme om de microfoto's van de plantentuin op te delen in voorbeelden van huidmondjes en voorbeelden van niet-huidmondjes.</li>
    <li>Een algoritme om het neurale netwerk te trainen.</li>
</ol>
Om het neurale netwerk te kunnen gebruiken:
<ol>
    <li>Een algoritme om de aangeboden foto op te delen in vierkantjes van 125 op 125 pixels. Deze vierkantjes worden aangeboden aan het convolutioneel neurale netwerk om te zien of er een huidmondje op staat.</li>
    <li>Een algoritme om de huidmondjes die hetzelfde zijn, te clusteren.   </li> 
    <li>Een algoritme om de huidmondjes te tellen. </li>
</ol>
</algorithms>
<implementation>
Voor de programma’s, zie het KIKS-project (https://dwengo.org/kiks).
</implementation>

