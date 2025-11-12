---
hruid: m_ct04_11
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
Ontwerp een toestel dat in werking treedt als je hand op minder dan 10 cm afstand ervan is, maar zonder dat je het aanraakt.
</context>
<decomposition>
**Decompositie**<br>
<ul>
    <li>Verkennen van het probleem:
        <ul>
            <li>kiezen welk toestel je zal ontwerpen, bijvoorbeeld een lcd-scherm waarop 'Hallo daar' verschijnt als je hand dicht genoeg bij het toestel komt.
            <li>een geschikte sensor kiezen: Met welke soort soort van sensoren kan je een afstand bepalden? Hoe gebeurt dat?
            <li>uitzoeken hoe je de boodschap na bepaalde tijd kan laten verdwijnen.</li>
        </ul>
    <li>Wat heb je nodig? Waarmee kan je dit verwezenlijken?
        <ul>
            <li>Microcontrollerplatform met lcd-scherm
            <li>Bewegingssensor (PIR-sensor) of afstandssensor (sonarsensor of infraroodsensor)</li>
        </ul>
    </li>
    <li>Aanpak:
        <ul>
            <li>Hoe sluit je de sensor aan op het platform?
            <li>Programma schrijven om de microcontroller aan te sturen. (Wat is de invoer? Wat is de uitvoer? Welke eenhuid gebruiken voor de afstand?)</li>
        </ul>
    </li>
</ul>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
<ul>
    <li>In de troiletten van restaurants, hotels, scholen... werken de kranen, zeep- en handdoekdispensers vaak op dezelfde manier; ze worden geactiveerd via een sensor, dus zonder ze aan te raken.
    <li>Ook automatische schuifdeuren werken op een vergelijkbare manier.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
<ul>
    <li>Met de sensor wordt de afstand tot een object bepaald. Er wordt geen rekening mee gehouden of het een hand is of niet.
    <li>In het programma kan je de berekende afstand abstraheren door een variabele te gebruiken.</li>
</ul>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
<ul>
    <li>ALS afstand van sensor tot object < 10 cm<br>
        DAN tekst 'Hallo daar' verschijnt op het lcd-scherm<br>
        ANDERS leeg lcd-scherm</li>
    <li>Deze instructie moet telkens worden herhaald om na te gaan of er een hand in de buurt is en om na te gaan of die al terug weg is. Want dan moet de boodschap verdwijnen.</li>
</ul>
</algorithms>
<implementation>
**Programma**<br>
Je kan de Dwenguino tekstueel programmeren of in een blokgebaseerde programmeeromgeving met simulator.
Je kan deze opdracht dus eventueel beperken tot de simulator; werk dan in het scenario 'Sociale robot'.
</implementation>




<context>
**Probleemstelling**<br>
**EXTRA:** Wat is de werking van een kraan die je kan laten lopen zonder deze aan te raken?
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