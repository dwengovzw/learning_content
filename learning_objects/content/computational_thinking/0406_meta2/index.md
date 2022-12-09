---
hruid: m_ct_cases6b
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
Decompositie in subtaken:
1. Roep de hulp in van een computer → gebruik een routeplanner, bv. Google maps.
2. Times Square en Empire State Building aanduiden.
3. Duid op de figuur aan wat gekend is.
4. Zoek de lengtes van de twee rechthoekszijden op in de gegeven route.
5. Pas de stelling van Pythagoras toe. 
![image](https://user-images.githubusercontent.com/48352335/206760776-a6f57eda-9706-4571-926d-5dcabc4bdd5e.png)
![image](https://user-images.githubusercontent.com/48352335/206760809-189326b9-00cc-43b9-be6b-924847648eb6.png)
![image](https://user-images.githubusercontent.com/48352335/206760823-a837820a-2010-4cb1-95c5-6818671f4867.png)
</decomposition>
<patternRecognition>
Het stratenplan vertoont een patroon: <br>
de straten vormen een rechthoekig rooster. <br>
De afstand in volgelvlucht kan dus bepaald worden als de schuine zijde van een rechthoekige driehoek.
Herkennen dat het probleem verwant is met een eerder opgelost probleem: oefening is er een van het type waarbij de schuine zijde berekend wordt als de twee rechthoekszijden gekend zijn.  
</patternRecognition>
<abstraction>
Het stratenplan van New York is een abstractie van de stad. 
Het gebouw en het plein worden geabstraheerd tot een puntje op de kaart.  
</abstraction>
<algorithms>
Algoritme: Bereken de vierkantswortel van de som van de kwadraten van de rechthoekszijden.
</algorithms>
<implementation>
Dit is een unplugged voorbeeld.
</implementation>

