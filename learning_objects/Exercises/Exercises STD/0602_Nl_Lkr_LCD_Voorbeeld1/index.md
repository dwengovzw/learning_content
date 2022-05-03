---
hruid: STD_lcdVB1-v1
version: 3
language: nl
title: "Voorbeeld Lcd 1"
description: "Voorbeeld Lcd 1"
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

OPGAVE 1

Laat 'Welkom robot' op het lcd-scherm verschijnen.

Oplossing:

![blockly](@learning-object/LCDM1-v1/nl/3)

"schrijf tekst": Hier kan je de tekst schrijven die je wilt laten verschijnen. Het lcd-scherm kan maximaal 16 karakters tonen op eenzelfde lijn. 
"op rij": Hier geef je aan op welke rij je de tekst wilt laten verschijnen; 0 voor de eerste en 1 voor de tweede rij.
"vanaf kolom": Hier geef je aan vanaf welke kolom de tekst moet verschijnen.

*Test deze voorbeelden ook zelf uit in de simulator! Als je de werking wat te pakken hebt, kan je zelf aan de slag.*