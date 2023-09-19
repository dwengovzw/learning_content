---
hruid: m_ct03_75
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
<ol>
    <li>Keuze maken tussen regelgebaseerd of datagebaseerd AI-systeem.</li>
    <li>Sentimentwoordenboek in Nederlands inladen.</li>
    <li>Hoe is een woord terug te vinden in een woordenboek?    </li>
    <li>De reviews voorverwerken (tokeniseren, hoofdletters en leestekens verwijderen).</li>
    <li>De reviews representeren a.d.h.v. woordenboekvorm van de woorden erin, samen met hun woordsoort.</li>
    <li>Matching tussen de woorden en het sentimentwoordenboek om de sentimentscore van elk woord te bepalen.</li>
    <li>Bepaal de sentimentscore en sentiment de reviews.</li>
</ol>
</decomposition>
<patternRecognition>
Het gebruik van een lexicon (woordenboek specifiek voor de taak) en tokeniseren is een techniek die veel wordt toegepast in taaltechnologie, bv. cyberpestdetectie, auteursherkenning,  automatisch vertalen, tekst genereren … (**patroonherkenning**)
</patternRecognition>
<abstraction>
Door te tokeniseren worden de zinnen herleid tot de woorden die ze bevatten. <br>
De hoofdletters en leestekens worden genegeerd. De woorden worden herleid tot hun woordenboekvorm en aangevuld met hun woordsoort.(**abstractie**)<br>
De voorverwerking laat toe om een datastructuur die geschikt is om efficiënt te zoeken, te gebruiken.
</abstraction>
<algorithms>
Een **algoritme** om het sentiment van een review te bepalen:<br>
<ul>
    <li>Maak een lijst van de woorden die in de zin voorkomen, met hun woordsoort. Negeer leestekens.</li>
    <li>Zoek elk woord op in het sentimentwoordenboek.</li>
    <li>Sla de score van elk woord op in een lijst.</li>
    <li>Tel de scores op.</li>
    <li>Bepaal het sentiment a.d.h.v. van een wiskundige uitdrukking (groter dan 0, gelijk aan 0, kleiner dan nul).</li>
</ul>
</algorithms>
<implementation>
Zie het project ‘Chatbot’. Deze activiteit kan zonder computer gebeuren.<br>
Wil je dit programmeren? Bij het project ‘Chatbot’ vind je de notebooks met het programmeergedeelte.
</implementation>

