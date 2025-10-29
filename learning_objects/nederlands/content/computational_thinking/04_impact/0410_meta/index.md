---
hruid: m_ct04_10
version: 3
language: nl
title: "Zwangerschapstest"
description: "Zwangerschapsteste"
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
Een zwangerschapstest kan je gemakkelijk zelf thuis uitvoeren. Je vindt deze in niet-digitale en digitale vorm. De digitale versie bevat een microcontroller en een display. Ontrafel de werking van een digitale zwangerschapstest. Vergelijk dit met een niet-digitale zwangerschapstest.  
</context>
<decomposition>
**Decompositie**<br>
<ol>
    <li>Wat is de invoer en wat is de uitvoer bij het uitvoeren van de test.</li>
    <li>Wat is de rol van de computer hierin?</li>
    <li>Hoe verschilt dit van een niet-digitale zwangerschapstest?</li>
</ol>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
Het gebruik van een niet-digitale en een digitale zwangerschapstest verloopt op quasi dezelfde manier.
<ul>
    <li>Bij beide is de invoer een urinestaal.</li>
    <li>Bij beide is de uitvoer een boodschap.</li>
    <li>Bij beide reageert het urinestaal al dan niet op een bepaalde stof die aanwezig is in het meettoestel.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
Het al dan niet zwanger zijn, wordt bij een zwangerschapstest weergegeven door een <strong>symbool</strong>: één of twee streepjes, een plus- of een minteken, …
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
Algoritme bij de digitale test:<br>  
ALS de urine reageert met de stof DAN<br>
&nbsp;&nbsp;&nbsp;&nbsp;toon boodschap + op het scherm <br>
ANDERS<br>
&nbsp;&nbsp;&nbsp;&nbsp;toon boodschap - op het scherm<br>
EINDE ALS<br>
ALS de test niet goed uitgevoerd is DAN<br>
&nbsp;&nbsp;&nbsp;&nbsp;geef een foutboodschap op het scherm<br>
EINDE ALS<br>

<strong>Algoritme bij de niet-digitale test:</strong><br>
ALS de urine reageert met de stof DAN <br>
&nbsp;&nbsp;&nbsp;&nbsp;verschijnen er twee streepjes<br>
ANDERS<br> 
&nbsp;&nbsp;&nbsp;&nbsp;is er slechts één streepje (het controlestreepje)<br>
EINDE ALS

Het uitvoeren van de test zelf verloopt ook volgens een stappenplan (zowel bij de digitale als bij de niet-digitale test). 
</algorithms>

