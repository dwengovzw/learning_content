---
hruid: org-dwengo-elevator-riddle-question
version: 1
language: nl
title: "Lift vraagstuk"
description: "Opgave van het vraagstuk."
keywords: ["grafen", "algoritme", "computationeel denken", "clustering"]
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---

# De uitdaging
De kantoren van Dwengo bevinden zich op de vierde tot en met elfde verdieping van een kantoorgebouw. Er is een gedeelde lift voor alle bedrijven in dit gebouw. Deze lift kan echter enkel gebruikt worden om zich van en naar de uitgang te verplaatsen en dus niet voor verplaatsingen tussen de verdiepingen. Hieronder zie je een tekening van hoe het kantoorgebouw eruitziet.

![Een tekening van een kantoorgebouw waarin Dwengo zes verdiepingen heeft die verbonden zijn met een privélift](M026_Kantoorgebouw.svg)

De werknemers van Dwengo kunnen zich tussen de eigen verdiepingen verplaatsen met een privélift. Omdat het werknemersaantal de laatse jaren sterk is toegenomen, is de lift vaak overbelast. Om dat op te lossen laat Dwengo een extra privélift installeren. Om deze efficiënt in te zetten, beslissen ze om ervoor te zorgen dat de twee liften een eigen verzameling van verdiepingen hebben waar ze stoppen. Bijvoorbeeld, de ene lift stopt enkel op de even verdiepingen en de andere lift enkel op de oneven verdiepingen. Merk op dat er hierdoor geen verplaatsingen met de lift meer mogelijk zijn tussen even en oneven verdiepingen. Deze mensen moeten de trap nemen.

Omdat er niet evenveel verplaatsingen zijn tussen de verdiepingen, wil Dwengo de opdeling zo kiezen dat er zo weinig mogelijk mensen de trap moeten nemen. Hierboven (tabel 1) kan je een overzicht zien van welke verplaatsingen er op een gemiddelde dag gebeuren.

Op welke verdiepingen moet elk van de liften stoppen om ervoor te zorgen dat er zo weinig mogelijk mensen de trap moeten nemen? De twee liften stoppen elk op hun eigen vier verdiepingen, deze verzamelingen overlappen niet.

