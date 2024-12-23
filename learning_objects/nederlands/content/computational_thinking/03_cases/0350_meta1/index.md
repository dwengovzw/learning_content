---
hruid: m_ct03_50a
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
Automatiseer het berekenen van de schuine zijde van een rechthoekige driehoek als de rechthoekszijden gekend zijn. Vraag de nodige input aan de gebruiker.
</context>
<decomposition>
Subtaken (**decompositie**):<br>
<ol>
    <li>Inzetten van de computer om de schuine zijde te berekenen. </li>
    <li>Formule? Gekend uit de stelling van Pythagoras.</li>
    <li>Gebruiker moet in staat zijn om de lengte van de  gegeven rechthoekszijden in te geven.</li>
    <li>Welk datatype is het meest geschikt voor die zijden? Int of float?</li>
    <li>Na de verwerking van de gegevens via de formule, is er een output. Hoe laat je de output proper verschijnen?</li>
</ol>
</decomposition>
<patternRecognition>

</patternRecognition>
<abstraction>

</abstraction>
<algorithms>
Het algoritme bevat (in deze volgorde) instructies om:
<ol>
    <li>de gegevens op te vragen aan de gebruiker;</li>
    <li>die gegevens te verwerken met als doel het bekomen van de lengte van de schuine zijde;</li>
    <li>de lengte van de schuine zijde te laten zien op het scherm. </li>
</ol>
</algorithms>
<implementation>
**Programma in Python**
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
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
