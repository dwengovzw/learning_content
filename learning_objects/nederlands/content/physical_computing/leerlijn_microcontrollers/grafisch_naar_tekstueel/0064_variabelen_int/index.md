---
hruid: leerlijn_grafisch_naar_tekstueel_variabelen_int
version: 1
language: nl
title: "Variabelen (int)"
description: "Hier zien we hoe een getalvariabele omgezet wordt naar tekstuele code."
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

# Variabelen: int

In de grafische code hebben we twee soorten variabelen. De ene kan getallen bevatten de andere tekst. Hier kijken we naar hoe een variabele waarin je een getal kan opslaan wordt vertaald naar tekstuele code. We vertrekken van de volgende grafische code:

![blockly](@learning-object/leerlijn_grafisch_naar_tekstueel_variabelen_int_blocks/nl/1)

Door in de Dwengo simulator over te schakelen naar de tekstuele weergave, zie je te tekstuele code voor de voorwaardelijke herhaling. Hieronder zie je dezelfde code maar met in de commentaar wat meer uitleg over de verschillende elementen van de code.

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

        // Deel van de basisstructuur
        #include <Wire.h>
        #include <Dwenguino.h>
        #include <LiquidCrystal.h>

        // Hier wordt de variabele aangemaakt.
        // Dit noemen we de declaratie.
        int item;

        // Deel van de basisstructuur
        void setup()
        {
            initDwenguino(); // Deel basisstructuur
        }

        // Deel van de basisstructuur
        void loop()
        {
            // Hier stellen we de waarde van de variabele in op 100.
            item = 100;
        }

</code>
    </pre>
</div>

Merk op dat alle variabelen die we in de grafische code aanmaken *globaal* zijn. Dat wil zeggen dat hun **declaratie** buiten een functie staat (dus niet in bijvoorbeeld de setup of loop functie). Als je de **declaratie** van een variabele verplaatst binnen een functie, dan kan je die variabele enkel binnen die functie gebruiken.

Bekijk de lijn waarop de **delcaratie** van de variabele staat:

<div class="dwengo-content">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

        // Hier wordt de variabele aangemaakt.
        // Dit noemen we de declaratie.
        int item;

</code>
    </pre>
</div>

Je ziet hier twee woorden: <code class="language-cpp">int</code> en <code class="language-cpp">item</code>. <code class="language-cpp">int</code> is het **type** van de variabele en geeft in dit geval aan dat je in de variabele gehele getallen zal opslaan. <code class="language-cpp">item</code> is de naam van de variabele, deze mag je zelf kiezen. Je zal deze naam doorheen je programma gebruiken om de waarde van de variabele op te vragen maar ook om deze waarde aan te passen.

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Kijk terug naar te tekstuele voorstelling van de begrensde herhaling (for-lus). Herken je daar de variabele? Wat is het type en de naam van die variabele?
    </div>
</div>

