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

<div class="dwengo-content dwengo-code-simulator">
    <pre>
        <code class="language-arduino">
    
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