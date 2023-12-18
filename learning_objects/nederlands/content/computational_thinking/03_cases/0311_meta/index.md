---
hruid: m_ct03_11
version: 3
language: nl
title: "Zwangerschapstest"
description: "Zwangerschapstest"
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
Een zwangerschapstest kan je gemakkelijk zelf thuis uitvoeren. Je vindt deze in niet-digitale en digitale vorm. De digitale versie bevat een microcontroller en een display. Ontrafel de werking van een digitale zwangerschapstest. Vergelijk dit met een niet-digitale zwangerschapstest.  
</context>
<decomposition>
<strong>Decompositie:</strong><br>
<ol>
    <li>Wat is de invoer en wat is de uitvoer bij het uitvoeren van de test.</li>
    <li>Wat is de rol van de computer hierin?</li>
    <li>Hoe verschilt dit van een niet-digitale zwangerschapstest?</li>
</ol>
</decomposition>
<patternRecognition>
Het gebruik van een niet-digitale en een digitale zwangerschapstest verloopt op quasi dezelfde manier. (<strong>patroonherkenning</strong>)<br> 
<ul>
    <li>Bij beide is de invoer een urinestaal.</li>
    <li>Bij beide is de uitvoer een boodschap.</li>
    <li>Bij beide reageert het urinestaal al dan niet op een bepaalde stof die aanwezig is in het meettoestel.</li>
</ul>
</patternRecognition>
<abstraction>
Het al dan niet zwanger zijn, wordt bij een zwangerschapstest weergegeven door een <strong>symbool</strong>: één of twee streepjes, een plus- of een minteken, … (<strong>abstractie</strong>)
</abstraction>
<algorithms>
<strong>Algoritme bij de digitale test:</strong><br>  
ALS de urine reageert met de stof <br>
&nbsp;&nbsp;&nbsp;&nbsp;DAN toon boodschap + op het scherm <br>
ANDERS toon boodschap - op het scherm<br>
ALS de test niet goed uitgevoerd is<br>
&nbsp;&nbsp;&nbsp;&nbsp;DAN geef een foutboodschap op het scherm

<strong>Algoritme bij de niet-digitale test:</strong><br>
ALS de urine reageert met de stof <br>
&nbsp;&nbsp;&nbsp;&nbsp;DAN verschijnen er twee streepjes<br>
ANDERS is er slechts één streepje (het controlestreepje)

Het uitvoeren van de test zelf verloopt ook volgens een stappenplan (zowel bij de digitale als bij de niet-digitale test). 
</algorithms>
<implementation>
Dit is een activiteit waarbij niet geprogrammeerd moet worden.
</implementation>

