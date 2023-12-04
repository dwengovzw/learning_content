---
hruid: leerlijn_basis_programmeren_delay_oplossing
version: 1
language: nl
title: "Delay (oplossing)"
description: "De uitvoering van je programma pauzeren."
keywords: ["programmeren", "delay", "microcontroller", "µC", "arduino", "dwenguino"]
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

# Delay (oplossing)


<div class="dwengo-content dwengo-code-simulator">
        <pre>
<code class="language-cpp" data-filename="delay_opl.cpp">

    #include <Dwenguino.h>

    void setup(){
        initDwenguino();
        pinMode(13, OUTPUT);
    }

    void loop(){
        digitalWrite(13, HIGH);
        delay(500);
        digitalWrite(13, LOW);
        delay(500);
    }
</code>
        </pre> 
        </div>
 