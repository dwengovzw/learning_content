---
hruid: anm_1300
version: 3
language: nl
title: "Inleiding"
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