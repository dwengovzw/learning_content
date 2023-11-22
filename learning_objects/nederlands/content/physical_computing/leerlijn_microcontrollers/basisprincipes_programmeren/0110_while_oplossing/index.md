---
hruid: leerlijn_basis_programmeren_lussen_while_oplossing
version: 1
language: nl
title: "Voorwaardelijke herhaling: while-lus (oplossing)"
description: "Wat is een while-lus en waarvoor wordt die gebruikt."
keywords: ["programmeren", "while", "lus", "herhaling", "microcontroller", "µC", "arduino", "dwenguino"]
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

# Voorwaardelijke herhaling: while-lus (oplossing)

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Schrijf een programma die bij het starten niets doet tot je een knop indrukt. Vanaf het moment dat de knop wordt ingedrukt, begint led 13 te knipperen met een frequentie van 1 Hz (= 1 keer per seconde).
    </div>
    <div class="dwengo-content dwengo-code-simulator">
        <pre>
<code class="language-arduino">

    #include <Wire.h>
    #include <Dwenguino.h>

    void setup()
    {
        initDwenguino();
        pinMode(SW_S, INPUT_PULLUP);
        while (digitalRead(SW_S) == HIGH){
            // Doe niets, wacht tot knop wordt ingedrukt.
        }
    }

    void loop()
    {
        digitalWrite(13, HIGH);
        delay(500);
        digitalWrite(13, LOW);
        delay(500);
    }
</code>
        </pre>
    </div>
</div>

