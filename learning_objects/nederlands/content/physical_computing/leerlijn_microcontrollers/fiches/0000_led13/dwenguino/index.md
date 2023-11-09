---
hruid: leerlijn_fiches_dwenguino_led13
version: 1
language: nl
title: "LED13"
description: "Hoe kan ik LED 13 aansluiten en programmeren?"
keywords: ["LED", "LED13", "fiche", "dwenguino"]
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
teacher_exclusive: true
---

<div class="dwengo_content fiche">
    <h1 class="title">LED13</h1>
    <h2 class="subtitle">Het lampje waarmee je alles kan testen.</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
            <p class="info_item_content">
                <img src="img/dwenguino_topview_led13_small.png" alt="Dwenguino location led 13" title="The location of led 13 on the dwenguino"></img>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Type</h3>
            <p class="info_item_content">
                Uitvoer, actuator 
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Pinnen</h3>
            <p class="info_item_content">
                De naam van de LED geeft het al weg, deze is verbonden met <strong>pin 13</strong> van de microcontroller. 
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                Leds bestaan in verschillende kleuren. De ingebouwde leds op de Dwenguino kan je rood laten oplichten. Door de pin waarmee de LED verbonden is op hoog te zetten, gaat de LED branden. Merk op dat wanneer je een LED aansluit op een pin van de µC (5V), je steeds een weerstand van ongeveer 200 Ohm in serie moet schakelen met de LED. De exacte waarde van de weerstand hangt af van het type LED die je gebruikt. Voor de LEDs op het Dwenguino bord is al een weerstand voorzien. Vind je die terug op het bord?
            </p>
        </div>
        <div class="example_item item">
            <h3 class="example_item_title">Voorbeeld: led 13 laten branden</h3>
            <p class="example_item_content">
                <pre><code class="language-arduino">
#include &lt;Wire.h&gt;
#include &lt;Dwenguino.h&gt;
#include &lt;LiquidCrystal.h&gt;

void setup()
{
    initDwenguino();
    pinMode(13, OUTPUT);
    digitalWrite(13, HIGH);
}

void loop()
{

}
                </code></pre> 
            </p>
        </div>
        <div class="example_item item">
            <h3 class="example_item_title">Voorbeeld: lampje laten knipperen</h3>
            <p class="example_item_content">
                <pre><code class="language-arduino">
#include &lt;Wire.h&gt;
#include &lt;Dwenguino.h&gt;
#include &lt;LiquidCrystal.h&gt;

void setup()
{
    initDwenguino();
    pinMode(13, OUTPUT);

}

void loop()
{
    digitalWrite(13, HIGH);
    delay(1000);
    digitalWrite(13, LOW);
    delay(1000);

}
                </code></pre> 
            </p>
        </div>
    </div>
</div>



