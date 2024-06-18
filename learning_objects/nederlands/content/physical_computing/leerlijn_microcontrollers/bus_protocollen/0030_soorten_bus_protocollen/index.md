---
hruid: org-dwengo-pc-bus-protocollen-standaarden
version: 1
language: nl
title: "Standaarden"
description: "Wat zijn bus protocollen en waarvoor dienen ze?"
keywords: ["dwenguino", "microcontroller", "bus", "communicatie", "i2c", "spi", "uart", "can"]
content_type: "text/markdown"
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-digitale-competenties-en-mediawijsheid',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-algebra-analyse',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-redeneren',

]
copyright: "CC BY dwengo"
target_ages: [16, 17, 18]
teacher_exclusive: False
---

# Standaarden

Omdat er verschillende manieren mogelijk zijn om apparaten die op een bus aangesloten zijn te laten communiceren, is het nodig om goed af te spreken hoe die communicatie moet verlopen. Zo'n afgesproken manier van communiceren noemen we een **standaard**. Verschillende **producenten van digitale elektronica gebruiken deze standaarden zodat de apparaten die ze produceren met elkaar kunnen spreken**. In dit leerpad bespreken we drie veelgebruikte standaarden voor bus communicatie. Dat zijn **I²C**, **SPI** en **CAN**. De eerste twee zijn vooral populair in de digitale elektronica. De laatste wordt vooral gebruikt in de autoindustrie om ervoor te zorgen dat de verschillende digitale systemen in de auto op een betrouwbare manier met elkaar kunnen communiceren.