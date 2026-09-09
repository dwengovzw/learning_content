---
hruid: org_dwengo_gripit_ledmatrix
version: 1
language: nl
title: "Led-matrix"
description: "Toon patronen op de led-matrix met de Halberd."
keywords: ["fiche", "gripit", "halberd", "led-matrix", "led", "uitvoer"]
educational_goals: [{source: Source, id: id}]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16, 17, 18]
difficulty: 1
estimated_time: 10
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

<div class="dwengo_content fiche">
    <h1 class="title">Led-matrix</h1>
    <h2 class="subtitle">Toon een patroon met leds</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">De led-matrix</h3>
            <p class="info_item_content">De led-matrix is een vierkant raster van 8 bij 8 rode leds. Je kunt er patronen, symbolen of een gezicht mee tonen. In het testprogramma verschijnt een hartpatroon op het eerste segment van de matrix.</p>
            <img src="img/ledmatrix.png" alt="Een 8 bij 8 led-matrix." title="Led-matrix"></img>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Aansluiten en instellen</h3>
            <p class="info_item_content">De matrix gebruikt voeding via VCC en GND en ontvangt signalen via data (D), chip select (CS) en clock (CLK). Het testprogramma gebruikt <code>LedController.hpp</code> en stelt de SPI-pinnen in met <code>PIN_SPI_SCK</code>, <code>PIN_SPI_MOSI</code> en <code>PIN_SPI_SS</code>.</p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Patroon tonen</h3>
            <p class="info_item_content">Na de initialisatie activeert het programma alle segmenten, stelt het de helderheid in op 8 en wist het scherm. Daarna bevat <code>pattern</code> acht bytes: elke byte beschrijft welke leds in een rij branden. Met <code>displayOnSegment(0, pattern)</code> verschijnt het patroon op segment 0.</p>
        </div>
    </div>
</div>