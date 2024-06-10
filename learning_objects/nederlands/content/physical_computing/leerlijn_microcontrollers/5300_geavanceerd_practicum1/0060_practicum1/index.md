---
hruid: pc_micro_practicum1
version: 3
language: nl
title: "Practicum 1"
description: "Practicum 1"
keywords: ["Microcontroller"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# Practicum 1

## Inleiding

In dit practicum leren jullie de basis van het microcontrollerprogrammeren. We gebruiken in dit practicum een AVR microcontroller, dit type wordt onder andere ook gebruikt voor het Arduino platform.

Als je vast komt te zitten tijdens het practicum, herbekijk zeker de video's 3 en 4 van *Operatoren* en *Tri-state logica*.

Het programmeren van de microcontroller doe je via de tekstuele optie in de simulator die jullie rechtsbovenaan deze pagina kunnen vinden.<br>
Eens je de simulator geopend hebt, kan je deze overschakelen naar de code-UI door linksbovenaan op de *Blockly-Code*-switch te drukken.


## De microcontroller

Voor deze oefening maken jullie gebruik van het dwenguino bord. Dit bord bevat een **AT90USB646** microcontroller, dit is de grote vierkante chip onder het LCD scherm. Het is deze chip die jullie in het practicum zullen programmeren.<br><br> 

Op onderstaande figuur zie je de pin layout van de chip. Het is via deze pinnen dat de chip communiceert met de compomenten op het dwenguino bord, zoals de 8 leds, 5 drukknopen, een LCD scherm, een motor controller, een speaker en Arduino compatibele expansion ports. In dit practicum moeten jullie enkel communiceren met de leds op het bord.

![](embed/microcontroller_chip.png "afbeelding chip")

