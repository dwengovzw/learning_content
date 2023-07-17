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
# Rupsenuitbraak modelleren met de exponentiële functie

## Inleiding
Vele insecten willen zo veel mogelijk nakomelingen voortbrengen. <br>
In een generatie verpopt een buxusmotrups zich tot een buxusmot, welke nieuwe eitjes legt op een haag. Uit deze eitjes kruipen nieuwe rupsen en de cyclus herbegint. <br>
Het leven van een insect is echter niet zonder gevaar. Op elk moment in de cyclus kunnen eitjes, rupsen, poppen en motten sterven door predatie van vogels, pesticiden, uithongering of andere gevaren. 

Gemiddeld gezien kan je echter aannemen dat elke rups aanleiding geeft tot een bepaald aantal nieuwe rupsen in de volgende generatie.<br>
Dit leidt tot de volgende regel: 
$$x_{t} = a . x_{t-1}$$

waarbij $a \in \rm IR_{0}^{+}$ de **groeifactor** is. 

#### Opdracht

-  Beschrijf de situatie naargelang de waarde van $a$.
-  De buxusmot vormt een plaag. Welke waarden van $a$ passen in deze situatie?
-  Leg uit waarom je hier te maken hebt met **exponentiële groei**.

## Model
Bij een groeifactor $a=1,8$ leidt elke rups gemiddeld tot iets minder dan twee nieuwe rupsen per generatie.<br>
Begin met een bescheiden populatie van vijf rupsen.

#### Opdracht
- Stel $a=1,8$ en $x_{0} = 5$.
- Bepaal het aantal rupsen op $t = 1$, $t = 2$, $t = 3$ en $t = 4$.
- Stel het functievoorschrift op voor deze exponentiele groei.

----------------------------
[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=6010 "Insect exponentieel")
