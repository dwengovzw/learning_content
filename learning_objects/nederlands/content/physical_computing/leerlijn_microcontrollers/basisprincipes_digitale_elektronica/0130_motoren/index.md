---
hruid: leerlijn_basisprincipes_motoren
version: 1
language: nl
title: "Motoren"
description: "Er zijn verschillende soorten motoren die je kan aansturen met de microcontroller, hier krijg je een overzicht."
keywords: ["digitale elektronica", "motoren", "basisprincipes", "microcontroller", "µC", "arduino", "dwenguino"]
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

# Motoren

Er bestaan verschillende soorten motoren die je kan aansturen aan de hand van de µC. Enkele voorbeelden zijn: brushed DC-motoren, servomotoren, stappenmotoren  en brushless DC-motoren. Hieronder zie je een voorbeeld van elk van deze motoren en waarvoor je ze kan gebruiken.


| Component | Beschrijving | Aansturen |
| --------- | ------------ | --------- |
| TODO: afbeelding | Brushed DC motoren zijn eenvoudige motoren die werken op gelijkstroom. Ze maken gebruik van koolstof “borstels” die langs de rotor slepen. Op die manier brengen ze de stroom over naar de rotor. | DC-motoren zijn eenvoudig aan te sturen. Ze hebben maar twee draden. De spanning over deze draden bepaalt hoe snel de motor draait. Hoe hoger de spanning hoe sneller de rotatie. |
| TODO: afbeelding | Brushless DC motoren hebben, zoals de naam al aangeeft, geen koolstofborstels. Dergelijke motoren bestaan uit een interne rotor met permanente magneten en een omhulsel (stator) met elektromagneten. Het magnetisch veld van deze elektromagneten wordt bepaald door het elektrisch signaal dat je naar de motor stuurt.  | Omdat de elektromagneten in de stator de juiste signalen moeten krijgen, is het aansturen een stuk complexer dan de brushed DC-motor. Daarom wordt hier vaak gebruikgemaakt van een afzonderlijke controller. De µC stuurt dan een digitaal signaal naar de controller die aangeeft wat de snelheid van de motor moet zijn. De controller zet deze om naar de juiste signalen naar de windingen van de elektromagneten in de motor. |
| TODO: afbeelding | Een stappenmotor is een speciale vorm van de brushless DC-motor. De elektromagneten in de motor zijn zodanig geplaatst dat je de motor in kleine stappen van positie kan doen veranderen. De motor kan ook op een specifieke positie blijven staan. | De stappenmotor gebruikt net zoals de gewone brushless DC-motor een controller. De µC stuurt een signaal naar de controller met daarin het aantal stappen en de richting waarin de motor moet draaien. De controller zet dit om naar elektrische golven die naar de elektromagneten in de motor worden gestuurd. |
| TODO: afbeelding | Een servomotor maakt meestal gebruik van een brushed DC-motor. De servomotor voegt daar een sensor (encoder) aan toe waardoor de motor steeds weet in welke positie die staat. De servomotor bestaat dus eigenlijk uit meerdere componenten: (1) Een motor (meestal brushed DC). (2) Een sensor/encoder om te bepalen wat de positie van de motor is. (3) Een kleine µC die invoersignalen leest en deze omzet in bewegingen van de motor. | Omdat een servomotor al een eigen controller heeft, kan je die relatief eenvoudig aansturen met een µC. De motor heeft drie aansluitingen: Vcc, GND en data. Op de datalijn stuur je een PWM signaal. De tijd dat dit signaal hoog is bepaalt de hoek die de motor zal aannemen. |


<div class="dwengo-content important">
    <h2 class="title">Opgelet!</h2>
    <div class="content">
        <p>
        Sluit een motor nooit rechtstreeks aan op de pinnen van de µC! Gebruik daarvoor steeds de gepaste “driver”. Motoren gebruiken te veel stroom. Door ze rechtstreeks op een pin van de µC aan te sluiten kan je de schakelingen op de µC letterlijk doorbranden. Op het Dwenguino platform is er al een driver aanwezig waardoor je makkelijk motoren kan aansluiten. Op het Arduino platform is dit niet het geval. Bijgevolg moet je daar zelf de motor aansluiten.
        </p>
    </div>
</div>

