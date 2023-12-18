---
hruid: leerlijn_grafisch_naar_tekstueel_selectie_met_else_oplossing
version: 1
language: nl
title: "Selectie (if-then-else): oplossing"
description: "Oplossing voor de opdracht over de if-then-else structuur."
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

# Selectie: if-then-else (oplossing)


**1: Schrijf een grafisch programma dat de tekst "AAN" toont op het scherm wanneer de zuid knop (S) van de Dwenguino wordt ingedrukt en de tekst "UIT" toont wanneer de zuid knop (S) niet ingedrukt wordt.**

Hieronder zie je het grafische programma waarmee je dit resultaat bekomt.

![blockly](@learning-object/leerlijn_grafisch_naar_tekstueel_selectie_met_else_oplossing_blocks/nl/1)

Merk op dat we buiten het als-dan-anders blok een wacht-blok en maak-lcd-scherm-leeg-blok toevoegen. Dit doen we om het scherm leeg te maken. De wachttijd is nodig om flikker op het lcd-scherm te vermijden. Door de wacht zal de tekst een veel groter percentage van de tijd zichtbaar zijn ten opzichte van de tijd dat het scherm leeg is. Daardoor zal je oog het aan en uit flikkeren van de tekst niet kunnen zien op het Dwenguino bord.

Merk ook op dat de code hier in het *herhaal* gedeelde van de code staat. Dit is nodig omdat we telkens opnieuw de waarde van de knop willen lezen en daarop reageren. 

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
    }


    void loop()
    {
        // Controleer of de zuid knop is ingedrukt.
        if (digitalRead(SW_S) == PRESSED) {
            // Deze code voer je uit als de conditie waar is.

            // Beweeg de cursor naar positie (0, 0)
            dwenguinoLCD.setCursor(0,0);
            // Druk de tekst AAN af op het scherm
            dwenguinoLCD.print(String("AAN"));
        } else {
            // Deze code voer je uit als de conditie vals is.

            // Beweeg de cursor naar positie (0, 0)
            dwenguinoLCD.setCursor(0,0);
            // Druk de tekst UIT af op het scherm
            dwenguinoLCD.print(String("UIT"));
        }
        // Wacht 20 ms.
        delay(20);
        // Maak het lcd-scherm leeg.
        dwenguinoLCD.clear();
    }

</code>
    </pre>
</div>

**3: Welke verschillen zie je met het tekstuele voorbeeld van de begrensde selectie hierboven?**

Je zal zien dat de structuur van de if-then-else dezelfde is maar dat zowel de conditie als de inhoud van zowel de <code class="language-cpp">if</code> als de <code class="language-cpp">else</code> anders is. Je zal zien dat we in de conditie rechtstreeks de waarde van een pin lezen met behulp van de functie <code class="language-cpp">digitalRead(SW_S)</code>. Deze waarde vergelijken we met een definitie met de naam <code class="language-cpp">PRESSED</code>. De waarde van <code class="language-cpp">PRESSED</code> wordt toegekend in de Dwenguino bibliotheek en is gelijk aan 0. Omdat je bovenaan in je programma de Dwenguino.h bibliotheek toevoegt, kan je deze definitie in je programma gebruiken.

De code in de <code class="language-cpp">if</code> en de <code class="language-cpp">else</code> is zeer gelijkaardig. Enkel de waarde die je afdrukt op het lcd-scherm is anders. Hieronder zie je de code die verschilt van de code in de basisstructuur.


<div class="dwengo-content">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

    // Controleer of de zuid knop is ingedrukt.
    if (digitalRead(SW_S) == PRESSED) {
        // Deze code voer je uit als de conditie waar is.

        // Beweeg de cursor naar positie (0, 0)
        dwenguinoLCD.setCursor(0,0);
        // Druk de tekst AAN af op het scherm
        dwenguinoLCD.print(String("AAN"));
    } else {
        // Deze code voer je uit als de conditie vals is.

        // Beweeg de cursor naar positie (0, 0)
        dwenguinoLCD.setCursor(0,0);
        // Druk de tekst UIT af op het scherm
        dwenguinoLCD.print(String("UIT"));
    }
    // Wacht 20 ms.
    delay(20);
    // Maak het lcd-scherm leeg.
    dwenguinoLCD.clear();

</code>
    </pre>
</div>

**4: Pas de tekstuele code aan zodat je de logica omdraait en "UIT" toont wanneer de knop is ingedrukt en "AAN" wanneer dat niet zo is.**

Hiervoor zijn twee mogelijke oplossingen. In een eerste oplossing draai je de logische operator in de conditie om:

<div class="dwengo-content">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

    // Controleer of de zuid knop NIET is ingedrukt.
    if (digitalRead(SW_S) != PRESSED) {
        // Deze code voer je uit als de conditie waar is.

        // Beweeg de cursor naar positie (0, 0)
        dwenguinoLCD.setCursor(0,0);
        // Druk de tekst AAN af op het scherm
        dwenguinoLCD.print(String("AAN"));
    } else {
        // Deze code voer je uit als de conditie vals is.

        // Beweeg de cursor naar positie (0, 0)
        dwenguinoLCD.setCursor(0,0);
        // Druk de tekst UIT af op het scherm
        dwenguinoLCD.print(String("UIT"));
    }
    // Wacht 20 ms.
    delay(20);
    // Maak het lcd-scherm leeg.
    dwenguinoLCD.clear();

</code>
    </pre>
</div>

Een tweede optie is om de code in de <code class="language-cpp">if</code> en de <code class="language-cpp">else</code> om te wisselen.


<div class="dwengo-content">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

    // Controleer of de zuid knop NIET is ingedrukt.
    if (digitalRead(SW_S) == PRESSED) {
        // Deze code voer je uit als de conditie waar is.

        // Beweeg de cursor naar positie (0, 0)
        dwenguinoLCD.setCursor(0,0);
        // Druk de tekst UIT af op het scherm
        dwenguinoLCD.print(String("UIT"));
    } else {
        // Deze code voer je uit als de conditie vals is.

        // Beweeg de cursor naar positie (0, 0)
        dwenguinoLCD.setCursor(0,0);
        // Druk de tekst AAN af op het scherm
        dwenguinoLCD.print(String("AAN"));
    }
    // Wacht 20 ms.
    delay(20);
    // Maak het lcd-scherm leeg.
    dwenguinoLCD.clear();

</code>
    </pre>
</div>
