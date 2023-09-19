---
hruid: m_ct03_31c
version: 3
language: nl
title: "Sociale robot"
description: "Sociale robot"
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
Realiseer een sociale robot gebaseerd op je eigen ontwerp.
</context>
<decomposition>
Leerlingen splitsen de opdracht op in de verschillende fasen/stappen die ze moeten doorlopen in het creëer-realiseer-evalueer proces (**decompositie**):
<ul>
    <li>(Planning opmaken)</li>
    <li>Schets van het ontwerp ‘Lichaam en acties robot’ die beantwoordt aan de criteria en gewenste acties</li>
    <li>Technische informatie: sensoren en actuatoren</li>
    <li>Tekening overbrengen op de gekozen drager</li>
    <li>Actie(s) programmeren in de simulator a.d.h.v. het neergeschreven algoritme</li>
    <li>Programma testen in de simulator, evalueren en bijsturen</li>
    <li>Acties testen a.d.h.v. de hardware </li>
    <li>Onderdelen monteren op robotlichaam</li>
    <li>Geheel testen en evalueren</li>
    <li>(Optimaliseren)</li>
</ul>
    
![schetsontwerp](schetsontwerp.png)
</decomposition>
<patternRecognition>

</patternRecognition>
<abstraction>
Hoek of snelheid van een servomotor worden **geabstraheerd** naar een geheel getal van -255 tot 255.
</abstraction>
<algorithms>
Actie(s) van de robot weergeven in een **algoritme** (Dit mag neergeschreven worden in pseudocode, omschreven worden in een zin ...)<br>
![schetsalgoritme](schetsalgoritme.png)<br>
Uit de decompositie volgt het stappenplan dat meegeeft hoe te werk te gaan. (**algoritme**)
</algorithms>
<implementation>
Plaats hier een screenshot van de Blockly-code.
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
tekst
</p></div>
</implementation>
