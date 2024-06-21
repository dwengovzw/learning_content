---
hruid: leerlijn_basis_programmeren_selectie
version: 1
language: nl
title: "Selectie (if-then-else)"
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
estimated_time: 15
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Selectie (if-then-else)

Met een selectie kunnen we "selecteren" welke code er uitgevoerd zal worden. Deze keuze gebeurt op basis van een voorwaarde of conditie. Als de conditie waar is, voeren we de ene code uit, als die vals is, de andere. Hieronder zie je een voorbeeld van een selectie.

```arduino
if (digitalRead(SW_S) == LOW){
    // Voer deze code uit als de waarde van de pin SW_S laag is 
    // (= de zuid knop is ingedrukt).
} else {
    // Voer deze code uit als de waarde van de pin SW_S hoog is 
    // (= de zuid knop is niet ingedrukt).
}
```


<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
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
        // Vul hier aan.
        delay(50);
    }
</code>
        </pre> 
        </div>
    </div>
</div>

<div class="dwengo-content sideinfo">
    <h2 class="title">Wist je dat!</h2>
    <div class="content">
        Merk op dat in de setup functie de lijn <code class="language-cpp">pinMode(SW_S, INPUT_PULLUP);</code> staat. Dit zorgt ervoor dat de pull-up weerstand van de pin SW_S automatisch ingeschakeld wordt. Weet jij nog hoe de schakeling van een pull-up weerstand eruitziet?
    </div>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Verander in je oplossing voor de vorige opdracht de lijn:
        <pre>
            <code class="language-cpp">
                pinMode(SW_S, INPUT_PULLUP);
            </code>
        </pre>
        in 
        <pre>
            <code class="language-cpp">
                pinMode(SW_S, INPUT);
            </code>
        </pre>
        Test je programma uit. Wat is het effect? Wat is de verklaring voor wat je ziet?
    </div>
</div>