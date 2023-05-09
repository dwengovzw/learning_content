---
hruid: m_ct_cases18
version: 3
language: nl
title: "Sentimentanalyse"
description: "Sentimentanalyse"
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
Ontwikkel een AI-systeem dat reviews op sociale media classificeert volgens sentiment (positief, neutraal, negatief).  
</div>
</context>
<decomposition>
Verkennen van het probleem. Wat heb je nodig? <br> Subtaken (**decompositie**):<br>
1. Keuze maken tussen regelgebaseerd of datagebaseerd AI-systeem
2. Sentimentwoordenboek in Nederlands inladen
3. Hoe is een woord terug te vinden in een woordenboek?    
4. De reviews voorverwerken (tokeniseren, hoofdletters en leestekens verwijderen)
5. De reviews representeren a.d.h.v. woordenboekvorm van de woorden erin, samen met hun woordsoort
6. Matching tussen de woorden en het sentiment- woordenboek om sentimentscore elk word te bepalen
7. Bepaal de sentimentscore en sentiment de reviews.
</decomposition>
<patternRecognition>
Het gebruik van een lexicon (woordenboek specifiek voor de taak) en tokeniseren is een techniek die veel wordt toegepast in taaltechnologie, bv. cyberpest detectie, auteursherkenning,  automatisch vertalen, tekst genereren … (**patroonherkenning**)
</patternRecognition>
<abstraction>
Door te tokeniseren worden de zinnen herleid tot de woorden die ze bevatten. <br>
De hoofdletters en leestekens worden genegeerd. De woorden worden herleid tot hun woordenboekvorm en aangevuld met hun woordsoort.(**abstractie**)<br>
De voorverwerking laat toe om een datastructuur die geschikt is om efficiënt te zoeken, te gebruiken.
</abstraction>
<algorithms>
Een **algoritme** om het sentiment van een review te bepalen:<br>
- Maak een lijst van de woorden die in de zin voorkomen, met hun woordsoort. Negeer leestekens.
- Zoek elk woord op in het sentimentwoordenboek.
- Sla de score van elk woord op in een lijst.
- Tel de scores op.
- Bepaal het sentiment a.d.h.v. van een wiskundige uitdrukking (groter dan 0, gelijk aan 0, kleiner dan nul).
</algorithms>
<implementation>
Zie het project ‘Chatbot’. Deze activiteit kan zonder computer gebeuren.<br>
Wil je dit programmeren? Bij het project ‘Chatbot’ vind je de notebooks met het programmeergedeelte.
</implementation>

