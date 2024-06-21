---
hruid: leerlijn_basis_programmeren_selectie_oplossing
version: 1
language: nl
title: "Selectie: if-then-else (oplossing)"
description: "Wat is selectie en hoe kan je het gebruiken."
keywords: ["programmeren", "if", "then", "else", "selectie", "microcontroller", "µC", "arduino", "dwenguino"]
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
teacher_exclusive: true
---

# Selectie: if-then-else (oplossing)


<div class="dwengo-content assignment">
    <h2 class="title">Oplossing</h2>
    <div class="content">
        Vul de code in de loop functie aan zodat led 13 gaat branden als je de zuid-knop indrukt en uitgaat wanneer je de knop loslaat. 
        <div class="dwengo-content dwengo-code-simulator">
        <pre>
<code class="language-cpp">

    #include <Dwenguino.h>

    void setup(){
        initDwenguino();
        pinMode(13, OUTPUT);
        pinMode(SW_S, INPUT_PULLUP);
    }

    void loop(){
        if (digitalRead(SW_S) == LOW){
            digitalWrite(13, HIGH);
        } else {
            digitalWrite(13, LOW);
        }
        delay(50);
    }
</code>
        </pre> 
        </div>
    </div>
</div>

## Pull-up weerstand
Zie leerpad over basisprincipes digitale elektronica: [De pull-up weerstand](@learning-object/leerlijn_invoer_basisprincipes_pull_up_weerstand/nl/1).


<div class="dwengo-content assignment">
    <h2 class="title">Oplossing</h2>
    <div class="content">
        Door de invoermodus <code class="language-cpp">INPUT_PULLUP</code> te gebruiken wordt de pull-up weerstand geactiveerd. Op die manier is de waarde op de pin, wanneer de knop niet wordt ingedrukt, altijd hoog. Wanneer je de knop indrukt wordt dan zal de waarde op de pin laag worden.
        Gebruiken we invoermodus <code class="language-cpp">INPUT</code> dan wordt de pull-up weerstand niet geactiveerd. Bijgevolg "zweeft" de waarde van de pin wanneer de knop niet wordt ingedrukt. Led 13 zal dus op willekeurige momenten aan- en uitgaan.
    </div>
</div>