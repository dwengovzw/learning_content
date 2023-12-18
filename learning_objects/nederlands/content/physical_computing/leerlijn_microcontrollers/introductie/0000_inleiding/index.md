---
hruid: leerlijn_uc_introductie_inleiding
version: 1
language: nl
title: "Inleiding"
description: "Inleiding"
keywords: ["Microcontroller", "µC"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16]
difficulty: 1
estimated_time: 3
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Inleiding

In deze leerlijn ontdek je hoe microcontrollers allerlei systemen in ons dagelijkse leven controleren. We gaan hands-on aan de slag met verschillende toepassingen die gebruik maken van microcontrollers (µC). Zo leer je deze microcontrollertoepassingen bouwen en programmeren. Naast deze praktische kennis leer je ook over de werking van de µC. Op die manier verwerf je inzicht in de manier waarop de elektrische schakelingen op de µC gebruikt kunnen worden om ons dagelijkse leven te automatiseren.

## Hardware
Om deze leerlijn te kunnen doorlopen zal je een microcontrollerplatform nodig hebben. Binnen deze leerlijn hebben we voorbeelden uitgewerkt voor twee platformen:

1. Het Dwenguino-platform dat we binnen Dwengo zelf ontwikkelen.
2. Het 'Arduino Uno'-platform.

| Het Dwenguino-platform  |
| - |
| ![Het Dwenguino-platform](img/dwenguino_labeled_nl_650x478.png "Het Dwenguino-platform") | 
| Het Arduino-platform | 
| TODO: add image arduino |


De basisfunctionaliteiten van het Dwenguino- en Arduino-platform zijn gelijkaardig. De Dwenguino heeft echter een aantal extra functies die het makkelijker maken om in de klas een microcontrollertoepassing te bouwen. De Dwenguino heeft onder andere een ingebouwd lcd-scherm en de mogelijkheid om motoren aan te sturen. Op de Arduino moet je zelf een lcd-scherm aansluiten en moet je, om motoren aan te sturen, gebruik maken van een externe motor driver. Daarnaast heeft de Dwenguino ook 9 aanstuurbare leds, een buzzer, vijf knoppen en speciale aansluitingen om gemakkelijk dc- en servomotoren aan te sluiten. Bovendien kan je de Dwenguino programmeren vanuit de browser zonder software te moeten installeren. Bijgevolg werkt dit op alle platformen: Windows, Linux, macOS, ChromeOS, ...

## Software
De software die je voor deze leerlijn nodig hebt hangt af van het gekozen platform. Voor leerlingen van de tweede graad maken we ofwel gebruik van de Dwengo-simulator op [blockly.dwengo.org](https://blockly.dwengo.org) ofwel van de [Arduino IDE](https://www.arduino.cc/en/software). Met de Dwengo-simulator kan je de Dwenguino zowel grafisch als tekstueel programmeren. Deze werkt volledig in de browser waardoor je niets hoeft te installeren. Met de Arduino IDE kan je de Arduino Uno enkel tekstueel programmeren. Je kan de Arduino IDE makkelijk installeren op Windows, Linux en macOS
In de derde graad kiezen we voor een professionele programmeeromgeving (VSCode) waarmee we zowel de Dwenguino als de Arduino Uno kunnen programmeren. Om dat op een efficiënte manier te kunnen doen maken we gebruik van de [PlatformIO](https://platformio.org/) plugin.
