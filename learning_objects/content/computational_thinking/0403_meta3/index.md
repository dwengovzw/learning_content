---
hruid: m_cd_cases3c
version: 3
language: nl
title: "Pythagoras - routeplanner"
description: "Pythagoras - routeplanner"
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
New York. Wat is de afstand in vogelvlucht van Times Square naar het Empire State Building, uitgedrukt in mijl. 
Vertrek hiervoor van de wandelafstanden die een routeplanner verstrekt om van Times Square naar het Empire State Building te wandelen. 
</context>
<decomposition>
**Decompositie** in subtaken:<br>
1. Bepaal het hoekpunt van de rechte hoek in de routeplanner (metrostation 34st/Herald Sq).
2. Gebruik de routeplanner om de wandelafstand te bepalen op de twee rechthoekszijden.
</decomposition>
<patternRecognition>
Het stratenplan vertoont een **patroon**:<br> 
de straten vormen een rechthoekig rooster.<br>
De afstand in vogelvlucht kan dus bepaald worden als de schuine zijde van een rechthoekige driehoek.
</patternRecognition>
<abstraction>
De straten en kruispunten worden **geabstraheerd** tot de zijden en de hoekpunten van een rechthoekige driehoek. 
</abstraction>
<algorithms>
**Algoritme**: Bereken de vierkantswortel van de som van de kwadraten van de parameters.
(De parameters zijn de lengtes van de rechthoekszijden.) 
</algorithms>
<implementation>
**Programma in Python**
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
def pythagoras(a, b):<br>
&nbsp;&nbsp;&nbsp;&nbsp;"""Schuine zijde berekenen uit gekende rechthoekszijden."""  
&nbsp;&nbsp;&nbsp;&nbsp;c = math.sqrt(a**2 + b**2)<br>
&nbsp;&nbsp;&nbsp;&nbsp;return c<br><br>
# invoer<br>
rhz1 = float(input("Lengte van de eerste rechthoekszijde: "))<br>
rhz2 = float(input("Geef de lengte van de tweede rechthoekszijde: "))<br><br>
# verwerking<br>
vogelvlucht = pythagoras(rhz1, rhz2)<br><br>
# uitvoer<br>
print("De afstand in vogelvlucht is: ", vogelvlucht)
</div>

</implementation>
