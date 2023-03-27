---
hruid: pc_micro_dwenguino
version: 3
language: nl
title: "dwenguino"
description: "dwenguino"
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
# De dwenguino

## Een kort overzicht

![](@youtube/https://www.youtube.com/embed/LQ4E649KPFc "De dwenguino: een kort overzicht")

Het dwenguino platform is een veelzijdig microcontrollerplatform dat ontwikkeld werd door [dwengo vzw](dwengo.org "dwengo website"). Het bevat reeds een aantal componenten waaronder een lcd-scherm, leds, een buzzer, knopjes en een motordriver zodat men heel snel allerlei toepassingen kan realiseren en testen.

![Microcontroller](embed/microcontroller2.png "Microcontroller")

De dwenguino wordt gebruikt in scholen en [internationale projecten](dwengo.org/projects "Internationale projecten"), en ook gaan het gebruiken in dit project. Echter, waar de meeste leerlingen en hobbyisten de dwenguino op een toegankelijke manier programmeren in Arduino IDE of dwenguino blockly, moeten jullie de dwenguino programmeren door te steunen op de AVR-bibliotheken en de lijvige datasheet. Dit maakt het welliswaar moeilijker, maar zorgt er wel voor dat je een goed en volledig begrip zal krijgen van de werking van een microcontroller.

![](@youtube/https://www.youtube.com/embed/MBsjYMm-Y90 "De dwenguino: het elektisch schema")