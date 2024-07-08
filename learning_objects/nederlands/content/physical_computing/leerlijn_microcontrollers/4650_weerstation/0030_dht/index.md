---
hruid: leerlijn_uc_introductie_weerstation_dht
version: 1
language: nl
title: "Temperatuur & luchtvochtigheid"
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

# Temperatuur en luchtvochtigheid

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="dht11.cpp">
    
    // Bibliotheken inladen
    #include <LiquidCrystal.h>
    #include <dht.h>    
    #include <Dwenguino.h>


    // Stel in met welke digitale pin de DHT module verbonden is.
    #define DHT11PIN 3 
    dht DHT; 

    void setup()
    {
        initDwenguino(); // Initialiseer de basisfuncties van de Dwenguino
    }

    void loop()
    {
        // Laat de DHT sensor een meting doen.    
        int chk = DHT.read11(DHT11PIN);

        // Voeg temperatuur en vochtigheidsgraad samen in csv formaat.
        String data_point = String(DHT.temperature)
                            + ";"
                            + String(DHT.humidity);

        // Toon de data op het scherm.
        dwenguinoLCD.clear();
        dwenguinoLCD.print(data_point);
    }

</code>
    </pre>
</div>