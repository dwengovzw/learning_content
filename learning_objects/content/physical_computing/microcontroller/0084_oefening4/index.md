---
hruid: pc_micro_p2_oef4
version: 3
language: nl
title: "Oefening 4"
description: "Oefening 4"
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
# Practicum 2 - Timers en Interrupts

## Oefening 4: Gebruik van externe interrupts om het indrukken van knoppen te detecteren zonder active polling

Ook interrupts zijn in de kennisclips al behandeld. Lees zeker de relevante delen van de Ufora-pagina nog eens. We tonen hieronder nog eens de overzichtsfiguur: 

![](embed/interrupts.png "overzicht interrupts")


### Opdracht 4.1 - Datasheet

Lees hoofdstuk **12** van de datasheet tot en met **12.0.4** en zoek specifiek naar volgende zaken:

* Hoe zet je de globale interrupts aan?
* Hoe schakel je een specifieke externe interrupt pin aan?
* Hoe bepaal je welk(e) signaal(veranderingen) op de pin een interrupt veroorzaken?


### Opdracht 4.2 - Tellen van hoe vaak een knop gedrukt is

Bij wijze van kennismaking gaan we nu een externe interrupt gebruiken om te tellen hoeveel keer een knop wordt ingedrukt.

In de vorige opdracht heb je hopelijk alle stappen in de datasheet kunnen vinden. We herhalen hier nog eens kort de configuratiestappen om een interrupt in te stellen:

* Het **SREG** register (Status REGister) bevat het globale interrupt enable bit (zie datasheet p.13).
* Het **EIMSK** register (External Interrupt MaSK) kan je gebruiken om de interrupt enable bits in te stellen.
* Het **EICRB** register (External Interrupt Control Register B) gebruik je om te configureren of de interrupt voorkomt bij een rising of falling edge. (Kies voor falling edge, de knop schakelt immers van 1 naar 0 als je hem indrukt)

Nu de registers juist zijn ingesteld kunnen we een interrupt-routine schrijven. Rest nog de vraag: welke interrupt willen we exact afhandelen? Je zal op het schema van de dwenguino zien dat er geen interrupt pin is verbonden met de C knop, **zoek daarom welke knop verbonden is met de INT6 pin**.

Vergeet ook niet de **INT6 pin van de microcontroller als invoer te configureren** en de pull-up weerstand ervan te activeren!

**Schrijf nu de nodige code om op het scherm te tonen hoeveel keer de knop die verbonden is met de INT6 pin ingedrukt werd.**


### Opdracht 4.3 - Verbeterd meetsysteem

Pas nu de code van het meetsysteem aan om het indrukken van de knop op te vangen met een interrupt. Gebruik opnieuw de knop die verbonden is met INT6 en doorloop alle stappen uit vorige opdracht. In de ISR lees je nu het TCNT register uit.

Vergeet ook niet te checken of de LEDs wel degelijk aan staan wanneer de knop wordt ingedrukt, om foutieve metingen te vermijden.

Check of je reactietijden in de buurt liggen van die uit de vorige oefening, anders heb je wellicht een fout gemaakt.


### Waarom alweer interrupts?

Door een interrupt te gebruiken om het indrukken van de knop af te handelen zal het interval zeer exact gemeten kunnen worden én is het timen van de reactietijd volledig onafhankelijk geworden van de code die in de main functie wordt uitgevoerd. Zo kunnen we nu bijvoorbeeld ondertussen op de onderste rij van het LCD een animatie afspelen of andere operaties uitvoeren.