---
hruid: kiks_opbouwdiepneuraalnetwerk
version: 3
language: nl
title: "Opbouw diep neuraal netwerk"
description: "Opbouw diep neuraal netwerk"
keywords: ["AI"]
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Opbouw diep neuraal netwerk

Om huidmondjes te kunnen tellen moet de computer ze eerst herkennen. Hij moet van de verschillende delen van een foto kunnen zien of er een huidmondje op staat of niet. 
De computer moet dus een *classificatieprobleem* oplossen, waarbij het nodig is dat hij een specifiek object herkent. Het AI-systeem zal dus een systeem voor *objectherkenning* moeten inhouden. Daarvoor is een convolutioneel neuraal netwerk uitermate geschikt.

In deze notebook maak je stap voor stap kennis met de opbouw van een *diep neuraal netwerk* dat een oplossing biedt voor dit classificatieprobleem. Bij de ontwikkeling van een neuraal netwerk maakt de architect van het systeem meerdere keuzes en legt ook de waarden van enkele parameters vast. Deze keuzes bepalen de architectuur van het netwerk en hoe de training van het netwerk verloopt.

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=1701 "Diep neuraal netwerk")
