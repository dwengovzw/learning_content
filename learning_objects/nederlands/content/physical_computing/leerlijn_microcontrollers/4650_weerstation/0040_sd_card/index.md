---
hruid: leerlijn_uc_introductie_weerstation_data_opslaan
version: 1
language: nl
title: "Gegevens loggen"
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
teacher_exclusive: false
---

# Gegevens loggen

<div class="dwengo-content dwengo-code-simulator">
    <pre>
        <code class="language-cpp" data-filename="sd_card.cpp">
    
    // Bibliotheken inladen
    #include <LiquidCrystal.h>
    #include <Wire.h>
    #include <dht.h>    
    #include <Dwenguino.h>
    #include <OneWire.h>
    #include <SPI.h>
    #include "SD.h"


    // Stel in met welke digitale pin de DHT module verbonden is.
    #define DHT11PIN 3 
    dht DHT; 

    // Stel de pinnummers in die op de Dwenguino gebruikt worden voor SPI communicatie.
    const int DW_CS = 10;
    const int DW_MOSI = 2;
    const int DW_MISO = 12;
    const int DW_CLK = 13;

    // Maak een bestand aan 
    File dataFile;

    void setup()
    {
        initDwenguino(); // Initialiseer de basisfuncties van de Dwenguino


        // Wacht om te starten tot de gebruiker op de S(outh) knop drukt.
        dwenguinoLCD.clear();
        dwenguinoLCD.print("Druk op S-knop");
        while(digitalRead(SW_S)){
            ;
        }
    
        // SD kaart verbinding klaarmaken
        dwenguinoLCD.clear();
        dwenguinoLCD.print("SD-kaart setup.");

        // see if the SD card is present and can be initialized:
        if (!SD.begin(DW_CS, DW_MOSI, DW_MISO, DW_CLK)) {
            dwenguinoLCD.clear();
            dwenguinoLCD.print("Geen SD-kaart?");
            // don't do anything more:
            return;
        }
        dwenguinoLCD.clear();
        dwenguinoLCD.print("Kaart klaar");


        /*
            Maak een bestand op de SD-kaart waar je gegevens naar
            gaat schrijven. LET OP!! De naam van het bestand mag maar
            acht tekens lang zijn bv. 12345678.txt.
        */
        dataFile = SD.open("weer.txt", FILE_WRITE);
        if (! dataFile) {
            dwenguinoLCD.clear();
            dwenguinoLCD.print("Fout bij openen.");
            // Wait forever since we cant write data
            while (1) ;
        }

        // Wacht 1s voor te starten met de hoofdlus.
        delay(1000);

        // Schrijf een header naar het bestand
        String data_header = "Temperatuur (°C);Luchtvochtigheid (%)";
    }

    void loop()
    {
        // Doe metingen zolang de N(orth) knop niet wordt ingedrukt.
        if (digitalRead(SW_N)){

            // Laat de DHT sensor een meting doen.    
            int chk = DHT.read11(DHT11PIN);

            // Voeg temperatuur en vochtigheidsgraad samen in csv formaat.
            String data_point = String(DHT.temperature)
                                + ";"
                                + String(DHT.humidity);

            // Toon de data op het scherm.
            dwenguinoLCD.clear();
            dwenguinoLCD.print(data_point);

            // Schrijf de data naar het bestand.
            dataFile.println(data_point);

            // Wacht 1s voor je een volgende meting doet.
            delay(1000);

        } else { // Sluit het bestand wanneer de N(orth) knop is ingedrukt.
            dwenguinoLCD.clear();
            dwenguinoLCD.print("closing file");

            // Schrijf de data weg naar het bestand en sluit het bestand.
            dataFile.flush();
            dataFile.close();

            // Gebruik  de 30s wachttijd om de Dwenguino af te sluiten.
            delay(30000); // Wacht 30s

        }
    }

        </code>
    </pre>
</div>