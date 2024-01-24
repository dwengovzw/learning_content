---
hruid: leerlijn_bluetooth_dwenguino
version: 1
language: nl
title: "Bluetooth communicatie (Dwenguino)"
description: "Hoe stuur en ontvang je data op de Dwenguino."
keywords: ["bluetooth", "UART", "serieel", "µC"]
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Bluetooth communicatie: data sturen vanop de Dwenguino

Wanneer je een Bluetooth module hebt aangesloten op de UART connector van de Dwenguino, kan je makkelijk gegevens versturen en ontvangen. Je kan deze data in verschillende formaten sturen. In dit voorbeeld werken we met **tekst** (het String datatype). We zullen deze tekst lijn per lijn sturen. De twee belangrijkste commando's die we nodig hebben zijn:

<pre>
    <code class="language-cpp">
        Serial1.begin(baud_rate);
    </code>
</pre> 

Hiermee initialiseren we de communicatie en stellen we de snelheid in waarmee data verstuurd zal worden (<code class="language-cpp">baud_rate</code>). 
En:

<pre>
    <code class="language-cpp">
        Serial1.println(tekst_om_te_sturen);
    </code>
</pre> 

Hiermee sturen we een stuk tekst (<code class="language-cpp">tekst_om_te_sturen</code>) over Bluetooth.

Hieronder zie je een basisprogramma dat de twee command's integreert in een programma. Dit programma zal elke 2 seconden de tekst <code class="language-cpp">"Mijn eerste pakket."</code> versturen.

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="sturen_bluetooth_eenvoudig.cpp">

    #include <LiquidCrystal.h>
    #include <Wire.h>
    #include <Dwenguino.h>

    void setup()
    {
        initDwenguino(); // Initialiseer de basisfuncties van de Dwenguino
        // Open communicatie via Serial1, dit is de UART poort waarmee je de Bluetooth module verbonden hebt.
        // We gebruiken een baud rate (=snelheid) van 9600 bit/s.
        Serial1.begin(9600);
    }

    void loop()
    {
        Serial1.println("Mijn eerste pakket.");
        delay(2000);
    }
</code>
    </pre>
</div>