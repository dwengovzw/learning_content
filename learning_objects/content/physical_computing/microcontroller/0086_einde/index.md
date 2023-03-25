---
hruid: pc_micro_p2_einde
version: 3
language: nl
title: "Samenvatting"
description: "Samenvatting"
keywords: ["Microcontroller"]
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
# Practicum 2 - Timers en Interrupts

## Einde

Hiermee zijn we ook aan het einde gekomen van dit practicum. We hebben nu een systeem dat:

* Zeer precieze wachttijden voor de stimulus kan uitvoeren
* Zeer precies de reactietijd kan uitmeten
* Ondertussen tijd heeft voor het uitvoeren van trage en/of minder kritische code zoals het aansturen van het LCD scherm.

Dit wordt mogelijk gemaakt door

* **Het gebruik van Timers om precieze tijdsintervallen te meten**
* **Het gebruik van interrupts om tijdskritische events tijdig af te handelen, onafhankelijk van de minder kritische code in de main functie.**

Deze twee concepten zullen tijdens jullie project veel aan bod komen, aarzel dus zeker niet om vragen te stellen als bepaalde aspecten onduidelijk zijn.

Het is ook een goede oefening om nu de hoofdstukken in de datasheet eens volledig te lezen, je zal merken dat je al veel beter snapt wat er allemaal gebeurt enerzijds en dat je anderzijds nog een aantal nieuwe zaken zal leren die nuttig zullen zijn in het project.