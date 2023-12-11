---
hruid: leerlijn_fiches_dwenguino_rgb
version: 1
language: nl
title: "RGB-led"
description: "De kleuren voor de RGB-led instellen"
keywords: ["rgb", "RGB-led", "fiche", "dwenguino"]
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
    <h1 class="title">RGB-led</h1>
    <h2 class="subtitle">Verschillende kleuren maken</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
            <p class="info_item_content">
                <img src="img/rgb.png" alt="Een afbeelding van de rgb-led." title="Een afbeelding van de rgb-led."></img>
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
                    <tr><td>R</td><td>...</td></tr>
                    <tr><td>G</td><td>...</td></tr>
                    <tr><td>B</td><td>...</td></tr>
                    <tr><td>GND</td><td>De referentiespanning of de grond, soms ook aangeduid met een -.</td></tr>
                </table>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                De RGB-led is een led waarvan je de kleur van het licht zelf kan bepalen door de intensiteit van rood, groen en blauw licht (de primaire kleuren) te programmeren. De intensiteit wordt doorgegeven als een getal tussen 0 en 255 (van lage tot hoge intensiteit). Houd er rekening mee dat niet alle kleuren even goed kunnen wordenweergegeven op de RGB-led via het RGB-kleurenmodel (bv. bruin).
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
            <h3 class="example_item_title">Voorbeeld: het RGB-led paars licht doen branden.</h3>
            <p class="example_item_content">
<pre>
<code class="language-arduino">
    
    #include <Wire.h>
    #include <Dwenguino.h>
    #include <LiquidCrystal.h>

    int red_value;
    int green_value;
    int blue_value;

    void setup(){
        initDwenguino();
    }

    void loop(){
        pinMode(11, OUTPUT);
        pinMode(14, OUTPUT);
        pinMode(15, OUTPUT);
        red_value = 148;
        green_value = 0;
        blue_value = 211;

        analogWrite(11, red_value);
        analogWrite(14, green_value);
        analogWrite(15, blue_value);   
    }
</code>
</pre> 
            </p>
        </div>
    </div>
</div>



