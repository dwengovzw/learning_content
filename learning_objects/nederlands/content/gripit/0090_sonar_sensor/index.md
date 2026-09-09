---
hruid: org_dwengo_gripit_sonar_sensor
version: 1
language: nl
title: "Sonar-sensor"
description: "Meet afstanden met een ultrasone sensor en de Halberd."
keywords: ["fiche", "gripit", "halberd", "sonar", "ultrasoon", "sensor"]
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
    <h1 class="title">Sonar-sensor</h1>
    <h2 class="subtitle">Meet de afstand tot een voorwerp</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">De sonar-sensor</h3>
            <p class="info_item_content">De sonar-sensor stuurt een ultrasoon geluidssignaal uit en meet wanneer de weerkaatsing terugkomt. Uit die tijd berekent de sensor de afstand tot een voorwerp in centimeter.</p>
            <img src="img/sonar.png" alt="Een ultrasone sonar-sensor." title="Sonar-sensor"></img>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Aansluiten</h3>
            <p class="info_item_content">De sensor gebruikt VCC voor 5V, GND voor massa, TRIG om een meting te starten en ECHO om de weerkaatsing te ontvangen. Het testprogramma gebruikt <code>A1</code> als TRIG en <code>A0</code> als ECHO, met een maximumafstand van 200 cm.</p>
            <div class="dwengo_content table_container"><table><tr><th>Sonar-sensor</th><th>Halberd</th></tr><tr><td>VCC</td><td>5V</td></tr><tr><td>GND</td><td>GND</td></tr><tr><td>TRIG</td><td>A1</td></tr><tr><td>ECHO</td><td>A0</td></tr></table></div>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">De testmeting</h3>
            <p class="info_item_content">Met <code>sonarA1A0.ping_cm()</code> leest het programma de afstand. Is die 50 cm of kleiner, dan laat het programma RGB-led 1 blauw branden. Zo test je zowel de afstandsmeting als de reactie van de robot.</p>
        </div>
    </div>
    <div class="example_item item">
        <h3 class="example_item_title">Test de sonar-sensor</h3>
        <div class="dwengo-content dwengo-code-simulator"><pre><code class="language-cpp" data-filename="sonar_test.cpp">
#include &lt;Dwenguino.h&gt;
#include &lt;NewPing.h&gt;

#define TRIGGER_PIN_A1 A1
#define ECHO_PIN_A0 A0
#define MAX_DISTANCE 200

NewPing sonarA1A0(TRIGGER_PIN_A1, ECHO_PIN_A0, MAX_DISTANCE);

void setup() {
    initDwenguino();
}

void loop() {
    if (sonarA1A0.ping_cm() &lt;= 50) {
        digitalWrite(RGB_1_B, HIGH);
    } else {
        digitalWrite(RGB_1_B, LOW);
    }
    delay(100);
}
</code></pre></div>
    </div>
</div>