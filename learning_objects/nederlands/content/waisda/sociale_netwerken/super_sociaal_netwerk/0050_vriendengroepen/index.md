---
hruid: org-dwengo-waisda-sociale-netwerken-super-sociaal-netwerk-vriendengroepen
version: 1
language: nl
title: "Vriendengroepen"
description: "Leer hoe je informatie kan halen uit een sociaal netwerk."
keywords: ["Sociale netwerken", "grafen", "AI", "Unsupervised learning", "clusters", "vriendengroepen"]
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

# Vriendengroepen

Groepen van personen die sterk met elkaar geconnecteerd zijn, zijn vaak vriendengroepen. Tussen deze groepen zijn regelmatig ook één of meerdere connecties. Je hebt bijvoorbeeld vrienden op school maar ook vrienden in je sportclub of jeugdbeweging. Jij bent dan de link tussen de vriendengroep op school, die in de sportclub en die in de jeugdbeweging. 

## Community detectie

Methodes om vriendengroepen te vinden in grafen worden technieken voor *community detectie* genoemd. Er zijn hier verschillende technieken voor. Eén methode werd bedacht door de Belgische wiskundige Vincent Daniel Blondel aan de UCL. Daarom wordt het ook de **Louvain methode** genoemd. Deze methode zal de *modulariteit* van de graaf berekenen waar elke knoop zijn eigen community is. Het algoritme voegt dan knopen zodanig samen in communities dat de modulariteit van de graaf stijgt. Dit blijft het algoritme herhalen totdat de modulariteit niet meer stijgt.