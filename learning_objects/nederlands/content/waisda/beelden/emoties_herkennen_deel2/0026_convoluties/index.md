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

# De convolutie

Wanneer je een **convolutie** toepast op een afbeelding, zal je bepaalde **eigenschappen van die afbeelding versterken of verzwakken**. Je kan de afbeelding bijvoorbeeld scherper maken of je kan de randen in de afbeelding uitvergroten. Wat het effect is van de convolutie wordt bepaald door de **filter** die je gekozen hebt. Hieronder kan je verschillende filters proberen. Wat is het effect van elk van deze filters?

<iframe src="https://dwengo.org/convolutie" title="Voorbeeld van een convolutie" width="720px" height="700px"></iframe>

De convolutie zal de **filter** (= raster van getallen) van links naar rechts en van boven naar onder over de afbeelding schuiven. Op elke positie van het raster wordt een pixelwaarde van de uitvoerafbeelding berekend. Bekijk onderstaande video om te begrijpen hoe je een convolutie kan toepassen op een afbeelding.

TODO: insert video about convolutions.

Aan de hand van Python kan je convoluties toepassen op een afbeelding. Via de volgende notebook leer je hoe je dat moet doen.

[![](embed/Knop.png "Button")](https://kiks.ilabt.imec.be/hub/tmplogin?id=1712 "Basic")

