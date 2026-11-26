---
hruid: org_dwengo_gripit_hackathon_pid_grijper
version: 1
language: nl
title: "Drukgeregelde grijper met Python"
description: "Onderzoek de drukregelende firmware en bestuur de open- en sluitstand via BLE."
keywords: ["gripit", "hackathon", "halberd", "arduino", "python", "ble", "pid", "sensor"]
educational_goals: []
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [17, 18]
difficulty: 4
estimated_time: 35
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

# Drukgeregelde grijper met Python

De eerdere sensorfirmware stuurde metingen naar de computer. Dit voorbeeld gebruikt de druksensor ook als **terugkoppeling**: bij een sluitcommando probeert de Halberd een ingestelde sensorwaarde te bereiken en daarna te behouden. De regeling loopt op de Halberd; Python verstuurt enkel commando's via BLE.

## Eerst veilig voorbereiden

Werk onder begeleiding. Schakel alle voeding uit voordat je bedrading aanpast en controleer de aansluitingen zoals in de vorige sensoractiviteit. Houd vingers, dieren en kwetsbare voorwerpen uit de grijper. Zorg dat je de servovoeding onmiddellijk en onafhankelijk van software kunt uitschakelen; een BLE-commando of verbindingsverlies is geen noodstop.

De voorbeeldwaarden zijn **niet automatisch veilig** voor jouw sensor, servomotoren, mechaniek of voorwerp. Een defecte of losgekoppelde druksensor wordt niet betrouwbaar herkend; de grijper kan dan blijven sluiten tot een grens of de tijdslimiet. De timeout en softwaregrenzen zijn geen bescherming tegen letsel of beschadiging. Laat de sensorrespons, bewegingsrichting, servohoeken, pulsbreedtes en doelwaarde eerst met begeleiding voor jouw opstelling controleren en kalibreren. Gebruik de drukwaarde niet als gekalibreerde kracht.

## Bekijk de firmware

