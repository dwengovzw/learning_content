---
hruid: Uitleg tekenrobot-v1.0.00
version: 1
language: nl
title: Uitleg tekenrobot
description: Uitleg tekenrobot
keywords: [voorbeeld, voorbeeld2]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [4, 3]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
---

# 6. De tekenrobot aansturen

De tekenrobot van WeGoSTEM heeft *twee motoren* en *twee armen*. Elke arm is verbonden met één van de motoren. Als deze motoren draaien, dan bewegen de armen van de tekenrobot. Elke motor kan *naar rechts* en *naar links* draaien en kan op *verschillende snelheden* worden ingesteld.

Een motor aansturen doe je met een motor-blok: 

![alt](https://scholen.dwengo.org/static/dcmotor.png "Afb. Tekenrobot")

Met dit blok controleer je de snelheid en de draaizin van de motor.


![alt](https://scholen.dwengo.org/static/positiemotorentekenrobot.png "Afb. Tekenrobot")

Op de plaats van de onderste rode bolletjes bevinden zich de motoren.
De twee motoren hebben nummers: de linkse motor is motor nummer 1 en de rechtse motor is motor nummer 2. Dit komt overeen met het nummer dat je ziet naast de tekst “nummer” op het motor-blok. 

Met het motor-blok kan je naast het nummer van de motor ook nog de snelheid van die motor instellen. *Die snelheid wordt bepaald door een getal tussen -255 en 255*. Bij een positieve waarde draait de motor in de ene richting, bij een negatieve waarde in de andere richting.
