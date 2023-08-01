---
hruid: stem5_1
version: 3
language: nl
title: "Exponentiële groei"
description: "Exponentiële groei"
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
# Modelleren van een rupsenuitbraak volgens de exponentiële groei

Vele insecten willen zo veel mogelijk nakomelingen voortbrengen. In een generatie verpoppen buxusmotrupsen zich tot een buxusmotten, die op hun beurt nieuwe eitjes leggen op een haag. Uit deze eitjes kruipen nieuwe rupsen en de cyclus herbegint. Het leven van een insect is echter niet zonder gevaar. Op elk moment in de cyclus kunnen eitjes, rupsen, poppen en motten sterven door predatie van vogels, pesticiden, uithongering of andere gevaren. Gemiddeld gezien kan je echter aannemen dat elke rups aanleiding geeft tot een bepaald aantal nieuwe rupsen in de volgende generatie. Deze aanname vormt de basis van de **exponentiële groei**.

## Exponentiële groei

Wanneer je mag aannemen dat een rups gemiddeld gezien aanleiding geeft tot a > 0 \\( a > 0 \\) $a > 0\$ nieuwe rupsen, bekom je de volgende uitdrukking:

$$u_t = a \cdot u_{t - 1}$$

Deze vergelijking is niets anders dan het recursieve voorschrift van een rij, waarbij je op basis van een gegeven element eenvoudig het volgende element kan bepalen door te vermenigvuldigen met $a$. Deze parameter $a$ wordt de **groeifactor** genoemd.

### Opdracht 1

- Beschrijf de situatie naargelang de waarde van $a$. Wat gebeurt er bijvoorbeeld indien $a < 1$?
- De rupsen van de buxusmot vormen een plaag. Welke waarden van $a$ passen in deze situatie?
- Leg uit waarom je hier te maken hebt met **exponentiële groei**.

## Exponentieel model

Bij een groeifactor $a = 1,6$ leidt elke rups gemiddeld tot iets meer dan anderhalve nieuwe rupsen per generatie. Beschouw een bescheiden beginpopulatie van vijf rupsen. Stel aan de hand van de volgende opdracht een wiskundig model op voor de evolutie van populatiegrootte.

### Opdracht 2

- Stel $a = 1,6$ en $u_0 = 5$. Bepaal dan het aantal rupsen op $t = 1$, $t = 2$, $t = 3$ en $t = 4$.
- Stel het algemene voorschrift op voor de rij met deze exponentiële groei.

Het algemene voorschrift stelt nu het exponentiële groeimodel voor!

## Interactieve notebook

Nu ga je aan de slag met een interactieve online notebook. In de notebook zet je Python in om te rekenen en om het model grafisch voor te stellen.

[![Knop](embed/knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=6010 "Insect exponentieel")
