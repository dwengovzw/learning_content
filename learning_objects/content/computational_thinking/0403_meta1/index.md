---
hruid: m_cd_cases3a
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
Automatiseer het berekenen van de schuine zijde van een rechthoekige driehoek als de rechthoekszijden gekend zijn.
</context>
<decomposition>
Subtaken (**decompositie**):<br>
1. Inzetten van de computer om de schuine zijde te berekenen. 
2. Formule? Gekend uit de stelling van Pythagoras.
3. Gebruiker moet in staat zijn om de lengte van de  gegeven rechthoekszijden in te geven.
4. Welk datatype is het meest geschikt voor die zijden? Int of float?
5. Na de verwerking van de gegevens via de formule, is er een output. Hoe laat je de output proper verschijnen?
</decomposition>
<patternRecognition>
Als eenzelfde berekening vaak moet herhaald worden, dan is het handig deze te vatten in een functie. (**patroonherkenning**)
    
De formule zal daarom opgenomen worden in een zelfgedefinieerde functie. 

</patternRecognition>
<abstraction>
Een functie is een **abstractie** van een subalgoritme.

</abstraction>
<algorithms>
Het algoritme bevat (in deze volgorde) instructies om:
1. de gegevens op te vragen aan de gebruiker;
2. die gegevens te verwerken met als doel het bekomen van de lengte van de schuine zijde;
3. de lengte van de schuine zijde te laten zien op het scherm. 


</algorithms>
<implementation>
**Programma in Python**
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
def pythagoras(a, b):<br>
&nbsp;&nbsp;&nbsp;&nbsp;c = math.sqrt(a**2 + b**2)<br>
&nbsp;&nbsp;&nbsp;&nbsp;return c<br><br>
# invoer<br>
rhz1 = float(input("Lengte van de eerste rechthoekszijde: "))<br>
rhz2 = float(input(“Geef de lengte van de tweede rechthoekszijde: "))<br><br>
# verwerking<br>
schz = pythagoras(rhz1, rhz2)<br><br>
# uitvoer<br>
print("De lengte van de schuine zijde is: ", schz)
</div>

</implementation>

