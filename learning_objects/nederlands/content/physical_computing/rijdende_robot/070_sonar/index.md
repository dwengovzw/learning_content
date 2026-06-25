---
hruid: pc_rijdenderobot_sonar
version: 1
language: nl
title: "Afstandssensor - sonar"
description: "Uitleg over afstandssensoren en de sonar"
keywords: ["Blockly", "Dwenguino", "robot", "rijdende robot", "servo", "afstandssensor", "ultrasone sensor", "sonar"]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [10, 11, 12]
difficulty: 3
estimated_time: 1
teacher_exclusive: false
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
---

# Afstandssensor: sonar

Een afstandssensor doet wat zijn naam zegt: het meet hoe ver iets voor de robot is. Dit is precies wat we zoeken!

Er zijn verschillende soorten afstandssensors. Wij gebruiken een ultrasone sensor of een **sonar**. Die stuurt ultrasone geluiden uit en meet hoe snel die terugkomen. Zo weet de robot hoe ver een muur (of ander object) is.

> Vleermuizen gebruiken hetzelfde principe om in het donker te 'zien'!

![afbeelding sonar](embed/sonar_afbeelding.png)

Het programmeerblokje voor de sonar vind je opnieuw onder 'Dwenguino'. We geven een voorbeeldje over hoe je het moet gebruiken. Het gegeven programma leest de waarde van de sonar uit en print deze op het lcd.

![blockly](@learning-object/pc_rijdenderobot_sonar_blocks/nl/1)

<div class="dwengo-content assignment">
<h2 class="title">Stoppen voor de muur</h2>
<div class="content">
Maak een nieuw programma waarin de robot vooruit rijdt en vlak voor de muur stopt.
</div>
</div>