---
hruid: leerlijn_fiches_dwenguino_zoemer
version: 1
language: nl
title: "Zoemer"
description: "De zoemer laten zoemen"
keywords: ["buzzer", "zoemer", "fiche", "dwenguino"]
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
    <h1 class="title">WIP - Zoemer</h1>
    <h2 class="subtitle">Tonen afspelen</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
            <p class="info_item_content">
                <img src="img/zoemer.png" alt="Een afbeelding van de zoemer." title="Een afbeelding van de zoemer."></img>
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
                Boven het lcd-scherm kan je een een ronde, zwarte component zien. Dit is de zoemer of buzzer. Hiermee kan je geluiden afspelen. <br>
                <br>
                Geluid is een golf van luchtdruk veroorzaakt door een trillend object zoals bijvoorbeeld een instrument of luidspreker. De hoeveelheid trillingen per seconde (de frequentie) bepaalt de toonhoogte. Wanneer het aantal trillingen per seconde tussen de 20 en 20 000 ligt, dan kan je dit als mens horen. Voor trillingen per seconde gebruiken we de eenheid Hertz, afgekort Hz. De mens kan dus trillingen horen tussen de 20 Hz en 20 000 Hz.<br>
                <br>
                Om geluid te kunnen afspelen is de dwenguino voorzien van een eenvoudige buzzer die je een gekozen frequentie kunt laten afspelen.
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
            <h3 class="example_item_title">Voorbeeld: de zoemer een toon herhaaldelijk laten afspelen.</h3>
            <p class="example_item_content">
<pre>
<code class="language-arduino">

    #include <Wire.h>
    #include <Dwenguino.h>
    #include <LiquidCrystal.h>

    void setup(){
        initDwenguino();
    }

    void loop(){
        pinMode(32, OUTPUT);
        digitalWrite(32, HIGH);
    }
</code>
</pre> 
            </p>
        </div>
    </div>
</div>



