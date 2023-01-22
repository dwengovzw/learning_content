---
hruid: m_ct_cases9
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
Volgende week staat er een uitstap naar Brussel op het programma met de trein. De leerlingen moeten uitzoeken wanneer en waar ze moeten vertrekken om tijdig in Brussel aan te komen.

</context>
<decomposition>
Het probleem bestaat uit deelproblemen (*decompositie**):<br>    
- Wat is het dichtstbijzijnde station?
    - Zijn daar rechtstreekse treinen naar Brussel of zullen we moeten overstappen?
    - Hoe geraken we in dat station? Te voet, met de fiets, met de bus?
- Waar moeten we zijn in Brussel? In welk station moeten we uitstappen?
- Op welk uur rijdt er een trein naar daar? 
    - Waar kunnen we de uren van de trein raadplegen? Bv. via de app van de NMBS. 
    - Om hoe laat moeten we dan naar het station vertrekken?
- Op welk perron moeten we opstappen?
- ...

</decomposition>
<patternRecognition>
Een reis met de bus of met de trein plannen gebeurt op een gelijksoortige manier. (**patroonherkenning**) <br>Voor beide kan eventueel een app gebruikt worden. Zowel de perrons als de bushaltes worden op een abstracte manier omschreven, door een naam of een perronnummer.  
</patternRecognition>
<abstraction>
Het perron wordt **geabstraheerd** tot een getal, het perronnummer of anders gezegd het spoor.
De reis wordt geabstraheerd tot de te volgen route: een opeenvolging van plaatsen (huis, school, stations …) 
</abstraction>
<algorithms>
De te volgen route is herleid tot een stappenplan: een lijst van de van de opeenvolgende uren en overeenkomstige plaatsen. (**algoritme**)
</algorithms>
<implementation>
Bij dit voorbeeld moet er niet geprogrammeerd worden. 
</implementation>

