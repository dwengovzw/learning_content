---
hruid: org_dwengo_gripit_hackathon_parallelle_grijper_firmware
version: 1
language: nl
title: "Firmware voor een parallelle grijper"
description: "Bereid firmware voor om een parallelle grijper via BLE aan te sturen."
keywords: ["gripit", "hackathon", "halberd", "arduino", "servo", "sensor", "ble"]
educational_goals: []
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [17, 18]
difficulty: 3
estimated_time: 25
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

# Firmware voor een parallelle grijper

In de vorige stap testte je de BLE-verbinding zonder grijper. Nu bereid je firmware voor die Bluetooth-commando's omzet in bewegingen van een echte [parallellogram-grijper](https://dwengo.org/learning-path.html?hruid=gripit_fiches&language=nl&te=true&source_page=%2Fgripit%2F&source_title=%20Grip-&gt;IT#org_dwengo_gripit_linkage_gripper_mechanica;nl;1).

### Het voorbeeld begrijpen

Open in de Arduino IDE *File \> Examples \> HalberdGripper \> parallel_gripper_servo*. De [broncode](https://github.com/dwengovzw/dwengo_nrf52_core/tree/main/nrf52/1.0.1/libraries/HalberdGripper/examples/parallel_gripper_servo) is ook online beschikbaar. Sla een eigen kopie op voordat je wijzigingen maakt.

De firmware stuurt twee servo's aan via `SERVO_1` en `SERVO_2`. Samen bewegen ze één as: de afstand tussen de vingers van de grijper. De sketch definieert twee standen (*poses*), `open` en `closed`. Bij een overeenkomstig BLE-commando stelt een callback een nieuwe doelbreedte in.

De functie `widthToAngle` zet de gewenste afstand tussen de vingers om naar een servohoek. Deze omzetting heet de inverse kinematica van de grijper. In `loop()` beweegt de berekende breedte naar de doelwaarde; `reportPosition()` rapporteert die waarde en `gripper.update()` verzorgt de communicatie.

### Pas de firmware aan en upload

1. Kies een unieke `GRIPPER_NAME` voor je team. Gebruik in de volgende Python-stap exact dezelfde naam.
2. Pas de servo-aansluitingen, pulsbreedtes, openingsgrenzen in meter, geometrie en hoekberekening aan jouw mechanisme aan. Controleer de labels en bedrading van jouw bord. De standaardwaarden zijn niet voor elke grijper geschikt.
3. Compileer en upload de firmware naar Halberd. Open de seriële monitor op 115200 baud en controleer de opstartmelding `HalberdGripper advertising as ...` met jouw naam.

**Veilig testen:** schakel de voeding uit bij het aansluiten, controleer GND, 5V en PWM en gebruik een geschikte voeding voor je servo's. Begin zonder voorwerp en met beperkte, gecontroleerde bewegingen; houd vingers uit het mechanisme. Zet bij onverwachte beweging de voeding uit.

De voorbeeldsketch rapporteert een berekende doel-/tussenpositie, geen gemeten vingeropening. De opgegeven snelheid en grijpkracht zijn niet automatisch fysiek begrensd. Test en implementeer zo nodig zelf grenzen, stopgedrag en feedback; verbindingsverlies is geen noodstop.

In de volgende stap verbind je Python met deze firmware en test je de standen `open` en `closed`.
