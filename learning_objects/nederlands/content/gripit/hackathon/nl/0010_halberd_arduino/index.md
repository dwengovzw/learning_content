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
target_ages: [17, 18]
difficulty: 2
estimated_time: 20
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

# Halberd programmeren met de Arduino IDE

### Voor je start

Voor je start met dit leerpad moet je zorgen dat aan de volgende voorwaarden voldaan is.

1. Je hebt een Halberd microcontroller en een usb-c datakabel om de microcontroller met je computer te verbinden.
2. Je computer heeft Bluetooth.
3. De [Arduino IDE](https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE) is geïnstalleerd.
4. [Python 3.11](https://www.python.org/downloads) of hoger is geïnstalleerd.

Voor fysieke beweging heb je bovendien een correct aangesloten en gevoede grijper met servo's nodig. Maak eerst kennis met de hardware en de voeding van jouw kit.

### Installeer het Hablerd bord

1.  Open *File \> Preferences* en voeg bij *Additional Boards Manager URLs* deze URL toe, zonder eventuele bestaande URL's te verwijderen:\
    `https://dwengovzw.github.io/dwengo_nrf52_core/package_dwengo_index.json`
2.  Open *Tools \> Board \> Boards Manager*, zoek `Dwengo nRF52 Boards` en installeer het pakket.
3.  Verbind de Halberd met de USB-datakabel. Selecteer onder *Tools \> Board* het bord `Halberd nRF52840 (DWENGO)` en selecteer onder *Tools \> Port* de bijbehorende poort. Zie je geen poort met `Halberd nRF52840 (DWENGO)` ernaast, dubbelklik dan op de resetknop van het bord.
4.  Open *File \> Examples \> 01.Basics \> Blink*. Klik op *Verify* en daarna op *Upload*. Controleer of de ingebouwde LED (groen) knippert.

De officiële instructies en updates staan in de [Dwengo nRF52-core](https://github.com/dwengovzw/dwengo_nrf52_core).

### Als uploaden niet lukt

Controleer de datakabel, voeding, bordselectie en poort. Koppel andere apparaten los om de juiste poort te herkennen en sluit toepassingen die de seriële poort gebruiken. Lees de volledige foutmelding in de IDE; vraag de begeleider om hulp als het bord of de bootloader niet wordt herkend.
