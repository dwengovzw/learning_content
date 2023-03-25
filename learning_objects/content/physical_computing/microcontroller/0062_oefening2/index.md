---
hruid: pc_micro_p1_oef2
version: 3
language: nl
title: "Oefening 2"
description: "Oefening 2"
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
teacher_exclusive: true
---
# Practicum 1

## Oefening 2: Schakelaar

### Opdracht oefening 2

Pas nu je code aan zodat je met de onderste knop de leds aan en uit kan schakelen. Zorg ervoor dat telkens je op de knop indrukt de toestand van de leds wisselt.

Test ook wat er gebeurt als je de knop ingedrukt houdt. Het is de bedoeling dat de toestand van de leds slecht eenmaal wisselt per druk, ongeacht hoe lang je de knop ingedrukt houdt.


### Button debounce

Bij het indrukken/loslaten van een drukknop wordt er een elektrische connectie gemaakt/onderbroken. In een perfecte wereld zou deze overgang onmiddellijk en eenmalig gebeuren, maar in de realiteit vertonen knoppen een "bounce" gedrag. Wanneer je een knop indrukt of loslaat, kan het zijn dat hij meerdere keren van toestand wisselt.

![](embed/debounce.jpg "button debounce")

Dit probleem oplossen wordt "de knop debouncen" genoemd, en kan je doen door in je code te wachten nadat je hebt ingelezen dat de knop van toestand is gewisseld. Om even te wachten in code, kan je gebruik maken van de de _delay_ms(int) functie:

<div class="highlight highlight-source-c">
<pre>#<span class="pl-k">include</span> <span class="pl-s"><span class="pl-pds">&lt;</span>util/delay.h<span class="pl-pds">&gt;</span></span> <span class="pl-c"><span class="pl-c">//</span> Include deze header wanneer je delays gebruikt.</span>

<span class="pl-en">_delay_ms</span>(<span class="pl-c1">50</span>);  <span class="pl-c"><span class="pl-c">//</span> De microcontroller zal nu 50 ms geen nuttige instructies uitvoeren.</span></pre>
</div>