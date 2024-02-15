---
hruid: leerlijn_microcontrollers_seriele_monitor_data_ontvangen
version: 1
language: nl
title: "Gegevens ontvangen op de computer"
description: "Hoe stuur je gegevens over een seriële connectie vanop de Dwenguino?"
keywords: ["seriële communicatie", "seriële monitor", "dwenguino", "robot", "project", "µC", "pid", "controletheorie"]
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Gegevens ontvangen

Wanneer je Dwenguino geprogrammeerd is om gegevens te sturen via de seriële verbinding, kunnen we deze gegevens weergeven in de seriële monitor. Volg daarvoor de volgende stappen:

- Zorg ervoor dat de Dwenguino verbonden is met de computer via de usb-kabel.
- Druk onderaan in de seriële monitor op de **Connect**-knop.
- Je ziet het onderstaande venster verschijnen linksboven in de browser.

<img src="img/poort_selecteren.png" alt="Het venster met de verbonden apparaten waarin je de Dwenguino moet selecteren"></img>

- Selecteer de Dwenguino en druk op **Verbinding maken**.
- Als alles goed is, zie je nu getallen verschijnen in de seriële monitor.

<img src="img/ontvangen_data.png" alt="Voorbeeld van hoe de data in de seriële monitor eruitziet">

