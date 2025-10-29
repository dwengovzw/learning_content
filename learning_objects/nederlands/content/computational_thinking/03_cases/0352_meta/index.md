---
hruid: m_ct03_52
version: 3
language: nl
title: "Zeeniveau - trendlijn"
description: "Zeeniveau - trendlijn"
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
Analyseer hoe het zeeniveau in Oostende in de toekomst zal evolueren. 
</context>
<decomposition>
**Decompositie**<br>
<ul>
    <li>Data verzamelen. Welke? Hoe? Waar? (Data uit het verleden zoeken via internet.)</li>
    <li>Data visualiseren.</li>
    <li>Trendlijnen bepalen (vorm, vergelijking).</li>
    <li>Software kiezen (bijvoorbeeld Python).</li>
</ul>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
![image](https://user-images.githubusercontent.com/48352335/205666980-64e8bf29-3e3f-49a9-8274-8fade3ca85fb.png)<br>
<ul>
    <li>Trendlijn? Kijk naar de vorm van het spreidingsdiagram. Ellipsvormig? Dat wijst op lineaire regressie.</li>
    <li>Als een berekening of een groep instructies (subalgoritme) vaak moet worden herhaald, dan is het handig deze te vatten in een zelfgedefinieerde functie: hier voor de gewenste gedaante van de vergelijking van de trendlijn en het bepalden van de coëfficiënten in deze vergelijking.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
<ul>
    <li>De trendlijn is een benadering (model) van het schommelende zeeniveau, die de stijgende trend weerspiegelt en toelaat voorspellingen te doen over de evolutie van het zeeniveau in de toekomst. (Een model is een abstractie van het werkelijke fenomeen.)</li>
    <li>Een functie is een abstractie van een subalgoritme.</li>
</ul>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
Een algoritme om in Python de trendlijnen te visualiseren (a.d.h.v. Python-modules):
<ol>
    <li>Definieer gedaante van vergelijking rechte.</li>
    <li>Definieer functie om coëfficiënten in vergelijking trendlijn te bepalen passend bij gegeven datapunten.</li>
    <li>Lees data in.</li>
    <li>Bepaal de trendlijn aan de hand van de data en bovenstaande definities.</li>
    <li>Visualiseer data en trendlijn.</li>
</ol>
</algorithms>
<implementation>
**Programma**<br>
Voor de implementatie verwijzen we naar het leerpad ['Klimaat'](https://www.dwengo.org/learning-path.html?hruid=pn_klimaatverandering&language=nl&te=true&source_page=%2Fstem%2F&source_title=%20STEM#pn_inleiding_klimaat;nl;3) van het lesthema ['Python in STEM'](https://www.dwengo.org/stem/).
</implementation>

