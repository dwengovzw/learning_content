---
hruid: leerlijn_fiches_dwenguino_rgb
version: 1
language: nl
title: "RGB-led"
description: "De kleuren voor de RGB-led instellen"
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
    <h1 class="title">SONAR-SENSOR</h1>
    <h2 class="subtitle">Een afstand meten</h2>
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
                Het lcd-scherm kan tekst weergeven. Hiermee kan bijvoorbeeld een boodschap worden meegedeeld.<br>
                Op het lcd-scherm van de dwenguino passen maximaal 32 karakters, zoals letters of cijfers, verspreid over twee regels. Je kan dus 16 karakters per regel tonen.<br>
                <br>
                De helderheid van het scherm is aanpasbaar. Je kan dit zelf regelen door aan de gele schroef te draaien (zie figuur) met een schroevendraaier, terwijl het lcd-scherm aanstaat.
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
    #include <NewPing.h>

    #define TRIGGER_PIN 11
    #define ECHO_PIN 12
    #define MAX_DISTANCE 200

    NewPing sonar(
        TRIGGER_PIN, 
        ECHO_PIN, 
        MAX_DISTANCE);
    int afstand;

    void setup(){
        initDwenguino();
        pinMode(13, OUTPUT);
    }

    void loop(){
        afstand = sonar.ping_cm();
        if (afstand > 0 && afstand < 100){
            digitalWrite(13, HIGH);
        } else {
            digitalWrite(13, LOW);
        }
        delay(100);
    }
</code>
</pre> 
            </p>
        </div>
    </div>
</div>



