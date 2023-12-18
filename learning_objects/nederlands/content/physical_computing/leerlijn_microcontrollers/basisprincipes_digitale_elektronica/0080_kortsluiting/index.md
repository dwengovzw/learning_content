---
hruid: leerlijn_invoer_basisprincipes_kortsluiting
version: 1
language: nl
title: "Kortsluiting"
description: "Je leert wat kortsluiting is en dat je het nooit mag veroorzaken."
keywords: ["digitale elektronica", "kortsluiting", "basisprincipes", "microcontroller", "µC", "arduino", "dwenguino"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16]
difficulty: 1
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Kortsluiting

<div class="dwengo-content important">
    <h2 class="title">LET OP!</h2>
    <div class="content">
        Je mag een circuit <strong>nooit kortsluiten</strong>. Op die manier maak je de µC of eventuele componenten die ermee verbonden zijn kapot.
    </div>
</div>

Een circuit is kortgesloten wanneer er een heel hoge stroom door het circuit gaat. Dit doet zich voor wanneer het circuit zelf bijna geen weerstand heeft. Dit volgt rechtstreeks uit de wet van Ohm. De spanning die een bron kan leveren blijft meestal relatief constant. Als we de kring sluiten met een kleine weerstand wordt de stroom heel hoog.
We krijgen bijvoorbeeld kortsluiting als we de Vcc en GND van onze µC rechtstreeks met elkaar verbinden met een koperdraad van 10 cm. Deze koperdraad heeft een weerstand van 1.7 nano Ohm ofwel 1.7e-9 Ω. Passen we hierop de wet van Ohm toe:

\\[\mathrm{I} = \frac{5\\,\mathrm{V}}{1.7 \cdot 10^{-9}\\,\mathrm{\Omega}} = 2.9\cdot 10^9\\,\mathrm{A} = 2.9\\,\mathrm{GA}\\]

Om dit in perspectief te plaatsen, een stroom van \\(0.1\\,\mathrm A\\) kan fataal zijn voor de mens. \\(2.9\\,\mathrm{GA}\\) is dus zeker fataal voor de µC!
