---
hruid: org-dwengo-pc-physics-valbeweging-opstelling
version: 1
language: nl
title: "De opstelling"
description: "Gebruik de Dwenguino in de les fysica!"
keywords: ["Fysica", "Dataverzameling", "Dataverwerking", "valbeweging"]
content_type: "text/markdown"
estimated_time: 2
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

# De opstelling

We zullen gebruik maken van een sonar-sensor om het verloop van een valbeweging te registreren. Een sonar-sensor meet de afstand tot het object dat ervoor staat. In dit experiment, monteren we de sonar-sensor op de rand van een tafel. De sensor kijkt naar beneden en meet de afstand tot de grond. Wanneer we nu een object onder de sensor houden en dit object laten vallen, zal de sensor het verloop van de valbeweging registreren. Je kan eventueel een papieren, kartonnen of pvc buis gebruiken om het object in te laten vallen. Zo zal het gemakkelijker zijn om ervoor te zorgen dat het object mooi naar beneden valt.

TODO: afbeelding tafel met aan de rand een sensor.

## De elektronica

Om metingen te kunnen doen, voegen we twee componenten toe aan de Dwenguino. Een Bluetooth module en een sonar sensor. De Bluetooth module kan je aansluiten op de UART connector bovenaan de Dwenguino (zie onderstaande afbeelding). Zorg dat de pinnen op de module overeen komen met de pinnen op het Dwenguino bord.

!["Render van een Dwenguino waarop bovenaan een bluetooth module is aangesloten."](./images/dwenguino_bt.PNG)

De sonar-sensor kan je via het breadboard verbinden met de correcte pinnen van de Dwenguino. Op het onderstaande schema kan je zien hoe je dat moet doen.

!["Voorbeeld van de aansluiting op pin 11 en 12 van de Dwenguino"](./images/connection.svg)