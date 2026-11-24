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

# Halberd programmeren met Arduino

## Van een werkende ontwikkelomgeving naar je eigen robotgrijper

### De uitdaging

Ontwerp, bouw en programmeer een grijper die verschillende alledaagse voorwerpen kan oppakken. Net als bij [Grip-\>IT](https://www.dwengo.org/gripit/) combineer je mechanica, elektronica en software. In dit traject installeer je de ontwikkelomgeving, maak je de grijper bereikbaar via Bluetooth Low Energy (BLE) en stuur je hem aan vanuit Python.

Je hebt een Halberd, een USB-datakabel, een computer met Bluetooth, Arduino IDE 2 en later Python 3.11 of nieuwer nodig. Voor fysieke beweging heb je bovendien een correct aangesloten en gevoede grijper met servo's nodig. Maak eerst kennis met de hardware en de voeding van jouw kit.

### Installeer het boardpakket

1.  Installeer [Arduino IDE](https://www.arduino.cc/en/software/). Open *File \> Preferences* en voeg bij *Additional Boards Manager URLs* deze URL toe, zonder eventuele bestaande URL's te verwijderen:\
    `https://dwengovzw.github.io/dwengo_nrf52_core/package_dwengo_index.json`
2.  Open *Tools \> Board \> Boards Manager*, zoek `Dwengo nRF52 Boards` en installeer het pakket.
3.  Verbind de Halberd met de USB-datakabel. Selecteer onder *Tools \> Board* het bord `Halberd nRF52840 (DWENGO)` en selecteer onder *Tools \> Port* de bijbehorende poort.
4.  Open *File \> Examples \> 01.Basics \> Blink*. Klik op *Verify* en daarna op *Upload*. Controleer of de ingebouwde LED knippert.

De officiële instructies en updates staan in de [Dwengo nRF52-core](https://github.com/dwengovzw/dwengo_nrf52_core). Deze installatie gebruikt de aanwezige bootloader; kies niet zomaar *Burn Bootloader* of een andere boarddefinitie.

### Als uploaden niet lukt

Controleer de datakabel, voeding, bordselectie en poort. Koppel andere apparaten los om de juiste poort te herkennen en sluit toepassingen die de seriële poort gebruiken. Lees de volledige foutmelding in de IDE; vraag de begeleider om hulp als het bord of de bootloader niet wordt herkend.
