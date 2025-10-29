---
hruid: m_ct03_10
version: 3
language: nl
title: "Bus en trein"
description: "Bus en trein"
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
Volgende week staat er een uitstap naar Brussel op het programma met de trein.<br>
Zoek uit waar en wanneer je moet vertrekken om op tijd in Brussel aan te komen.

</context>
<decomposition>
**Decompositie**<br>
<ul>
    <li>Wat is het dichtstbijzijnde station?
        <ul>
            <li>Zijn daar rechtstreekse treinen naar Brussel of zullen we moeten overstappen?</li>
            <li>Hoe geraken we in het station? Te voet, met de fiets, met de bus?</li>
        </ul>
    </li>
    <li>Waar moeten we zijn in Brussel? In welk station moeten we uitstappen?</li>
    <li>Op welke tijdstippen vertrekt er een trein richting Brussel? 
        <ul>
            <li>Waar vinden we de treinuren?</li>
            <li>Om hoe laat moeten we dan naar het station vertrekken?</li>
        </ul>
    </li>
    <li>Op welk perron moeten we opstappen?</li>
    <li>Zijn er vertragingen of is er een staking aangekondigd?</li>
    <li>...</li>
</ul>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
<ul>
    <li>Een reis met de bus of met de trein plannen gebeurt op een gelijksoortige manier. Voor beide kan eventueel een app worden gebruikt. Zowel de perrons als de bushaltes worden op een abstracte manier aangeduid, met een naam of een nummer.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
<ul>
    <li>Het perron wordt geabstraheerd tot een getal, het perronnummer.
    <li>De reis wordt geabstraheerd tot de te volgen route: een opeenvolging van plaatsen (huis, school, stations …).</li>
</ul>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
<ul>
    <li>De te volgen route: een lijst van de opeenvolgende tijdstippen en overeenkomstige plaatsen.
</ul>
</algorithms>
<implementation>
**Programma**
Bij dit voorbeeld wordt er niet geprogrammeerd. 
</implementation>

