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
target_ages: [18]
difficulty: 3
estimated_time: 35
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

<div class="dwengo_content fiche">
<h1 class="title">Grijperbibliotheken en BLE-firmware</h1>
<h2 class="subtitle">Laat de Halberd spreken met airo-robots</h2>
<div class="items">
<div class="info_item item">
<h3 class="info_item_title">Wat doen de bibliotheken?</h3>
<p><a href="https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripper">HalberdGripper</a> implementeert het Airo Gripper Protocol (AGP) over BLE. Je sketch beschrijft de assen en posities en bepaalt hoe de motoren reageren. <a href="https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripperSensor">HalberdGripperSensor</a> leest de analoge druksensor en de VL53L4CD-afstandssensor van de vingertopmodule. De sensorbibliotheek is optioneel voor het eerste BLE-voorbeeld.</p>
<p>De bibliotheken worden ook gebruikt in de online programmeeromgeving, maar zijn niet automatisch beschikbaar in je Arduino-sketchbook. Het boardpakket levert onder meer Servo en Bluefruit; installeer de twee grijperbibliotheken apart.</p>
</div>
<div class="info_item item">
<h3 class="info_item_title">Installeer vanuit GitHub</h3>
<ol>
<li>Open de <a href="https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified">unified-tak van Blockly-for-Dwenguino</a> en kies <em>Code &gt; Download ZIP</em>. Pak het volledige archief uit. De ZIP bevat de volledige repository, niet alleen de bibliotheken.</li>
<li>Zoek in de uitgepakte map naar <code>backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries</code>. Kopieer de volledige mappen <code>HalberdGripper</code> en <code>HalberdGripperSensor</code>, inclusief <code>library.properties</code>, <code>src</code> en <code>examples</code>.</li>
<li>Open in Arduino IDE <em>File &gt; Preferences</em> en zoek de <em>Sketchbook location</em>. Plaats beide mappen rechtstreeks in de submap <code>libraries</code> daarvan; maak die submap indien nodig aan. Het resultaat is bijvoorbeeld <code>libraries/HalberdGripper/library.properties</code>, niet een extra geneste map.</li>
<li>Herstart de IDE, selecteer de Halberd en controleer onder <em>File &gt; Examples</em> of de voorbeelden van beide bibliotheken zichtbaar zijn. Installeer geen volledige repository-ZIP via <em>Add .ZIP Library</em>: dat is geen afzonderlijke Arduino-bibliotheek.</li>
</ol>
</div>
<div class="info_item item">
<h3 class="info_item_title">Bereid een parallelle grijper voor</h3>
<ol>
<li>Open <em>File &gt; Examples &gt; HalberdGripper &gt; parallel_gripper_servo</em>. De <a href="https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripper/examples/parallel_gripper_servo">broncode</a> is ook online beschikbaar. Sla een eigen kopie op voordat je wijzigingen maakt.</li>
<li>Kies een unieke <code>GRIPPER_NAME</code> voor je team en gebruik exact dezelfde naam in Python. Het voorbeeld configureert een parallelle as, de poses <code>open</code> en <code>closed</code>, callbacks en positie-updates. <code>gripper.update()</code> moet regelmatig in <code>loop()</code> uitgevoerd worden.</li>
<li>Het Dwengo-boardpakket 1.0.0 kent de namen <code>SERVO_1</code> en <code>SERVO_2</code> uit de sketch niet. Vervang ze in je eigen kopie respectievelijk door <code>D1</code> en <code>D2</code>. Dit behoudt de pinnummers van het oorspronkelijke voorbeeld; de boarddefinitie duidt D1 en D2 aan als respectievelijk SERVO2 en SERVO3. Controleer altijd de labels en bedrading van jouw bord.</li>
<li>Pas de servo-aansluitingen, pulsbreedtes, openingsgrenzen in meter, geometrie en hoekberekening aan jouw mechanisme aan. De sketch stuurt twee servo's aan; vertrouw niet op de beschrijving bovenaan de sketch als die van de code verschilt. De sensorwaarden in dit voorbeeld zijn gesimuleerd.</li>
<li>Verifieer en upload de aangepaste sketch. Open de seriële monitor op 115200 baud om de opstartmelding te bekijken; de Halberd adverteert vervolgens met de ingestelde naam.</li>
</ol>
<p><strong>Veilig testen:</strong> schakel de voeding uit bij het aansluiten, controleer GND, 5V en PWM en gebruik een geschikte voeding voor je servo's. Begin zonder voorwerp en met beperkte, gecontroleerde bewegingen; houd vingers uit het mechanisme. Servohoeken en geometrie uit het voorbeeld zijn geen veilige universele kalibratie. Zet bij onverwachte beweging de voeding uit.</p>
<p>De voorbeeldsketch rapporteert een berekende doel-/tussenpositie, geen gemeten vingeropening. De opgegeven snelheid en grijpkracht zijn niet automatisch fysiek begrensd. Test en implementeer zo nodig zelf grenzen, stopgedrag en feedback; verbindingsverlies is geen noodstop.</p>
</div>
<div class="info_item item">
<h3 class="info_item_title">Optioneel: echte sensoren</h3>
<p>Bekijk <em>HalberdGripperSensor &gt; read_pressure_and_distance</em> voor een seriële sensortest en <em>HalberdGripper &gt; parallel_gripper_servo_with_sensors</em> voor integratie met BLE. Pas ook in die integratiesketch de servoaliassen aan zoals hierboven. Volg de bedrading en I2C-bus in de betreffende sketch: de integratiesketch gebruikt <code>Wire</code> en druk op <code>A0</code>. Controleer de module en voedingsspanning vóór het aansluiten. Drukspanning is niet rechtstreeks een gekalibreerde kracht; een afstandsmeting kan ongeldig zijn.</p>
</div>
</div>
</div>
