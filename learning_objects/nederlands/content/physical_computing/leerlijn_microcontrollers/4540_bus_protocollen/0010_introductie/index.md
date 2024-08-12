---
hruid: org-dwengo-pc-bus-protocollen-introductie
version: 1
language: nl
title: "Introductie"
description: "Wat zijn bus protocollen en waarvoor dienen ze?"
keywords: ["dwenguino", "microcontroller", "bus", "communicatie", "i2c", "spi", "uart", "can"]
content_type: "text/markdown"
estimated_time: 10
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

De bus protocollen die we hier zien leggen vast hoe je elektrische signalen kan genereren om informatie tussen geïntegreerde schakelingen uit te wisselen. We noemen dergelijke communicatie, **communicatie op laag niveau**, omdat het sterk verwant is met de gekozen hardware. Communicatie op dit niveau verloopt op de **fysieke laag** en de **datalinklaag**.

In moderne computernetwerken liggen er nog heel wat extra lagen bovenop de **fysieke laag**. Een aantal van deze lagen heb je misschien al van gehoord. De **datalinklaag** zorgt bijvoorbeeld voor de addressering van apparaten aan de hand van een MAC adres. De **netwerklaag** zal zorgen dat je apparaten kan bereiken aan de hand van hun IP-adres. De **transportlaag** zorgt ervoor dat wanneer je grote hoeveelheden data verstuurd, deze worden opgesplitst in kleinere deeltjes en een voor een en in de juiste volgorde worden verstuurd over het netwerk (TCP). De **applicatielaag** zal de ontvangen gegevens interpreteren en deze op de correcte manier weergeven bv. als een website in je internetbrowser (HTTP).

Deze manier om netwerkcommunicatie op te delen in lagen van abstractie wordt vastgeled in het OSI-model (Open Systems Interconnection). Hieronder zie je een tabel met een vereenvoudigde versie van het OSI-model, het TCP/IP-model.

<table>
    <tr>
        <td>Nr.</td>
        <td>Naam laag</td>
        <td>Data eenheid</td>
        <td>Functie laag</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Applicatielaag</td>
        <td>Applicatiegegevens</td>
        <td>Deze laag is verantwoordelijk om de gegevens die toekomen in een applicatie correct te interpreteren en weer te geven. De Netflix applicatie zal de data omzetten naar een video, je internetbrowser zal de data omzetten naar een website.</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Transportlaag</td>
        <td>Segment</td>
        <td>Deze laag zorgt ervoor dat grote hoeveelheden data op een correcte manier verstuurd kunnen worden. Daarvoor zal deze laag de data opsplitsen in kleinere deeltjes en deze een voor een en in de correct volgorde versturen. Deze laag kan ook foutdetectie en foutcorrectie toepassen. Het meestgebruikte protocol op deze laag is TCP (Transport Control Protocol).</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Netwerklaag</td>
        <td>Packet</td>
        <td>De netwerklaag, ook wel de IP-laag genoemd, zal ervoor zorgen dat elke computer die met het netwerk verbonden is een uniek adres krijgt (het IP-adres). Daarnaast legt het vast hoe gegevens over het internet verstuurd kunnen worden via routers. </td>
    </tr>
    <tr>
        <td>2</td>
        <td>Datalinklaag</td>
        <td>Frame</td>
        <td>De datalinklaag legt vast hoe gegevens verstuurd worden op de fysieke drager (bv. op een bus). Wanneer er meerdere apparaten verbonden zijn met eenzelfde bus, krijgen deze een uniek adres (bv. een MAC-adres) om ze te kunnen onderscheiden. Er zijn ook mechanismen nodig om botsingen op de bus te vermijden (bv. CSMA/CD)</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Fysieke laag</td>
        <td>Bit</td>
        <td>Deze laag is verantwoordelijk om de binaire data die verstuurd moet worden om te zetten in elektrische signalen. Je zal hier voorbeelden van zien in het lesmateriaal over SPI en CAN.</td>
    </tr>
</table>

</div>
</div>