---
hruid: g_servo_vb2
version: 3
language: nl
title: "Voorbeeld Servomotor 2"
description: "Voorbeeld Servomotor 2"
keywords: ["oefeningen", "servomotor"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
## Servomotor

OPGAVE 2

Programmeer beide handen zodat ze op en neer kunnen bewegen in intervallen van 1 seconde.

Laat je niet misleiden! Dit is niet hetzelfde als de vorige oefening. I.p.v. gebruik te maken van de voorgeprogrammeerde functie voor het zwaaien, programmeer je nu beide handen apart. Je kan dus beide handen onafhankelijk van elkaar bewegen of kiezen om de hand in een bepaalde positie stil te houden.

Oplossing:  

![blockly](@learning-object/servo_m2/nl/3)

Je bent nu in staat om een hele hoop andere acties te doen! Je robot kan iemand de hand schudden, z'n ogen bedekken...

<div class="alert alert-box alert-success">
Hiervoor is er uiteraard reeds enige kennis over hoeken en graden nodig. Het is een extra uitdaging die je je leerlingen kan laten aangaan indien je merkt dat ze de basisblokken te eenvoudig vinden.
</div>

<div class="alert alert-box alert-danger">
Merk op dat je in de simulator beperkt bent in het draaien en plaatsen van de servomotoren. Bij het bouwen van een robot is het belangrijk om te onthouden dat de simulator slechts een hulpmiddel is bij het bouwen van een echte robot. 

Bij het uittesten van servomotoren is het aan te raden om vooral rekening te houden met de fysieke robot. De oriëntatie van de servomotor speelt immers voor een groot deel mee!
</div>