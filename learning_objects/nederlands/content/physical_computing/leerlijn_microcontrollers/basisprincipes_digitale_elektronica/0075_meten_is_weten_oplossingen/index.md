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
    <h2 class="title">Opdracht 1</h2>
    <div class="content">
        <div>Je krijgt van de leerkracht de volgende schakeling:</div>
        <img src="img/diagram_01.svg" alt="Schakeling" title="Schakeling">
        <div>Gebruik de multimeter om de volgende vragen te beantwoorden.</div>
        <ul>
            <li>Meet de weerstandswaarde van R1.<br><em>Wij kozen voor een weerstand van 556 Ω.</em></li>
            <li>Bereken de stroom door het circuit wanneer we de punten a en b met elkaar verbinden.<br><em>Voor die weerstand krijg je een stroom van 8.992 mA.</em></li>
            <li>Controleer de stroom door deze te meten met de multimeter.<br><em>Deze waarde moeten ze meten maar zou dicht bij de berekende waarde moeten liggen.</em></li>
            <li>Wat is de afwijking die je bekomt?<br><em>Dit bepalen ze op basis van de meting.</em></li>
        </ul>
    </div>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 2</h2>
    <div class="content">
        <div>Je krijgt van de leerkracht de volgende schakeling:</div>
        <img src="img/diagram_02.svg"></img>
        <div>Gebruik de multimeter om de volgende vragen te beantwoorden.</div>
        <ul>
            <li>Wat is de weerstandswaarde van R1?<br><em>Wij kozen voor een weerstand van 1 MΩ.</em></li>
            <li>Wat is de spanning over de weerstand R1?<br><em>5 V</em></li>
            <li>Bereken de stroom die door R1 loopt?<br><em>5 µA</em></li>
        </ul>
    </div>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 3</h2>
    <div class="content">
        <div>Je krijgt van de leerkracht de volgende schakeling:</div>
        <img src="img/diagram_03.svg"></img>
        <div>Gebruik de multimeter om de volgende vragen te beantwoorden.</div>
        <ul>
            <li>Meet de weerstand van R1 en R2. Wat merk je op?<br><em>Hier kiezen we voor de weerstand van R1 een veelvoud van de weerstand van R2. Bv. \(R1 = 2 * R2\), \(R1 = R2\) of \(R1 = 10 * R2\)</em></li>
            <li>Meet de spanning tussen de punten a en b, en tussen de punten b en c. Wat merk je op?<br><em>Hier zouden de leerlingen moeten opmerken dat de verhoudig tussen de spanningen gelijk is aan de verhoudingen tussen de weerstandswaarden.</em></li>
            <li>Meet de weerstand en spanning tussen a en c. Wat merk je op?<br><em>In dit geval 5 V. Ze zouden moeten zien dat dit de som is van de spanningen over de verschillende componenten.</em></li>
        </ul>
    </div>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 4</h2>
    <div class="content">
        <div>Je krijgt van de leerkracht de volgende schakeling:</div>
        <img src="img/diagram_04.svg"></img>
        <div>Gebruik de multimeter om de volgende vragen te beantwoorden.</div>
        <ul>
            <li>Meet de weerstand van R1 en R2.<br><em>Hier kiezen we voor de weerstand van R1 een veelvoud van de weerstand van R2. Bv. \(R1 = 2 * R2\), \(R1 = R2\) of \(R1 = 10 * R2\)</em></li>
            <li>Meet de spanning tussen a en b.<br><em>5 V</em></li>
            <li>Bereken de stroom door het punt c.<br><em>\(\frac{5V}{R1}\)</em></li>
            <li>Bereken de stroom door het punt d.<br><em>\(\frac{5V}{R2}\)</em></li>
        </ul>
    </div>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 5</h2>
    <div class="content">
        <div>Je krijgt van de leerkracht de volgende schakeling:</div>
        <img src="img/diagram_05.svg"></img>
        <div>Gebruik de multimeter om de volgende vragen te beantwoorden.</div>
        <ul>
            <li>Meet de weerstand van R1, R2, R3 en R4.<br><em>R1 = 220 Ω, R2 = 550 Ω, R3 = 220 Ω, R4 = 1 KΩ</em></li>
            <li>Meet de spanning tussen de punten a en b, b en c, c en d, d en e.<br><em>U1 ≈ 0.55 V, U2 ≈ 1.38V, U3 ≈ 0.55V, U4 ≈ 2.51V</em></li>
            <li>Wat merk je als je de weerstanden en spanningen van/over een weerstand met elkaar vergelijkt?<br><em>De spanningen verouden zich op dezelfde manier tot elkaar als de weerstanden.</em></li>
        </ul>
    </div>
</div>

