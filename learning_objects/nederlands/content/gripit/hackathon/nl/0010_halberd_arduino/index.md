---
hruid: org_dwengo_gripit_hackathon_halberd_arduino
version: 1
language: nl
title: "Halberd programmeren met Arduino"
description: "Installeer de Halberd-boarddefinitie en upload een eerste programma."
keywords: ["gripit", "hackathon", "halberd", "arduino"]
educational_goals: []
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [18]
difficulty: 2
estimated_time: 20
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

<div class="dwengo_content fiche">
<h1 class="title">Halberd programmeren met Arduino</h1>
<h2 class="subtitle">Van een werkende ontwikkelomgeving naar je eigen robotgrijper</h2>
<div class="items">
<div class="info_item item">
<h3 class="info_item_title">De uitdaging</h3>
<p>Ontwerp, bouw en programmeer een grijper die verschillende alledaagse voorwerpen kan oppakken. Net als bij <a href="https://www.dwengo.org/gripit/">Grip-&gt;IT</a> combineer je mechanica, elektronica en software. In dit traject installeer je de ontwikkelomgeving, maak je de grijper bereikbaar via Bluetooth Low Energy (BLE) en stuur je hem aan vanuit Python.</p>
<p>Je hebt een Halberd, een USB-datakabel, een computer met Bluetooth, Arduino IDE 2 en later Python 3.11 of nieuwer nodig. Voor fysieke beweging heb je bovendien een correct aangesloten en gevoede grijper met servo's nodig. Maak eerst kennis met de hardware en de voeding van jouw kit.</p>
</div>
<div class="info_item item">
<h3 class="info_item_title">Installeer het boardpakket</h3>
<ol>
<li>Installeer <a href="https://www.arduino.cc/en/software/">Arduino IDE</a>. Open <em>File &gt; Preferences</em> en voeg bij <em>Additional Boards Manager URLs</em> deze URL toe, zonder eventuele bestaande URL's te verwijderen:<br><code>https://dwengovzw.github.io/dwengo_nrf52_core/package_dwengo_index.json</code></li>
<li>Open <em>Tools &gt; Board &gt; Boards Manager</em>, zoek <code>Dwengo nRF52 Boards</code> en installeer het pakket.</li>
<li>Verbind de Halberd met de USB-datakabel. Selecteer onder <em>Tools &gt; Board</em> het bord <code>Halberd nRF52840 (DWENGO)</code> en selecteer onder <em>Tools &gt; Port</em> de bijbehorende poort.</li>
<li>Open <em>File &gt; Examples &gt; 01.Basics &gt; Blink</em>. Klik op <em>Verify</em> en daarna op <em>Upload</em>. Controleer of de ingebouwde LED knippert.</li>
</ol>
<p>De officiële instructies en updates staan in de <a href="https://github.com/dwengovzw/dwengo_nrf52_core">Dwengo nRF52-core</a>. Deze installatie gebruikt de aanwezige bootloader; kies niet zomaar <em>Burn Bootloader</em> of een andere boarddefinitie.</p>
</div>
<div class="info_item item">
<h3 class="info_item_title">Als uploaden niet lukt</h3>
<p>Controleer de datakabel, voeding, bordselectie en poort. Koppel andere apparaten los om de juiste poort te herkennen en sluit toepassingen die de seriële poort gebruiken. Lees de volledige foutmelding in de IDE; vraag de begeleider om hulp als het bord of de bootloader niet wordt herkend.</p>
</div>
</div>
</div>
