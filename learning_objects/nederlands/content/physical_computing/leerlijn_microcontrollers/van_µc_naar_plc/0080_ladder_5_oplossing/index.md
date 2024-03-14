---
hruid: leerlijn_microcontrollers_microcontroller_naar_plc_ladder_4
version: 1
language: nl
title: "Ladder logica: latch (oplossing)"
description: "Wat is Ladder logica?"
keywords: ["microcontroller", "plc", "automatisatie", "programmable logic controller", "µC", "ladder", "latch"]
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

# Latch (oplossing)

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
    #include <Wire.h>
    #include <Dwenguino.h>

    // Leg vast welke pinnen je gaat gebruiken als schakelaars.
    #define PIN_A 0
    #define PIN_B 1

    // Leg vast welke pin je gaat gebruiken als uitvoer.
    #define PIN_Q 2
    #define PIN_L 3

    // Maak een variabele om de logische waarde van de pin in op te slaan.
    int A = 0;
    int B = 0;
    int Q = 0;
    int L = 0;

    // Lees de waarde van de pinnen en sla die op.
    void leesSchakelaars(){
        A = digitalRead(PIN_A);
        B = digitalRead(PIN_B);
        Q = digitalRead(PIN_Q);
    }

    // Deze functie bevat de logica van ons ladder diagram.
    void voerRijLogicaUit(){
        if(!A && (B || Q)){
            Q = 1;
        } else {
            Q = 0;
        }
        if (Q) {
            L = 1;
        } else {
            L = 0;
        }
    }

    // Schrijf de uitvoerwaarden naar de overeenkomstige pinnen.
    void schrijfUitvoerwaarde(){
        digitalWrite(PIN_Q, Q);
        digitalWrite(PIN_L, L);
    }

    void setup()
    {
        initDwenguino();
    }

    void loop()
    {
        leesSchakelaars();
        voerRijLogicaUit();
        schrijfUitvoerwaarde();
    }

</code>
    </pre>
</div>

