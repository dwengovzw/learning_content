---
hruid: leerlijn_fiches_dwenguino_ledmatrix
version: 1
language: nl
title: "Ledmatrix"
description: "Figuren maken met de ledmatrix"
keywords: ["led", "ledmatrix", "fiche", "dwenguino"]
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
estimated_time: 15
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

<div class="dwengo_content fiche">
    <h1 class="title">Led-matrix</h1>
    <h2 class="subtitle">Figuren tonen op de led-matrix</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
            <p class="info_item_content">
                <img src="img/ledmatrix.png" alt="Een afbeelding van een ledmatrix." title="Een afbeelding van het ledmatrix."></img>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Type</h3>
            <p class="info_item_content">
                Uitvoer, digitale actuator 
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Pinnen</h3>
            <p class="info_item_content">
                <table>
                    <tr><td>VCC</td><td>De 5 V-voeding, soms ook aangeduid met een +.</td></tr>
                    <tr><td>GND</td><td>De referentiespanning of de grond, soms ook aangeduid met een -.</td></tr>
                    <tr><td>D</td><td>...</td></tr>
                    <tr><td>CS</td><td>...</td></tr>
                    <tr><td>CLK</td><td>...</td></tr>
                </table>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                De led-matrix is een vierkante 8x8 matrix met 64 leds in een vaste kleur (rood). De matrix is ideaal om bepaalde patronen te laten oplichten, zoals een oog of een mond van de robot of een ander symbool. Je kan de matrices ook met elkaar verbinden (maximaal 4), als je meerdere matrices tegelijk wil gebruiken. Je kan programmeren welke leds er tegelijk moeten oplichten.
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Symbool</h3>
            <p class="info_item_content">
                <img src="img/icon.svg" title="LED symbool">
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Aansluiting</h3>
            <p class="info_item_content">
                <img src="img/connection.svg" title="LED aansluiting" >
            </p>
        </div>
        <div class="example_item item">
            <h3 class="example_item_title">Voorbeeld: led laten branden als sonar-sensor object detecteert tot een afstand van 100cm.</h3>
            <p class="example_item_content">
<pre>
<code class="language-arduino">
    
    #include <Wire.h>
    #include <Dwenguino.h>
    #include <LiquidCrystal.h>
    #include <LedController.hpp>

    auto led_matrix = LedController<4,1>();
    ByteBlock pattern = {};

    void setup(){
        initDwenguino();

        auto conf = controller_configuration<4,1>();
        conf.useHardwareSpi = false;
        conf.SPI_CLK = 13;
        conf.SPI_MOSI = 2;
        conf.SPI_CS = 10;
        led_matrix.init(conf);
        led_matrix.activateAllSegments();
        led_matrix.setIntensity(8);
        led_matrix.clearMatrix();
    }

    void loop(){
        pattern = {B00000000,B01100110,B11111111,B11111111,B01111110,B00111100,B00011000,B00000000};
        led_matrix.displayOnSegment(0, pattern);
    }
</code>
</pre> 
            </p>
        </div>
    </div>
</div>



