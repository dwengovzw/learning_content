---
hruid: pp_aep10
version: 3
language: nl
title: "Gradient descent"
description: "Gradient descent"
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

# Gradient descent
Om een neuraal netwerk te ontwikkelen zal de architect van het netwerk een algoritme programmeren dat nog parameters bevat, de zogenaamde gewichten of *weights*. De waarden van deze parameters zullen bepalen hoe goed het AI-systeem presteert. De training van het neurale netwerk komt erop neer dat het systeem op zoek gaat naar de meest optimale waarden voor deze gewichten. Hiervoor levert de architect een zogenaamde kostenfunctie aan, dat is een functie die afhangt van de gewichten en die aangeeft hoe ver het systeem nog afzit van de optimale situatie. Bij de training poogt men dus om de kostenfunctie te minimaliseren: men gaat op zoek naar het minimum door de gewichten stap voor stap aan te passen.

In de wiskunde leer je om het minimum van een functie te zoeken door bv. de functie af te leiden en de afgeleide gelijk te stellen aan nul. Dat leidt tot een vergelijking die je moet gaan oplossen a.d.h.v. geleerde algebraïsche technieken. Bij veel vergelijkingen leiden deze technieken echter niet tot een oplossing. Aangezien neurale netwerken heel veel parameters hebben en de ermee gepaard gaande kostenfunctie heel veel dimensies telt, is deze vertrouwde techniek niet bruikbaar en moet men een andere manier hanteren om het minimum van de kostenfunctie te bepalen. Men gebruikt de methode van _gradient descent_.

Bij  _gradient descent_ gaat men op zoek naar het minimum door de gewichten **stap voor stap** aan te passen, en zo dichter en dichter bij het minimum te komen. Geleidelijk aan vindt men zo de meest optimale gewichten waarnaar men op zoek is. De grootte van de stappen wordt bepaald door de zogenaamde *learning rate*; afhankelijk van de waarde van de *learning rate* zullen er grote of kleine aanpassingen plaatsvinden.  

In de volgende notebook word je ingewijd in de methode van _gradient descent_. Voor de eenvoud zal je op zoek gaan naar het minimum van enkele functies die afhankelijk zijn van slechts 1 variabele. Ook de functies worden vrij eenvoudig gehouden, de notebook beperkt zicht tot veeltermfuncties.   

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=1760 "Gradient descent")

---------
In de notebook komen enkele **wiskundige concepten** aan bod: tweedegraadsfunctie en parabool, punt op een grafiek, derde- en vierdegraadsfunctie (optioneel), de richtingscoëfficiënt van een raaklijn aan een functie, m.a.w. de afgeleide in een punt, lokaal en globaal minimum (optioneel).  

De afgeleide in een punt van een parabool is de richtingscoëfficiënt van de raaklijn in dat punt aan de parabool.<br>
Waar de parabool stijgt, is de raaklijn een stijgende rechte en is de richtingscoëfficiënt van de raaklijn positief. Waar de parabool daalt, is ze negatief.
In een top van de parabool is de raaklijn horizontaal en de afgeleide 0.
Hoe steiler de raaklijn, hoe groter de richtingscoëfficiënt van de raaklijn in absolute waarde, dus hoe groter de afgeleide in absolute waarde.

Een functie kan meer dan een minimum hebben. Als er bv. meerdere lokale minima zijn, dan is het de bedoeling om op zoek te gaan naar het globale minimum: het kleinste lokale minimum.  

---------
#### Verband met minimumdoelen informaticawetenschappen
In de notebook leer je met gradient descent een minimum benaderen; het is een *numerieke methode*.
