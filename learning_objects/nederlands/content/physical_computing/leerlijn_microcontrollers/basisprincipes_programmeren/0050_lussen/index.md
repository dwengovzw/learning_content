---
hruid: leerlijn_basis_programmeren_lussen
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Begrensde herhaling (for-lus)

Zoals we al zagen wordt de code in de <code class="language-cpp">loop()</code> functie herhaalt tot je het programma stopt. Als je een onderdeel van je code wil laten herhalen, maak je gebruik van een lus. Een eerste soort lus is de for-lus. Deze zal starten bij een bepaalde ondergrens en herhalen tot een bovengrens is bereikt. Daarom spreken we van een begrensde herhaling. Hieronder zie je een voorbeeld van zo'n for-lus.

```arduino
for (int i = 0 ; i < 10 ; i++){
    // Wat hier staat zal 10 keer herhaalt worden.
}
```
Deze lus start met een variabele <code class="language-cpp">i</code> van het type <code class="language-cpp">int</code> die de waarde <code class="language-cpp">0</code> heeft. De lus blijft herhalen zolang <code class="language-cpp">i < 10</code>. Telkens we de lus doorlopen hebben, verhogen we i met 1: <code class="language-cpp">i++</code> dit is een verkorte versie van <code class="language-cpp">i = i + 1</code>.

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Hieronder zie je code die led 13 aan- en uitzet. Voeg op de gepaste plaats een for-lus toe om ervoor te zorgend dat de led 10 keer aan en uit gaat. Erna stop het programma. 
        <div class="dwengo-content dwengo-code-simulator">
        <pre>
<code class="language-cpp">

    #include <Dwenguino.h>

    void setup(){
        initDwenguino();
        pinMode(13, OUTPUT);
        digitalWrite(13, HIGH);
        delay(500);
        digitalWrite(13, LOW);
        delay(500);
    }

    void loop(){
        // De loop is hier leeg.
    }
</code>
        </pre> 
        </div>
    </div>
</div>