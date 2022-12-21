---
hruid: m_ct_cases1
version: 3
language: nl
title: "Vierkantsvergelijking"
description: "Vierkantsvergelijking"
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
Automatiseer het berekenen van de (reële) wortels van een vierkantsvergelijking. Er wordt op zoek gegaan naar het aantal wortels en de waarde van de wortels.
</context>
<decomposition>
Subtaken (**decompositie**):
1. Inzetten van de computer om de wortels van een vierkantsvergelijking te berekenen. 
2. Formules op een of andere manier aan de computer geven om de wortels te berekenen: discriminant, formules voor de wortels zelf.
3. Gebruiker moet in staat zijn om de coëfficiënten van de vierkantsvergelijking in te geven.
4. Welk datatype is het meest geschikt voor die coëfficiënten? Int of float?
5. Na de verwerking van de gegevens via de formule, is er een output. Hoe laat je de output proper verschijnen?
</decomposition>
<patternRecognition>
Als eenzelfde berekening vaak moet herhaald worden, dan is het handig deze te vatten in een functie. (**patroonherkenning**)
De formules zullen daarom opgenomen worden in een zelfgedefinieerde functie: een voor de discriminant en een voor de wortels.
 (**patroonherkenning**)
</patternRecognition>
<abstraction>
Een functie is een **abstractie** van een subalgoritme.<br><br>
*Weetje: een vierkantsvergelijking is een abstractie van het zoeken naar de snijpunten van een parabool met de x-as.*
</abstraction>
<algorithms>
Het **algoritme** bevat (in deze volgorde) instructies om:<br>
de gegevens op te vragen aan de gebruiker;<br>
die gegevens te verwerken met als doel het bekomen van de discriminant en de wortels;<br>
het aantal wortels te laten zien op het scherm;<br>
de wortels te laten zien op het scherm. 
</algorithms>
<implementation>
**Programma in Python**<br>
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
def discriminant(a, b, c):<br>
&nbsp;&nbsp;&nbsp;&nbsp;"""Berekenen van discriminant."""<br>
&nbsp;&nbsp;&nbsp;&nbsp;d = b**2 – 4 * a * c<br>
&nbsp;&nbsp;&nbsp;&nbsp;return d<br><br>
def aantalwortels(a, b, c):<br>
&nbsp;&nbsp;&nbsp;&nbsp;"""Bepalen van aantal wortels."""<br>
&nbsp;&nbsp;&nbsp;&nbsp;d = discriminant(a, b, c)<br>
&nbsp;&nbsp;&nbsp;&nbsp;aantal = 0<br>
&nbsp;&nbsp;&nbsp;&nbsp;if d > 0: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;aantal = 2<br>
&nbsp;&nbsp;&nbsp;&nbsp;elif d = 0:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;aantal = 1  <br>
&nbsp;&nbsp;&nbsp;&nbsp;return aantal<br><br>
def wortels(a, b, c):<br>
&nbsp;&nbsp;&nbsp;&nbsp;"""Berekenen van de wortels."""<br>
&nbsp;&nbsp;&nbsp;&nbsp;d = discriminant(a, b, c)<br>
&nbsp;&nbsp;&nbsp;&nbsp;w1 = (- b + math.sqrt(d)) / (2 * a )<br>
&nbsp;&nbsp;&nbsp;&nbsp;w2 = (- b - math.sqrt(d)) / (2 * a )<br>
&nbsp;&nbsp;&nbsp;&nbsp;return w1, w2<br><br>
# invoer<br>
a = float(input("Geef de coëfficiënt van x^2: "))<br>
b = float(input("Geef de coëfficiënt van x: "))<br>
c = float(input("Geef de constante term: "))<br><br>
# verwerking<br>
d = discriminant(a, b, c)<br>
n = aantalwortels(a, b, c)<br>
if d >= 0:<br>
&nbsp;&nbsp;&nbsp;&nbsp;x1, x2 = wortels(a, b, c)<br><br>
# uitvoer<br>
print("Het aantal wortels is:", n)<br>
if d >= 0:
&nbsp;&nbsp;&nbsp;&nbsp;print("De wortels zijn: ", x1, "en", x2)
</div>
</implementation>

