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
# Rupsenuitbraak modelleren volgens exponentiële groei

## Inleiding
Vele insecten willen zo veel mogelijk nakomelingen voortbrengen. <br>
In een generatie verpoppen buxusmotrupsen zich tot een buxusmotten, die op hun beurt nieuwe eitjes leggen op een haag. Uit deze eitjes kruipen nieuwe rupsen en de cyclus herbegint. <br>
Het leven van een insect is echter niet zonder gevaar. Op elk moment in de cyclus kunnen eitjes, rupsen, poppen en motten sterven door predatie van vogels, pesticiden, uithongering of andere gevaren. 

Gemiddeld gezien kan je echter aannemen dat elke rups aanleiding geeft tot een bepaald aantal nieuwe rupsen in de volgende generatie.

Dit leidt tot de volgende uitdrukking:<br>
<p align="center"><em> u<sub>t</sub> = a . u<sub>t-1</sub></em></p>

waarbij <em>a</em> een strikt positief getal is. <br>
Deze vergelijking is niets anders dan het recursief voorschrift van een rij.

#### Opdracht 1
-  Beschrijf de situatie naargelang de waarde van <em>a</em>.
-  De rupsen van de buxusmot vormen een plaag. Welke waarden van <em>a</em> passen in deze situatie?
-  Leg uit waarom je hier te maken hebt met **exponentiële groei**.

## Model
Bij een groeifactor <em>a = 1,8</em> leidt elke rups gemiddeld tot iets minder dan twee nieuwe rupsen per generatie.<br>
Beschouw een bescheiden beginpopulatie van vijf rupsen.<br>
A.d.h.v. de volgende opdracht stel je een wiskundig model op voor de evolutie van deze populatie rupsen. 

#### Opdracht 2
- Stel <em>a = 1,8</em> en <em>u<sub>0</sub> = 5</em>.
- Bepaal het aantal rupsen op <em>t = 1</em>, <em>t = 2</em>, <em>t = 3</em> en <em>t = 4</em>.
- Stel het algemeen voorschrift op voor de rij met deze exponentiële groei.

----------------------------
Nu ga je aan de slag met een interactieve online notebook. In de notebook zet je Python in om te rekenen en om het model grafisch voor te stellen.

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=6010 "Insect exponentieel")
