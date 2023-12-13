---
hruid: leerlijn_grafisch_naar_tekstueel_voorwaardelijke_herhaling
version: 1
language: nl
title: "Voorwaardelijke herhaling (while-lus)"
description: "Hier bekijken we hoe een while lus wordt omgezet van grafische naar tekstuele code."
keywords: ["programmeren", "blockly", "setup", "while", "loop", "microcontroller", "µC", "arduino", "dwenguino"]
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

# Voorwaardelijke herhaling

In grafische code kunnen we een *herhalen zolang* blok gebruiken om code te blijven herhalen zolang een conditie waar is. Hieronder zie je een voorbeeld van een lus die wacht zolang je de ZUID knop niet hebt ingedrukt.

![blockly](@learning-object/leerlijn_grafisch_naar_tekstueel_voorwaardelijke_herhaling_blocks/nl/1)

Door in de Dwengo simulator over te schakelen naar de tekstuele weergave, zie je te tekstuele code voor de voorwaardelijke herhaling. Hieronder zie je dezelfde code maar met in de commentaar wat meer uitleg over de verschillende elementen van de code.

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

        // Deel van de basisstructuur
        #include <Wire.h>
        #include <Dwenguino.h>
        #include <LiquidCrystal.h>

        // Deel van de basisstructuur
        void setup()
        {
            initDwenguino(); // Deel basisstructuur

            // De voorwaardelijke herhaling met een conditie.
            // Deze conditie is waar zolang de knop niet wordt ingedrukt.
            while (digitalRead(SW_S) != PRESSED) {
                /* Deze code blijft herhalen tot je  */
                /* de ZUID knop indrukt. */
            }
            /* De code na de lus wordt pas uitgevoerd wanneer  */
            /* je de ZUID knop hebt ingedrukt. */
        }

        // Deel van de basisstructuur
        void loop()
        {
            // De herhaal is hier leeg.
        }

</code>
    </pre>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        <ol>
            <li>Schrijf een grafisch programma dat led13 doet knipperen wanneer je de zuid knop hebt ingedrukt.</li>
            <li>Bekijk de tekstuele code van je afgewerkte programma door in de Dwengo simulator over te schakelen naar de tekstuele weergave.</li>
            <li>Welke verschillen zie je met het tekstuele voorbeeld van de voorwaardelijke herhaling hierboven?</li>
        </ol>
    </div>
</div>

