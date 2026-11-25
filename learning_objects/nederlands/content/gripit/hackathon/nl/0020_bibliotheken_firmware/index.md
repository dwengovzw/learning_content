---
hruid: org_dwengo_gripit_hackathon_bibliotheken_firmware
version: 1
language: nl
title: "Grijperbibliotheken en BLE-firmware"
description: "Installeer de Halberd-bibliotheken en bereid de firmware voor je grijper voor."
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

Wij hebben al een aantal bibliotheken voorzien die het makkelijker maken om je eigen robotgrijper te bouwen. Hieronder lees je hoe je die kan installeren.

### Wat doen de bibliotheken?

- [DwengoCompatibilityLayer](https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/DwengoCompatibilityLayer) zorgt dat alle functies die ook beschikbaar zijn inde [dwengo simulator](https://blockly.dwengo.org) ook gebruikt kunnen worden in de Arduino IDE.
- [HalberdGripper](https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripper) implementeert het Airo Gripper Protocol (AGP) over BLE. Je sketch beschrijft de assen en posities en bepaalt hoe de motoren reageren. 
- [HalberdGripperSensor](https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripperSensor) leest de analoge druksensor en de VL53L4CD-afstandssensor van de vingertopmodule. De sensorbibliotheek is optioneel voor het eerste BLE-voorbeeld.

De bibliotheken worden ook gebruikt in de online programmeeromgeving, maar zijn niet automatisch beschikbaar in je Arduino-sketchbook.

### Installeer vanuit GitHub

1.  Download de bibliotheken: [DwengoCompatibilityLayer.zip](https://raw.githubusercontent.com/dwengovzw/Blockly-for-Dwenguino/refs/heads/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/DwengoCompatibilityLayer/DwengoCompatibilityLayer.zip), [HalberdGripper.zip](https://raw.githubusercontent.com/dwengovzw/Blockly-for-Dwenguino/refs/heads/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripper/HalberdGripper.zip) en [HalberdGripperSensor.zip](https://raw.githubusercontent.com/dwengovzw/Blockly-for-Dwenguino/refs/heads/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripperSensor/HalberdGripperSensor.zip).
2.  Kies in Arduino IDE *Sketch \> Include Library \> Add .ZIP Library...* en selecteer de gedownloade ZIP-bestanden één voor één.
3.  Herstart de IDE, selecteer de Halberd en controleer onder *File \> Examples* of de voorbeelden van `HalberdGripper` zichtbaar zijn en, indien geïnstalleerd, ook die van `HalberdGripperSensor`.

### Bereid een parallelle grijper voor

1.  Open *File \> Examples \> HalberdGripper \> parallel_gripper_servo*. De [broncode](https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripper/examples/parallel_gripper_servo) is ook online beschikbaar. Sla een eigen kopie op voordat je wijzigingen maakt.
2.  Kies een unieke `GRIPPER_NAME` voor je team en gebruik exact dezelfde naam in Python. Het voorbeeld configureert een parallelle as, de poses `open` en `closed`, callbacks en positie-updates. `gripper.update()` moet regelmatig in `loop()` uitgevoerd worden.
3.  Het Dwengo-boardpakket 1.0.0 kent de namen `SERVO_1` en `SERVO_2` uit de sketch niet. Vervang ze in je eigen kopie respectievelijk door `D1` en `D2`. Dit behoudt de pinnummers van het oorspronkelijke voorbeeld; de boarddefinitie duidt D1 en D2 aan als respectievelijk SERVO2 en SERVO3. Controleer altijd de labels en bedrading van jouw bord.
4.  Pas de servo-aansluitingen, pulsbreedtes, openingsgrenzen in meter, geometrie en hoekberekening aan jouw mechanisme aan. De sketch stuurt twee servo's aan; vertrouw niet op de beschrijving bovenaan de sketch als die van de code verschilt. De sensorwaarden in dit voorbeeld zijn gesimuleerd.
5.  Verifieer en upload de aangepaste sketch. Open de seriële monitor op 115200 baud om de opstartmelding te bekijken; de Halberd adverteert vervolgens met de ingestelde naam.

**Veilig testen:** schakel de voeding uit bij het aansluiten, controleer GND, 5V en PWM en gebruik een geschikte voeding voor je servo's. Begin zonder voorwerp en met beperkte, gecontroleerde bewegingen; houd vingers uit het mechanisme. Servohoeken en geometrie uit het voorbeeld zijn geen veilige universele kalibratie. Zet bij onverwachte beweging de voeding uit.

De voorbeeldsketch rapporteert een berekende doel-/tussenpositie, geen gemeten vingeropening. De opgegeven snelheid en grijpkracht zijn niet automatisch fysiek begrensd. Test en implementeer zo nodig zelf grenzen, stopgedrag en feedback; verbindingsverlies is geen noodstop.

### Optioneel: echte sensoren

Bekijk *HalberdGripperSensor \> read_pressure_and_distance* voor een seriële sensortest en *HalberdGripper \> parallel_gripper_servo_with_sensors* voor integratie met BLE. Pas ook in die integratiesketch de servoaliassen aan zoals hierboven. Volg de bedrading en I2C-bus in de betreffende sketch: de integratiesketch gebruikt `Wire` en druk op `A0`. Controleer de module en voedingsspanning vóór het aansluiten. Drukspanning is niet rechtstreeks een gekalibreerde kracht; een afstandsmeting kan ongeldig zijn.
