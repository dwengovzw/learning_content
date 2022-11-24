---
hruid: cd_cases1-v1
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
Een functie is een abstractie van een subalgoritme.<br><br>
Een vierkantsvergelijking is een abstractie van de verzameling van de nulpunten van een tweedegraadsfunctie, wat op zijn beurt een abstractie is van de snijpunten van een parabool met de x-as.
(**abstractie**)
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
def discriminant(a, b, c):
    """Berekenen van discriminant en bepalen van aantal wortels."""
    d = b**2 – 4 * a * c
    aantal = 0
    if d > 0: 
        aantal = 2
    elif d = 0:
         aantal = 1  
    return d, aantal

def wortels(a, b, c):
    d = discriminant(a, b, c)[0]
    x1 = (- b + math.sqrt(d)) / (2 * a )
    x2 = (- b - math.sqrt(d)) / (2 * a )
    return x1, x2
    
# invoer
a = float(input("Geef de coëfficiënt van x^2: "))
b = float(input("Geef de coëfficiënt van x: "))
c = float(input("Geef de constante term: "))
    
# verwerking
n = discriminant(a, b, c)[1]
wortels = wortels(a, b, c)

# uitvoer
print("Er zijn", n, "wortels.")
print("De wortels zijn: ", wortels[0], "en", wortels[1])

</implementation>

