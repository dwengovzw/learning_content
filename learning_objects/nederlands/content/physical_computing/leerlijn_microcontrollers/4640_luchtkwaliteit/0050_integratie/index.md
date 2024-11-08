---
hruid: org-dwengo-pc-luchtkwaliteit-integratie
version: 1
language: nl
title: "Integratie"
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

# Integratie

Als volgende stap combineren we de gegevens die we lezen van SCD40 en de ENS160 zodat we in de seriëlen monitor een lijn te zien krijgen per meting.

<div class="dwengo-content assignment">
<h2 class="title">Opdracht</h2>
<div class="content">
<p>Integreer de code voor de meting van de SCD40 en de ENS160 in één programma. Zorg ervoor dat je, telkens je een meting doet, de resultaten in csv formaat doorstuurd via seriële communicatie. Hieronder zie je een voorbeeld van hoe die csv data eruit kan zien.</p>

<pre>
<code class="lang-csv">
CO2 (ppm);Temp (°C);Vocht (%);TVOC (ppb);AQI
488;20;62;21;1
488;20;62;21;1
488;20;62;21;1
</code>
</pre>

<p>Probeer de code zo duidelijk mogelijk op te splitsen in functies met eigen verantwoordelijkheden.</p>

</div>
</div>

<div class="dwengo-content sideinfo">
<h2 class="title">ppm en ppb</h2>
<div class="content">
De eenheden ppm en ppb staan respectievelijk voor <strong>parts per million</strong> en <strong>parts per billion</strong> ofwel deeltjes per miljoen en deeltjes per miljard. Omdat we hier met gassen werken, bekijken we dit per volume. Als er bijvoorbeeld 1ppm ethanol in de lucht zit, wil dat zeggen dat per 1000000 liter lucht, 1 liter ethanol zal voorkomen.
</div>
</div>