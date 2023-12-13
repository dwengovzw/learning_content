---
hruid: leerlijn_grafisch_naar_tekstueel_voorwaardelijke_herhaling_oplossing
version: 1
language: nl
title: "Voorwaardelijke herhaling (while-lus): oplossing"
description: "Oplossing opdracht voorwaardelijke herhaling."
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
teacher_exclusive: true
---

# Voorwaardelijke herhaling (oplossing)


**1: Schrijf een grafisch programma dat led13 doet knipperen wanneer je de zuid knop hebt ingedrukt.**

Hieronder zie je het grafische programma waarmee je dit resultaat bekomt.

![blockly](@learning-object/leerlijn_grafisch_naar_tekstueel_voorwaardelijke_herhaling_oplossing_blocks/nl/1)

**2: Bekijk de tekstuele code van je afgewerkte programma door in de Dwengo simulator over te schakelen naar de tekstuele weergave.**

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

    #include <Wire.h>
    #include <Dwenguino.h>
    #include <LiquidCrystal.h>

    void setup()
    {
        initDwenguino(); // Basisfuncties Dwenguino initialiseren.
        // De begrensde herhaling voor i van 0 tot en met 10 in stappen van 1
        // Opmerking i+=1 is een afkorting voor i = i + 1
        for ( int i = 0 ; i <= 10 ; i+=1) {
            // Ga met de cursor naar positie (0, 0) op het scherm (linksboven).
            dwenguinoLCD.setCursor(0,0);    
            // Drukt de tekst "Getal: " af met daarna de waarde van i.
            // Je zet i hier om van een getal (int) naar tekst (String).
            dwenguinoLCD.print(String("Getal: ") + String(i));
            // Wacht 1000 ms = 1s.
            delay(1000);
            // Maak het scherm leeg zodat je de volgende waarde op een leeg scherm kan schrijven.
            dwenguinoLCD.clear();
        }
    }


    void loop()
    {
        pinMode(13, OUTPUT);
        digitalWrite(13, HIGH);
        delay(1000);
        pinMode(13, OUTPUT);
        digitalWrite(13, LOW);
        delay(1000);
    }

</code>
    </pre>
</div>

**3: Welke verschillen zie je met het tekstuele voorbeeld van de begrensde herhaling hierboven?**

Je zal zien dat er niets is aangepast aan de voorwaardelijke herhaling. Er is enkel code na de while-lus bijgekomen. Merk op dat een blokkerende lus in de <code class="language-cpp">setup</code> functie, ervoor zorgt dat ook de code in de <code class="language-cpp">loop</code> functie niet zal uitvoeren tot je de ZUID knop indrukt. Hieronder zie je welke code anders is ten opzichte van het basisvoorbeeld.

<div class="dwengo-content">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

    pinMode(13, OUTPUT);
    digitalWrite(13, HIGH);
    delay(1000);
    pinMode(13, OUTPUT);
    digitalWrite(13, LOW);
    delay(1000);

</code>
    </pre>
</div>
