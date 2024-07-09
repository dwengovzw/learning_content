---
hruid: leerlijn_uc_introductie_weerstation_luchtdruk
version: 1
language: nl
title: "Luchtdruk"
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
teacher_exclusive: false
---

# Luchtdruk

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="dht11.cpp">
    
    // Bibliotheken inladen
    #include <LiquidCrystal.h>
    #include <Adafruit_MPL3115A2.h>
    #include <Dwenguino.h>

    // Initialiseer de luchtdrukmeter.
    Adafruit_MPL3115A2 mpl;

    void setup()
    {
        initDwenguino(); // Initialiseer de basisfuncties van de Dwenguino
        
        // Test connectie met luchtdrukmeter
        if (!mpl.begin()) {
            dwenguinoLCD.clear();
            dwenguinoLCD.print("ERROR luchtdruk");
            while(1);
        }
    }

    void loop()
    {
        // Sla de luchtdruk op als string.
        String data_point = 
            String(mpl.getPressure());

        // Toon de data op het scherm.
        dwenguinoLCD.clear();
        dwenguinoLCD.print(data_point);

        // Wacht 1s voor je een volgende meting doet.
        delay(1000);
    }

</code>
    </pre>
</div>