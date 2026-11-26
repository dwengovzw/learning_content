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

### Maak je programma klaar

Upload eerst de aangepaste `parallel_gripper_servo`-firmware uit de vorige stap en laat de Halberd ingeschakeld. Schakel Bluetooth op je computer in. Deze firmware gebruikt AGP, niet de Nordic UART Service uit andere BLE-voorbeelden.

Gebruik dezelfde werkmap en virtuele omgeving als bij `identify.py`. Als je een nieuwe terminal opent, activeer je de bestaande omgeving opnieuw met `.\.venv\Scripts\Activate.ps1` in Windows PowerShell of `source .venv/bin/activate` op macOS of Linux. Je hoeft de omgeving of de driver niet opnieuw te installeren.

### Verbind, open en sluit

Maak een nieuw bestand `gripper.py` in dezelfde werkmap en sla daarin volgende code op. Vervang de naam door jouw `GRIPPER_NAME`. Test eerst zonder voorwerp, nadat de bewegingen en grenzen in de firmware veilig zijn gekalibreerd.

<pre><code class="language-python" data-filename="gripper.py">

from airo_robots.grippers import HalberdBLEGripper

print("Gevonden:", HalberdBLEGripper.discover())
gripper = HalberdBLEGripper.connect(name="my-first-gripper")
try:
    gripper.identify()
    gripper.open().wait()
    gripper.close().wait()
    gripper.open().wait()
finally:
    gripper.disconnect()


</code></pre>

Start met `python gripper.py`. De LED knippert kort bij `identify()` en de grijper opent, sluit en opent opnieuw. `wait()` wacht op de voltooiingsmelding van de firmware, niet op een onafhankelijke meting. Ontbreekt beweging of volgt een fout, controleer dan de firmware en onderbreek indien nodig de voeding.

Voor beweging naar een specifieke opening, bijvoorbeeld met `gripper.move(0.02).wait()`, moet de firmware ook een `onMove`-callback implementeren. Het basisvoorbeeld `parallel_gripper_servo` ondersteunt alleen de standen `open` en `closed`. Gebruik een aangepaste firmware met veilig gekalibreerde grenzen voor andere doelposities.

### Problemen oplossen

- Geen grijper gevonden? Controleer Bluetooth, voeding, de AGP-firmware, de exacte naam en of een andere client al verbonden is. Een verbonden grijper adverteert niet.
- Meerdere grijpers met dezelfde naam? Geef elk team een unieke naam in de sketch. De driver meldt anders een dubbelzinnige naam. Indien nodig kun je ook `connect(name="gripper-left", address="...")` gebruiken met het adres uit de ontdekking.
- Importfout? Activeer dezelfde virtuele omgeving waarmee je het pakket installeerde. Controleer je Python-versie en herhaal de installatie in die omgeving.
- Geen voltooiing? Controleer de seriële output, callbacks, `reportPosition()` en `update()`. Een gemelde positie bewijst niet dat de mechaniek werkelijk bewogen heeft.
