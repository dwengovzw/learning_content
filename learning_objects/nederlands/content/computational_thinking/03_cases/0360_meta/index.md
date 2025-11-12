---
hruid: m_ct03_60
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
Visualiseer en interpreteer de conversaties in Harry Potter en de steen der wijzen.
</div>
</context>
<decomposition>
**Decompositie**<br>
<ul>
    <li>Welke conversaties noteer je en welke negeer je?
    <li>Kies met welke factoren je wel of geen rekening houdt: aantal conversaties, lengte van een conversatie...
    <li>Hoe geef je de personages weer?
    <li>Hoe geef je de conversaties weer?</li>
</ul> 
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
<ul>
    <li>Dergelijke relaties worden vaak weergegeven door een graaf.
    <li>Je ziet door de dikte van de bogen welke personages het vaakst converseren.
    <li>De hoofdpersonages springen zowel in de graaf van hoofdstuk 11 als in de graaf van het volledige boek in het oog.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
<ul>
    <li>Je focust op de conversaties. De rest van de tekst negeer je.
    <li>Je beperkt je tot conversaties die duidelijk plaatsvinden tussen twee of meer personages. Mompelen, fluisteren, een kreet slaken... negeer je.
    <li>Je houdt geen rekening met de lengte van een conversatie.
    <li>Personages worden weergegeven door een knoop, conversaties door een boog en het aantal conversaties wordt weergegeven door de dikte van de boog.</li>
</ul>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
<ul>
    <li>Noteer alle personages en alle conversaties tussen twee of meer personages.
    <li>Geef de personages weer door een knoop.
    <li>Geef de conversaties weer door een boog.
    <li>Voor elke bijkomende conversatie tussen dezelfde personages, maak je de boog dikker.</li>
</ul>
</algorithms>
<implementation>
**Programma**<br>
In deze opdracht wordt niet geprogrammeerd.
</implementation>

