---
hruid: org_dwengo_gripit_hackathon_bibliotheken_firmware
version: 1
language: nl
title: "Grijperbibliotheken en BLE-firmware"
description: "Gebruik de Halberd-bibliotheken uit de Dwengo nRF52-core en bereid de firmware voor je grijper voor."
keywords: ["gripit", "hackathon", "halberd", "arduino", "servo", "sensor", "ble"]
educational_goals: []
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [17, 18]
difficulty: 3
estimated_time: 35
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

# Grijperbibliotheken en BLE-firmware

De bibliotheken die je nodig hebt voor de grijper zijn opgenomen in de [Dwengo nRF52-core](https://github.com/dwengovzw/dwengo_nrf52_core). De `Dwengo nRF52 Boards` heb je in de vorige stap geïnstalleerd via de boards manager.

### Wat doen de bibliotheken?

- `DwengoCompatibilityLayer` zorgt dat functies die ook beschikbaar zijn in de [Dwengo-simulator](https://blockly.dwengo.org) gebruikt kunnen worden in de Arduino IDE. Hierin worden ook een aantal pin aliassen gedefinieerd (bv. SERO_0 tot SERO_3).
- `HalberdGripper` implementeert het Airo Gripper Protocol (AGP) over BLE. Je sketch beschrijft de assen en posities en bepaalt hoe de motoren reageren.
- `HalberdGripperSensor` leest de analoge druksensor en de VL53L4CD-afstandssensor van de vingertopmodule. De sensorbibliotheek is optioneel voor het eerste BLE-voorbeeld.

**Tip:** Onder *File \> Examples \> HalberdGripper* vind je een aantal voorbeelden van hoe je de bibliotheek kan gebruiken. Je kan die al eens verkennen.

### Firmware voor een parallelle grijper.

De code die we in de Arduino IDE zullen schrijven noemen we de *firmware* van onze grijper. Deze firmware zal commando's ontvangen via de Bluetooth verbinding en deze omzetten in acties van de grijper. De firmware leest ook de sensoren van de grijper uit en stuurt die waarden terug naar de computer via Bleutooth.

Om het schrijven van de firmware van de grijper makkelijker te maken, zijn er een aantal bibliotheken voorzien. Deze vereenvoudigen het communicatieprotocol tussen de computer en de grijper. Hieronder volgen de instructies om een eenvoudige voorbeeldfirmware te uploaden naar het Halberdbord.  


1.  Open *File \> Examples \> HalberdGripper \> parallel_gripper_servo*. De [broncode](https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripper/examples/parallel_gripper_servo) is ook online beschikbaar. 
  
Deze firmware is geschreven om de [parallellogram-grijper](https://dwengo.org/learning-path.html?hruid=gripit_fiches&language=nl&te=true&source_page=%2Fgripit%2F&source_title=%20Grip-&gt;IT#org_dwengo_gripit_linkage_gripper_mechanica;nl;1) aan te sturen. Deze firmware stuurt de twee servo's van de grijper aan (SERVO_1 en SERVO_2). Deze servo's zijn verantwoordelijk voor de beweging van 1 as (axis) in dit geval is dat de afstand tussen de twee vingers van de parallellogram-grijper. In deze firmware heeft deze grijper maar twee standen (poses): *open* en *closed*. De firmware zal luisteren naar open en close commando's via de Bluetooth verbinding en zo de grijper aansturen.

2.  Kies een unieke `GRIPPER_NAME` voor je team, straks gebruik je exact dezelfde naam in je Python programma. De naam van de grijper wordt gebruikt om de Bluetooth connectie op te zetten.

We sturen de grijper aan door de afstand tussen de vingers in te stellen. Die afstand moeten we dan omzetten naar de juiste servo hoeken. Daarvoor dient de *widthToAngle* functie. Deze omzetten noemen we de inverse kinematica berekening van de grijper.

3. Compileer en upload deze firmware naar Halberd. Controleer via de seriële monitor dat de firmware correct is geupload. Dat is zo als de uitvoer de tekst *Width: 0.079 m* bevat.



De voorbeeldsketch rapporteert een berekende doel-/tussenpositie, geen gemeten vingeropening. De opgegeven snelheid en grijpkracht zijn niet automatisch fysiek begrensd. Test en implementeer zo nodig zelf grenzen, stopgedrag en feedback; verbindingsverlies is geen noodstop.


