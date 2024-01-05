---
hruid: anm_1401
version: 3
language: nl
title: "Riemannsom"
description: "Riemannsom"
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

# De Riemannsom en de trapeziummethode

In de **inleidende notebook** leer je hoe je met de Riemannsom de oppervlakte tussen een kromme en de x-as kunt benaderen. Als toepassing wordt een halve cirkel gebruikt. Zo kan je a.d.h.v. de formule van de oppervlakte van een cirkel ook meteen nagaan hoe goed de benadering is die je vindt.

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=6530 "Riemannsom en trapeziummethode")

----------------
In de notebook maak je gebruik van het beginpunt van elk deelinterval om de breedte van elke rechthoek te bepalen. In de wiskundeles hoorde je in deze context misschien van boven- en ondersommen. Voor de Riemannsom maakt het echter niet uit welke waarde in een deelinterval je gebruikt om de breedte van de betreffende rechthoek te bepalen. De limiet van de rij van de oppervlaktes zal steeds naar de werkelijke oppervlakte naderen.
