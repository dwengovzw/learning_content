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

**Het bus protocol definieert hoe digitale systemen met elkaar kunnen communiceren over een gedeelde kabel.** Het protocol legt vast hoe de systemen geïdentificeerd kunnen worden, hoe data verstuurd kan worden en hoe conflicten vermeden kunnen worden. In dit leerpad zal je zien hoe communicatie over een bus werkt. Je ziet ook een aantal voorbeelden van veelgebruikte bus protocollen bijvoorbeeld I²C, SPI en CAM.

<div class="dwengo-content sideinfo">
<h2 class="title">Het bredere plaatje</h2>
<div class="content">
De bus protocollen die we hier zien leggen vast hoe je elektrische signalen kan genereren om informatie tussen geïntegreerde schakelingen uit te wisselen. We noemen dergelijke communicatie **communicatie op laag niveau** sterk verwant is met de gekozen hardware. Communicatie op dit niveau wordt ook wel een communicatie op de **fysieke laag** genoemd.

In moderne computernetwerken liggen er nog heel wat extra lagen bovenop de **fysieke laag**. Een aantal van deze lagen heb je misschien al van gehoord. De **Data link laag** zorgt bijvoorbeeld voor de addressering van apparaten aan de hand van een MAC adres. De **netwerk laag** zal zorgen dat je apparaten kan bereiken aan de hand van hun IP-adres. De **transport laag** zorgt ervoor dat wanneer je grote hoeveelheden data verstuurd, deze worden opgesplitst in kleinere deeltjes en een voor een en in de juiste volgorde worden verstuurd over het netwerk (TCP). De **applicatie** laag zal de ontvangen gegevens interpreteren en deze op de correcte manier weergeven bv. als een video in de Netflix applicatie.

Deze manier om netwerkcommunicatie op te delen in lagen wordt vastgeled in het OSI-model.
</div>
</div>