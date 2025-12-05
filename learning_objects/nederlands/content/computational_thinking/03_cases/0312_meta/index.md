---
hruid: m_ct03_12
version: 3
language: nl
title: "Jommeke"
description: "Jommeke"
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
Geef het AI-systeem om Jommekes in te kleuren een zelfgemaakte tekening met elementen die je bewust hebt toegevoegd om het systeem te misleiden.
</div>
</context>
<decomposition>
**Decompositie**<br>
<ul>
    <li>Hoe werkt het systeem?
        <ul>
            <li>Het systeem is getraind met afbeeldingen uit Jommekes en kleurt daarom alles in in de stijl van Jommeke.
            <li>Het systeem zal lijnencombinaties die het herkent, inkleuren op de manier die het heeft geleerd.
            <li>Het systeem zet aangeboden afbeeldingen eerst om naar zwart-witte lijntekeningen.</li>
        </ul>
    </li>
    <li>Welke vormen zijn er typisch voor Jommekes?
    <li>Welke van deze vormen kan je gebruiken voor andere objecten dan waarvoor ze in de strips worden gebruikt? (Bv. plant met de vorm van het haar van Jommeke, wolk in de vorm van een tekstballon.)
    <li>Omdat het systeem afbeeldingen omzet naar zwart-witte lijntekeningen, is het voldoende dat je een zwart-witte tekening aanbiedt.</li>
</ul>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
<ul>
    <li>Het systeem zal bepaalde combinaties van lijnen herkennen.
    <li>Het systeem zal ook in bepaalde mate generaliseren, bijvoorbeeld andere kapsels, andere tekstballonnen ...</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
<ul>
    <li>Wij zien de lijnencombinatie op het hoofd van Jommeke als 'haar'. De computer doet dat niet. Voor een computer is het alleen een combinatie van lijnen.
    <li>Het is mogelijk dat het systeem toch generaliseert naar verschillende kapsels, bijvoorbeeld doordat het de context meeneemt zoals waar die lijnen staan op een tafereel. We weten echter niet met welke elementen het systeem allemaal rekening houdt ('black box').</li>
</ul>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>

</algorithms>
<implementation>
**Programma**<br>
Neem een kijkje naar volgend <a href="https://www.dwengo.org/backend/api/learningObject/getWrapped?hruid=org-dwengo-jommeke-zelf-tekening-maken&version=1&language=nl">notebook</a> voor de uitvoering van deze case.
</implementation>