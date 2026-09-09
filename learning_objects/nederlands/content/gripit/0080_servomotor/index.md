---
hruid: org_dwengo_gripit_servomotor
version: 1
language: nl
title: "Servomotor"
description: "Bestuur een servomotor met de Halberd."
keywords: ["fiche", "gripit", "halberd", "servomotor", "servo", "uitvoer"]
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
    <h1 class="title">Servomotor</h1>
    <h2 class="subtitle">Laat een motor naar een gekozen positie draaien</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">De servomotor</h3>
            <p class="info_item_content">Een servomotor is een actuator waarvan je de positie kunt aansturen. Een 180-gradenservo is geschikt voor nauwkeurige bewegingen, zoals een arm of grijper die naar een bepaalde hoek moet bewegen.</p>
            <img src="img/servos.png" alt="Servomotoren uit de socialrobotkit." title="Servomotoren"></img>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Aansluiten</h3>
            <p class="info_item_content">Een servo heeft drie aansluitingen: GND voor massa, VCC voor de 5V-voeding en Signal voor het stuursignaal. In het testprogramma wordt de motor met <code>attach(SERVO_1)</code> aan de servo-aansluiting <code>SERVO_1</code> gekoppeld.</p>
            <div class="dwengo_content table_container"><table><tr><th>Servomotor</th><th>Halberd-aansluiting SERVO_1</th></tr><tr><td>GND</td><td>GND</td></tr><tr><td>VCC</td><td>5V</td></tr><tr><td>Signal</td><td>PWM</td></tr></table></div>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">De testbeweging</h3>
            <p class="info_item_content">De test beweegt de servo in stappen van 15 graden van 0 tot 75 graden. <code>servoOnPinSERVO_1.write(i * 15)</code> stuurt de gewenste positie door; na elke stap wacht het programma 200 milliseconden.</p>
        </div>
    </div>
    <div class="example_item item">
        <h3 class="example_item_title">Test de servomotor</h3>
        <div class="dwengo-content dwengo-code-simulator"><pre><code class="language-cpp" data-filename="servo_test.cpp">
#include &lt;Dwenguino.h&gt;
#include &lt;Servo.h&gt;

Servo servoOnPinSERVO_1;

void setup() {
    initDwenguino();
    servoOnPinSERVO_1.attach(SERVO_1);
}

void loop() {
    for (int angle = 0; angle &lt;= 75; angle += 15) {
        servoOnPinSERVO_1.write(angle);
        delay(200);
    }
}
</code></pre></div>
    </div>
</div>