---
hruid: Wacht Voorbeeld-v1.0.1
version: 1
language: nl
title: Wacht Voorbeeld
description: Wacht Voorbeeld
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

### Voorbeeld

OPGAVE 1

Shchrijf een programma dat het volgende doet:

* Laat "Hallo mensen" op het lcd-scherm verschijnen voor 1 seconde (1000 ms).
* Laat "Ik ben Dwenguino" op het lcd-scherm verschijnen voor 2 seconden (2000 ms).

Oplossing:

**Voorbeeld 1**

De wacht-blok die **na** een bepaalde instructie staat, geeft weer hoelang de computer moet **wachten** vooraleer deze met de volgende instructie mag beginnen.

Het probleem dat zich nu voordoet, is dat "ik ben Dwenguino" op het scherm blijft staan. *Denk even na over wat dit zou veroorzaken.*

Dit kan je op 2 manieren oplossen. 

**Manier 1**

De eerste manier is om de tekst te verwijderen. Hiervoor gebruik je het blok **MaakLCDLeeg**.

**Voorbeeld 11**


**Manier 2**

De tweede manier is om alle code te verplaatsen van het "*Zet klaar*"-deel naar het "*herhaal*"-deel. Dan zal de computer simpelweg de code opnieuw uitvoeren eens ze allemaal uitgevoerd is.

**Voorbeeld 13**


OPGAVE 2

Maak een reclamebord voor de UGent en Dwengo. De namen moeten afwisselend verschijnen in een interval van 5 seconden. Zorg er ook voor dat de namen gecentreerd zijn.

Oplossing:

**Voorbeeld 2**


*Test deze voorbeelden ook zelf uit in de simulator!*
