---
hruid: pc_micro_p2_oef1
version: 3
language: nl
title: "Oefening 1"
description: "Oefening 1"
keywords: ["Microcontroller", "lcd", "lcd-scherm"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# Practicum 2 - Timers en Interrupts

## Oefening 1: Het printen op het lcd-scherm

Het dwenguino bord beschikt over een 2x16 lcd-scherm. In dit practicum maken we gebruik van een voorgeprogrammeerde library om het scherm aan te sturen, maar alle details om zelf het scherm aan te sturen zijn terug te vinden in de datasheet van het lcd-scherm.

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 1.1</h2>
    <div class="content">
        <h3>Verkennen van de lcd-bibliotheek</h3>
        <p>
            Voor je het lcd-scherm kan gebruiken, moet je in je code volgende functies oproepen in je main functie:
        </p>
        <p>
            <div class="dwengo-content dwengo-code-simulator">
                <pre>
                    <code class="language-cpp" data-filename="filename.cpp">
                        initLCD();      // initialize communication with LCD
                        clearLCD();     // remove characters from LCD 
                        backlightOn();  // turn on the LCD backlight
                    </code>
                </pre>
            </div>
        </p>
        <p>
            Daarna kan je gebruik maken van functies zoals appendStringToLCD, printStringToLCD,printIntToLCD.
        </p>
        <p>
            <strong>Zoek in de source code van de library wat deze functies precies doen</strong> (al doet de naam al het een en ander vermoeden, wat meestal gewenst is om ervoor te zorgen dat andere mensen snel kunnen snappen wat er gebeurt in je code).
        </p>
    </div>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 1.2</h2>
    <div class="content">
        <h3>De datum printen op het lcd</h3>
        <p>
            Schrijf nu de volgende boodschap op je lcd-scherm: 
        </p>
        <p>
            <div class="dwengo-content dwengo-code-simulator">
                <pre>
                    <code class="language-cpp" data-filename="filename.cpp">
                        De datum is:
                        DD-MM-YYYY
                    </code>
                </pre>
            </div>
        </p>
        <p>
            Daarna kan je gebruik maken van functies zoals appendStringToLCD, printStringToLCD,printIntToLCD.
        </p>
        <p>
            <strong>Zoek in de source code van de library wat deze functies precies doen</strong> (al doet de naam al het een en ander vermoeden, wat meestal gewenst is om ervoor te zorgen dat andere mensen snel kunnen snappen wat er gebeurt in je code).
        </p>
        <p>
            Vervang de placeholder door de effectieve datum op het moment dat je dit practicum maakt (je mag de datum hardcoden). Maak hiervoor gebruik van de functies die je in de vorige oefening hebt leren kennen. Vergeet niet om het bord te initialiseren.
        </p>
    </div>
</div>