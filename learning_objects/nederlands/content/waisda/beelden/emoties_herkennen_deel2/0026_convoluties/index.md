---
hruid: org-dwengo-waisda-beelden-emoties-deel2-conv2d
version: 1
language: nl
title: "De convolutie"
description: "Wat is de convolutieoperatie?"
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

# Convolutionele lagen

## De convolutie operatie

Wanneer je een **convolutie** toepast op een afbeelding, zal je bepaalde **eigenschappen van die afbeelding versterken of verzwakken**. Je kan de afbeelding bijvoorbeeld scherper maken of je kan de randen in de afbeelding uitvergroten. Wat het effect is van de convolutie wordt bepaald door de **filter** die je gekozen hebt. Hieronder kan je verschillende filters proberen. Wat is het effect van elk van deze filters?

<iframe src="https://dwengo.org/convolutie" title="Voorbeeld van een convolutie" width="720px" height="800px"></iframe>

De convolutie zal de **filter** (= raster van getallen) van links naar rechts en van boven naar onder over de afbeelding schuiven. Op elke positie van het raster wordt een pixelwaarde van de uitvoerafbeelding berekend. Bekijk onderstaande video om te begrijpen hoe je een convolutie kan toepassen op een afbeelding.

TODO: insert video about convolutions.

Aan de hand van Python kan je convoluties toepassen op een afbeelding. Via de volgende notebook leer je hoe je dat moet doen.

[![](img/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=1712 "Basic")

## De convolutionele laag

Een convolutionele laag zal een invoerafbeelding omvormen door er een convolutie op toe te passen. De laag zal dat niet doen met een vaste **filter** maar zal **zelf een filter leren** tijdens het trainingsproces. Zo kan het neurale netwerk de eigenschappen die relevant zijn voor de taak uit de afbeelding halen. 

<div class="dwengo-content sideinfo">
<h2 class="title">Wanneer gebruik je convoluties?</h2>
<div class="content">
<p>Convoluties zijn vooral nuttig voor gegevens waar er een verband is tussen naburige waarden. De convolutie zal immers naburige waarden combineren tot een nieuwe waarde.</p>
<p>Bij afbeeldingen combineren we bijvoorbeeld regio's van 3x3 pixels tot 1 nieuwe waarde. Deze waarde stelt dan een eigenschap van deze regio voor. Bijvoorbeeld of er in de regio een rand te zien is of niet.</p>
<p>
Naast afbeeldingen, kunnen convoluties gebruikt worden voor: geluid, financiële tijdreeksen, ECG signalen, sensorgegevens, ... Convoluties zijn niet nuttig voor gegevens zonder lokale verbanden zoals een tabel met klantengegevens of medische gegevens in een patiëntendossier.
</p>
</div>
</div>