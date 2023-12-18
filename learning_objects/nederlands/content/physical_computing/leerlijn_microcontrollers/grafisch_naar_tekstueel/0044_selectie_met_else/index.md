---
hruid: leerlijn_grafisch_naar_tekstueel_selectie_met_else
version: 1
language: nl
title: "Selectie (if-then-else)"
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

# Selectie (if-then-else)

Je kan aan een selectie blok ook een "anders" of <code class="language-cpp">else</code> structuur toevoegen. De code in de <code class="language-cpp">else</code> wordt uitgevoerd wanneer de conditie vals is.

![blockly](@learning-object/leerlijn_grafisch_naar_tekstueel_selectie_blocks_2/nl/1)


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
            } else {
                /* Dit doe je als de conditie vals is */
            }
        }

        void loop()
        {
            // De loop is hier leeg
        }

</code>
    </pre>
</div>


<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        <ol>
            <li>Schrijf een grafisch programma dat de tekst "AAN" toont op het scherm wanneer de zuid knop (S) van de Dwenguino wordt ingedrukt en de tekst "UIT" toont wanneer de zuid knop (S) niet ingedrukt wordt.</li>
            <li>Bekijk de tekstuele code van je afgewerkte programma door in de Dwengo simulator over te schakelen naar de tekstuele weergave.</li>
            <li>Welke verschillen zie je met het tekstuele voorbeeld van de selectie herhaling hierboven?</li>
            <li>Pas de tekstuele code aan zodat je de logica omdraait en "UIT" toont wanneer de knop is ingedrukt en "AAN" wanneer dat niet zo is.</li>
        </ol>
    </div>
</div>