---
hruid: pc_micro_tsl
version: 3
language: nl
title: "Tri-state logica"
description: "Tri-state logica"
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
# Ingangen en uitgangen bij de microcontroller

## Tri-state logica

Tri-state (drie toestanden) is een aanduiding van een digitale pin die zich in drie verschillende toestanden kan bevinden:

* hoog (logische 1)
* laag (logische 0)
* zwevend (met hoge impedantie)

In de derde toestand kan je de pin als (hoogimpedante) ingang gebruiken en dit wordt ook wel de tri-state genoemd. In deze toestand staat de pin ook te zweven. Dankzij tri-state kan de pin dus in twee richtingen werken: als ingang en als uitgang. 

Ook in andere contexten wordt dit veel gebruikt. Denk bijvoorbeeld aan de databus tussen de processor en geheugen in je computer. Ook op de microcontroller wordt dit veel gebruikt, waaronder voor de digitale ingangen en uitgangen. Hoe je dit kan instellen leg ik uit in het volgende filmpje.

![](@youtube/https://www.youtube.com/embed/vkrsgYTuI8A "Tri-state logica")

<div class="alert alert-box alert-success">
Een pin van een microcontroller kan dus gebruikt worden als digitale ingang of uitgang.<br><br> 

Om een pin als uitgang te configureren moeten we eerst de desbetreffende bit van het DDRn-register op 1 instellen. Hierbij stel n de letter van de overeenkomstige poort voor.<br>
Vervolgens kan je de pin van poort n op 1 (hoog) of 0 (laag) zetten door respectievelijk een 1 of 0 te schrijven naar de juiste bit van het PORTn-register. Merk op dat over deze pin 5V of 0V zal komen te staan.<br><br>

Om een pin als ingang te configureren (de tri-state toestand) moeten we eerst de desbetreffende bit van het DDRn-register op 0 instellen.<br>
Vervolgens kunnen we, indien dit vereist is voor de toepassing die we beogen, de interne pull-up weerstand activeren door een 1 te schrijven naar de overeenkomstige bit van het PORTn-register.<br>
Tot slot kunnen we de toestand van deze pin uitlezen door de juiste bit van het PINn-register te lezen. Hiermee zal je ook oefenen in het eerste practicum.
</div>

<div class="alert alert-box alert-danger">
De oplossing voor het instellen van de ingangen en uitgangen geven we jou cadeau. Het is echter belangrijk dat je dit ook kan terugvinden in de [datasheet van de AT90USB646](embed/Atmel 8-bit Microcontroller AT90USB646.pdf). Kijk daarom na of je de uitleg van de video zelf kan terugvinden in de secties 11.1 en 11.2 van hoofdstuk 11 (I/O-ports) van de datasheet.
</div>