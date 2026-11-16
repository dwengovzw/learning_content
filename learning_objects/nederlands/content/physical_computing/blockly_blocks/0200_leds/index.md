---
hruid: blocks_leds
version: 1
language: nl
title: "LEDs"
description: "Beschrijving van LED blok."
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
    <h1 class="title">LED - Light-Emitting Diode</h1>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
                <img src="img/led_echt.jpg" alt="De LEDs die op de Dwenguino te vinden zijn."></img>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">In de simulator</h3>
                <img src="img/led_sim.png" alt="De LEDs hoe ze worden voorgesteld in onze simulator."></img>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Programmeerblokken</h3>
                <img src="img/led_blocks.png" alt="DwenguinoBlockly blokken die te maken hebben met de LEDs."></img>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                LEDs zijn lampjes die je aan en uit kan zetten.<br>
                De dwenguino heeft 9 ingebouwde rode LEDs die je kunt gebruiken. LD0 tot en met LD7 staan op één rij en kun je gezamelijk aansturen, LD13 staat afzonderlijk in de linkerbovenhoed van het bordje.<br><br>
                <b>Blok 1</b> kun je gebruiken om één specifieke LED aan of uit te zetten.<br>
                Met <b>blok 2</b> kun je meteen een volledig patroon meegeven aan de onderste rij van LEDs. Een '1' betekent dat de LED zal branden, bij een '0' niet.
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Voorbeeld</h3>
                <img src="img/led_vb.png" alt="DwenguinoBlockly voorbeeld."></img>
            <p class="info_item_content">
                Dit voorbeeld zet alle LEDs aan, laat ze één seconde branden en zet ze dan weer allemaal uit.
            </p>
        </div>
    </div>
</div>