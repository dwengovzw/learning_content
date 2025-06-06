---
hruid: Lkr_lcd_Voorbeeld
version: 3
language: nl
title: "Lcd Voorbeeld"
description: "lcd Voorbeeld"
keywords: ["StartTodwenguino", "lcd", "lcd-scherm"]
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
teacher_exclusive: true
---

### Voorbeeld lcd-scherm

OPGAVE 1

Laat 'Welkom robot' op het lcd-scherm verschijnen.

Oplossing:

![blockly](@learning-object/LCDM1/nl/3)

De tekst 'Welkom robot' kan je aanpassen. De twee nullen betekenen: eerste lijn, eerste karakter.


OPGAVE 2

Zorg ervoor dat 'Welkom' en 'robot' op aparte lijnen verschijnen.

Oplossing:

![blockly](@learning-object/LCDM2/nl/3)

Om de tekst in 2 rijen te splitsen, heb je een tweede *'lcd-scherm'-blok* nodig.
Verander je bij 'op rij:' de 0 in een 1, dan komt je tekst op de tweede lijn.


OPGAVE 3

Plaats de tekst nu in het midden van het lcd-scherm.

Oplossing:

![blockly](@learning-object/LCDM3/nl/3)

Verander je bij 'op kolom' de 0 in een 5, dan schuift de tekst 5 plaatsen opnaar rechts.


*Test deze voorbeelden ook zelf uit in de simulator! Als je de werking wat te pakken hebt, kan je zelf aan de slag.*