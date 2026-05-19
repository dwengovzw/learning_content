---
hruid: pc_toestandsautomaten8
version: 3
language: nl
title: "Eindopdracht"
description: "Oefening op het omzetten van gedragsbeschrijving naar code."
keywords: ["toestandsautomaat", "toestandsdiagram", "finite state machine", "toestand", "dwenguino", "arduino", "python"]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [13, 14, 15, 16, 17, 18]
difficulty: 3
estimated_time: 30
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Opdracht omzetting naar code

Om af te sluiten, bieden we nog een oefening aan om te oefenen op het omzetten van een gedragsbeschrijving naar effectieve code. De opdracht is dezelfde als hiervoor: schrijf een programma (in onze simulator) die het omschreven systeem realiseert. Je kan dit doen met code, of aan de hand van onze grafische methode Blockly.

We willen dat het programma ervoor zorgt dat jij de snelheid van een motor kan aanpassen. Het heeft twee toestanden:
1. De snelheid van de motor kan worden aangepast door op de N- of S-knop te drukken. Dit gebeurt in stappen van 50 en gaat niet boven 250 of onder -250. De motor blijft tijdens het instellen draaien op de vorige snelheid (dus de snelheid wordt niet direct aangepast).
2. De motor draait op de ingestelde snelheid.

Om van de ene toestand naar de andere over te gaan, moet er op de C-knop gedrukt worden.

*Tip* Als extra kun je de snelheid op het LCD schrijven.