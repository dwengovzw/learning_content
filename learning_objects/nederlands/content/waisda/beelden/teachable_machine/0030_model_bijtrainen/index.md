---
hruid: org-dwengo-waisda-beelden-teachable-machine-example-transfer-learning
version: 1
language: nl
title: "Transfer learning"
description: "Hoe kan ik een bestaand model aanpassen"
keywords: ["Neurale netwerken", "Imagenet", "Teachable machine", "fine tuning", "Transfer learning"]
content_type: "text/markdown"
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# Transfer learning

Transfer learning ofwel transfer leren, is een techniek waarmee je de kracht van een bestaand AI-model kan gebruiken voor een nieuwe taak. Stel dat je een model wil trainen dat afbeeldingen van afval kan indelen in de categorieën "Papier" en "PMD". Je zou daarvoor kunnen starten vanaf nul en een volledig nieuw AI-model trainen. Hiervoor heb je echter heel wat data nodig. Deze dataset zal duizenden afbeeldingen van papier en PMD moeten bevatten. Het zal dus veel werk zijn om deze afbeeldingen te verzamelen. Om dit te vermijden, kan je vertrekken van een bestaand model dat al door iemand anders getraind is voor een gelijkaardige taak. Er zijn verschillende modellen (bv. ImageNet) die getraind zijn om objecten in afbeeldingen te detecteren. ImageNet is bijvoorbeeld getraind op meer dan een miljoen afbeeldingen en kan 1000 verschillende objecten detecteren. Door van dit model te vertrekken en het aan te passen voor onze taak, kunnen we tot een goed resultaat komen met een beperkt aantal afbeeldingen. 

## Extra laag

Concreet voegen we bij transfer learning een nieuwe laag toe aan een bestaand model. Stel dat we vertrekken van het volgende model:

![Voorbeeldarchtectuur van een neuraal netwerk.](images/neural_network_with_labels.svg)

Zoals je ziet is het model getraind om objecten op afbeeldingen te detecteren. Wij voegen nu een extra laag toe aan dit model. Deze laag zullen we trainen om de vertaling te maken van objecttype naar afvalcategorie.

![Voorbeeldarchtectuur van een neuraal netwerk.](images/neural_network_with_extra_layer.svg)