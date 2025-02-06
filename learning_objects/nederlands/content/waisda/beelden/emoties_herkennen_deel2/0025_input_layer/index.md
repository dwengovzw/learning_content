---
hruid: org-dwengo-waisda-beelden-emoties-deel2-input-layer
version: 1
language: nl
title: "De invoerlaag"
description: "Leer uit welke lagen een neuraal netwerk bestaat en waarvoor deze lagen dienen."
keywords: ["lagen", "AI", "neurale netwerken"]
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

# De invoerlaag (InputLayer)

Deze laag is de eenvoudigste laag in het netwerk. Deze laag zal de gegevens die het ontvangt doorgeven aan de rest van het netwerk. Het zal dus de invoerafbeelding één op één doorgeven aan de volgende laag in het netwerk. Hieronder zie je visueel wat de invoerlaag doet

![Afbeelding invoerlaag](img/invoerlaag.png)

<div class="dwengo-content sideinfo">
<h2 class="title">Wat is een laag?</h2>
<div class="content">
<p>
Een laag kan je zien als een <strong>bewerking</strong> die een bepaalde <strong>invoer omvormt naar een bepaalde uitvoer</strong>. Hoe de invoer wordt omgevormd, ligt niet vast. Je kan gelijk welke operatie toepassen op de invoer. De enige voorwaarde is dat deze operatie <strong>afleidbaar</strong> is. De operatie moet afleidbaar zijn omdat we het netwerk anders niet kunnen trainen met <strong>gradient descent</strong>.
</p>
<p>
Bij de invoerlaag is de operatie dus een kopie nemen van de invoer.
</p>
</div>
</div>