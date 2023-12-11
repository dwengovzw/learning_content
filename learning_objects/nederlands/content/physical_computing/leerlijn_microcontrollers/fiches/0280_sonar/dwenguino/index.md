---
hruid: leerlijn_fiches_dwenguino_sonar
version: 1
language: nl
title: "Sonar-sensor"
description: "Een afstand meten met de sonar-sensor"
keywords: ["afstand", "sonar", "fiche", "dwenguino"]
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
                <img src="img/sonar.png" alt="Een afbeelding van de sonar-sensor." title="Een afbeelding van de sonar-sensor."></img>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Type</h3>
            <p class="info_item_content">
                Invoer, digitale sensor 
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Pinnen</h3>
            <p class="info_item_content">
                <table>
                    <tr><td>VCC</td><td>De 5 V-voeding, soms ook aangeduid met een +.</td></tr>
                    <tr><td>GND</td><td>De referentiespanning of de grond, soms ook aangeduid met een -.</td></tr>
                    <tr><td>TRIG</td><td>De Trigger pin. Deze pin geeft aan wanneer de ultrasone sensor moet beginnen te meten. </td></tr>
                    <tr><td>ECHO</td><td>De echo pin. Deze pin geeft aan wanneer het weerkaatste, ultrasone signaal ontvangen is.</td></tr>
                </table>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                De sensor stuurt een ultrasoon geluidssignaal uit. Indien er een voorwerp binnen bereik is, zal deze ultrasone geluidsgolf op dit voorwerp weerkaatsen. Je kan de werking vergelijken met de echolocatie van vleermuizen. Door de tijd te meten tussen het verzenden van het geluidssignaal en het ontvangen van de weerkaatste straal, kan de sensor de afstand tot het object nauwkeurig bepalen. De afstand wordt teruggegeven in cm.
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



