---
hruid: pp_aep9
version: 3
language: nl
title: "Nulwaarden"
description: "Nulwaarden"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
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
teacher_exclusive: false
---

# Nulwaarden 

In de wiskunde leer je de nulwaarden van een functie berekenen door vergelijkingen op te stellen en die op te lossen door technieken, zoals de regel van Horner en de methode van de discriminant, toe te passen. Soms is het echter niet mogelijk om de nulwaarden op die manier te vinden. Denk bv. aan een veeltermfunctie - wat een relatief eenvoudige functie is - met enkel niet-rationale nulpunten. In de wiskundeles zal men dan naar de grafische rekenmachine of de computer grijpen om die nulwaarden te bepalen.

Deze toestellen maken gebruik van zogenaamde numerieke methodes om de nulwaarden te bepalen: Ze passen bepaalde technieken iteratief toe om **stap voor stap** de nulwaarden te benaderen.  

Er bestaan meerdere numerieke methodes om de nulwaarden te bepalen. <br>
Hier worden twee methodes voorgesteld. In een eerste notebook maak je kennis met de bissectiemethode, een tweede notebook gaat in op de methode van Newton.   

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=6520 "Nulwaarden numeriek bepalen")

---------
In de eerste notebook komen enkele **wiskundige concepten** aan bod: tweedegraadsfunctie en parabool, punt op een grafiek, derde- en vierdegraadsfunctie (optioneel), het (rekenkundig) gemiddelde van twee getallen, continue functie, functiewaarde, snijpunt van de grafiek van een functie met de x-as.

In de tweede notebook komen enkele **wiskundige concepten** aan bod: tweedegraadsfunctie en parabool, punt op een grafiek, derde- en vierdegraadsfunctie (optioneel), het (rekenkundig) gemiddelde van twee getallen, continue functie, functiewaarde, snijpunt van de grafiek van een functie met de x-as.

De afgeleide in een punt van een parabool is de richtingscoëfficiënt van de raaklijn in dat punt aan de parabool.<br>
Waar de parabool stijgt, is de raaklijn een stijgende rechte en is de richtingscoëfficiënt van de raaklijn positief. Waar de parabool daalt, is ze negatief.
In een top van de parabool is de raaklijn horizontaal en de afgeleide 0.
Hoe steiler de raaklijn, hoe groter de richtingscoëfficiënt van de raaklijn in absolute waarde, dus hoe groter de afgeleide in absolute waarde.
 

---------
#### Verband met minimumdoelen informaticawetenschappen
In de notebooks leer je a.d.h.v. een *numerieke methode* een nulwaarde benaderen. 
Misschien verdiepte je je ook in het facultatief onderdeel over *recursie*.

