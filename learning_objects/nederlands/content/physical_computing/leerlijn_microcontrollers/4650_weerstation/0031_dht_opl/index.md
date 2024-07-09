---
hruid: leerlijn_uc_introductie_weerstation_dht_opl
version: 1
language: nl
title: "Temperatuur & luchtvochtigheid (oplossing)"
description: "Wat is een weerstation"
keywords: ["Microcontroller", "µC", "weerstation", "dht", "temperatuur", "luchtvochtigheid"]
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

# Temperatuur en luchtvochtigheid (oplossing)

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="dht11.cpp">
    
    // Bibliotheken inladen
    #include <LiquidCrystal.h>
    #include <dht.h>    
    #include <Dwenguino.h>


    #define DHT11PIN 3 
    dht DHT; // Aanmaken van het DHT object.

    void setup()
    {
        initDwenguino();
        Serial.begin(9600);
    }

    void loop()
    {
        // Laat de DHT sensor een meting doen.    
        int chk = DHT.read11(DHT11PIN);

        // Voeg temperatuur en vochtigheidsgraad samen in csv formaat.
        String data_point = String(DHT.temperature)
                            + ";"
                            + String(DHT.humidity);

        dwenguinoLCD.clear();
        dwenguinoLCD.print(data_point);

        Serial.println(data_point);

           delay(1000);
    }

</code>
    </pre>
</div>
