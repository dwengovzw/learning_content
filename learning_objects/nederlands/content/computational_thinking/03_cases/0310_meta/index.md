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
Zoek uit wanneer en waar je moet vertrekken om tijdig in Brussel aan te komen.

</context>
<decomposition>
Het probleem bestaat uit deelproblemen (<strong>decompositie</strong>):<br> 
<ul>
    <li>Wat is het dichtstbijzijnde station?
        <ul>
            <li>Zijn daar rechtstreekse treinen naar Brussel of zullen we moeten overstappen?</li>
            <li>Hoe geraken we in dat station? Te voet, met de fiets, met de bus?</li>
        </ul>
    </li>
    <li>Waar moeten we zijn in Brussel? In welk station moeten we uitstappen?</li>
    <li>Op welk uur rijdt er een trein naar daar? 
        <ul>
            <li>Waar kunnen we de uren van de trein raadplegen? Bv. via de app van de NMBS.</li>
            <li>Om hoe laat moeten we dan naar het station vertrekken?</li>
        </ul>
    </li>
    <li>Op welk perron moeten we opstappen?</li>
    <li>...</li>
</ul>
</decomposition>
<patternRecognition>
Een reis met de bus of met de trein plannen gebeurt op een gelijksoortige manier. (<strong>patroonherkenning</strong>) <br>Voor beide kan eventueel een app gebruikt worden. Zowel de perrons als de bushaltes worden op een abstracte manier omschreven, door een naam of een perronnummer.  
</patternRecognition>
<abstraction>
Het perron wordt <strong>geabstraheerd</strong> tot een getal, het perronnummer of anders gezegd het spoor.
De reis wordt geabstraheerd tot de te volgen route: een opeenvolging van plaatsen (huis, school, stations …) 
</abstraction>
<algorithms>
De te volgen route is herleid tot een stappenplan: een lijst van de opeenvolgende uren en overeenkomstige plaatsen. (<strong>algoritme</strong>)
</algorithms>
<implementation>
Bij dit voorbeeld moet er niet geprogrammeerd worden. 
</implementation>

