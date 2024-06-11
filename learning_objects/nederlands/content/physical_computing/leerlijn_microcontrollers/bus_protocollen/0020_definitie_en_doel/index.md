---
hruid: org-dwengo-pc-bus-protocollen-definitie
version: 1
language: nl
title: "Definitie en doel"
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

 # Definitie

 Bus communicatie verloopt tussen complexere digitale componenten. Dit kan zijn tussen twee microcontroller maar ook tussen een microcontroller en een geavanceerde sensor. Om te kunnen communiceren zijn deze componenten meestal verbonden met een of meerdere draden. Eigen aan een bus protocol is dat er **meer dan twee** apparaten met die draden verbonden kunnen zijn. Op onderstaande afbeelding zie je een voorbeeld van vier apparaten die verbonden zijn met een bus (= een of meerdere draden). In dit geval is dat een microcontroller en drie sensoren.

 ![Voorbeeld van vier apparaten die verbonden zijn met een bus.](images/simple_bus_diagram.svg) 

 Je ziet in de afbeelding ook dat apparaten op de bus ofwel een *master* ofwel een *slave* zijn. Er is maar één apparaat op de bus dat de *master* kan zijn. Deze is verantwoordelijk voor de coördinatie van van de bus. De master zorgt er dus voor dat apparaten niet tegelijk data sturen op de bus. Anders zou er een conflict ontstaan. De slave luistert op de bus en zal enkel antwoorden op berichten die specifiek aan die slave geadresseerd zijn.
 