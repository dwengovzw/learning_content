---
hruid: leerlijn_basis_programmeren_lussen_oplossing
version: 1
language: nl
title: "Begrensde herhaling (for-lus)"
description: "Wat is een for-lus en waarvoor wordt die gebruikt."
keywords: ["programmeren", "for", "lus", "herhaling", "microcontroller", "µC", "arduino", "dwenguino"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Begrensde herhaling: for-lus (oplossing)

<div class="dwengo-content dwengo-code-simulator">
        <pre>
<code class="language-cpp">

    #include <Dwenguino.h>

    void setup(){
        initDwenguino();
        pinMode(13, OUTPUT);
        for (int i = 0 ; i < 10 ; i++){
            digitalWrite(13, HIGH);
            delay(500);
            digitalWrite(13, LOW);
            delay(500);
        }
    }

    void loop(){
        // De loop is hier leeg.
    }
</code>
        </pre> 
        </div>