---
hruid: leerlijn_basis_programmeren_lussen_while
version: 1
language: nl
title: "Voorwaardelijke herhaling (while-lus)"
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
teacher_exclusive: false
---

# Voorwaardelijke herhaling (while-lus)

Naast de begrensde herhaling (for-lus) bestaat er in C++ ook een voorwaardelijke herhaling. Dat is een lus die blijft herhalen zolang een bepaalde conditie waar is. Vanaf het moment dat die conditie niet meer waar is, stopt de lus. Willen we bijvoorbeeld code blijven uitvoeren zolang de zuid knop ingedrukt is, gebruiken we de volgende code:

<pre>
    <code class="language-cpp">
        while (digitalRead(SW_S) == LOW){
            // Blijf deze code herhalen zolang de zuid knop ingedrukt is.
        }
    </code>
</pre>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Schrijf een programma die bij het starten niets doet tot je een knop indrukt. Vanaf het moment dat de knop wordt ingedrukt, begint led 13 te knipperen met een frequentie van 1 Hz (= 1 keer per seconde).
    </div>
</div>