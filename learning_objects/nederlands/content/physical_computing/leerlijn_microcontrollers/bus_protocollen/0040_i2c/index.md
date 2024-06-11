---
hruid: org-dwengo-pc-bus-protocollen-introductie-i2c
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

# I²C

I²C (*I kwadraat C*) staat voor *inter-integrated circuit* en is dus ontworpen voor communicatie tussen geïntegreerde schakelingen (bv. microcontrollers). De standaard werd in 1982 ontwikkeld door Philips (nu NXP Semiconductors) en wordt nog steeds heel vaak gebruikt. 

I²C maakt gebruik van twee draden voor de communicatie <code class="lang-cpp">SDA</code> en <code class="lang-cpp">SCL</code>. <code class="lang-cpp">SDA</code> staat voor seriële data en <code class="lang-cpp">SCL</code> voor seriële klok. Het I²C protocol verwacht dat de spanning op deze lijnen standaard hoog is (5V). Daarom worden de <code class="lang-cpp">SDA</code> en <code class="lang-cpp">SCL</code> hoog getrokken via een pull-up weerstand. Op onderstaande afbeelding zie je hoe verschillende apparaten op een I²C bus aangesloten kunnen worden.

![Een voorbeeld van een aantal devices op een I²C bus.](images/i2c.svg)

