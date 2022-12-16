---
hruid: m_ct_cases6
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
**Decompositie** in subtaken:
1. Roep de hulp in van een computer → gebruik een routeplanner, bv. Google maps.
2. Times Square en Empire State Building aanduiden.
 ![image](https://user-images.githubusercontent.com/48352335/206757334-ebdad093-2ee7-493c-9d53-2c14c598115c.png)
</decomposition>
<patternRecognition>

</patternRecognition>
<abstraction>
Het stratenplan van New York is een **abstractie** van de stad. 
Het gebouw en het plein worden geabstraheerd tot een puntje op de kaart.  
</abstraction>
<algorithms>

</algorithms>
<implementation>
Oplossing laten bepalen door de computer door gebruik te maken van de functionaliteit van Google maps: 'measure distance'.
![image](https://user-images.githubusercontent.com/48352335/206757540-f5205128-03b3-46e4-adac-09efecb53a39.png)
</implementation>