1. Open in Arduino IDE *File \> Examples \> HalberdGripper \> parallel_gripper_servo_with_sensors_pid*. Dit is het voorbeeld in `Dwengo nRF52 Boards` versie 1.0.1. De [broncode](https://github.com/dwengovzw/dwengo_nrf52_core/tree/main/nrf52/1.0.1/libraries/HalberdGripper/examples/parallel_gripper_servo_with_sensors_pid) is ook online beschikbaar. Sla eerst een eigen kopie op.
2. Gebruik een unieke `GRIPPER_NAME`. Neem alleen instellingen over die voor jouw opstelling veilig zijn gecontroleerd. De sketch gebruikt twee servo's op `D1` en `D2`, de druksensor op `A0` en de afstandssensor op `Wire`. De afstandscompensatie van het voorbeeld is specifiek voor de opstelling en hoeft niet bij jouw sensor te passen.
3. Na de veiligheidscontrole: compileer en upload. Let op: bij het opstarten stuurt de sketch de servo's naar de openhoek, nog vóór een Python-commando. Controleer in de seriële monitor op 115200 baud de melding `HalberdGripper advertising as ...`. Bij fouten in de afstandssensor, servo-initialisatie of BLE wordt `ready` niet ingeschakeld; controleer de foutmelding en schakel de voeding uit voordat je iets aanpast.

## Wat gebeurt er in de code?

| Onderdeel | Functie |
|---|---|
| `targetPressure`, `pressureDeadband` | Doelwaarde en toegelaten afwijking in ruwe ADC-counts; niet in newton. |
| `kp`, `ki`, `kd` | Versterkingen voor de drukregeling. Standaard is `ki = kd = 0`: alleen P werkt mee. |
| `pressureSpeed(error, dt)` | Berekent een begrensde servohoeksnelheid op basis van fout en tijd. |
| `OPENING` | Beweegt naar de openhoek en meldt de opdracht daarna als voltooid. |
| `ACQUIRE_PRESSURE` | Regelt naar de drukdoelwaarde. Na 100 ms binnen de dode zone meldt de sketch voltooiing; na 10 s zonder stabiele meting meldt ze een fout. |
| `HOLD_PRESSURE` | Blijft na voltooiing de druk regelen. |
| `HOLD` | Stopt de regeling en houdt de laatst aangestuurde servohoek vast; dit is niet automatisch openen of uitschakelen. |

`onOpen` en `onClose` plaatsen een verzoek voor de hoofdlus. `loop()` leest de druk, voert de regeling uit en roept `gripper.update()` aan. De opgegeven openingsbreedte wordt uit de **aangestuurde** servohoek geschat, niet met een positiesensor gemeten. `tof` en `pressure` zijn BLE-sensorwaarden; de laatste is spanning in volt, terwijl de regelaar ruwe counts gebruikt. De afstandswaarde kan ontbreken, nul zijn of verouderd raken.

De sketch implementeert de standen `open` en `closed`, maar geen callback voor een willekeurige `move`-positie. De drukdoelwaarde en regelaarversterkingen staan in de firmware; Python past ze met dit voorbeeld niet aan.

## Bedien de standen vanuit Python

Gebruik de bestaande werkmap en virtuele omgeving uit de vorige stappen. Sluit `sensoren.py` en andere BLE-clients voordat je verbindt. Maak een nieuw bestand `pid_grijper.py` en gebruik dezelfde naam als `GRIPPER_NAME` in de firmware. Lees de veiligheidsinstructies hierboven voordat je een commando uitvoert.

```python
import time

from airo_robots.grippers import GenericHalberdGripper
from airo_robots.grippers.hardware.halberd_ble.client import CommandStatus

gripper = GenericHalberdGripper.connect(name="gripper-left-pid")
try:
    def pose(name):
        sequence = gripper.client.move_pose(name)
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            if not gripper.client.is_connected:
                raise ConnectionError("BLE-verbinding verloren")
            status = gripper.client.command_status(sequence)
            if status == CommandStatus.DONE:
                return
            if status == CommandStatus.FAILED:
                raise RuntimeError(f"Commando {name} is mislukt; controleer de seriële monitor")
            time.sleep(0.1)
        raise TimeoutError(f"Geen voltooiing voor {name}; controleer de grijper")

    input("Controleer de vrije ruimte. Druk op Enter om te openen, of Ctrl+C om te stoppen: ")
    pose("open")
    input("Controleer de opstelling met de begeleider. Enter sluit de grijper; Ctrl+C stopt: ")
    pose("closed")
    print("Drukdoel bereikt; de regeling blijft actief.")
    input("Controleer de vrije ruimte. Druk op Enter om te openen, of Ctrl+C om te stoppen: ")
    pose("open")
finally:
    gripper.disconnect()
```

Start met `python pid_grijper.py`. De eerste Enter geeft een opencommando; de tweede geeft pas een sluitcommando. De derde opent opnieuw. Een leeg of ongeschikt voorwerp kan ervoor zorgen dat de druk niet bereikt wordt: de firmware meldt dan na de timeout een fout. Het programma controleert expliciet `DONE` en `FAILED`, omdat de gewone `.wait()` in deze driver ook bij een mislukt commando kan terugkeren. Controleer bij een fout of time-out de seriële uitvoer; ga niet automatisch verder.

Ook na een geslaagde sluitopdracht blijft de drukregeling actief totdat je opent, stopt of de verbinding verbreekt. Bij `STOP` of een verbroken verbinding gaat de firmware naar `HOLD`: ze behoudt de laatst aangestuurde hoek en laat een voorwerp niet noodzakelijk los. Een onderbreking in Python verbreekt de verbinding, maar vervangt de onafhankelijke uitschakeling niet.

## Vergelijk met de metingen

Sluit `pid_grijper.py` voordat je de grafiek uit de vorige stap gebruikt. Pas daarin de BLE-naam aan naar `gripper-left-pid` of jouw gekozen naam. De grafiek toont de laatst ontvangen spanning en afstand, niet de ruwe fout, de PID-bijdragen of een gegarandeerd actuele afstand. Gebruik de grafiek om gegevens te onderzoeken, niet als veiligheidsbewaking.
