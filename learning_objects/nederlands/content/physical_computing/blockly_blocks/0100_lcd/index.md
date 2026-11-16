---
hruid: blocks_lcd
version: 1
language: nl
title: "LCD"
description: "Beschrijving van LCD blok."
keywords: []
educational_goals: [
    {source: Source, id: id}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14, 15, 16, 17, 18]
difficulty: 1
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

<div class="dwengo_content fiche">
    <h1 class="title">LCD - Liquid Crystal Display</h1>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
                <img src="img/lcd_echt.png" alt="Het LCD dat op de Dwenguino te vinden is."></img>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">In de simulator</h3>
                <img src="img/lcd_sim.png" alt="Het LCD hoe het wordt voorgesteld in onze simulator."></img>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Programmeerblokken</h3>
                <img src="img/lcd_blocks.png" alt="DwenguinoBlockly blokken die te maken hebben met het LCD."></img>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                Een LCD kan tekst weergeven om bijvoorbeeld een boodschap mee te delen.<br>
                Op het scherm van de dwenguino passen maximaal 32 karakters, zoals letters of cijfers. Dit is verspreid over twee regels, dus je kan 16 karakters per regel tonen.<br><br>
                <b>Blok 1</b> maakt het LCD op de dwenguino leeg.<br>
                <b>Blok 2</b> kun je in combinatie met een 'tekst'-blok gebruiken om ergens op het scherm iets te printen.
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Voorbeeld</h3>
                <img src="img/lcd_vb.png" alt="DwenguinoBlockly voorbeeld."></img>
            <p class="info_item_content">
                Dit voorbeeld zorgt ervoor dat de tekst 'Hallo!' getoond wordt op de bovenste rij van het LCD en de tekst 'Welkom :)' op de onderste.
            </p>
        </div>
    </div>
</div>