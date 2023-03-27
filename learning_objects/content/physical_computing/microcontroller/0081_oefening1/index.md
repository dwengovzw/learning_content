---
hruid: pc_micro_p2_oef1
version: 3
language: nl
title: "Oefening 1"
description: "Oefening 1"
keywords: ["Microcontroller"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14]
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

Het Dwenguino bord beschikt over een 2x16 LCD scherm. In dit practicum maken we gebruik van een voorgeprogrammeerde library om het scherm aan te sturen, maar alle details om zelf het scherm aan te sturen zijn terug te vinden in de datasheet van het LCD scherm.

### Opdracht 1.2 - Verkennen van de lcd bibliotheek

Voor je het LCD scherm kan gebruiken moet je in je code volgende functies oproepen in je main functie:

<div class="highlight highlight-source-c++">
<pre><span class="pl-en">initLCD</span>();      <span class="pl-c"><span class="pl-c">//</span> initialize communication with LCD</span>
<span class="pl-en">clearLCD</span>();     <span class="pl-c"><span class="pl-c">//</span> remove characters from LCD </span>
<span class="pl-en">backlightOn</span>();  <span class="pl-c"><span class="pl-c">//</span> turn on the LCD backlight</span></pre>
</div>

Daarna kan je gebruik maken van functies zoals appendStringToLCD, printStringToLCD,printIntToLCD.

**Zoek in de source code van de library wat deze functies precies doen** (al doet de naam al het een en ander vermoeden, wat meestal gewenst is om ervoor te zorgen dat andere mensen snel kunnen snappen wat er gebeurt in je code).

### Opdracht 1.3 - De datum printen op het lcd

Schrijf nu de volgende boodschap op je lcd-scherm: 

<pre><code>De datum is:
DD-MM-YYYY
</code></pre>

Vervang de placeholder door de effectieve datum op het moment dat je dit practicum maakt (je mag de datum hardcoden). Maak hiervoor gebruik van de functies die je in de vorige oefening hebt leren kennen. Vergeet niet om het bord te initialiseren.

Vervang de placeholder door de effectieve datum op het moment dat je dit practicum maakt (je mag de datum hardcoden). Maak hiervoor gebruik van de functies die je in de vorige oefening hebt leren kennen. Vergeet niet om het bord te initialiseren.

Vervang de placeholder door de effectieve datum op het moment dat je dit practicum maakt (je mag de datum hardcoden). Maak hiervoor gebruik van de functies die je in de vorige oefening hebt leren kennen. Vergeet niet om het bord te initialiseren.