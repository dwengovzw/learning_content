---
hruid: leerlijn_fiches_arduino_led
version: 1
language: nl
title: "Leds"
description: "De leds op het bordje aansteken"
keywords: ["led", "fiche", "arduino"]
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
    <h1 class="title">Led</h1>
    <h2 class="subtitle">Leds laten branden</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
            <p class="info_item_content">
                <img src="img/leds.png" alt="Een afbeelding van de leds." title="Een afbeelding van de leds."></img>
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
               Op een arduino-bord vind je meestal een led terug.<br>
               <br>
               Hieronder vind je een simpel voorbeeld om deze led te laten branden.
            </p>
        </div>
        <div class="example_item item">
            <h3 class="example_item_title">Voorbeeld: led laten branden.</h3>
            <p class="example_item_content">
<pre>
<code class="language-arduino">
    
void setup() {
  // put your setup code here, to run once:
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
    delay(1000);                      // wait for a second
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
    delay(1000);                      // wait for a second
}

</code>
</pre> 
            </p>
        </div>
    </div>
</div>



