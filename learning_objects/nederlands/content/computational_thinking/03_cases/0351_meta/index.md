---
hruid: m_ct03_51
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
**Probleemstelling**<br>
Automatiseer het berekenen van de (reële) wortels van een vierkantsvergelijking. Er wordt op zoek gegaan naar het aantal wortels en de waarde van de wortels.
</context>
<decomposition>
**Decompositie**<br>
<ol>
    <li>Inzetten van de computer om de wortels van een vierkantsvergelijking te berekenen. </li>
    <li>Formules op een of andere manier aan de computer geven om de wortels te berekenen: discriminant, formules voor de wortels zelf.</li>
    <li>Gebruiker moet in staat zijn om de coëfficiënten van de vierkantsvergelijking in te geven.</li>
    <li>Welk datatype is het meest geschikt voor die coëfficiënten? Int of float?</li>
    <li>Na de verwerking van de gegevens via de formule, is er een output. Hoe laat je de output proper verschijnen?</li>
</ol>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
Als eenzelfde berekening vaak moet herhaald worden, dan is het handig deze te vatten in een functie.
De formules zullen daarom opgenomen worden in een zelfgedefinieerde functie: een voor de discriminant en een voor de wortels.
</patternRecognition>
<abstraction>
**Abstractie**<br>
Een functie is een abstractie van een subalgoritme.<br><br>
*Weetje: een vierkantsvergelijking is een abstractie van het zoeken naar de snijpunten van een parabool met de x-as.*
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
Het algoritme bevat (in deze volgorde) instructies om:<br>
<ol>
    <li>de gegevens op te vragen aan de gebruiker;</li>
    <li>die gegevens te verwerken met als doel het bekomen van de discriminant en de wortels;</li>
    <li>het aantal wortels te laten zien op het scherm;</li>
    <li>de wortels te laten zien op het scherm.</li>
</ol>
</algorithms>
<implementation>
**Programma**<br>
<!-- <div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
def discriminant(a, b, c):<br>
&nbsp;&nbsp;&nbsp;&nbsp;"""Berekenen van discriminant."""<br>
&nbsp;&nbsp;&nbsp;&nbsp;d = b**2 – 4 * a * c<br>
&nbsp;&nbsp;&nbsp;&nbsp;return d<br><br>
def wortels(a, b, c, d):<br>
&nbsp;&nbsp;&nbsp;&nbsp;"""Berekenen van de wortels bij niet-negatieve discriminant."""<br>
&nbsp;&nbsp;&nbsp;&nbsp;w1 = (- b + math.sqrt(d)) / (2 * a )<br>
&nbsp;&nbsp;&nbsp;&nbsp;w2 = (- b - math.sqrt(d)) / (2 * a )<br>
&nbsp;&nbsp;&nbsp;&nbsp;return w1, w2<br><br>
# invoer<br>
a = float(input("Geef de coëfficiënt van x²: "))<br>
b = float(input("Geef de coëfficiënt van x: "))<br>
c = float(input("Geef de constante term: "))<br><br>
# verwerking<br>
d = discriminant(a, b, c)<br>
if d >= 0:<br>
&nbsp;&nbsp;&nbsp;&nbsp;x1, x2 = wortels(a, b, c, d)<br><br>
# uitvoer<br>
if d >= 0:<br>
&nbsp;&nbsp;&nbsp;&nbsp;print("De wortels zijn: ", x1, "en", x2)<br>
&nbsp;&nbsp;&nbsp;&nbsp;if d > 0:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("Er zijn 2 verschillende wortels.")<br> 
&nbsp;&nbsp;&nbsp;&nbsp;else:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("Er zijn 2 samenvallende wortels.")<br>
else:<br>
&nbsp;&nbsp;&nbsp;&nbsp;print("Er zijn geen reële wortels.")    
</p>
</div> -->

```Python

    import math
    def discriminant(a, b, c):
        """Bereken discriminant van vierkantsvergelijking."""
        d = b**2 - 4 * a * c
        return d
    
    def aantal_wortels(d):
        """Bepaal aantal wortels en multipliciteit."""
        n = 0
        m = 1
        if d > 0:
            n = 2
        if d == 0:
            n =  1
            m = 2
        return n, m
    
    def wortels(a, b, c, d):
        """Bereken wortels bij niet-negatieve discriminant d."""
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    
    # invoer
    a = float(input("Geef de coëfficiënt van x² (verschillend van nul): "))
    b = float(input("Geef de coëfficiënt van x: "))
    c = float(input("Geef de constante term: "))

    # verwerking
    d = discriminant(a, b, c)
    n, m = aantal_wortels(d)

    if n != 0:  # wortels berekenen bij niet-negatieve discriminant
        wortel1, wortel2 = wortels(a, b, c, d)
    
    # uitvoer
    if n != 0:
        print("De wortels zijn: ", wortel1, "en ", wortel2)
        print("Aantal oplossingen: ", n, " met multipliciteit", m)
    else:
        print("Er zijn geen reële wortels")
```

</implementation>

