---
hruid: leerlijn_grafisch_naar_tekstueel_variabelen_string
version: 1
language: nl
title: "Variabelen (String)"
description: "Hier zien we hoe een textvariabele omgezet wordt naar tekstuele code."
keywords: ["programmeren", "String", "blockly", "setup", "while", "loop", "microcontroller", "µC", "arduino", "dwenguino"]
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

# Variabelen (String)

In de grafische code hebben we twee soorten variabelen. De ene kan getallen bevatten de andere tekst. Hier kijken we naar hoe een variabele waarin je tekst kan opslaan wordt vertaald naar tekstuele code. Je zal merken dat deze code zeer gelijkaardig is aan de code van een getalvariabele. Toch zijn er subtiele verschillen. **Let dus op dat je de twee niet door elkaar haalt**.

We vertrekken van de volgende grafische code:

![blockly](@learning-object/leerlijn_grafisch_naar_tekstueel_variabelen_string_blocks/nl/1)

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
        String item;

        // Deel van de basisstructuur
        void setup()
        {
            initDwenguino(); // Deel basisstructuur
        }

        // Deel van de basisstructuur
        void loop()
        {
            // Hier stellen we de waarde van de variabele in op de tekst Hallo Dwenguino.
            item = String("Hallo Dwenguino");
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
        String item;

</code>
    </pre>
</div>

Je ziet hier twee woorden: <code class="language-cpp">String</code> en <code class="language-cpp">item</code>. <code class="language-cpp">String</code> is het **type** van de variabele en geeft in dit geval aan dat je in de variabele gehele getallen zal opslaan. <code class="language-cpp">item</code> is de naam van de variabele, deze mag je zelf kiezen. Je zal deze naam doorheen je programma gebruiken om de waarde van de variabele op te vragen maar ook om deze waarde aan te passen.

Wanneer we de code kijken waarin onze variabele een waarde krijgt, zien we een subtiel verschil met de code voor een variabele van het type <code class="language-cpp">int</code>.

<div class="dwengo-content">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

        // Hier ken je de waarde Hallo Dwenguino toe aan de variabele item.
        item = String("Hallo Dwenguino");

</code>
    </pre>
</div>

Merk op dat <code class="language-cpp">"Hallo Dwenguino"</code> tussen aanhalingstekens staat. Dit geeft in tekstuele code aan dat het hier over een tekstwaarde gaat. Verder zie je ook dat de tekst omringt is door nog wat extra code: <code class="language-cpp">String(...)</code>. In dit geval is deze code eigenlijk overbodig maar de grafische blokken voegen dit deel automatisch toe om ervoor te zorgen dat er geen fouten voorkomen wanneer je een getal probeert om te zetten naar een stuk tekst. Je kan de lijn <code class="language-cpp">item = String("Hallo Dwenguino");</code> dus vervangen door <code class="language-cpp">item = "Hallo Dwenguino";</code>



