---
hruid: leerlijn_fiches_dwenguino_knoppen
version: 1
language: nl
title: "Knoppen"
description: "Leer de knoppen gebruiken"
keywords: ["Knoppen", "fiche", "dwenguino"]
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
    <h1 class="title">WIP - Knoppen</h1>
    <h2 class="subtitle">Programma's starten m.b.v. knoppen</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
            <p class="info_item_content">
                <img src="img/knoppen.png" alt="Een afbeelding van de knoppen." title="Een afbeelding van de knoppen."></img>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Type</h3>
            <p class="info_item_content">
                Invoer 
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
                Op de dwenguino vind je vijf drukknoppen. De buitenste knoppen kregen de namen NOORD, ZUID, OOST, WEST, net als in aardrijkskunde. De middelste knop heet MIDDEN.<br>
                <br>
                Je kan deze gebruiken om bepaalde delen van je programma niet te laten uitvoeren tot je dit expliciet aangeeft door een knop in te drukken.
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
            <h3 class="example_item_title">Voorbeeld: led 0 gaat pas branden wanneer je een knop indrukt.</h3>
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
        if (digitalRead(SW_N) == PRESSED) {
            pinMode(32, OUTPUT);
            digitalWrite(32, HIGH);
        }
    }
</code>
</pre> 
            </p>
        </div>
    </div>
</div>



