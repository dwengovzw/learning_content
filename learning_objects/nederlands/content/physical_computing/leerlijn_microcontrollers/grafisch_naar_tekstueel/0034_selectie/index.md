---
hruid: leerlijn_grafisch_naar_tekstueel_selectie
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

Je kan aan een selectie blok ook een "anders" of <code class="language-cpp">else<code> structuur toevoegen. De code in de <code class="language-cpp">else<code> wordt uitgevoerd wanneer de conditie vals is.

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
            <li>Schrijf een grafisch programma dat de getallen 0 tot en met 10 afdrukt op het lcd-scherm van de Dwenguino. Je drukt de cijfers op dezelfde plaats op het scherm af. Zorg dat elk cijfer 1 seconde zichtbaar is op het scherm.</li>
            <li>Bekijk de tekstuele code van je afgewerkte programma door in de Dwengo simulator over te schakelen naar de tekstuele weergave.</li>
            <li>Welke verschillen zie je met het tekstuele voorbeeld van de begrensde herhaling hierboven?</li>
            <li>Pas de tekstuele code aan zodat je de getallen 31 tot en met 42 afdrukt op het scherm.</li>
        </ol>
    </div>
</div>

