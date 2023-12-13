---
hruid: leerlijn_grafisch_naar_tekstueel_begrensde_herhaling_oplossing
version: 1
language: nl
title: "Begrensde herhaling (for-lus): oplossing"
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
teacher_exclusive: true
---

# Begrensde herhaling (oplossing)


**1: Schrijf een grafisch programma dat de getallen 0 tot en met 10 afdrukt op het lcd-scherm van de Dwenguino. Je drukt de cijfers op dezelfde plaats op het scherm af. Zorg dat elk cijfer 1 seconde zichtbaar is op het scherm.**

Hieronder zie je het grafische programma waarmee je dit resultaat bekomt.

![blockly](@learning-object/leerlijn_grafisch_naar_tekstueel_begrensde_herhaling_oplossing_blocks/nl/1)

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
        // De herhaal is hier leeg.
    }

</code>
    </pre>
</div>

**3: Welke verschillen zie je met het tekstuele voorbeeld van de begrensde herhaling hierboven?**

Je zal zien dat er, net zoals bij de grafische code, enkel tekstuele code is bijgekomen in de for-lus. Je merkt ook op dat één grafische codeblok omgezet kan worden naar meerdere lijnen tekstuele code. De lcd-scherm blok wordt bijvoorbeeld omgezet naar de lijnen <code class="language-cpp">dwenguinoLCD.setCursor(0,0);</code> en <code class="language-cpp">dwenguinoLCD.print(String("Getal: ") + String(i));</code>. Hieronder zie je het stuk van de code waar er veranderingen zijn. Merk op dat we geen nieuwe bibliotheken moeten toevoegen in het begin van ons programma omdat in de Dwengo simulator standaard de dwenguino en lcd bibliotheken toegevoegd worden.

<div class="dwengo-content">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

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

</code>
    </pre>
</div>

**4: Pas de tekstuele code aan zodat je de getallen 31 tot en met 42 afdrukt op het scherm.**

Hiervoor moet je de start- en eindwaarde voor i aanpassen in de for-lus:

<div class="dwengo-content">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

    // De begrensde herhaling voor i van 31 tot en met 42 in stappen van 1
    // Opmerking i+=1 is een afkorting voor i = i + 1
    for ( int i = 31 ; i <= 42 ; i+=1) {
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

</code>
    </pre>
</div>