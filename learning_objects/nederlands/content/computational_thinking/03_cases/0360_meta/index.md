---
hruid: m_ct03_60
version: 3
language: nl
title: "Zwangerschapstest"
description: "Zwangerschapstest"
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
Een zwangerschapstest kan je gemakkelijk zelf thuis uitvoeren. Je vindt ze in niet-digitale en digitale vorm. Ontrafel de werking van een digitale zwangerschapstest. Vergelijk deze werking met die van een niet-digitale zwangerschapstest.  
</context>
<decomposition>
**Decompositie**<br>
<ul>
    <li>Uit welke onderdelen bestaat een digitale zwangerschapstest?
        <ul>
            <li>Een staafje om in contact te brengen met urine. Een bepaalde stof op dat staafje waarmee de urine al dan niet kan reageren op basis van de aanwezigheid van zwangerschapshormonen.
            <li>In het toestel zit een papaieren strookje waarop een controlestreepje verschijnt als de test correct werd uitgevoerd en een tweede streepje verschijnt bij reactie met het urinestaal.
            <li>Een sensor die detecteert of er al dan niet een reactie heeft plaatsgevonden. Welke sensor is dat? (kleurensensor)
            <li>Een microcontroller die het resultaat toont op de display.
            <li>Een display waarop het resultaat van de test verschijnt (via tekst of via een symbool).</li>
        </ul>
    <li>Wat gebeurt er bij zo'n test? Wat is de rol van de computer hierin?
    <li>Wat is de invoer en wat is de uitvoer bij de digitale test?
    <li>Wat zijn de verschillen tussen de digitale en de niet-digitale versie van een zwangerschapstest?</li>
</ul>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
<ul>
    <li>Invoer- verwerking - uitvoer
    <li>Het gebruik van een niet-digitale en een digitale test verloopt op quasi dezelfde manier.
    <li>Bij beide is de invoer een urinestaal en de (uiteindelijke) uitvoer een boodschap.
    <li>Beide testen bevatten een papieren strookje waarop een controlestreepje verschijnt. Bij de digitale test bevindt dit zich in het toestel. Bij beide reageert het urinestaal al dan niet met een bepaalde stof aanwesig in het meettoestel. Als deze reactie plaatsvindt, dan verschijnt er een tweede streepje op de papieren strip.
    <li>De microcontroller krijgt input van de sensor. Daarvoor meet de kleurensensor of het tweede streepje gekleurd is of niet. De sensor zal dus in de microcontroller invoeren of de test positief is of niet. De microcontroller zal deze invoer verwerken en doorgeven werlke boodschap er als uitvoer op het display moet verschijnen.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
<ul>
    <li>De digitale waarde, een rij van nullen en enen, die de sensor teruggeeft aan de microcontroller, is een abstractie van het resultaat op de papieren strip.
    <li>Het resultaat van een zwangerschapstest wordt vaak op een abstracte manier weergegeven door een symbool: een of twee streepjes, een plus- of minteren ...</li>
</ul>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
<ul>
    <li>Het uitvoeren van de test zelf verloopt volgens het stappenplan dat in de handleiding staat.
    <li>Algoritme bij de niet-digitale test:<br>
    ALS de urine reageert met de stof<br>
    DAN 2 streepjes<br>
    ANDERS 1 streepje
    <li>Algoritme bij de digitale test:<br>
    ALS sensorwaarde is 1<br>
    DAN toon 'ZWANGER' op het scherm<br>
    ANDERS toon 'NIET ZWANGER' op het scherm</li>
</ul>
</algorithms>
<implementation>
**Programma**<br>
Dit is een activiteit waarbij niet wordt geprogrammeerd.
</implementation>

