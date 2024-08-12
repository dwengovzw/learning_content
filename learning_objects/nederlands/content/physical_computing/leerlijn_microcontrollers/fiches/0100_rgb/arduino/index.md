---
hruid: leerlijn_fiches_arduino_rgb
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
                    <tr><td>R</td><td>De digitale pin die instaat voor de intensiteit van het rode licht.</td></tr>
                    <tr><td>G</td><td>De digitale pin die instaat voor de intensiteit van het groene licht.</td></tr>
                    <tr><td>B</td><td>De digitale pin die instaat voor de intensiteit van het blauwe licht.</td></tr>
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
        <div class="example_item item">
            <h3 class="example_item_title">Voorbeeld: het RGB-led in een kleur naar keuze doen branden.</h3>
            <p class="example_item_content">
<pre>
<code class="language-cpp">
    
    const int PIN_RED   = 5;
    const int PIN_GREEN = 6;
    const int PIN_BLUE  = 9;

    void setup() {
        pinMode(PIN_RED,   OUTPUT);
        pinMode(PIN_GREEN, OUTPUT);
        pinMode(PIN_BLUE,  OUTPUT);
    }

    void loop() {
        // color code #00C9CC (R = 0,   G = 201, B = 204)
        analogWrite(PIN_RED,   0);
        analogWrite(PIN_GREEN, 201);
        analogWrite(PIN_BLUE,  204);

        delay(1000); // keep the color 1 second

        // color code #F7788A (R = 247, G = 120, B = 138)
        analogWrite(PIN_RED,   247);
        analogWrite(PIN_GREEN, 120);
        analogWrite(PIN_BLUE,  138);

        delay(1000); // keep the color 1 second

        // color code #34A853 (R = 52,  G = 168, B = 83)
        analogWrite(PIN_RED,   52);
        analogWrite(PIN_GREEN, 168);
        analogWrite(PIN_BLUE,  83);

        delay(1000); // keep the color 1 second
    }
</code>
</pre> 
            </p>
        </div>
    </div>
</div>



