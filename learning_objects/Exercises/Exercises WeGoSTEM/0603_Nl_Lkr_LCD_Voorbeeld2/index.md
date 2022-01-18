---
hruid: WGS_Lkr_lcd2-v1
version: 3
language: nl
title: "Voorbeeld Lcd 2"
description: "Voorbeeld Lcd 2"
keywords: ["StartToDwenguino", "lcd", "lcd-scherm"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [10, 11, 12]
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

OPGAVE 2

Zorg ervoor dat 'Welkom' en 'robot' op aparte lijnen verschijnen.

Oplossing:

![blockly](@learning-object/LCDM2-v1/nl/3)

Om de tekst in 2 rijen te splitsen, heb je een tweede *'lcd-scherm'-blok* nodig.
Verander je bij 'op rij:' de 0 in een 1, dan komt je tekst op de tweede lijn.

*Test deze voorbeelden ook zelf uit in de simulator! Als je de werking wat te pakken hebt, kan je zelf aan de slag.*