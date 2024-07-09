---
hruid: leerlijn_uc_introductie_weerstation_luchtdruk_opl
version: 1
language: nl
title: "Luchtdruk (oplossing)"
description: "Hoe meten we de luchtdruk?"
keywords: ["Microcontroller", "µC", "weerstation", "dht", "luchtdruk"]
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

# Luchtdruk (oplossing)
 
<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="dht11.cpp">
    
    // Bibliotheken inladen
    #include <LiquidCrystal.h>
    #include <Adafruit_MPL3115A2.h>
    #include <dht.h>  
    #include <Dwenguino.h>

    // Initialiseer de luchtdrukmeter.
    Adafruit_MPL3115A2 mpl;

    #define DHT11PIN 3 
    dht DHT; // Aanmaken van het DHT object.

    void setup()
    {
        initDwenguino(); // Initialiseer de basisfuncties van de Dwenguino

        Serial.begin(9600);
        
        // Test connectie met luchtdrukmeter
        if (!mpl.begin()) {
            dwenguinoLCD.clear();
            dwenguinoLCD.print("ERROR luchtdruk");
            while(1);
        }
    }

    void loop()
    {
        // Laat de DHT sensor een meting doen.    
        int chk = DHT.read11(DHT11PIN);

        // Voeg temperatuur, vochtigheidsgraad 
        // en luchtdruk samen in csv formaat.
        String data_point = String(DHT.temperature)
                            + ";"
                            + String(DHT.humidity)
                            + ";"
                            + String(mpl.getPressure());

        // Toon de data op het scherm.
        dwenguinoLCD.clear();
        dwenguinoLCD.print(data_point);

        // Verstuur het datapunt over de seriële verbinding.
        Serial.println(data_point);

        // Wacht 1s voor je een volgende meting doet.
        delay(1000);
    }

</code>
    </pre>
</div>

