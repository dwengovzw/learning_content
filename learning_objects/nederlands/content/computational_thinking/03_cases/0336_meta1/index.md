---
hruid: m_ct03_36a
version: 3
language: nl
title: "Pythagoras - schuine zijde"
description: "Pythagoras - schuine zijde"
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
![Driehoek1](pyth1.png)<br>
<br>
**Probleemstelling**<br>
Automatiseer het berekenen van de schuine zijde van een rechthoekige driehoek als de rechthoekszijden gekend zijn. Vraag de nodige input aan de gebruiker.
</context>
<decomposition>
**Decompositie**<br>
<ul>
    <li><p style="color: Gray">Algoritme opstellen om de schuine zijde te berekenen. Dit algoritme maakt gebruik van de wiskundige formule uit de stelling van Pythagoras.</p></li>
    <li><p style="color: Gray">Algoritme implementeren in de computer (keuze software, bijvoorbeeld Python).</p></li>
    <li>Ervoor zorgen dat de gebruiker de lengte van de gegeven rechthoekszijden kan ingeven.</li><br>
    <li><p style="color: Gray">Datatype kiezen voor die zijden. Welk datatype is het meest geschikt? Int of float?</p></li>
    <li><p style="color: Gray">Ervoor zorgen dat de output na de verwerking van de gegevens proper verschijnt.</p></li>
</ul>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
<ul>
    <li>Invoer - verwerking - uitvoer</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
<ul>
    <li><p style="color: Gray">Alleen het feit dat de driehoek rechthoekig is en de afmetingen van de rechthoekszijden zijn van belang.</p></li>
</ul>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
<p style="color: Gray">Het programma bevat (in deze volgorde) instructies om:</p>
<ol>
    <li>de gegevens op te vragen aan de gebruiker;</li><br>
    <li><p style="color: Gray">die gegevens te verwerken met als doel het bekomen van de lengte van de schuine zijde;</p></li>
    <li><p style="color: Gray">de lengte van de schuine zijde te laten zien op het scherm.</p></li>
</ol>
</algorithms>
<implementation>
**Programma in Python**
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
import math<br>
# invoer<br>
rhz1 = float(input("Lengte van de eerste rechthoekszijde: "))<br>
rhz2 = float(input(“Geef de lengte van de tweede rechthoekszijde: "))<br><br>
# verwerking<br>
schz = math.sqrt(rhz1**2 + rhz2**2)<br><br>
# uitvoer<br>
print("De lengte van de schuine zijde is: ", schz)
</p>
</div>
</implementation>
