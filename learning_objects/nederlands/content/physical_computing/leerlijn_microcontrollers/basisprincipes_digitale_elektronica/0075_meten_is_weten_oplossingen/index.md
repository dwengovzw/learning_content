---
hruid: leerlijn_invoer_basisprincipes_meten_is_weten_oefeningen_oplossingen
version: 1
language: nl
title: "Meten is weten: oplossingen!"
description: "Oefen op het meten van spanning, stroom en weerstand?"
keywords: ["spanning", "stroom", "weerstand", "multimeter", "meten", "basisprincipes", "microcontroller", "µC", "arduino", "dwenguino", "oefening"]
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
teacher_exclusive: true
---

# Meten is weten (oplossingen)

Hieronder vind je een aantal mogelijke oplossingen. Deze zijn afhankelijk van de weerstandwaarden die je kiest. Als leerkracht kan je de vragen makkelijk aanpassen naar andere weerstandswaarden.

<div class="dwengo-content assignment">
<h2>Opdracht 1</h2>
<p>
    <div>Je krijgt van de leerkracht de volgende schakeling:</div>
    <img src="img/diagram_01.svg"></img>
</p>
<p>
    Gebruik de multimeter om de volgende vragen te beantwoorden.
    <ul>
        <li>Meet de weerstandswaarde van R1.</li>
        <li><em>Wij kozen voor een weerstand van 556 Ω.</em></li>
        <li>Bereken de stroom voor een VCC van 5V.</li>
        <li><em>Voor die weerstand krijg je een stroom van 8.992 mA.</em></li>
        <li>Controleer de stroom door deze te meten met de multimeter.</li>
        <li><em>Deze waarde moeten ze meten maar zou dicht bij de berekende waarde moeten liggen.</em></li>
        <li>Wat is de afwijking die je bekomt?</li>
        <li><em>Dit bepalen ze op basis van de meting.</em></li>
    </ul>
</p>
</div>

<div class="dwengo-content assignment">
<h2>Opdracht 2</h2>
<p>
    <div>Je krijgt van de leerkracht de volgende schakeling:</div>
    <img src="img/diagram_02.svg"></img>
</p>
<p>
    Gebruik de multimeter om de volgende vragen te beantwoorden.
    <ul>
        <li>Wat is de weerstandswaarde van R1?</li>
        <li><em>Wij kozen voor een weerstand van 1 MΩ.</em></li>
        <li>Wat is de spanning over de weerstand R1?</li>
        <li><em>5 V</em></li>
        <li>Bereken de stroom die door R1 loopt?</li>
        <li><em>5 µA</em></li>
    </ul>
</p>
</div>

<div class="dwengo-content assignment">
<h2>Opdracht 3</h2>
<p>
    <div>Je krijgt van de leerkracht de volgende schakeling:</div>
    <img src="img/diagram_03.svg"></img>
</p>
<p>
    Gebruik de multimeter om de volgende vragen te beantwoorden.
    <ul>
        <li>Meet de weerstand van R1 en R2. Wat merk je op?</li>
        <li><em>Hier kiezen we voor de weerstand van R1 een veelvoud van de weerstand van R2. Bv. \\(R1 = 2 * R2\\), \\(R1 = R2\\) of \\(R1 = 10 * R2\\)</em></li>
        <li>Meet de spanning tussen de punten a en b, en tussen de punten b en c. Wat merk je op?</li>
        <li><em>Hier zouden de leerlingen moeten opmerken dat de verhoudig tussen de spanningen gelijk is aan de verhoudingen tussen de weerstandswaarden.</em></li>
        <li>Meet de weerstand en spanning tussen a en c. Wat merk je op?</li>
        <li><em>In dit geval 5 V. Ze zouden moeten zien dat dit de som is van de spanningen over de verschillende componenten.</em></li>
    </ul>
</p>
</div>

<div class="dwengo-content assignment">
<h2>Opdracht 4</h2>
<p>
    <div>Je krijgt van de leerkracht de volgende schakeling:</div>
    <img src="img/diagram_04.svg"></img>
</p>
<p>
    Gebruik de multimeter om de volgende vragen te beantwoorden.
    <ul>
        <li>Meet de weerstand van R1 en R2.</li>
        <li><em>Hier kiezen we voor de weerstand van R1 een veelvoud van de weerstand van R2. Bv. \\(R1 = 2 * R2\\), \\(R1 = R2\\) of \\(R1 = 10 * R2\\)</em></li>
        <li>Meet de spanning tussen a en b.</li>
        <li><em>5 V</em></li>
        <li>Bereken de stroom door het punt c.</li>
        <li><em>\\(\frac{5V}{R1}\\)</em></li>
        <li>Bereken de stroom door het punt d.</li>
        <li><em>\\(\frac{5V}{R2}\\)</em></li>
    </ul>
</p>
</div>

<div class="dwengo-content assignment">
<h2>Opdracht 5</h2>
<p>
    <div>Je krijgt van de leerkracht de volgende schakeling:</div>
    <img src="img/diagram_05.svg"></img>
</p>
<p>
    Gebruik de multimeter om de volgende vragen te beantwoorden.
    <ul>
        <li>Meet de weerstand van R1, R2, R3 en R4.</li>
        <li><em>R1 = 220 Ω, R2 = 550 Ω, R3 = 220 Ω, R4 = 1 KΩ</em></li>
        <li>Meet de spanning tussen de punten a en b, b en c, c en d, d en e.</li>
        <li><em>V1 ≈ 0.55 V, V2 ≈ 1.38V, V3 ≈ 0.55V, V4 ≈ 2.51V</em></li>
        <li>Wat merk je als je de weerstanden en spanningen van/over een weerstand met elkaar vergelijkt?</li>
        <li><em>De spanningen verouden zich op dezelfde manier tot elkaar als de weerstanden.</em></li>
    </ul>
</p>
</div>



