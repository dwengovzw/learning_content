---
hruid: org_dwengo_gripit_knoppen
version: 1
language: nl
title: "Knoppen"
description: "Gebruik de knoppen van de Halberd als invoer."
keywords: ["fiche", "gripit", "halberd", "knop", "invoer", "schakelaar"]
educational_goals: [{source: Source, id: id}]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16, 17, 18]
difficulty: 1
estimated_time: 10
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

<div class="dwengo_content fiche">
    <h1 class="title">Knoppen</h1>
    <h2 class="subtitle">Gebruik een knop als invoer</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">Een externe knop aansluiten</h3>
            <p class="info_item_content">De Halberd heeft geen ingebouwde knoppen. Gebruik daarom een externe knopmodule. Die geeft je programma een eenvoudige invoer: ingedrukt of niet ingedrukt.</p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Bedrading</h3>
            <p class="info_item_content">Een knopmodule heeft meestal de aansluitingen VCC, GND en DO (digital output). Sluit DO aan op een vrije digitale pin. In dit voorbeeld gebruiken we D2.</p>
            <div class="dwengo_content table_container"><table><tr><th>Knopmodule</th><th>Halberd</th></tr><tr><td>VCC</td><td>3.3V of 5V, volgens de module</td></tr><tr><td>GND</td><td>GND</td></tr><tr><td>DO</td><td>D2</td></tr></table></div>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">De testreactie</h3>
            <p class="info_item_content">Het programma leest de digitale uitgang van de module met <code>digitalRead()</code>. Afhankelijk van de knopmodule is de waarde bij indrukken HIGH of LOW. Controleer dit met het testprogramma en pas de voorwaarde aan wanneer nodig.</p>
        </div>
    </div>
    <div class="example_item item">
        <h3 class="example_item_title">Test een externe knopmodule</h3>
        <div class="dwengo-content dwengo-code-simulator"><pre><code class="language-cpp" data-filename="button_module_test.cpp">
#include &lt;Dwenguino.h&gt;

#define BUTTON_PIN D2

void setup() {
    initDwenguino();
    pinMode(BUTTON_PIN, INPUT_PULLUP);
    pinMode(RGB_1_G, OUTPUT);
}

void loop() {
    if (digitalRead(BUTTON_PIN) == LOW) {
        digitalWrite(RGB_1_G, HIGH);
    } else {
        digitalWrite(RGB_1_G, LOW);
    }
}
</code></pre></div>
    </div>
</div>