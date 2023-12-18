---
hruid: leerlijn_grafisch_naar_tekstueel_basisstructuur
version: 1
language: nl
title: "Basisstructuur"
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

# Basisstructuur

De basisstructuur van elk grafisch programma voor de Dwenguino is het *zet klaar, herhaal* blok. Alle code onder de *zet klaar* wordt een keer uitgevoerd bij het starten van je programma. Je gebruikt dit deel om variabelen aan te maken of standaardwaarden in te stellen. Onder de *herhaal* komt code die steeds herhaald zal worden tot het uitvoeren stopt (bv. wanneer je de µC reset of de stroom uittrekt). Onder *herhaal* komt het grootste deel van de logica van je programma. Hieronder zie je een voorbeeld van hoe deze blok eruitziet.

![blockly](@learning-object/leerlijn_grafisch_naar_tekstueel_basisstructuur_blocks/nl/1)

Door in de Dwengo simulator over te schakelen naar de tekstuele weergave, zie je te tekstuele code voor de *zet klaar, herhaal* blok. Hieronder zie je dezelfde code maar met in de commentaar wat meer uitleg over de verschillende elementen van de code.

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

// In dit eerste deel zeg je welke bibliotheken je zal gebruiken.
// Een bibliotheek bevat code die iemand anders geschreven heeft
// en die jij kan gebruiken. 
#include <Wire.h>           // Bibliotheek voor communicatie
#include <Dwenguino.h>      // Bibliotheek voor basisfuncties van de Dwenguino
#include <LiquidCrystal.h>  // Bibliotheek om het lcd-scherm aan te sturen.

// De zet klaar functie, in het engels setup genoemd.
void setup()
{
    // Code die hierin staat wordt een keer uitgevoerd
    // bij het begin van je programma.
    initDwenguino(); // Zet alle instellingen juist om de functies van de Dwenguino te kunnen gebruiken.
}

// De herhaal functie of loop in het engels.
void loop()
{
    // Code die in deze functie staat zal telkens opnieuw
    // uitgevoerd worden tot je het programma stopt.
}

</code>
    </pre>
</div>

In de volgende voorbeelden zullen we telkens code toevoegen aan deze *zet klaar, herhaal* blok en uitleggen hoe deze code wordt omgezet naar tekst. We doen dit omdat code buiten de *zet klaar, herhaal* blok niet omgezet zal worden.
