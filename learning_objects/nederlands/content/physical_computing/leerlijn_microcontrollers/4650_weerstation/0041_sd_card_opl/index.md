---
hruid: leerlijn_uc_introductie_weerstation_data_opslaan_opl
version: 1
language: nl
title: "Gegevens loggen (oplossing)"
description: "Hoe kunnen we gegevens loggen naar een sd-kaartje."
keywords: ["Microcontroller", "µC", "weerstation", "sd", "sd-card", "logger", "data", "opslag"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16]
difficulty: 1
estimated_time: 3
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Gegevens loggen (oplossing)

<div>
    <pre>
<code class="language-cpp" data-filename="sd_card.cpp">
    
    // Bibliotheken inladen
    #include <LiquidCrystal.h>
    #include <Dwenguino.h>
    #include <OneWire.h>
    #include <SPI.h>
    #include "SD.h"

    // Stel de pinnummers in die op de Dwenguino
    // gebruikt worden voor SPI communicatie.
    const int DW_CS = 10;
    const int DW_MOSI = 2;
    const int DW_MISO = 12;
    const int DW_CLK = 13;

    // Maak een bestand aan
    File dataFile;

    void setup()
    {
        initDwenguino(); // Initialiseer de basisfuncties van de Dwenguino

        // SD kaart verbinding klaarmaken
        dwenguinoLCD.clear();
        dwenguinoLCD.print("SD-kaart setup.");

        // Controleer of de SD-kaart geinitialiseerd kan worden:
        if (!SD.begin(DW_CS, DW_MOSI, DW_MISO, DW_CLK)) {
            dwenguinoLCD.clear();
            dwenguinoLCD.print("Geen SD-kaart?");
            // Geen SD-kaart, blijf wachten.
            while(1);
        }
        dwenguinoLCD.clear();
        dwenguinoLCD.print("Kaart klaar");

        /*
            Maak een bestand op de SD-kaart waar je gegevens naar
            gaat schrijven. LET OP!! De naam van het bestand mag maar
            acht tekens lang zijn bv. 12345678.txt.
        */
        dataFile = SD.open("weer.txt", FILE_WRITE);
        if (!dataFile) {
            dwenguinoLCD.clear();
            dwenguinoLCD.print("Fout bij openen.");
            // Wacht voor altijd: niet mogelijk om data te schrijven.
            while(1);
        }
    }

    void loop()
    {
        // Schrijf een waarde zolang de N(orth) knop niet wordt ingedrukt.
        if (digitalRead(SW_N)){
            // Maak test data aan.
            String data_point = "test";

            // Toon de data op het scherm.
            dwenguinoLCD.clear();
            dwenguinoLCD.print(data_point);

            // Schrijf de data naar het bestand.
            dataFile.println(data_point);

            // Wacht 1s voor je een volgende meting doet.
            delay(1000);

        } else { // Sluit het bestand wanneer de N(orth) knop is ingedrukt.
            // Schrijf de data weg naar het bestand en sluit het bestand.
            dataFile.flush();
            dataFile.close();

            dwenguinoLCD.clear();
            dwenguinoLCD.print("Bestand gesloten");

            // Stop het programma.
            while(1);
        }
    }

</code>
    </pre>
</div>