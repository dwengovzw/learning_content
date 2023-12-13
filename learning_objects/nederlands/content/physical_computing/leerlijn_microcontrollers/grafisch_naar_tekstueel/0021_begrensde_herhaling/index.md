---
hruid: leerlijn_grafisch_naar_tekstueel_begrensde_herhaling
version: 1
language: nl
title: "Begrensde herhaling (for-lus)"
description: "Hier bekijken we de basisstructuur van een µC programma."
keywords: ["programmeren", "blockly", "setup", "loop", "microcontroller", "µC", "arduino", "dwenguino"]
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

# Begrensde herhaling

De lus waarmee we in de grafische code tellen met i van een bepaald getal tot een ander getal in een aantal stappen, wordt omgezet naar een for-lus. Hieronder zie je hoe zo'n begrensde lus eruit ziet in de grafische programmeeromgeving van Dwengo.

![blockly](@learning-object/leerlijn_grafisch_naar_tekstueel_begrensde_herhaling_blocks/nl/1)

Door in de Dwengo simulator over te schakelen naar de tekstuele weergave, zie je te tekstuele code voor de begrensde herhaling. Hieronder zie je dezelfde code maar met in de commentaar wat meer uitleg over de verschillende elementen van de code.

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
            // Deel van de basisstructuur voor Dwenguino
            initDwenguino();

            // De begrensde herhaling.
            // Deze lus zal blijven herhalen tot i gelijk is aan 10.
            // i start op de waarde 0 en gaat telkens je de lus doorlopen hebt
            // omhoog met 1.
            for (int i = 0 ; i <= 10 ; i+=1) {
            }
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
            <li>Schrijf een grafisch programma dat de getallen 0 tot en met 10 afdrukt op het lcd-scherm van de Dwenguino. Je drukt de cijfers op dezelfde plaats op het scherm af. Zorg dat elk cijfer 1 seconde zichtbaar is op het scherm.</li>
            <li>Bekijk de tekstuele code van je afgewerkte programma door in de Dwengo simulator over te schakelen naar de tekstuele weergave.</li>
            <li>Welke verschillen zie je met het tekstuele voorbeeld van de begrensde herhaling hierboven?</li>
            <li>Pas de tekstuele code aan zodat je de getallen 31 tot en met 42 afdrukt op het scherm.</li>
        </ol>
    </div>
</div>

