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
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">De testbeweging</h3>
            <p class="info_item_content">De test beweegt de servo in stappen van 15 graden van 0 tot 75 graden. <code>servoOnPinSERVO_1.write(i * 15)</code> stuurt de gewenste positie door; na elke stap wacht het programma 200 milliseconden.</p>
        </div>
    </div>
</div>