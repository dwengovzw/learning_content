---
hruid: leerlijn_basis_programmeren_delay
version: 1
language: nl
title: "Delay"
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Delay

Standaard worden de instructies in je programma zo snel mogelijk na elkaar uitgevoerd. Soms is het echter nodig om de uitvoering van je programma even te pauzeren. Hiervoor kan je de <code class="language-cpp">delay(tijd_in_ms)</code> functie gebruiken. Hier vul je op de plaats van <code class="language-cpp">tijd_in_ms</code> in hoe lang je wil wachten. Bijvoorbeeld: 

```arduino
    delay(500); // Wacht een halve seconde.
```


<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Hieronder zie je code die led 13 aan- en uitzet. Voeg op de gepaste plaats(en) een wachttijd toe zodat het lampje een halve seconde aan gaat en erna een halve seconde uit blijft (=knipperen met frequentie van 1Hz). 
        <div class="dwengo-code-simulator">
        <pre>
<code class="language-cpp" data-filename="delay.cpp">

    #include <Dwenguino.h>

    void setup(){
        initDwenguino();
        pinMode(13, OUTPUT);
    }

    void loop(){
        digitalWrite(13, HIGH);
        digitalWrite(13, LOW);
    }
</code>
        </pre> 
        </div>
    </div>
</div>