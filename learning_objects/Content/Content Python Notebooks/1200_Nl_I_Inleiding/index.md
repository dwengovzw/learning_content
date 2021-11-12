---
hruid: PN_InleidingEpidemie-v1
version: 3
language: nl
title: "Inleiding"
description: "Inleiding"
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', 
    'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso'
]
---

# Inleiding
De COVID-19 pandemie houdt heel de wereld in haar greep. 
Om de impact van het virus te controleren, kan men het principe van sociale uitsluiting hanteren of inzetten op groepsimmuniteit. 
In dit project kunnen leerlingen een epidemie simuleren doorheen een sociaal netwerk, en onderzoeken welke strategieën de ziekte het best onder de knoet kunnen houden. 

In de berichtgeving van de COVID-19 pandemie komen termen zoals 'wiskundig model' en 'exponentiële groei' vaak aan bod. In dit leerpad ga je zelf aan de slag met de data en exponentiële functies en leer je hoe zo'n wiskundig model voor een epidemie wordt ontwikkeld.

## besmettelijke ziektes
In de geschiedenis van de mensheid heeft niets zoveel mensen gedood als besmettelijke ziekten. 
De ziekte die de meeste mensen heeft gedood is waarschijnlijk tuberculose, waarbij 1 miljard mensen in alleen de 19de en 20ste eeuw omkwamen. 
De ziekte die het snelst gedood heeft, is de Spaansegriepepidemie die 50 tot 100 miljoen mensen doodde tussen 1918 en 1920. De ziekte met het grootste evenredige dodental blijkt de Zwarte Dood, die 20% van de wereldbevolking en zelfs 50% van de Europese bevolking in de 14e eeuw doodde. Nog erger dan die ramp was het dodental op het Amerikaanse continent na de Europese kolonisatie. Er wordt geschat dat 90% van de inheemse bevolking geëlimineerd werd door de door Europeanen meegebrachte ziektes. De inheemse bevolking was namelijk nog nooit eerder met deze ziektes in contact gekomen en had dus nog niet de gelegenheid gehad om resistentie te ontwikkelen tegen deze ziektes.

Tegenwoordig veroorzaken besmettelijke ziektes minder doden door betere medische kennis, technieken en middelen. Ze blijven echter een ernstig probleem voor de volksgezondheid, zoals bijvoorbeeld de COVID-19 pandemie. Bovendien kunnen personen gemakkelijk ziektes verspreiden. Zo kan in een paar uur tijd een ziekte naar een ander continent verspreiden via het vliegtuig.

![Verschillende vliegtuigroutes tussen luchthavens.]([STATIC]/luchthaven.png)

***

**Zelf aan de slag: COVID-19 België**

COVID-19 is aan een steile opmars bezig. Ook in België vertoont het aantal besmettingen een exponentiële stijging. 

We hebben een Jupyter Notebook ontwikkeld waarin je leert hoe je aan exponentiële regressie doet: je zal met Python de exponentiële functie bepalen die het best past bij de data.

Je kan hiermee zelf aan de slag. Surf naar [onze Jupyter Notebook server](http://kiks.ilabt.imec.be/jupyter/) en kies *Simuleer Epidemie*. Klik vervolgens op *Spawn*. <br>
Open vervolgens de notebook *CoronaBelgie.ipynb*. Kunnen programmeren is niet echt vereist. <br>
In dezelfde map vind je ook een notebook *WerkenMetNotebooks.ipynb* met uitleg over de praktische werkwijze.
Wil je toch eerst wat programmeerervaring opdoen? Neem dan eerst onze [oefeningen programmeren]("link WerkenMetDeNotebooks") door.<br>
Op de gebruikte computers moet geen extra software worden geïnstalleerd om met de notebooks aan de slag te gaan.

***