---
hruid: anm_1400
version: 3
language: nl
title: "Inleiding"
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
target_ages: [16, 17, 18]
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

# De Riemannsom en de trapeziummethode

Stel dat een schilder een object met een speciale vorm moet verven. Hij wil berekenen hoeveel verf hij zal moeten maken in de gewenste kleur.  Om de oppervlakte te bepalen van het object beschikt hij over functies die overeenkomen met de contouren van het object. Hij kan echter geen beroep doen op de gekende formules van rechthoek, cirkel, ...,  om de oppervlakte van de figuur te berekenen. 

Hij kan de oppervlakte wel benaderen door de oppervlakte te benaderen door rechthoeken en daarvan de totale oppervlakte te berekenen.

Stel dat je de gekleurde oppervlakte op de eerste figuur zou willen bepalen, dan kan je deze benaderen door de totale oppervlakte van de rechthoeken op de tweede figuur te berekenen.

![oppervlakte](https://github.com/dwengovzw/learning_content/assets/48352335/9ed0232b-3e8b-431f-8455-cc446a6b6522)

![benaderingopp](https://github.com/dwengovzw/learning_content/assets/48352335/fc66a8bf-aed5-4ff1-bcfd-4e5c6bb47428)

Hoe smaller de rechthoeken zijn, dus hoe meer er zijn, hoe nauwkeuriger de totale oppervlakte van de rechthoeken de gezochte oppervlakte benadert. 
