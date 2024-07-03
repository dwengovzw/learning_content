---
hruid: org-dwengo-pc-luchtkwaliteit-integratie-opl
version: 1
language: nl
title: "Integratie (oplossing)"
description: "Hoe kan ik de luchtkwaliteit meten?"
keywords: ["dwenguino", "microcontroller", "wifi", "i2c", "webserver", "internet", "co2", "luchtkwaliteit"]
content_type: "text/markdown"
estimated_time: 8
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

# Integratie (oplossing)

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="integratie_luchtkwaliteit.cpp">

    // Bibliotheken inladen
    #include <Dwenguino.h>
    #include <Wire.h>
    #include "ScioSense_ENS160.h"
    #include <SensirionI2CScd4x.h>
    #include <Wire.h>


    // Sensorobjecten maken
    ScioSense_ENS160 ens160(ENS160_I2CADDR_0);
    SensirionI2CScd4x scd4x;

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
        unsigned int aqi, tvoc, co2 = 0;
        float temp, vocht = 0.0f;
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

        // Neem tijd om te verbinden via de seriële monitor.
        delay(5000);
        Serial.println("CO2 (ppm);Temp (C);Vocht (%);TVOC (ppb);AQI");
    }

    void loop() {
        doeMetingMetSensoren();
        delay(100);
    }

</code>
    </pre>
</div>