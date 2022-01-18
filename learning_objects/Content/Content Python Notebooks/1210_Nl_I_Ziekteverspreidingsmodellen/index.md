---
hruid: PN_Epidemie1-v1
version: 3
language: nl
title: "Ziekteverspreidingsmodellen"
description: "Epidemie"
keywords: ["voorbeeld", "voorbeeld2"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [14, 15, 16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-digitale-media-en-toepassingen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-kansrekenen-statistiek',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek', 
    http://ilearn.ilabt.imec.be/vocab/curr1/s-stem-onderzoek
]
---

# Ziekteverspreidingsmodellen

Bij de uitbraak van een besmettelijke ziekte is het belangrijk om inzicht te krijgen in hoe deze ziekte zich de volgende dagen en weken kan verspreiden. Dit zal helpen om het optimale gebruik van middelen en mensen te plannen om de ziekteverspreiding een halt toe te roepen. Bovendien, voordat we deze maatregelen ten uitvoer leggen, moeten we weten hoe ze het verloop van de ziekte kunnen beïnvloeden, zodat de meest efficiënte en goedkoopste maatregelen eerst geïmplementeerd kunnen worden.

Om deze en andere belangrijke vragen te beantwoorden, worden vaak *ziekteverspreidingsmodellen* gebruikt. Deze modellen zijn gebaseerd op wiskundige vergelijkingen die beschrijven hoe een besmettelijke ziekte zich doorheen de tijd en/of ruimte verspreidt. Ze kunnen worden gebruikt om relevante vragen te beantwoorden, zoals:

* Zonder tussenkomst, zal de ziekte uitsterven of ongecontroleerd verspreiden?
* Hoeveel mensen moeten gevaccineerd worden om de verspreiding te stoppen?
* Hoe beïnvloedt het gedrag van mensen of dieren de verspreiding van ziektes?
* Welk effect zullen verschillende quarantainemaatregelen hebben?

Aangezien het verloop doorheen de tijd cruciaal is in het geval van ziekteverspreiding, zijn 
bijna alle ziekteverspreidingsmodellen *dynamisch* van aard. Ze modelleren dus een verandering in de tijd. 
In dit project zullen we een veel gebruikt type ziekteverspreidingsmodel bestuderen: het SIR-model.

Bij elke golf in de COVID-19 pandemie kennen het aantal besmettingen of het aantal ziekenhuisopnames op een gegeven moment een exponentiële groei. In dit project leer je met regressie een exponentiële functie bepalen die die trend in de data weerspiegelt.