---
hruid: org_dwengo_gripit_hackathon_python_ble
version: 1
language: nl
title: "Bestuur je grijper met Python en BLE"
description: "Verbind airo-robots met je Halberd-grijper en test een eenvoudige grijptaak."
keywords: ["gripit", "hackathon", "halberd", "python", "ble", "airo"]
educational_goals: []
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [17, 18]
difficulty: 3
estimated_time: 30
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

# Bestuur je grijper met Python en BLE

## Van draadloze verbinding naar een eerste grijptaak

### Installeer de Python-driver

Upload eerst de aangepaste `parallel_gripper_servo`-firmware uit de vorige stap en laat de Halberd ingeschakeld. Schakel Bluetooth op je computer in. Deze firmware gebruikt AGP, niet de Nordic UART Service uit andere BLE-voorbeelden.

Maak met Python 3.11 of nieuwer een virtuele omgeving aan in je werkmap en installeer de driver. Gebruik op Windows PowerShell:

    py -3 --version
    py -3 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install "airo-robots[halberd]"

Gebruik op macOS of Linux:

    python3 --version
    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install "airo-robots[halberd]"

Controleer met `python --version` of de geactiveerde omgeving Python 3.11 of nieuwer gebruikt. Op Linux moet de Bluetooth-service actief zijn en moet de gebruiker toegang hebben tot BlueZ. De [airo-mono-documentatie](https://github.com/airo-ugent/airo-mono/blob/main/airo-robots/airo_robots/grippers/hardware/halberd_ble.md) beschrijft de driver en extra mogelijkheden.

### Verbind, open en sluit

Sla dit op als `gripper.py`. Vervang de naam door jouw `GRIPPER_NAME`. Test eerst zonder voorwerp, nadat de bewegingen en grenzen in de firmware veilig zijn gekalibreerd.

``` python
from airo_robots.grippers import HalberdBLEGripper

print("Gevonden:", HalberdBLEGripper.discover())
gripper = HalberdBLEGripper.connect(name="gripper-left")
try:
    gripper.identify()
    gripper.open().wait()
    gripper.close().wait()
    gripper.open().wait()
finally:
    gripper.disconnect()
```

Start met `python gripper.py`. De LED knippert kort bij `identify()`; de grijper opent, sluit en opent opnieuw. `wait()` wacht op de voltooiingsmelding van de firmware, niet op een onafhankelijke meting. Ontbreekt beweging of volgt een fout, controleer dan de firmware en onderbreek indien nodig de voeding.

Voor een parallelle grijper kun je ook `gripper.move(0.02).wait()` gebruiken: de gewenste opening is hier 0,02 meter en moet binnen je gekalibreerde bereik liggen. De driver begrenst aanvragen tot de door de firmware opgegeven grenzen. Andere mechanismen kunnen `GenericHalberdGripper` met eigen assen en poses gebruiken.

### Problemen oplossen

- Geen grijper gevonden? Controleer Bluetooth, voeding, de AGP-firmware, de exacte naam en of een andere client al verbonden is. Een verbonden grijper adverteert niet.
- Meerdere grijpers met dezelfde naam? Geef elk team een unieke naam in de sketch; de driver meldt anders een dubbelzinnige naam. Indien nodig kun je ook `connect(name="gripper-left", address="...")` gebruiken met het adres uit de ontdekking.
- Importfout? Activeer dezelfde virtuele omgeving waarmee je het pakket installeerde. Controleer je Python-versie en herhaal de installatie in die omgeving.
- Geen voltooiing? Controleer de seriële output, callbacks, `reportPosition()` en `update()`. Een gemelde positie bewijst niet dat de mechaniek werkelijk bewogen heeft.

### Hackathonopdracht

Test je ontwerp met verschillende alledaagse voorwerpen. Noteer per voorwerp de openingsbreedte, het resultaat en mogelijke oorzaken van falen. Verander één eigenschap tegelijk en vergelijk opnieuw. Gebruik sensoren alleen na kalibratie en implementeer expliciet wat de grijper bij contact, blokkering en verbindingsverlies moet doen.
