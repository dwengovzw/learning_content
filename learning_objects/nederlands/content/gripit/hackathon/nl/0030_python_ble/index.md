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
target_ages: [18]
difficulty: 3
estimated_time: 30
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

<div class="dwengo_content fiche">
<h1 class="title">Bestuur je grijper met Python en BLE</h1>
<h2 class="subtitle">Van draadloze verbinding naar een eerste grijptaak</h2>
<div class="items">
<div class="info_item item">
<h3 class="info_item_title">Installeer de Python-driver</h3>
<p>Upload eerst de aangepaste <code>parallel_gripper_servo</code>-firmware uit de vorige stap en laat de Halberd ingeschakeld. Schakel Bluetooth op je computer in. Deze firmware gebruikt AGP, niet de Nordic UART Service uit andere BLE-voorbeelden.</p>
<p>Maak met Python 3.11 of nieuwer een virtuele omgeving aan in je werkmap en installeer de driver. Gebruik op Windows PowerShell:</p>
<pre><code>py -3 --version
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "airo-robots[halberd]"</code></pre>
<p>Gebruik op macOS of Linux:</p>
<pre><code>python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "airo-robots[halberd]"</code></pre>
<p>Controleer met <code>python --version</code> of de geactiveerde omgeving Python 3.11 of nieuwer gebruikt. Op Linux moet de Bluetooth-service actief zijn en moet de gebruiker toegang hebben tot BlueZ. De <a href="https://github.com/airo-ugent/airo-mono/blob/main/airo-robots/airo_robots/grippers/hardware/halberd_ble.md">airo-mono-documentatie</a> beschrijft de driver en extra mogelijkheden.</p>
</div>
<div class="example_item item">
<h3 class="info_item_title">Verbind, open en sluit</h3>
<p>Sla dit op als <code>gripper.py</code>. Vervang de naam door jouw <code>GRIPPER_NAME</code>. Test eerst zonder voorwerp, nadat de bewegingen en grenzen in de firmware veilig zijn gekalibreerd.</p>
<pre><code class="language-python">from airo_robots.grippers import HalberdBLEGripper

print("Gevonden:", HalberdBLEGripper.discover())
gripper = HalberdBLEGripper.connect(name="gripper-left")
try:
    gripper.identify()
    gripper.open().wait()
    gripper.close().wait()
    gripper.open().wait()
finally:
    gripper.disconnect()</code></pre>
<p>Start met <code>python gripper.py</code>. De LED knippert kort bij <code>identify()</code>; de grijper opent, sluit en opent opnieuw. <code>wait()</code> wacht op de voltooiingsmelding van de firmware, niet op een onafhankelijke meting. Ontbreekt beweging of volgt een fout, controleer dan de firmware en onderbreek indien nodig de voeding.</p>
<p>Voor een parallelle grijper kun je ook <code>gripper.move(0.02).wait()</code> gebruiken: de gewenste opening is hier 0,02 meter en moet binnen je gekalibreerde bereik liggen. De driver begrenst aanvragen tot de door de firmware opgegeven grenzen. Andere mechanismen kunnen <code>GenericHalberdGripper</code> met eigen assen en poses gebruiken.</p>
</div>
<div class="info_item item">
<h3 class="info_item_title">Problemen oplossen</h3>
<ul>
<li>Geen grijper gevonden? Controleer Bluetooth, voeding, de AGP-firmware, de exacte naam en of een andere client al verbonden is. Een verbonden grijper adverteert niet.</li>
<li>Meerdere grijpers met dezelfde naam? Geef elk team een unieke naam in de sketch; de driver meldt anders een dubbelzinnige naam. Indien nodig kun je ook <code>connect(name="gripper-left", address="...")</code> gebruiken met het adres uit de ontdekking.</li>
<li>Importfout? Activeer dezelfde virtuele omgeving waarmee je het pakket installeerde. Controleer je Python-versie en herhaal de installatie in die omgeving.</li>
<li>Geen voltooiing? Controleer de seriële output, callbacks, <code>reportPosition()</code> en <code>update()</code>. Een gemelde positie bewijst niet dat de mechaniek werkelijk bewogen heeft.</li>
</ul>
</div>
<div class="info_item item">
<h3 class="info_item_title">Hackathonopdracht</h3>
<p>Test je ontwerp met verschillende alledaagse voorwerpen. Noteer per voorwerp de openingsbreedte, het resultaat en mogelijke oorzaken van falen. Verander één eigenschap tegelijk en vergelijk opnieuw. Gebruik sensoren alleen na kalibratie en implementeer expliciet wat de grijper bij contact, blokkering en verbindingsverlies moet doen.</p>
</div>
</div>
</div>
