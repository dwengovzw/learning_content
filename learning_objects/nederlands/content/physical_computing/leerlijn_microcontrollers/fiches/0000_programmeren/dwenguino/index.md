---
hruid: leerlijn_fiches_dwenguino_programmeren
version: 1
language: nl
title: "Code uploaden"
description: "Hoe zet ik code vanop mijn computer over naar de Dwenguino?"
keywords: ["upload", "uploaden", "fiche", "dwenguino", "programmeren"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [10, 11, 12, 13, 14, 15, 16, 17, 18]
difficulty: 1
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

<div class="dwengo_content fiche">
    <h1 class="title">Code uploaden</h1>
    <h2 class="subtitle">Hoe zet ik code vanop mijn computer over naar de Dwenguino?</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">1. De binaire code downloaden.</h3>
            <p class="info_item_content">
                Download het programma uit de simulator met de knop uit het hoofdmenu: <img src="img/compile_button.png" alt="Dwenguino compile button." title="Dwenguino compile button."></img>. Het programma komt automatisch in de ‘Downloads’-map met bestandsnaam “program.dw”. Het dw-bestand bevat de binaire code van je programma. Het is de vertaling van je programma naar een taal die de Dwenguino begrijpt. Voor meer uitleg hierover kan je het online leerpad op de Dwengo website raadplegen. 
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">2. USB kabel aansluiten.</h3>
            <p class="info_item_content">
                Verbind de computer met de Dwenguino door middel van de meegeleverde USB-kabel.
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">3. Zet Dwenguino in programmeermodus.</h3>
            <p class="info_item_content">
                Druk de ‘zuid’-knop van de Dwenguino in en houd de knop ingedrukt. 
                Druk vervolgens de ‘reset’-knop van de Dwenguino in.
                Los dan eerst de ‘reset’-knop. 
                Los daarna de ‘zuid’-knop. Op het lcd-scherm verschijnt de boodschap “Zet bestand over”.  
            </p>
            <p class="info_item_content">
                <div class="iframe-container iframe-16-9">
                    <iframe allowfullscreen="" src="https://youtu.be/VpAXLlT_JP0?si=ZZ7A1UwEE0-hPWsu" height="315px" width="420px"></iframe>
                </div>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                Leds bestaan in verschillende kleuren. De ingebouwde leds op de Dwenguino kan je rood laten oplichten. Door de pin waarmee de LED verbonden is op hoog te zetten, gaat de LED branden. Merk op dat wanneer je een LED aansluit op een pin van de µC (5V), je steeds een weerstand van ongeveer 400 Ohm in serie moet schakelen met de LED. De exacte waarde van de weerstand hangt af van het type LED die je gebruikt. Voor de LEDs op het Dwenguino bord is al een weerstand van 470 Ohm voorzien. Vind je die terug op het bord?
            </p>
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
            <h3 class="example_item_title">Voorbeeld: led 13 laten knipperen</h3>
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



