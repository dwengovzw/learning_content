---
hruid: org_dwengo_gripit_rgb_led
version: 1
language: nl
title: "RGB-led"
description: "Maak kleuren met de RGB-led van de Halberd."
keywords: ["fiche", "gripit", "halberd", "rgb", "led", "uitvoer"]
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
    <h1 class="title">RGB-led</h1>
    <h2 class="subtitle">Geef de robot een kleurensignaal</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">De RGB-led</h3>
            <p class="info_item_content">Een RGB-led combineert rood, groen en blauw licht. Door de intensiteit van elk kanaal te kiezen, maak je verschillende kleuren. Elke intensiteit ligt tussen 0, uit, en 255, volledig helder.</p>
            <img src="img/rgb.png" alt="Een RGB-led uit de socialrobotkit." title="RGB-led"></img>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Halberd-aansluitingen</h3>
            <p class="info_item_content">Het testprogramma gebruikt de ingebouwde RGB-led 1 met <code>RGB_1_R</code>, <code>RGB_1_G</code> en <code>RGB_1_B</code>. Stel deze drie pinnen in als uitvoer en gebruik <code>analogWrite()</code> om de helderheid per kleurkanaal te bepalen.</p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">De testkleuren</h3>
            <p class="info_item_content">De RGB-led geeft de toestand van het testprogramma weer: blauw wanneer de sonar een voorwerp tot 50 cm detecteert, groen wanneer de oostknop is ingedrukt en rood in alle andere gevallen.</p>
        </div>
    </div>
</div>