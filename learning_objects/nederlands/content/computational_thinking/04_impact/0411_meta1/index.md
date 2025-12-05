---
hruid: m_ct04_11a
version: 3
language: nl
title: "Automatische kraan"
description: "Automatische kraan"
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
Wat is de werking van een kraan die je kan laten lopen zonder deze aan te raken?
</context>
<decomposition>
**Decompositie**<br>
<ul>
    <li>Wat moet het toestel doen?
        <ul>
            <li>Bij een geactiveerd toestel: er loopt water uit de kraan.
            <li>Na een tijdje moet het water stoppen met lopen.
            <li>Is de kraan ingesteld op een bepaald debier of bepaalde tijdsduur?</li>
        </ul>
    <li>Componenten identificeren: soort sensor, microcontroller
    <li>Wat is de invoer? (Afstand hand tot sensor)
    <li>Wat is de uitvoer? (Kraan open)</li>
</ul>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
<ul>
    <li>Alle toestellen die worden geactiveerd zonder ze aan te raken, werken met een sensor die iets detecteert: afstand tot een object, beweging, licht, het doorbreken van een infraroodstraal... Ze worden dus door gelijksoortige computerprogramma's aangestuurd. Bijvoorbeeld een automatische zeep- of handdoekdispenser, maar ook automatische schuifdeuren.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
<ul>
    <li>Met de sensor wordt de afstand tot een object bepaald. Er wordt geen rekening mee gehouden of het een hand is of niet.
    <li>Kraan gaat open als de hand dicht genoeg bij de sensor is. Dicht genoeg is een abstractie van de afstand die je moet kiezen als je de microcontroller programmeert.
    <li>Programmeer je, dan kan je de berekende afstand abstraheren door een variabele te gebruiken.</li>
</ul>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
<ul>
    <li>ALS iets dicht bij sensor<br>
        DAN kraan loopt<br>
        ANDERS kraan loopt niet
    <li>Meer abstract:<br>
        ALS iets dicht bij sensor<br>
        DAN toestel wordt geactiveerd<br>
        ANDERS toestel niet actief
    </li>
</ul>
</algorithms>
<implementation>
**Programma**<br>
Deze activiteit kan zonder computer gebeuren.
Kies je ervoor om te programmeren, laat je leerlingen dan de extra opdracht maken. (zie volgend kader)
</implementation>