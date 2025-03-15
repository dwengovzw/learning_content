---
hruid: org-dwengo-pc-physics-valbeweging-meten
version: 1
language: nl
title: "Data verzamelen"
description: "Gebruik de Dwenguino in de les fysica!"
keywords: ["Fysica", "Dataverzameling", "Dataverwerking", "valbeweging"]
content_type: "text/markdown"
estimated_time: 20
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
teacher_exclusive: False
---

# Data verzamelen

Om de data van de val te capteren, moet je de microcontroller programmeren om waarden van de sensor te lezen en deze door te sturen naar de computer. Merk op dat het object snel valt. Het zal dus nodig zijn om zo veel mogelijk metingen te doen per seconde om een realistisch beeld te krijgen van de valbeweging.

Hieronder zie je de code die je nodig hebt om de data te capteren. In de commentaar is uitleg voorzien over waarvoor de verschillende onderdelen van het programma dienen.

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="afstand_meten.cpp">

    /*
    Hier importeer de de nodige bibliotheken.
    Deze heb je nodig om de sonar-sensor uit te lezen
    en om gegevens naar het lcd-scherm te schrijven.
    */
    #include <Wire.h>
    #include <Dwenguino.h>
    #include <LiquidCrystal.h>
    #include <NewPing.h>

    /*
    In dit voorbeeld is de sensor verbonden met pinnen 11 en 12 van de Dwenguino.
    */
    #define TRIGGER_PIN_11 11
    #define ECHO_PIN_12 12

    /*
    De maximale afstand die je zal meten is 200 cm.
    */
    #define MAX_DISTANCE 200

    /*
    Maak een sonar-sensor object aan.
    */
    NewPing sonar1112(TRIGGER_PIN_11, ECHO_PIN_12, MAX_DISTANCE);

    int afstand;

    void setup()
    {
    initDwenguino();     // Initialiseer de functies op het Dwenguino bord.
    Serial1.begin(9600); // Start de seriële verbinding met snelheid 9600 bps.
    }

    void loop()
    {
        /*
        De ping() functie van het sonar object geeft de tijd dat een geluidspuls 
        onderweg is vanaf de sensor naar het object en terug.
        Je gebruikt deze functie en niet de ping_cm()-functie omdat deze je
        nauwkeurigere waarden zal geven. 
        */
        afstand = sonar1112.ping();  

        /*
        Laat de gemeten afstand zien op het scherm.
        */   
        dwenguinoLCD.setCursor(0,0);
        dwenguinoLCD.print("afstand: " + String(afstand) + "cm");

        /*
        Stuur de gegevens over een seriële verbinding naar de computer.
        Hier maak je gebruik van Serial1. Dit is de bluetoothverbinding van 
        de Dwenguino. Wil je gegevens versturen via de USB-kabel, gebruik dan 
        Serial in plaats van Serial1.
        Je stuurt het huidige tijdstip en de gemeten afstand door in csv-formaat.
        De waardes worden hier gescheiden door een ;
        */
        Serial1.print(millis());
        Serial1.print(";");
        Serial1.println(afstand); 
    }
</code>
    </pre>
</div>

<div class="dwengo-content assignment">
<h2 class="title">Opdracht: gegevens ontvangen op de computer</h2>
<div class="content">
Hierboven staat het programma dat je nodig hebt om de afstand te meten en deze door te sturen naar de computer. Bekijk op <a href="https://www.dwengo.org/physical_computing">dwengo.org/physical_computing</a> de leerpaden over de seriële monitor en bluetoothcommunicatie. Gebruik de informatie die je daar kan vinden om de verstuurde gegevens te ontvangen op de computer. Schrijf deze gegevens weg naar een bestand met extentie .csv waarin elke meting op een andere lijn komt. Hieronder zie je een voorbeeld van hoe zo'n bestand er moet uitzien.

<pre class="lang-csv">
<code>
tijd (ms);afstand (ms)
199361;351
199375;347
199391;371
199405;371
199420;371
199435;367
199449;375
199464;375
199479;371
199493;367
199508;371
199523;371
</code>
</pre>

</div>
</div>

<div class="dwengo-content assignment">
<h2 class="title">Opdracht: meet de valbeweging</h2>
<div class="content">
Meet nu het verloop van de valbeweging door gegevens te verzamelen over de afstand terwijl je een object onder de sensor naar beneden laat vallen. 
</div>

