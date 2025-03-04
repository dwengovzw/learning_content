---
hruid: org-dwengo-pc-luchtkwaliteit-iot-sensor
version: 1
language: nl
title: "IoT sensor"
description: "Hoe kan ik de luchtkwaliteit meten?"
keywords: ["dwenguino", "microcontroller", "wifi", "i2c", "webserver", "internet", "co2", "luchtkwaliteit"]
content_type: "text/markdown"
estimated_time: 45
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-digitale-competenties-en-mediawijsheid',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-algebra-analyse',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-redeneren',

]
copyright: "CC BY dwengo"
target_ages: [16, 17, 18]
teacher_exclusive: False
---

# IoT sensor

Om data gemakkelijk vanop afstand te kunnen opvragen en te visualiseren op onze computer, kunnen we de Dwenguino verbinden met het internet. Zo wordt het een internet of things (IoT) apparaat. 

Alle details over hoe je de Dwenguino kan instellen als webserver kan je vinden in het leerpad over [wifi communicatie](https://www.dwengo.org/learning-path.html?hruid=pc_leerlijn_wifi&language=nl&te=true&source_page=%2Fphysical_computing%2F&source_title=%20Physical%20computing#org-dwengo-pc-wifi-intro;nl;1).

<div class="dwengo-content assignment">
<h2 class="title">Opdracht</h2>
<div class="content">
Gebruik de informatie uit het wifi leerpad om de Dwenguino in te stellen als web server. Voeg een <strong>route</strong> <em>luchtkwaliteit</em> met een <strong>handler</strong> waarin een meting van de luchtkwaliteit gedaan wordt (CO2, temperatuur, luchtvochtigheid, AQI en TOVC). Geeft deze waarden terug in csv formaat.
</div>
</div>

