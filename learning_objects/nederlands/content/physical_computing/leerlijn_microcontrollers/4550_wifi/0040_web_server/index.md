---
hruid: org-dwengo-pc-wifi-webserver
version: 1
language: nl
title: "Webserver"
description: "Wat is een webserver?"
keywords: ["dwenguino", "microcontroller", "wifi", "uart", "webserver", "web", "internet"]
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

# Webserver

Hier configureren we de Dwenguino als een **webserver**. Dit is een apparaat dat verbonden is met het internet en constant luistert naar inkomende berichten. Wanneer de server een bericht ontvangt, zal deze het bericht verwerken en een antwoord sturen naar de verzender van het bericht. Een webserver verwacht dat berichten een specifiek formaat hebben. Dit formaat wordt vastgelegd in de **HTTP** standaard. HTTP heeft een aantal berichttypes een aantal voorbeelden zijn **GET**, **POST** en **PUT**. 


<div class="dwengo-content sideinfo">
<h2 class="title">HTTP is overal</h2>
<div class="content">
Je maakt dagelijks gebruik van de HTTP standaard wanneer je surft op het internet of apps op je telefoon gebruikt. In je internetbrowser kan je dat duidelijk zien omdat elke url in het begin aangeeft dat een website opgevraagd moet worden via het HTTP procotol.

<img src="images/http_in_url.png"></img>

Merk op dat websites tegenwoordig meestal **HTTPS** gebruiken. Hier staat de **S** voor **secure** ofwel **beveiligd**. **HTTPS** voegt een extra laag toe bovenop HTTP waarin de gegevens versleuteld zullen worden. Zo kunnen mensen die het bericht onderscheppen de inhoud ervan niet lezen.

</div>
</div>

