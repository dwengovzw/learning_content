---
hruid: leerlijn_project_lijnvolger_telemetrie
version: 1
language: nl
title: "Telemetrie"
description: "Hoe stuur ik telemetrie van de robot naar de computer."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "bluetooth", "telemetrie"]
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

# Telemetrie

Voor we onze robot laten rijden, zorgen we ervoor dat we gegevens kunnen verzamelen over het gedrag van de robot. We zullen deze gegevens nodig hebben om fouten in het gedrag van de robot te debuggen. Omdat onze robot vrij moet kunnen rondrijden, zullen we deze data vanop afstand draadloos verzamelen. Deze techniek noemen we telemetrie ofwel het meten vanop afstand. De belangrijkste gegevens die we willen verzamelen zijn: de metingen van de sensoren, de snelheden van de motoren en het gedrag van de controlevariabelen. Je bent echter niet beperkt om enkel deze gegevens te verzamelen. Als je nog andere data wil meten, kan je de code gemakkelijk aanpassen om dat te doen.

In onze toepassing zullen we via Bluetooth gegevens over de robot versturen naar de computer. Op de computer lezen we deze gegevens en visualiseren ze in verschillende grafieken. Zo krijgen we inzicht in het gedrag van onze robot.

<div class="dwengo-content sideinfo">
<h2 class="title">Telemetrie</h2>
<div class="content">
Telemetrie is een zeer belangrijke techniek die ingenieurs heel vaak gebruiken. Denk bijvoorbeeld aan toepassingen waarbij het voor een mens onmogelijk is om in de buurt te blijven van het gemonitorde systeem. Bijvoorbeeld een satelliet of een onbemande duikboot. Ook in andere toepassingen is telemetrie nuttig. Bijvoorbeeld om de vitale functies van een patiënt in het ziekenhuis op te volgen. 
</div>
</div>