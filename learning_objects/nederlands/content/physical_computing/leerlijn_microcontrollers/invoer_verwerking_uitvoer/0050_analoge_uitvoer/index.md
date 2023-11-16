---
hruid: leerlijn_invoer_verwerking_uitvoer_analoge_uitvoer
version: 1
language: nl
title: "Analoge uitvoer"
description: "Leer hoe je een analoge schrijft naar van een pin van de µC."
keywords: ["invoer", "verwerking", "uitvoer", "microcontroller", "µC", "arduino", "dwenguino", "analogWrite"]
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
estimated_time: 20
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Analoge uitvoer

De µC kan eigenlijk geen analoge uitvoer genereren. Om dat in bepaalde situaties te "simuleren" kan je gebruik maken van een PWM signaal. PWM staat voor **Pulse Width Modulation** ofwel **pulsbreedtemodulatie**. De microcontroller zal pulsen uitsturen. Een puls bestaat uit een tijdsinterval waarin het uitgestuurde signaal 1 (5V) is en een interval waarin het uitgestuurde signaal 0 is (0V). Door de lengte van deze twee intervallen te variëren, kan je de verhouding tussen de tijd dat het signaal hoog is en de tijd dat het signaal laag is veranderen. Als je dat heel snel doet dan krijg je een uitgemiddeld signaal tussen de 0V en 5V.

<table>
    <tr>
        <td><img src="img/diagram.svg" alt="Diagram PWM signaal." title="Diagram PWM signaal." style="width: 80%"></td>
    </tr>
    <tr>
        <td>In deze grafiek zien we hoe we aan de hand van een PWM signaal een analoge waarde kunnen benaderen. De oranje lijn geeft de spanning weer die in de tijd varieert volgens de functie sin(t). Om deze te benaderen passen we de breedte van de pulsen aan zodat de gemiddelde waarde van het blauwe PWM signaal overeenkomt met de waarde van sin(t). Wanneer sin(t) hoog is, zullen de pulsen lang hoog blijven (en dus breder zijn). Wanneer de waarde van sin(t) laag is, zullen de pulsen maar heel kort hoog blijven (en dus smaller zijn). Vandaar de naam <strong>pulsbreedtemodulatie<strong>.</td>
    </tr>
</table>

<h2>Opdracht</h2>
<p>
Probeer LED 13 op de microcontroller te dimmen 50% door er een PWM signaal naar te sturen. Dat PWM signaal is de helft van de tijd 1 en de andere helft 0.
</p>
</div>

<div class="dwengo-content sideinfo">
    <h2 class="title">Goed om te weten!</h2>
    <div class="content">
        <p>
        Er bestaan een functie die voor jou een PWM signaal zal genereren (<code class="language-cpp">analogWrite(pin)</code>). Deze functie kan je enkel gebruiken wanneer een pin specifieke hardware heeft om een PWM signaal te genereren. Op elke pin van de µC kan je echter zelf een PWM-signaal genereren door zelf de pin hoog en laag te zetten op de juiste momenten.
        </p>
    </div>
</div>