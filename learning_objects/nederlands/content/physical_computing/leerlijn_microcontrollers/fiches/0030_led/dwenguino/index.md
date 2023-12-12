---
hruid: leerlijn_fiches_dwenguino_led
version: 1
language: nl
title: "Leds"
description: "De leds op het bordje aansteken"
keywords: ["led", "fiche", "dwenguino"]
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
    <h1 class="title">WIP - Led</h1>
    <h2 class="subtitle">Leds laten branden</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
            <p class="info_item_content">
                <img src="img/leds.png" alt="Een afbeelding van de leds." title="Een afbeelding van de leds."></img>
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
                    <tr><td>PIN</td><td>...</td></tr>
                    <tr><td>PIN</td><td>...</td></tr>
                    <tr><td>PIN</td><td>...</td></tr>
                </table>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
               Links onderaan op het dwenguino-bord vind je acht leds.<br>
               <br>
               Deze leds zijn *led 0*, *led 1*, ..., *led 7*, van rechts naar links. De eerste led is dus *led 0*. In computerwetenschappen is het vaak de conventie om te beginnen tellen vanaf 0. Dit heb je misschien ook al gemerkt bij het lcd-scherm.<br>
               <br>
               Links bovenaan is er nog een extra led: *led 13*. Dit laatste led heeft enkele speciale functionaliteiten en krijgt daarom een aparte fiche.
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
            <h3 class="example_item_title">Voorbeeld: led 0 laten branden.</h3>
            <p class="example_item_content">
<pre>
<code class="language-arduino">
    
    #include <Wire.h>  
    #include <Dwenguino.h>
    #include <LiquidCrystal.h>

    void setup(){
        initDwenguino();

        dwenguinoLCD.setCursor(0,0);
        dwenguinoLCD.print(String("Welkom robot"));
    }

    void loop(){

    }
</code>
</pre> 
            </p>
        </div>
    </div>
</div>



