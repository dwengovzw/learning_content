---
hruid: g_lcd_vb2
version: 3
language: nl
title: "Voorbeeld Lcd 2"
description: "Voorbeeld Lcd 2"
keywords: ["oefeningen", "lcd", "lcd-scherm"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
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
## Lcd-scherm

OPGAVE 2

Zorg ervoor dat 'Welkom' en 'robot' op aparte lijnen verschijnen.

Oplossing:

![blockly](@learning-object/lcd_m2/nl/3)

<div class="alert alert-box alert-success">
Om de tekst in 2 rijen te splitsen, heb je een tweede <em>'lcd-scherm'-blok</em> nodig.<br>
Verander je bij 'op rij:' de 0 in een 1, dan komt de tekst op de tweede lijn.
</div>