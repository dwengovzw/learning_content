---
hruid: g_lcd_vb1
version: 3
language: nl
title: "Voorbeeld Lcd 1"
description: "Voorbeeld Lcd 1"
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

OPGAVE 1

Laat 'Welkom robot' op het lcd-scherm verschijnen.

Oplossing:

![blockly](@learning-object/lcd_m1/nl/3)

<div class="alert alert-box alert-success">
De tekst 'Welkom robot' in het blauwe blokje kan je aanpassen.<br><br>
De twee nullen eronder zijn ook van belang:<br>
<ul><li><em>op rij 0</em>: de tekst verschijnt op de eerste regel.</li></ul>
<ul><li><em> vanaf kolom 0: de tekst verschijnt vanaf het eerste karakter.</li></ul>
</div>