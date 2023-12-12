---
hruid: leerlijn_fiches_dwenguino_servo1
version: 1
language: nl
title: "180° servomotor"
description: "Hoe werkt de 180° servomotor?"
keywords: ["servomotor", "blauw", "fiche", "dwenguino"]
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
estimated_time: 15
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

<div class="dwengo_content fiche">
    <h1 class="title">WIP - 180° servomotor</h1>
    <h2 class="subtitle">Rotaties uitvoeren</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
            <p class="info_item_content">
                <img src="img/servos.png" alt="Een afbeelding van de servomotoren." title="Een afbeelding van de servomotoren."></img>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Type</h3>
            <p class="info_item_content">
                Uitvoer, digitale actuator 
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Pinnen</h3>
            <p class="info_item_content">
                <table>
                    <tr><td>GND</td><td>De referentiespanning of de grond, soms ook aangeduid met een -.</td></tr>
                    <tr><td>VCC</td><td>De 5 V-voeding, soms ook aangeduid met een +.</td></tr>
                    <tr><td>PIN</td><td>...</td></tr>
                </table>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                Je beschikt over 2 soorten:<br>
                <br>
                - *De blauwe servomotor*: Deze servomotor kan slechts 180 graden draaien. Je kan deze m.a.w. gebruiken om een halve draaibeweging uit te voeren.
                - *De zwarte servomotor*: Deze servomotor kan 360 graden draaien. Deze gebruik je bijvoorbeeld om iets constant te laten draaien.<br>
                <br>
                Het voordeel van de blauwe servomotor t.o.v. de zwarte servomotor is dat je de positie (de draaihoek) exact kunt bepalen. Hij is dus beter voor precieze bewegingen. Het nadeel is dan weer dat het wat ingewikkelder is om deze te programmeren
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Symbool</h3>
            <p class="info_item_content">
                <img src="img/icon.svg" title="LED symbool">
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Aansluiting</h3>
            <p class="info_item_content">
                <img src="img/connection.svg" title="LED aansluiting" >
            </p>
        </div>
        <div class="example_item item">
            <h3 class="example_item_title">Voorbeeld: 2 servomotoren bewegen herhaaldelijk op en neer zoals armen die zwaaien.</h3>
            <p class="example_item_content">
<pre>
<code class="language-arduino">
    
    #include <Wire.h>
    #include <Dwenguino.h>
    #include <LiquidCrystal.h>
    #include <Servo.h>

    Servo servoOnPin19;
    Servo servoOnPin18;

    void setup(){
        initDwenguino();
    }

    void loop(){
        servoOnPin19.attach(19);
        servoOnPin19.write(0);
        servoOnPin18.attach(18);
        servoOnPin18.write(0);
        delay(1000);
        servoOnPin19.attach(19);
        servoOnPin19.write(180);
        servoOnPin18.attach(18);
        servoOnPin18.write(180);
        delay(1000);
    }
</code>
</pre> 
            </p>
        </div>
    </div>
</div>



