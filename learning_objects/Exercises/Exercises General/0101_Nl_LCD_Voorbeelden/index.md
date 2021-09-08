---
hruid: lcd Voorbeeld-v1.0.1
version: 1
language: nl
title: lcd Voorbeeld
description: lcd Voorbeeld
keywords: [lcd, lcd-scherm]
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

Laat 'Welkom robot' op het lcd-scherm verschijnen.

Oplossing:

**Voorbeeld 1**

De tekst 'Welkom robot' kan je aanpassen. De twee nullen betekenen: eerste lijn, eerste karakter.


OPGAVE 2

Zorg ervoor dat 'Welkom' en 'robot' op aparte lijnen verschijnen.

Oplossing:

**Voorbeeld 2**

Om de tekst in 2 rijen te splitsen, heb je een tweede lcd-scherm-blok nodig.
Verander je bij 'op rij:' de 0 in een 1, dan komt je tekst op de tweede lijn.


OPGAVE 3

Plaats de tekst nu ook in het midden van het LCD-scherm.

Oplossing:

**Voorbeeld 3**

Verander je bij 'op kolom' de 0 in een 5, dan schuift de tekst 4 plaatsen op naar rechts.


*Test deze voorbeeldjes alvast eens uit in de simulator! Als je de werking wat te pakken hebt, kan je zelf aan de slag.*

**Eens een programma werkt in de simulator, kan je het ook uitproberen op een echte Dwenguino! Hieronder Wordt uitgebreid beschreven hoe je een programma van de simulator kunt uploaden naar de Dwenguino.**