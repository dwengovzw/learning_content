---
hruid: m_ct03_70a
version: 3
language: nl
title: "Routeplanner"
description: "Routeplanner"
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
New York. Wat is de afstand in vogelvlucht van Times Square naar het Empire State Building, uitgedrukt in mijl? 
</div>
</context>
<decomposition>
**Decompositie**
<ul>
    <li>Roep de hulp in van een computer <span style="color: yellowgreen">→ gebruik een routeplanner, bv. Google Maps.</span>
    <li>Times Square en Empire State Building aanduiden.</li>

![image](https://user-images.githubusercontent.com/48352335/206757334-ebdad093-2ee7-493c-9d53-2c14c598115c.png)
</ul>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
In de routeplanner worden straten, pleinen, parken ... op een bepaalde manier voorgesteld. Herkennen wat straten, parken ... zijn, is een vorm van patroonherkenning.
</patternRecognition>
<abstraction>
**Abstractie**<br>
Het stratenplan van New York is een abstractie van de stad. 
Het gebouw en het plein zijn geabstraheerd tot een puntje op de kaart.  
</abstraction>
<algorithms>

</algorithms>
<implementation>
**Programma**<br>
Oplossing laten bepalen door de computer door gebruik te maken van de functionaliteit van Google Maps: 'measure distance'.<br>
![image](https://user-images.githubusercontent.com/48352335/206757540-f5205128-03b3-46e4-adac-09efecb53a39.png)
</implementation>

