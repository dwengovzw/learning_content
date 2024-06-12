---
hruid: org-dwengo-pc-bus-protocollen-introductie-i2c
version: 1
language: nl
title: "I²C"
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

## Bedrading

I²C maakt gebruik van twee draden voor de communicatie, deze krijgen de namen <code class="lang-cpp">SDA</code> en <code class="lang-cpp">SCL</code>. <code class="lang-cpp">SDA</code> staat voor seriële data en <code class="lang-cpp">SCL</code> voor seriële klok. Het I²C protocol verwacht dat de spanning op deze lijnen standaard hoog is (5V). Daarom worden de <code class="lang-cpp">SDA</code> en <code class="lang-cpp">SCL</code> hoog getrokken via een pull-up weerstand. De waarde van deze weerstand is minimaal \\(1.6\mathrm{K \Omega}\\). De maximale waarde die je voor de pull-up weerstand kan gebruiken hangt af van de capaciteitswaarde van de bus. Hoe hoger deze capaciteitswaarde, hoe lager de waarde van de pull-up weerstand moet zijn. Je wil eigenlijk een zo hoog mogelijke waarde voor de pull-up weerstand met de voorwaarde dat deze laag genoeg is om het systeem te doen werken. Een hogere waarde voor de pull-up weerstand zorgt er immers voor dat er minder stroomverbruik zal zijn. Voor eenvoudige schakelingen, met korte draden en weinig apparaten op de bus, kan je de interne pull-up weerstanden van de microcontroller gebruiken. De waarde van de interne pull-up weerstand ligt tussen de \\(20\mathrm{K \Omega}\\) en \\(50\mathrm{K \Omega}\\). 

Op onderstaande afbeelding zie je hoe verschillende apparaten op een I²C bus aangesloten kunnen worden.

![Een voorbeeld van een aantal devices op een I²C bus.](images/i2c.svg)

Op de Dwenguino zijn standaard twee pinnnen voorzien met de nodige logica om gegevens te sturen via I²C. Pin <code class="lang-cpp">15</code> moet je verbinden met de <code class="lang-cpp">SDA</code> lijn. Pin <code class="lang-cpp">14</code> met de <code class="lang-cpp">SCL</code> lijn.

## Werking

Het apparaat dat de controle heeft over de bus (de master), is deze verantwoordelijk om de communicatie met een van de randapparaten (slaves) te starten. Hieronder zie je een voorbeeld van het verloop van de communicatie tussen master en slave wanneer de master een waarde wil schrijven in een register van de slave. Je leest de tabel van links naar rechts. Elke kolom stelt een transmissie op de bus voor en zal ofwel door de master ofwel door de slave verstuurd worden.

<table>
    <tr>
        <th>Master</th>
        <td>START</td>
        <td>ADRES + SCHRIJF_BIT</td>
        <td></td>
        <td>REGISTER ADRES</td>
        <td></td>
        <td>DATA</td>
        <td></td>
        <td>STOP</td>
    </tr>
    <tr>
        <th>Slave</th>
        <td></td>
        <td></td>
        <td>ACK</td>
        <td></td>
        <td>ACK</td>
        <td></td>
        <td>ACK</td>
        <td></td>
    </tr>
</table>

Elke transmissie in de tabel komt overeen met een specifiek signaal op de <code class="lang-cpp">SDA</code> en <code class="lang-cpp">SCL</code> lijnen. Hieronder lees je een korte beschrijving van deze transmissies.

* **START**: De start conditie geeft aan dat er een I²C transmissie zal starten. Om dit duidelijk te maken zal de master de <code class="lang-cpp">SDA</code> en <code class="lang-cpp">SCL</code> hoog zetten en daarna de <code class="lang-cpp">SDA</code> lijn terug laag brengen. Deze overgang van de <code class="lang-cpp">SDA</code> lijn maakt aan de apparaten op de bus duidelijk dat er een transmissie gestart is.
* **ADRES + SCHRIJF_BIT**: De volgende transmissie komt ook van de master. Deze zal het adres van de slave die hij wil aanspreken op de bus plaatsen. Dit adres bestaat uit 7 bits. Aan dat adres wordt nog een achtste bit toegevoegd die aangeeft of de master wil schrijven naar of lezen van de slave. In dit geval wil de master schrijven naar de slave dus is die achtste bit gelijk aan \\(0\\).
* **ACK**: Dit staat voor acknowledge, het is een signaal van de slave aan de master om te laten weten dat deze de boodschap goed ontvangen heeft. De slave stuurt een acknowledge door de <code class="lang-cpp">SDA</code> lijn hoog te houden voor een volledige duty-cycle van het signaal op de <code class="lang-cpp">SCL</code> lijn (= de tijd van de hoge puls).
* **REGISTER ADRES**: Dit is het adres van het register op de slave waar de master naar wil schrijven. Bij een temperatuursensor kan dit bijvoorbeeld een register zijn waarin je kan instellen of de temperatuur in Celsius of in Fahrenheit gemeten moet worden.
* **DATA**: Dit is de data die in het register van de slave geschreven moet worden.
* **STOP**: De stop conditie geeft aan dat de transmissie voorbij is. De master zal deze genereren door de <code class="lang-cpp">SDA</code> lijn laag te brengen en de <code class="lang-cpp">SCL</code> lijn hoog. En daarna de <code class="lang-cpp">SDA</code> lijn terug hoog te brengen.



## Hoe programmeren


Om te communiceren via I²C, kan je gebruik maken van de Wire bibliotheek. Hieronder zie je een codevoorbeeld voor de transmissie die we hierboven in het blokschema uitlegden.

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="i2c_schrijf_voorbeeld.cpp">

#include <Dwenguino.h>
#include <Wire.h>


#define ADR_WRITE 0b11010000
#define ADR_REGISTER 0b00011100
void setup()
{
  initDwenguino();
  Wire.begin(); // Start de transmissie (START)
}
unsigned char data = 0b11100011;
void loop()
{
  Wire.beginTransmission(ADR_WRITE);    // Stuur naar apparaat met adres 0b1101000
  Wire.write(ADR_REGISTER);             // Stuur het register adres.
  Wire.write(data);                     // Stuur de data voor het register.
  Wire.endTransmission();               // STOP
  delay(500);
}

</code>
    </pre>
</div>


<div class="dwengo-content sideinfo">
<h2 class="title">Bibliotheken</h2>
<div class="content">
De Wire bibliotheek is basisbibliotheek die je altijd kan gebruiken om met apparaten te communiceren via I²C. Toch moet je de Wire bibliotheek zelf vaak niet gebruiken wanneer je via I²C wil spreken met een sensor. Dit komt omdat veel sensoren een eigen bibliotheek hebben die het makkelijk maakt om de waarde van de sensor te lezen over I²C. De communicatie met de Wire bibliotheek zit dan verborgen in de bibliotheek van de sensor.
</div>
</div>