---
hruid: leerlijn_grafisch_naar_tekstueel_selectie
version: 1
language: nl
title: "Selectie (if-then)"
description: "Hier bekijken we de basisstructuur van een µC programma."
keywords: ["programmeren", "if", "then", "else", "blockly", "setup", "loop", "microcontroller", "µC", "arduino", "dwenguino"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16]
difficulty: 3
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Selectie (if-then)

Hieronder zie je hoe de selectiestructuur eruitziet in grafische code. Hier beperken we ons eerst tot de eenvoudige <code class="language-cpp">if</code> structuur. Merk op dat de conditie <code class="language-cpp">100 < 50</code> hier altijd vals is. Deze code heeft weinig nut maar we gebruiken het hier enkel als voorbeeld.

![blockly](@learning-object/leerlijn_grafisch_naar_tekstueel_selectie_blocks/nl/1)

Door in de Dwengo simulator over te schakelen naar de tekstuele weergave, zie je te tekstuele code voor de eenvoudige selectie. Hieronder zie je dezelfde code maar met in de commentaar wat meer uitleg over de verschillende elementen van de code.

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

        // Deel van de basisstructuur
        #include <Wire.h>
        #include <Dwenguino.h>
        #include <LiquidCrystal.h>

        void setup()
        {
            initDwenguino();
            // Hier zie je de tekstuele vorm van de selectie blok.
            if (100 < 50) {
                /* Dit doe je als de conditie waar is */
            }
        }

        void loop()
        {
            // De loop is hier leeg
        }

</code>
    </pre>
</div>


