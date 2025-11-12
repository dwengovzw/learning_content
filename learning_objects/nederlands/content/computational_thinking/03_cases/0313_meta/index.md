---
hruid: m_ct03_13
version: 3
language: nl
title: "Sonarsensor"
description: "Sonarsensor"
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14]
difficulty: 3
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

<context>
**Probleemstelling**<br>
Denk na over de werking van de sonarsensor vanuit de principes van computationeel denken. (1)
</context>
<decomposition>
**Decompositie**<br>
<ul>
    <li>Wat is echolocatie?
    <li>Wat is de snelheid waarmee het signaal zich verplaatst?
    <li>Wat is het verband tussen snelheid, afstand en tijdsduur?
        <ul>
            <li>Wat betekent dit voor de afstand tussen sonar en object?
            <li>Hoe kan je die afstand berekenen?
            <li>In welke eenheid wordt de afstand uitgedrukt?
        </ul>
    </li>
</ul>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
<ul>
    <li>Werking van sonar volgens principe van echolocatie, dus uitsturen en terug opvangen van een geluidssignaal.
    <li>De sonarsensor is een invoerelement.
    <li>De gemeten tijdsduur wordt door de rekeneenheid verwerkt tot een afstand in cm.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
<ul>
    <li>Formule om de gemeten tijd om te zetten naar de afstand in meter: x = 340 * (∆t/2), met x de afstand in meter en ∆t de gemeten tijd in seconden tussen het uitsturen en het opnieuw ontvangen van het geluidssignaal.</li>
</ul>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
<ul>
    <li>Bereken de afstand uit de gemeten tijd.
    <li>De afstand wordt door de sonar gegeven in cm, dus de afstand in meter wordt nog vermenigvuldigd met 100.
    <li>Dus: afstand = 340 * (tijdsinterval/2)*100, met de afstand in centimeter en de tijd in seconden.</li>
</ul>
</algorithms>
<implementation>
**Programma**<br>
In deze activiteit wordt er niet geprogrammeerd.
</implementation>

