---
hruid: m_ct03_90
version: 3
language: nl
title: "Meta"
description: "Meta"
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
De *Levenshteinafstand* is een metriek om de afstand tussen twee woorden of zinnen te bepalen. Om de afstand tussen twee woorden te bepalen, tel je het aantal letters dat je moet toevoegen, verwijderen of vervangen om het ene woord om te vormen in het andere. Indien we dit probleem willen oplossen met behulp van een computer doen we aan **computationeel denken**. We kunnen de computer dan een matrix laten opbouwen waarbij we deze stapsgewijs opvullen met de afstand van (een deel van) woord A, naar (een deel van) woord B.
Een gedetailleerde beschrijving vind je in het<a href="/learning-path.html?hruid=anm4&language=nl&te=true&source_page=%2Falgorithms%2F&source_title=%20Algoritmes#org_dewengo_levenshtein_algorithm;nl;1"><strong> leerpad algoritmen - De Levenshteinafstand</strong></a> terug.  
</div>
</context>
<decomposition>
**Decompositie**<br>
Om de Levenshteinafstand te berekenen met een computer doen we het volgende:
<ol>
    <li>Opbouwen van een matrix</li>
    <li>Het berekenen van de minimale hoeveelheid bewerkingen die nodig zijn om van het ene (deel van een) woord naar het andere te gaan.</li>
    <li>Het bepalen van de gepaste bewerkingen zodat we niet te veel aanpassingen moeten doen.</li>
    <li>Het bepalen van de uiteindelijke afstand tussen twee woorden.</li>
</ol>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
De Levenshtein-afstand wordt gebruikt door chatbots om een gestelde vraag die niet in het 'woordenboek' staat te koppelen aan een vraag die er wel in staat en hier het meest op lijkt. Het zoeken naar de afstand tussen twee woorden wordt ook in de genetica gebruikt. In dit vakgebied is het vaak nodig om gelijkenissen te zoeken in DNA-sequenties. Deze worden gewoonlijk voorgesteld als een opeenvolging van de letters C, G, A en T (dit zijn de vier verschillende nucleobasen voor in een DNA-sequentie). Door de afstand te berekenen tussen deze "woorden" bestaande uit deze 4 letters, kunnen we dus ook de gelijkenissen tussen DNA-sequenties vinden.
</patternRecognition>
<abstraction>
**Abstractie**<br>
Bij het berekenen van de Levenshtein-afstand zijn we enkel geïnteresseerd in het aantal en de soort operaties die nodig zijn om van woord A naar woord B te gaan. De specifieke karakters en woorden, alsook hun betekenis, zijn hierbij details die we achterwege kunnen laten.
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
Om de Levenshtein-afstand op een correcte manier te berekenen, moeten we een stappenplan opstellen. Zo'n stappenplan of algoritme kan worden uitgevoerd door een computer.
</algorithms>
<implementation>
**Programma**<br>
Een implementatie van dit algoritme is terug te vinden in het <a href="/learning-path.html?hruid=anm4&language=nl&te=true&source_page=%2Falgorithms%2F&source_title=%20Algoritmes#org_dewengo_levenshtein_algorithm_dynamic;nl;1"><strong> leerpad algoritmen - De Levenshteinafstand</strong></a>
</implementation>

