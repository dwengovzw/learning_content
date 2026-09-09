---
hruid: org_dwengo_gripit_knoppen
version: 1
language: nl
title: "Knoppen"
description: "Gebruik de knoppen van de Halberd als invoer."
keywords: ["fiche", "gripit", "halberd", "knop", "invoer", "schakelaar"]
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
    <h1 class="title">Knoppen</h1>
    <h2 class="subtitle">Gebruik een knop als invoer</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">De knoppen</h3>
            <p class="info_item_content">Knoppen geven je programma een eenvoudige invoer: ingedrukt of niet ingedrukt. Je kunt ze gebruiken om een actie te starten of een toestand van je robot te kiezen.</p>
            <img src="img/knoppen.png" alt="De vijf knoppen van de socialrobotkit." title="Knoppen"></img>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Knopnamen</h3>
            <p class="info_item_content">De richtingsknoppen heten <code>SW_N</code>, <code>SW_S</code>, <code>SW_E</code> en <code>SW_W</code>. De middelste knop heet <code>SW_MIDDLE</code>. Het testprogramma kiest <code>SW_E</code>, de oostknop, en configureert die als <code>INPUT_PULLUP</code>.</p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">De testreactie</h3>
            <p class="info_item_content">Het programma leest de oostknop met <code>digitalRead(BUTTON_PIN_SW_E)</code>. Wanneer de voorwaarde voor de knop wordt bereikt en de sonar geen voorwerp dichtbij ziet, brandt RGB-led 1 groen.</p>
        </div>
    </div>
</div>