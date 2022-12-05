---
hruid: m_cd_cases4
version: 3
language: nl
title: "Zeeniveau"
description: "Zeeniveau"
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
1. Nodig: data uit het verleden
2. Data verzamelen
3. Data visualiseren
4. Trendlijnen bepalen
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
1. Definieer gedaante van vergelijking rechte
2. Definieer functie om coëfficiënten trendlijn te bepalen passend bij gegeven datapunten
3. Lees data in
4. Bepaal a.d.h.v. data en bovenstaande definities de trendlijn
5. Visualiseer data en trendlijn
</algorithms>
<implementation>
Voor de implementatie verwijzen we naar het leerpad 'Klimaat' van het lesthema 'Python in STEM'.
</implementation>

