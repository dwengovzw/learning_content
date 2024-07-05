---
hruid: org-dwengo-pc-luchtkwaliteit-iot-sensor-opl
version: 1
language: nl
title: "IoT sensor (oplossing)"
description: "Hoe kan ik de luchtkwaliteit meten?"
keywords: ["dwenguino", "microcontroller", "wifi", "i2c", "webserver", "internet", "co2", "luchtkwaliteit"]
content_type: "text/markdown"
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-digitale-competenties-en-mediawijsheid',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-algebra-analyse',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-redeneren',

]
copyright: "CC BY dwengo"
target_ages: [16, 17, 18]
teacher_exclusive: True
---

# IoT sensor: oplossing

## Microcontroller code

Op de Dwenguino combineren we nu verschillende codevoorbeelden tot een programma. We lezen elke 100 ms de waarden van de sensoren uit en slaan deze op in een variabele. Tegelijk luisteren we naar inkomende requests op de webserver. Wanneer er een request toekomt op de */luchtkwaliteit* route, sturen we de waarden van de laatste meting terug in csv formaat.

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="iot_luchtkwaliteit_meter.cpp">

    // Bibliotheken inladen
    #include <Dwenguino.h>
    #include <Wire.h>
    #include "ScioSense_ENS160.h"
    #include <SensirionI2CScd4x.h>
    #include <Wire.h>
    #include <DwenguinoWIFI.h>


    // Sensorobjecten maken
    ScioSense_ENS160 ens160(ENS160_I2CADDR_0);
    SensirionI2CScd4x scd4x;

    // Laatste waarde metingen.
    unsigned int aqi, tvoc, co2 = 0;
    float temp, vocht = 0.0f;

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
    void handleGETLuchtkwaliteit(char* query, char* result){
        String meting = String(co2) + ";" + 
                        String(temp) + ";" + 
                        String(vocht) + ";" +
                        String(tvoc) + ";" +
                        String(aqi);
        strcpy(result, meting.c_str());
    }

    void initialiseerENS(){
        // Initialiseer de sensor
        ens160.begin();
        Serial.println(ens160.available() ? "done." : "failed!");
        if (ens160.available()) {
            Serial.println("Instellen op standaard modus");
            Serial.println(ens160.setMode(ENS160_OPMODE_STD) ? "done." : "failed!");
        }
    }

    void initialiseerSCD40(){
        // Initialiseer I²C
        Wire.begin();
        scd4x.begin(Wire);

        unsigned int error;
        char errorMessage[256];

        // Stop metingen om sensor te resetten.
        error = scd4x.stopPeriodicMeasurement();
        if (error) {
            Serial.print("Fout bij stoppen: ");
            errorToString(error, errorMessage, 256);
            Serial.println(errorMessage);
        }

        // Start periodieke metingen.
        error = scd4x.startPeriodicMeasurement();
        if (error) {
            Serial.print("Fout bij starten periodieke metingen: ");
            errorToString(error, errorMessage, 256);
            Serial.println(errorMessage);
        }
    }

    // Vraag waarde op en vul die in als de waarde beschikbaar is.
    // Anders geef een foutmelding terug.
    int doeMetingMetENS160(unsigned int &aqi, unsigned int &tvoc){
        if (ens160.available()) {
            ens160.measure(true);
            ens160.measureRaw(true);
            aqi = ens160.getAQI();
            tvoc = ens160.getTVOC();
            return 0;
        } else {
            return 1;
        }
    }

    // Vraag waarde op en vul die in als de waarde beschikbaar is.
    // Anders geef een foutmelding terug.
    int doeMetingMetSCD40(unsigned int &co2, float &temp, float &vocht){
        unsigned int error;  // Foutstatus
        char errorMessage[256]; // Foutmelding
        bool isDataReady = false;

        // Wacht tot data klaar is.
        error = scd4x.getDataReadyFlag(isDataReady);
        if (error) {
            errorToString(error, errorMessage, 256);
            Serial.println(errorMessage);
            return 1;
        }
        // Start meting wanneer sensor klaar is.
        if (isDataReady) {
            // Doe een meting.
            error = scd4x.readMeasurement(co2, temp, vocht);
            if (error) {
                errorToString(error, errorMessage, 256);
                Serial.println(errorMessage);
                return 1;
            } else if (co2 == 0 || temp == 0 || vocht == 0) {
                return 1;
            } 
            return 0;
        }
        // Data not ready
        return 1;
    }

    void doeMetingMetSensoren(){
        int errorENS, errorSCD;
        // Doe metingen
        errorENS = doeMetingMetENS160(aqi, tvoc);
        errorSCD = doeMetingMetSCD40(co2, temp, vocht);

        // Controleer op fouten en stuur data door.
        if (!errorENS && !errorSCD){
            // Stuur data door naar computer.
            Serial.print(co2);Serial.print(";");
            Serial.print(temp);Serial.print(";");
            Serial.print(vocht);Serial.print(";");
            Serial.print(tvoc);Serial.print(";");
            Serial.println(aqi);

            // Print de waarden op het lcd-scherm.
            dwenguinoLCD.setCursor(0,0);
            dwenguinoLCD.print(String("CO2: "));
            dwenguinoLCD.print(String(co2));
            dwenguinoLCD.print(String(" ppm"));
            dwenguinoLCD.setCursor(0,1);
            dwenguinoLCD.print(String("TOVC: "));
            dwenguinoLCD.print(String(tvoc));
            dwenguinoLCD.print(String(" ppb"));
        }  
    }

    void setup() {
        initDwenguino();

        // Start de seriële communicatie.
        Serial.begin(9600);
        while (!Serial) {}

        // Initialiseer de sensoren.
        initialiseerENS();
        initialiseerSCD40();   

        DwenguinoWIFI.routeManager.addRouteHandler("luchtkwaliteit", 
                                            handleGETLuchtkwaliteit);
        // Initialiseer de wifi module
        DwenguinoWIFI.setupESP(); 

        // Neem tijd om te verbinden via de seriële monitor.
        delay(5000);
        Serial.println("CO2 (ppm);Temp (C);Vocht (%);TVOC (ppb);AQI");
    }

    void loop() {
        doeMetingMetSensoren();
        delay(100);
        DwenguinoWIFI.handleHTTPRequest();
    }

</code>
    </pre>
</div>

