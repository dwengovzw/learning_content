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
Analyseer hoe het zeeniveau in Oostende in de toekomst zal evolueren. 
</context>
<decomposition>
Verkennen van het probleem. Wat heb ik nodig? Subtaken (**decompositie**):<br>
<ol>
    <li>Nodig: data uit het verleden </li>
    <li>Data verzamelen <span style="color: yellowgreen">→ website MIRA</span></li>
    <li>Data visualiseren <span style="color: yellowgreen">→ keuze software, bv. Python</span></li>
    <li>Trendlijnen bepalen</li>
</ol>
</decomposition>
<patternRecognition>
Welke trendlijn is geschikt? <br>
Kijk naar de vorm van het spreidingsdiagram. Ellipsvormig? Dat wijst op lineaire regressie. (**patroonherkenning**)
![image](https://user-images.githubusercontent.com/48352335/205666980-64e8bf29-3e3f-49a9-8274-8fade3ca85fb.png)
</patternRecognition>
<abstraction>
De trendlijn is een benadering (model) van het schommelende zeeniveau die de stijgende trend weerspiegelt, en toelaat voorspellingen te doen voor de evolutie van het zeeniveau in de toekomst. (**abstractie**)
</abstraction>
<algorithms>
Een **algoritme** om in Python de trendlijnen te visualiseren (a.d.h.v. Python-modules):
<ol>
    <li>Definieer gedaante van vergelijking rechte</li>
    <li>Definieer functie om coëfficiënten-trendlijn te bepalen passend bij gegeven datapunten</li>
    <li>Lees data in</li>
    <li>Bepaal a.d.h.v. data en bovenstaande definities de trendlijn</li>
    <li>Visualiseer data en trendlijn</li>
</ol>
</algorithms>
<implementation>
Voor de implementatie verwijzen we naar het leerpad ['Klimaat'](https://www.dwengo.org/learning-path.html?hruid=pn_klimaatverandering&language=nl&te=true&source_page=%2Fstem%2F&source_title=%20STEM#pn_inleiding_klimaat;nl;3) van het lesthema ['Python in STEM'](https://www.dwengo.org/stem/).
</implementation>

