---
hruid: org_dwengo_gripit_hackathon_bibliotheken_firmware
version: 1
language: nl
title: "Basiscommunicatie met BLE"
description: "Maak met de Halberd-bibliotheek een eerste BLE-verbinding en laat de led knipperen."
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

# Basiscommunicatie met BLE

De bibliotheken die je nodig hebt voor de grijper zijn opgenomen in de [Dwengo nRF52-core](https://github.com/dwengovzw/dwengo_nrf52_core). Installeer of update `Dwengo nRF52 Boards` via de Boards Manager tot versie 1.0.1 of nieuwer, zoals beschreven in de vorige stap. Je hoeft de bibliotheken niet apart te installeren.

### Wat doen de bibliotheken?

- `DwengoCompatibilityLayer` zorgt dat functies die ook beschikbaar zijn in de [Dwengo-simulator](https://blockly.dwengo.org) gebruikt kunnen worden in de Arduino IDE.
- `HalberdGripper` implementeert het Airo Gripper Protocol (AGP) over BLE. Je sketch beschrijft de assen en posities en bepaalt hoe de motoren reageren.
- `HalberdGripperSensor` leest de analoge druksensor en de VL53L4CD-afstandssensor van de vingertopmodule. De sensorbibliotheek is optioneel voor het eerste BLE-voorbeeld.

**Tip:** Onder *File \> Examples \> HalberdGripper* vind je een aantal voorbeelden van hoe je de bibliotheek kan gebruiken. Je kan die al eens verkennen.

### Firmware voor basiscommunicatie

De code op het Halberdbord noemen we de *firmware*. Met het voorbeeld `identify_only` test je de Bluetooth Low Energy-verbinding (BLE) tussen de computer en de Halberd. Je hebt hiervoor geen grijper, servo's of sensoren nodig: de firmware beweegt geen motoren en voert geen grijperbewegingen uit.

1. Open *File \> Examples \> HalberdGripper \> identify_only*. Sla eventueel een eigen kopie op om die te wijzigen. Het voorbeeld bevat deze code:

```cpp
#include <HalberdGripper.h>

HalberdGripper gripper;

void setup() {
  Serial.begin(115200);

  gripper.configureAxis(0, 0.0f, 0.079f, 0.25f);

  if (!gripper.begin("my-first-gripper")) {
    Serial.println("Failed to start HalberdGripper BLE");
    while (true) {
      delay(1000);
    }
  }
  Serial.println("HalberdGripper advertising as my-first-gripper");
}

void loop() {
  gripper.update();
  delay(10);
}
```

`configureAxis` beschrijft een fictieve as die de Python-driver verwacht. De grenzen en snelheid zijn hier enkel beschrijvende waarden: er wordt geen positie gemeten en niets beweegt. `begin` start BLE en maakt het bord vindbaar onder de naam `my-first-gripper`. Als opstarten mislukt, verschijnt een foutmelding en stopt de sketch in de `while`-lus. `gripper.update()` verwerkt onder meer het knipperen van de led en moet regelmatig worden uitgevoerd.

2. Gebruik voor elk team een unieke naam in `gripper.begin(...)`. Pas ook de tekst in de daaropvolgende `Serial.println(...)` aan zodat de melding overeenkomt. Gebruik straks exact dezelfde naam in Python.
3. Selecteer de Halberd en de juiste poort, compileer en upload de sketch. Open de seriële monitor op 115200 baud. Bij de standaardnaam verschijnt `HalberdGripper advertising as my-first-gripper`; een foutmelding wijst erop dat BLE niet is gestart.

### Test de verbinding met Python

Laat de Halberd ingeschakeld en schakel Bluetooth op je computer in. Maak een map op je computer waarin je het Python programma zal opslaan. Open een terminal in deze map (PowerShell op Windows, bash op linux) Installeer de Python-driver in een virtuele omgeving met Python 3.11 of nieuwer. Gebruik op Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "airo-robots[halberd]"
```

Gebruik op macOS of Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "airo-robots[halberd]"
```

Controleer met `python --version` of de actieve omgeving Python 3.11 of nieuwer gebruikt. Bewaar deze omgeving voor de latere Python-stap.

Sla het volgende op als `identify.py`. Als je de naam in de firmware wijzigde, gebruik dan hier dezelfde naam:

```python
from airo_robots.grippers import HalberdBLEGripper

gripper = HalberdBLEGripper.connect(name="my-first-gripper")
try:
    gripper.identify()
finally:
    gripper.disconnect()
```

Voer `python identify.py` uit in de actieve omgeving. Het `identify`-commando laat de ingebouwde led van de Halberd kort knipperen, zodat je het verbonden bord kunt herkennen. De bibliotheek verzorgt dit knipperen; de sketch hoeft de led niet zelf aan te sturen. `disconnect()` sluit de verbinding.

Lukt de verbinding niet, controleer dan de bordvoeding, Bluetooth, de exacte naam, de seriële melding en of een andere toepassing al verbonden is. Controleer bij een importfout of de virtuele omgeving actief is. Hierna kun je firmware voor een echte parallelle grijper voorbereiden.


