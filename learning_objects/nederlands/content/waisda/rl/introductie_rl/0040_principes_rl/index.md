---
hruid: org-dwengo-waisda-rl-introductie-rl-principes
version: 1
language: nl
title: "Principes versterkend leren (2)"
description: "Maak kennis met reïnforcement learning."
keywords: ["AI", "reïnforcement learning"]
content_type: "text/markdown"
estimated_time: 7
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# Principes versterkend leren

We laten je het spel spelen omdat we het kunnen gebruiken om alle basisprincipes van het versterken leren uit te leggen. Deze principes zijn:

- **De agent** is diegene die leert om het spel te spelen. Hier ben jij dus de agent. Als we een AI-systeem zouden aanleren om het spel te spelen dan is dat AI-systeem de agent.
- **De omgeving** is de wereld waarin de **agent** zal leren. Hier is de wereld het spel zelf. In ons spel bestaat de wereld uit twee palletten en een bal.
- De omgeving heeft ook een **toestand**, dat is hoe de wereld er op dat moment uitziet. De toestand van ons spel kan bijvoorbeeld zijn: pallet 1 staat op hoogte 5, de bal staat op positie (6, 9) en pallet 2 staat op hoogte 9.
- **De acties**: Jij kan als **agent** de **toestand** van de **omgeving** beïnvloeden. In het spel doe je dat door op de knoppen te drukken en je pallet naar boven of beneden te doen bewegen. Door je pallet te bewegen, kan je ook onrechtstreeks de positie van de bal beïnvloeden.
- **Een beloning**: tijdens het spel krijgen we een beloning wanneer we de wereld positief beïnvloeden en worden we gestraft (= een negatieve beloning) wanneer we die negatief beïnvloeden. Bij mensen en dieren komt een beloning overeen met de gevoelens van geluk en pijn. 
- **De policy of het beleid**: Dit is de strategie die de **agent**, jij dus, op dat moment toepast. De policy legt vast welke actie je zal ondernemen in een gegeven **toestand** van de **omgeving**.
- **De waardefunctie**: Terwijl de **beloning** je een idee geeft van welke **acties** goed of slecht waren in een bepaalde **toestand**, zegt de **waardefunctie** iets over wat goed is op lange termijn. 

Veel van deze principes zijn relatief abstract. In het vervolg van dit leerpad leggen we de principes meer in detail uit.