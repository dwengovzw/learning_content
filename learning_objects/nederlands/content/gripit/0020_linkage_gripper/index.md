---
hruid: org_dwengo_gripit_linkage_gripper_mechanica
version: 1
language: nl
title: "De parallellogram-grijper"
description: "Hoe werkt de mechanica van de parallellogram-grijper?"
keywords: ["fiche", "gripit", "parallellogram-grijper", "mechanica", "grijper"]
educational_goals: [
    {source: Source, id: id}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16, 17, 18]
difficulty: 1
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

<div class="dwengo_content fiche">
    <h1 class="title">De mechanica van de parallellogram-grijper</h1>
    <h2 class="subtitle">Hoe werkt de parallellogram-grijper?</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">De parallellogram-grijper</h3>
            <p class="info_item_content">
                De parallellogram-grijper gebruikt een eenvoudig parallellogrammechanisme om de draaiende beweging van de motor om te zetten in een beweging van de vingers. Wanneer de motor draait, beweegt de koppeling de vingers naar elkaar toe of van elkaar weg. Door de vorm van het parallellogram blijven de vingers tijdens die beweging ongeveer evenwijdig, zodat de grijper een voorwerp recht en stevig kan vastnemen.
            </p>
            <img src="img/linkage_gripper3_scaled_for_web.png" alt="Render van de parallellogram-grijper" title="Parallellogram-grijper"></img>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Onderdelen</h3>
            <div class="dwengo_content table_container">
                <table>
                    <tr>
                        <th>Onderdeel</th>
                        <th>Aantal</th>
                        <th>Stap</th>
                    </tr>
                    <tr><td>Halberd-connectieplaat</td><td>1</td><td>1</td></tr>
                    <tr><td>Vingerbasis</td><td>1</td><td>1</td></tr>
                    <tr><td>MG90s-servo</td><td>1</td><td>1</td></tr>
                    <tr><td>M3 x 6-inbusbout</td><td>4</td><td>1</td></tr>
                    <tr><td>M2 x 6-inbusbout</td><td>2</td><td>1</td></tr>
                    <tr><td>M2,5 x 6-inbusbout</td><td>1</td><td>1</td></tr>
                    <tr><td>Tandwiel (d10, Z1, m10)</td><td>1</td><td>1</td></tr>
                    <tr><td>Stang met tandwiel</td><td>1</td><td>2</td></tr>
                    <tr><td>Stang zonder tandwiel</td><td>1</td><td>2</td></tr>
                    <tr><td>Stang voor de vingerverbinding</td><td>1</td><td>2</td></tr>
                    <tr><td>M4-zeskantmoer</td><td>4</td><td>2</td></tr>
                    <tr><td>M3 x 4 x 18-pasbout</td><td>4</td><td>2</td></tr>
                    <tr><td>Vingertop-zwaluwstaartverbinding</td><td>1</td><td>3</td></tr>
                    <tr><td>Vingertop</td><td>1</td><td>3</td></tr>
                    <tr><td>Sensormodule (optioneel)</td><td>1</td><td>3</td></tr>
                    <tr><td>M5 x 8-inbusbout</td><td>1</td><td>3</td></tr>
                </table>
            </div>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Stap 1: Monteer de basis van de vinger</h3>
            <p class="info_item_content">
                In deze eerste stap monteer je de basis van de vinger. Hiervoor heb je de volgende onderdelen nodig:
            </p>
            <ul class="info_item_content">
                <li>De Halberd-connectieplaat</li>
                <li>De vingerbasis</li>
                <li>De MG90s-servo</li>
                <li>4 M3 x 6-inbusbouten</li>
                <li>2 M2 x 6-inbusbouten</li>
                <li>1 M2,5 x 6-inbusbout</li>
                <li>Tandwiel (d10, Z1, m10)</li>
            </ul>
            <p class="info_item_content">
                Gebruik de vier M3 x 6-inbusbouten om de vingerbasis aan de Halberd-connectieplaat te bevestigen. Bevestig de MG90s-servo met de twee M2 x 6-inbusbouten.
            </p>
            <p class="info_item_content">
                Bevestig vervolgens het tandwiel aan de servo met de M2,5 x 6-inbusbout. De eerste keer dat je het tandwiel op de servo schroeft, kan dat vrij stroef gaan. Een 3D-printer kan de fijne vorm van de servohoorn niet volledig afdrukken. Daarom wordt de vorm van de servohoorn bij de eerste montage vast in het tandwiel gedrukt.
            </p>
            <video controls title="Montage van de basis van de vinger">
                <source src="img/finger_base_assembly.mp4" type="video/mp4">
                Je browser ondersteunt deze video niet.
            </video>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Stap 2: Monteer de koppeling</h3>
            <p class="info_item_content">
                Monteer de koppeling zoals getoond in de video. Hiervoor heb je de volgende onderdelen nodig:
            </p>
            <ul class="info_item_content">
                <li>De stang met tandwiel</li>
                <li>De stang zonder tandwiel</li>
                <li>De stang voor de vingerverbinding</li>
                <li>4 M4-zeskantmoeren</li>
                <li>4 M3 x 4 x 18-pasbouten</li>
            </ul>
            <video controls title="Montage van de koppeling">
                <source src="img/finger_linkage_assembly.mp4" type="video/mp4">
                Je browser ondersteunt deze video niet.
            </video>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Stap 3: Monteer de vingertop</h3>
            <p class="info_item_content">
                Bevestig de vingertop aan de vinger zoals getoond in de video. Hiervoor heb je de volgende onderdelen nodig:
            </p>
            <ul class="info_item_content">
                <li>De vingertop-zwaluwstaartverbinding</li>
                <li>De vingertop</li>
                <li>De sensormodule (optioneel)</li>
                <li>Een M5 x 8-inbusbout</li>
            </ul>
            <video controls title="Montage van de vingertop">
                <source src="img/finger_fingertip_assembly.mp4" type="video/mp4">
                Je browser ondersteunt deze video niet.
            </video>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                De MG90s-servo draait het tandwiel. Via de vingerbasis wordt deze draaiende beweging doorgegeven aan de koppelingen van het parallellogram. Daardoor bewegen de vingers gelijktijdig naar binnen om een voorwerp vast te nemen, of naar buiten om het weer los te laten. De koppelingen zorgen ervoor dat de vingers tijdens het openen en sluiten ongeveer evenwijdig blijven.
            </p>
        </div>
    </div>
</div>