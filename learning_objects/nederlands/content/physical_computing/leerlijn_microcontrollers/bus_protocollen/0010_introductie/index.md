---
hruid: org-dwengo-pc-bus-protocollen-introductie
version: 1
language: nl
title: "Introductie"
description: "Wat zijn bus protocollen en waarvoor dienen ze?"
keywords: ["dwenguino", "microcontroller", "bus", "communicatie", "i2c", "spi", "uart", "can"]
content_type: "text/markdown"
estimated_time: 50
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

# Introductie

In deze leerlijn heb je al kennis gemaakt met verschillende sensoren die je kon verbinden met de microcontroller. Dit waren meestal eenvoudige sensoren zoals een lichtsensor of een geluidssensor. Zo'n sensoren geven een 1 (5V) of een 0 (0V) als signaal. Toch zijn er heel wat sensoren die meer complexe data kunnen doorsturen. Denk bijboorbeeld aan een versnellingsmeter die de versnelling in x-, y-, en z-richting meet of een sensor in een weerstation die luchtdruk en temperatuur meet. Om met deze complexere sensoren, maar ook tussen microcontrollers, te communiceren, wordt vaak gebruik gemaakt van een **bus protocol**. 

**Het bus protocol definieert hoe digitale systemen met elkaar kunnen communiceren over een gedeelde kabel.** Het protocol legt vast hoe de systemen geïdentificeerd kunnen worden, hoe data verstuurd kan worden en hoe conflicten vermeden kunnen worden. In dit leerpad zal je zien hoe communicatie over een bus werkt. Je ziet ook een aantal voorbeelden van veelgebruikte bus protocollen bijvoorbeeld I²C, SPI, UART en CAM.