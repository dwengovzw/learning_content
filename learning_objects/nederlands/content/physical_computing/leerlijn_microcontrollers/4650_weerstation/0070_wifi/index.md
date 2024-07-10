---
hruid: leerlijn_uc_introductie_weerstation_wifi
version: 1
language: nl
title: "Uitbreiding: wifi"
description: "Wat is een weerstation"
keywords: ["Microcontroller", "µC", "weerstation", "dht", "temperatuur", "luchtvochtigheid", "sd", "rtc", "wifi"]
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
estimated_time: 3
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Uitbreiding: data opvragen via wifi

We hebben nu alles wat we nodig hebben om gegevens over het lokaal microklimaat te verzamelen. Toch kan het handig zijn om een live overzicht te hebben van de metingen zonder dat we de SD kaart uit ons systeem moeten halen. Dat kunnen we doen door een wifi module toe te voegen aan ons systeem en de Dwenguino te programmeren als webserver. Bekijk het [wifi leerpad](https://www.dwengo.org/learning-path.html?hruid=pc_leerlijn_wifi&language=nl&te=true&source_page=%2Fphysical_computing%2F&source_title=%20Physical%20computing#org-dwengo-pc-wifi-intro;nl;1) om te weten te komen hoe je dat kan doen.

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht: wifi</h2>
    <div class="content">
        Voeg een wifi module toe aan je systeem en programmer de Dwenguino als webserver zodat je over het internet gegevens kan opvragen. Stuur de gegevens door in csv formaat.
    </div>
</div>