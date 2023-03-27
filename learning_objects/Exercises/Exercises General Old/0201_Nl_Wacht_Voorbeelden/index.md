---
hruid: Wacht_Voorbeeld
version: 3
language: nl
title: "Wacht Voorbeeld"
description: "Wacht Voorbeeld"
keywords: ["StartToDwenguino", "wacht"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [10, 11, 12, 13, 14]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

### Voorbeeld Wacht

OPGAVE 1

Schrijf een programma dat het volgende doet:

* Laat "Hallo mensen" op het lcd-scherm verschijnen gedurende 1 seconde (1000 ms).
* Laat "Ik ben Dwenguino" op het lcd-scherm verschijnen voor 2 seconden (2000 ms).

Oplossing:

**Voorbeeld 1**

Het *'wacht'-blok* dat **na** een bepaalde instructie staat, geeft weer hoelang de computer moet **wachten** vooraleer deze met de volgende instructie mag beginnen.

Het probleem dat zich nu voordoet, is dat "Ik ben Dwenguino" op het scherm blijft staan. *Denk even na over wat dit zou veroorzaken.*

Dit kan je op 2 manieren oplossen. 

**Manier 1**

De eerste manier is om de tekst te verwijderen. Hiervoor gebruik je het blok **MaakLCDLeeg**.

**Voorbeeld 11**


**Manier 2**

De tweede manier is om alle code te verplaatsen van het *'zet klaar'-deel* naar het *'herhaal'-deel*. Dan zal de computer simpelweg de code opnieuw uitvoeren eens ze allemaal uitgevoerd is.

**Voorbeeld 13**


OPGAVE 2

Maak een reclamebord voor de UGent en dwengo. De namen moeten afwisselend verschijnen in een interval van 5 seconden. Zorg er ook voor dat de namen gecentreerd zijn.

Oplossing:

**Voorbeeld 2**


*Test deze voorbeelden ook zelf uit in de simulator!*
