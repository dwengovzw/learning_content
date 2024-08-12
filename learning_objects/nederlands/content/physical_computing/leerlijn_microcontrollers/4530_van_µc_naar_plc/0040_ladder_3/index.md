---
hruid: leerlijn_microcontrollers_microcontroller_naar_plc_ladder_3
version: 1
language: nl
title: "Ladder logica: invoer"
description: "Wat is Ladder logica?"
keywords: ["microcontroller", "plc", "automatisatie", "programmable logic controller", "µC", "ladder"]
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

# Ladder logica: invoer

We zagen al hoe we een eenvoudig ladder logica programma kunnen omzetten naar een microcontrollerprogramma in C++. Hier gaan we dieper in op de twee soorten invoer die je kan gebruiken in een ladder diagram.

## De IF invoer

De eerste soort invoer is de IF invoer. Deze heeft het volgende symbool.

![Symbool voor de IF invoer in een ladder diagram](images/if_input.svg)

We kunnen de werking van deze invoer voorstellen aan de hand van de volgende C++ code.

<div class="dwengo-content">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
   
   if (A){
        // Laat stroom lopen van links naar rechts.
   } else {
        // Laat geen stroom lopen van links naar rechts.
   }

</code>
    </pre>
</div>

In woorden kunnen we dus zeggen dat deze invoer enkel stroom zal laten lopen van links naar rechts wanneer de logische waarde van A gelijk is aan 1.


## De IF NOT invoer

De tweede soort invoer is de IF NOT invoer. Deze heeft het volgende symbool.

![Symbool voor de IF invoer in een ladder diagram](images/not_if_input.svg)

We kunnen de werking van deze invoer voorstellen aan de hand van de volgende C++ code.

<div class="dwengo-content">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
   
   if (!A){
        // Laat stroom lopen van links naar rechts.
   } else {
        // Laat geen stroom lopen van links naar rechts.
   }

</code>
    </pre>
</div>

In woorden kunnen we dus zeggen dat deze invoer enkel stroom zal laten lopen van links naar rechts wanneer de logische waarde van A gelijk is aan 0. We zouden kunnen zeggen dat de NOT IF invoer de logische waarde van de invoer omdraait.

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        <p>
            We zagen eerder al het volgende ladder digagram.
        </p>
        <img src="images/sample.png" alt="Voorbeeld van een ladder diagram">
        <p>
            Welke logische poort implementeert deze schakeling?
        </p>
    </div>
</div>