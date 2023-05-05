---
hruid: sr3_elektronica1
version: 3
language: nl
title: "Moederbord"
description: "Moederbord"
keywords: ["Sociale Robot", "AI Op School", "STEM", "Computationeel denken", "Grafisch programmeren"]
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
estimated_time: 20
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-technologie-en-technieken'
]
teacher_exclusive: false
---

# Bouwen van de fysieke robot
## Het moederbord
Je zal gebruikmaken van de Dwenguino en het bijbehorende uitbreidingsbord. Bij het snijden van de uitsparingen zal je hier dus ook plaats voor moeten voorzien!  

<div class="alert alert-box alert-danger">
Houd er rekening mee dat de USB-poort van de Dwenguino toegankelijk moet zijn om de USB-kabel comfortabel aan te sluiten.
</div>

### Bedrading en monteren

Voordat je de onderdelen op het lichaam van de robot bevestigt, is het verstandig om eerst de bedrading tussen de Dwenguino en de andere componenten aan te sluiten. Dit voorkomt dat er te weinig ruimte overblijft om de draden aan te sluiten, nadat de componenten zijn bevestigd.

Onderstaande afbeelding toont welke onderdelen aanwezig zijn op de Dwenguino en welke actuatoren hier rechtstreeks op kunnen worden aangesloten.

![](embed/assemblage1.png "Dwenguino")

*Het contrast van het lcd-scherm kan worden aangepast. Je kan de Dwenguino van stroom voorzien via de USB-kabel of een adapter.*

Op de *extension connector* zal je het uitbreidingsbord kunnen aansluiten (zie afbeelding). Dit is speciaal op maat gemaakt voor de sociale robot. Hiermee kan je alle andere sensoren en actuatoren aansluiten.  

![](embed/pcb.png "Uitbreidingsbord")