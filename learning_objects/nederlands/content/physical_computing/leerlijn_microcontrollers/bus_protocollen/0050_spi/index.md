---
hruid: org-dwengo-pc-bus-protocollen-introductie-spi
version: 1
language: nl
title: "SPI"
description: "Communicatie via spi?"
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

# SPI

SPI staat voor *serial peripheral interface* en legt een methode vast waarop geïntegreerde schakelingen met elkaar kunnen communiceren. De standaard werd in 1980 ontwikkeld door Motorola. 

## Bedrading

SPI maakt gebruik van minimaal vier draden om informatie uit te wisselen tussen systemen. Deze draden krijgen de volgende namen:

<table>
<tr>
<th>Afkorting</th>
<th>Naam</th>
<th>Beschrijving</th>
</tr>
<tr>
<td><code class="lang-cpp" style="text-decoration:overline">CS</code></td>
<td>Chip Select</td>
<td>Vanop de master vertrekt er een <code class="lang-cpp" style="text-decoration:overline">CS</code> draad naar elke slave. De master zal het signaal op de draad van de slave waarmee deze wil communiceren naar 0V brengen. Zo weet de slave dat die moet luisteren op de bus.</td>
</tr>
<tr>
<td><code class="lang-cpp">SCLK</code></td>
<td>Serial Clock</td>
<td>De master zal op de <code class="lang-cpp">SCLK</code> lijn een blokgolf sturen. Elke keer dat deze blokgolf van een lage waarde naar een hoge waarde gaat (rising edge) zullen de master en slave de waarde op respectivelijk de <code class="lang-cpp">MISO</code> en <code class="lang-cpp">MOSI</code> lijnen inlezen.</td>
</tr>
<tr>
<td><code class="lang-cpp">MOSI</code></td>
<td>Master Out, Slave In</td>
<td>Op deze draad wordt de data gezet die <strong>van de master naar de slave gaat</strong>.</td>
</tr>
<tr>
<td><code class="lang-cpp">MISO</code></td>
<td>Master In, Slave Out</td>
<td>Op deze draad wordt de data gezet die <strong>van de slave naar de master gaat</strong>.</td>
</tr>
</table>

Wanneer er maar één master en één slave met elkaar communiceren, zijn er vier draden nodig. Voor elke extra slave op de bus komt er echter een <code class="lang-cpp" style="text-decoration:overline">CS</code> lijn bij. Dit is een van de nadelen van SPI. Het voordeel van SPI is dan weer dat we op hetzelfde moment in twee richtingen data kunnen sturen via de <code class="lang-cpp">MOSI</code> en <code class="lang-cpp">MISO</code> lijnen. Bijgevolg spreken we hier van een **full-duplex** protocol.

Op onderstaande afbeelding kan je zien hoe je apparaten via een SPI bus kan verbinden.

![Een voorbeeld van een SPI schakeling.](images/spi.svg)