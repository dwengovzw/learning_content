---
hruid: leerlijn_fiches_arduino_zoemer
version: 1
language: nl
title: "Zoemer"
description: "De zoemer laten zoemen"
keywords: ["buzzer", "zoemer", "fiche", "arduino"]
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
    <h1 class="title">Zoemer</h1>
    <h2 class="subtitle">Tonen afspelen</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
            <p class="info_item_content">
                <img src="img/zoemer.png" alt="Een afbeelding van de zoemer." title="Een afbeelding van de zoemer."></img>
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
                N.v.t.
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                Met een zoemer of buzzer kan je geluiden afspelen. <br>
                <br>
                Geluid is een golf van luchtdruk veroorzaakt door een trillend object zoals bijvoorbeeld een instrument of luidspreker. De hoeveelheid trillingen per seconde (de frequentie) bepaalt de toonhoogte. Wanneer het aantal trillingen per seconde tussen de 20 en 20 000 ligt, dan kan je dit als mens horen. Voor trillingen per seconde gebruiken we de eenheid Hertz, afgekort Hz. De mens kan dus trillingen horen tussen de 20 Hz en 20 000 Hz.<br>
                <br>
            </p>
        </div>
        <div class="example_item item">
            <h3 class="example_item_title">Voorbeeld: een zoemer een toon herhaaldelijk laten afspelen.</h3>
            <p class="example_item_content">
<pre>
<code class="language-arduino">

const int buzzer = 9; //buzzer to arduino pin 9

void setup(){
  pinMode(buzzer, OUTPUT); // Set buzzer - pin 9 as an output
}

void loop(){
  tone(buzzer, 1000); // Send 1KHz sound signal...
  delay(1000);        // ...for 1 sec
  noTone(buzzer);     // Stop sound...
  delay(1000);        // ...for 1sec
}

</code>
</pre> 
            </p>
        </div>
    </div>
</div>



