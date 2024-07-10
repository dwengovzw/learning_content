---
hruid: leerlijn_uc_introductie_weerstation_wifi_opl
version: 1
language: nl
title: "Uitbreiding: wifi (opl)"
description: "Wat is een weerstation"
keywords: ["Microcontroller", "µC", "weerstation", "dht", "temperatuur", "luchtvochtigheid", "sd", "rtc", "wifi"]
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
estimated_time: 20
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Uitbreiding: data opvragen via wifi (oplossing)

<div>
    <pre>
<code class="language-cpp" data-filename="weerstation_wifi.cpp">

    // Bibliotheken inladen
    #include <LiquidCrystal.h>
    #include <Wire.h>
    #include <dht.h>
    #include <Adafruit_MPL3115A2.h>
    #include <Dwenguino.h>
    #include <OneWire.h>
    #include <SPI.h>
    #include "SD.h"
    #include <DS3231-RTC.h>
    #include <DwenguinoWIFI.h>

    // Initialiseer het RTC object.
    RTClib rtcLib;

    // Initialiseer de luchtdrukmeter.
    Adafruit_MPL3115A2 mpl;

    // Stel in met welke digitale pin de DHT module verbonden is.
    #define DHT11PIN 3
    dht DHT;

    // Stel de pinnummers in die op de Dwenguino gebruikt worden voor SPI communicatie.
    const int DW_CS = 10;
    const int DW_MOSI = 2;
    const int DW_MISO = 12;
    const int DW_CLK = 13;

    char data_point[80]; 

    // Maak een bestand aan
    File dataFile;

    // Wi-Fi gegevens
    /*
    Zorg ervoor dat je hier de naam
    en het wachtwoord van je wifi netwerk
    correct aanvult.
    */
    const char* ssid = "Vul-hier-de-naam-van-het-netwerk-in";
    const char* password = "Vul-hier-het-wachtwoord-in";
    DwenguinoWIFI DwenguinoWIFI(ssid, password, true);

    // Verwerk request voor luchtkwaliteit.
    void handleGETWeer(char* query, char* result){
        strcpy(result, data_point);
    }

    void setup()
    {
        initDwenguino(); // Initialiseer de basisfuncties van de Dwenguino

        // Test connectie met luchtdrukmeter
        if (!mpl.begin()) {
            dwenguinoLCD.clear();
            dwenguinoLCD.print("ERROR luchtdruk");
            while(1);
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

        // Schrijf een header naar het bestand
        String data_header = "Datum & Tijd;Temperatuur (°C);Luchtvochtigheid (%);Luchtdruk (hPa)";
        // Schrijf de data naar het bestand.
        dataFile.println(data_header);

        DwenguinoWIFI.routeManager.addRouteHandler("weer",
                                            handleGETWeer);
        // Initialiseer de wifi module
        DwenguinoWIFI.setupESP();
    }

    void loop()
    {
        // Doe metingen zolang de N(orth) knop niet wordt ingedrukt.
        if (digitalRead(SW_N)){

            // Laat de DHT sensor een meting doen.
            int chk = DHT.read11(DHT11PIN);

            // Vraag de huidige datum en tijd op.
            DateTime now = rtcLib.now();


            float temp = DHT.temperature;
            float vocht = DHT.humidity;
            float druk = mpl.getPressure();

            /* Voeg tijd, temperatuur, vochtigheidsgraad
            en luchtdruk samen in csv formaat. 
            Hier gebruiken we de sprintf functie om 
            onze gegevens in een geformatte string te 
            schrijven. Merk op dat sprintf op de µC
            geen floats ondersteund. Daardoor moeten 
            we de weergave van de floats zelf opsplitsen
            en de waarde voor en na de komma zelf berekenen.*/
            sprintf(data_point, "%d/%d/%d %d:%d:%d;%d.%d;%d.%d;%d.%d",
                now.getDay(),
                now.getMonth(),
                now.getYear(),
                now.getHour(),
                now.getMinute(),
                now.getSecond(),
                int(temp),
                int((temp - int(temp))*100),
                int(vocht),
                int((vocht - int(vocht))*100),
                int(druk),
                int((druk - int(druk))*100)
                );

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
        // Handel HTTP request af.
        DwenguinoWIFI.handleHTTPRequest();
    }

</code>
    </pre>
</div>