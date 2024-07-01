---
hruid: org-dwengo-pc-luchtkwaliteit-ens160
version: 1
language: nl
title: "VOS en AQI"
description: "Hoe kan ik de luchtkwaliteit meten?"
keywords: ["dwenguino", "microcontroller", "wifi", "i2c", "webserver", "internet", "co2", "luchtkwaliteit"]
content_type: "text/markdown"
estimated_time: 25
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

# Volatile organische stoffen (VOS) en air quality index (AQI)

Voor het meten van VOS en AQI gebruiken we de ENS160 sensormodule. Deze bevragen we vie **I²C**. De sensor heeft naast het meten van de hoeveelheid VOS ook de mogelijkheid om het CO<sub>2</sub> gehalte te schatten. Dit kan aan de hand van een berekening op basis van de hoeveelheid VOS. Deze is echter minder precies dus kiezen we er hier voor om het CO<sub>2</sub> gehalte met een andere sensor te meten.

## Aansluiten van de sensor
 
De ENS160 maakt gebruik van I²C. We sluiten de sensor dan ook zo aan op de Dwenguino.

<table>
    <tr>
        <th>Dwenguino</th>
        <th>ENS160</th>
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
        <td>15</td>
        <td>SDA</td>
    </tr>
    <tr>
        <td>14</td>
        <td>SCL</td>
    </tr>
    <tr>
        <td>-</td>
        <td>ADO</td>
    </tr>
</table>

<div class="dwengo-content important">
<h2 class="title">ADO pin</h2>
<div class="content">
De AD0 pin legt vast wat de waarde is van de laatste bit in het I²C adres van de sensor. Wanneer we AD0 verbinden met de grond, dan is die waarde 0, wanneer we die verbinden met de 5V, dan is deze waarde een 1. Dit systeem zorgt ervoor dat er twee sensoren op dezelfde I²C bus aangesloten kunnen worden.
</div>
</div>

## Waarden lezen via de seriële monitor


<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="luchtkwaliteit_serieel.cpp">

// Bibliotheken inladen
#include <Dwenguino.h>
#include <Wire.h>
#include "ScioSense_ENS160.h"

// Sensorobject maken
ScioSense_ENS160 ens160(ENS160_I2CADDR_0);

void setup() {
  initDwenguino();

  // Start de seriële communicatie
  Serial.begin(9600);
  while (!Serial) {}

  Serial.println("--------------------------------------------------");
  Serial.println("ENS160 - luchtkwaliteitsensor");
  Serial.println();
  Serial.println("--------------------------------------------------");
  delay(1000);

  // Initialiseer de sensor
  ens160.begin();
  Serial.println(ens160.available() ? "done." : "failed!");
  if (ens160.available()) {
    Serial.println("Instellen op standaard modus");
    Serial.println(ens160.setMode(ENS160_OPMODE_STD) ? "done." : "failed!");
  }
}

void loop() {
  // Doe een meting.  
  if (ens160.available()) {
    ens160.measure(true);
    ens160.measureRaw(true);
    Serial.print("AQI: ");
    Serial.print(ens160.getAQI());
    Serial.print("\t");
    Serial.print("TVOC: ");
    Serial.print(ens160.getTVOC());
    Serial.println("ppb");
  }
  delay(1000);
}

</code>
    </pre>
</div>


<div class="dwengo-content assignment">
<h2 class="title">Opdracht</h2>
<div class="content">
  <ul>
    <li>Sluit de ENS160 sensor aan op de Dwenguino.</li>
    <li>Open bovenstaande voorbeeld in de Dwengo simulator, compileer de code en zet deze over naar de Dwenguino.</li>
    <li>Bekijk de uitvoer van de sensor in de seriële monitor.</li>
  </ul>
</div>
</div>

<div class="dwengo-content important">
<h2 class="title">Geduld</h2>
<div class="content">
De ENS160 zal niet onmiddellijk een correcte waarde geven. De sensor heeft een stabilisatietijd van 1 uur. Dat wil dus zeggen dat je pas nadat de sensor 1 uur gewerkt heeft, betrouwbare waarden kan verwachten.
</div>
</div>


Wil je meer te weten komen over I²C, dan kan je terecht in het [leerpad over busprotocollen](https://staging.dwengo.org/learning-path.html?hruid=pc_leerlijn_bus_protocollen&language=nl&te=true&source_page=%2Fphysical_computing%2F&source_title=%20Physical%20computing#org-dwengo-pc-bus-protocollen-introductie-i2c;nl;1).