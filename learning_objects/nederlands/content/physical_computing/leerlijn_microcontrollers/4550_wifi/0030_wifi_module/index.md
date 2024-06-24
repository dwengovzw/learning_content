---
hruid: org-dwengo-pc-wifi-esp
version: 1
language: nl
title: "De wifi module"
description: "Hoe kan ik communiceren via wifi?"
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

# De wifi module

De Dwenguino heeft standaard geen manier om verbinding te maken met het internet. Toch kan je dat makkelijk doen door er een wifi module mee te verbinden. Wij maken gebruik van de **ESP-01** module. Op deze module zit een **ESP-8266** chip die de verbinding met het wifi netwerk zal uitvoeren. Hieronder zie je een afbeelding van links de ESP-01 module en rechts de ESP-8266 chip met antenne. Je kan de ESP-8266 makkelijk inpluggen op de ESP-01 module.

![Voorbeeld van de esp-01 module met esp-8266 chip.](images/esp_01.jpg)

## Aansluiten op de Dwenguino

De **ESP-01** kan via **UART** spreken met de Dwenguino. Om de module met de Dwenguino te verbinden heb je dus vier male-female draden nodig. Deze kan je verbinden volgens de volgende tabel. Gebruik daarvoor de connector boven het lcd-scherm op de Dwenguino.

<table>
    <tr>
        <th>Dwenguino</th>
        <th>ESP-01</th>
    </tr>
    <tr>
        <td>+</td>
        <td>VCC</td>
    </tr>
    <tr>
        <td>-</td>
        <td>GND</td>
    </tr>
    <tr>
        <td>TX</td>
        <td>RX</td>
    </tr>
    <tr>
        <td>RX</td>
        <td>TX</td>
    </tr>
</table>

