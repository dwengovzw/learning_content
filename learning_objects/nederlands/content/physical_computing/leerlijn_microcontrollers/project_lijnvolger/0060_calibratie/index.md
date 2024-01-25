---
hruid: leerlijn_project_lijnvolger_kalibratie
version: 1
language: nl
title: "Kalibratie"
description: "Hoe kan ik de grondsensoren kalibreren."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "grondsensor", "kalibratie", "calibratie"]
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
estimated_time: 15
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Kalibratie

Wanneer we een systeem kalibreren stellen we het af op een aantal gekende meetpunten. In ons geval zullen we elke sensor afstellen zodat de gemeten waarde op een wit oppervlak dicht bij nul ligt en de waarde op een zwart oppervlak dicht bij één. Hiervoor gaan we voor elke sensor een aantal waarden meten op een wit en een zwart oppervlak. We berekenen dan de gemiddelde waarde van deze metingen per oppervlak. Wanneer we een nieuwe waarde meten, zetten we deze om door de gemiddelde waarde op een wit oppervlak ervan af te trekken en te delen door het verschil tussen de gemiddelde waarde op het zwart oppervlak en de gemiddelde waarde op het wit oppervlak. Dit process noemen we *normaliseren*.

\\[
\mathrm{genormaliseerde\\_waarde} = \frac{\mathrm{originele\\_waarde} - \mathrm{gemiddelde\\_wit}}{\mathrm{gemiddelde\\_zwart} - \mathrm{gemiddelde\\_wit}}
\\]

In onze code berekenen we de gemiddelde waarden aan de hand van een exponentieel gemiddelde. We doen dit omdat we dan geen lijst van metingen moeten bijhouden. Een exponentieel gemiddelde neemt een weging tussen de nieuwe waarde en het vorige exponentieel gemiddelde.

\\[
\mathrm{exp\\_gemiddelde} = 0.05\cdot\mathrm{nieuwe\\_waarde} + 0.95\cdot\mathrm{exp\\_gemiddelde}
\\]

De Coëfficiënten \\(0.05\\) en \\(0.95\\) bepalen voor hoeveel procent je de nieuwe waarde in rekening brengt bij het berekenen van het gemiddelde. Je kan deze waarden zelf kiezen maar de som moet altijd gelijk zijn aan \\(1\\).

## Kalibratieprocedure

Hieronder zie je de code voor de kalibratieprocedure. Deze zal aan de gebruiker vragen om voor de start de robot eerst een tijd op een zwart en daarna een tijd op een wit oppervlak te plaatsen. Je kan de procedure starten door de <code class="lang-cpp">kalibreer</code> functie op te roepen.

<pre>
<code class="lang-cpp">

    unsigned char sensorPinnen[AANTAL_SENSOREN] = {A0, A1, A2, A3, A4, A5};
    float sensorKalibratieHoog[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};
    float sensorKalibratieLaag[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};

    void printStringsToLCD(String lijn1, String lijn2){
        dwenguinoLCD.clear();
        dwenguinoLCD.setCursor(0,0);
        dwenguinoLCD.print(lijn1);
        dwenguinoLCD.setCursor(0,1);
        dwenguinoLCD.print(lijn2);
    }

    // Sla een referentiewaarde op voor het huidige oppervlak.
    void kalibreerReferentiepunt(float* kalibratieReferentiePunten){
        // Lees een eerste sensorwaarde voor elke sensor
        for (unsigned char i = 0 ; i < AANTAL_SENSOREN ; ++i){
            kalibratieReferentiePunten[i] = (float)analogRead(sensorPinnen[i]);
        }
        // Lees meerdere waarden tot op de E knop wordt gedrukt. 
        // Bereken exponentieel gemiddelde.
        while (digitalRead(SW_E) == HIGH){
            for (unsigned char i = 0 ; i < AANTAL_SENSOREN ; ++i){
                kalibratieReferentiePunten[i] = (float)analogRead(sensorPinnen[i]) * 0.95 + kalibratieReferentiePunten[i] * 0.05;
            }
        }
        delay(500); // Debounce
    }

    // Start de kalibratieprocedure
    void kalibreer(){
        printStringsToLCD("Naar zwart", "E -> Ga verder");
        while (digitalRead(SW_E) == HIGH){
            // Wacht tot de oost knop wordt ingedrukt.
        }
        delay(500); // Debounce knop

        printStringsToLCD("Zwart kalibreren", "E -> Ga verder");
        // Kalibreer waarde zwart
        kalibreerReferentiepunt(sensorKalibratieHoog);

        printStringsToLCD("Naar wit", "E -> Ga verder");
        while (digitalRead(SW_E) == HIGH){
            // Wacht tot de oost knop wordt ingedrukt.
        }
        delay(500); // Debounce

        printStringsToLCD("Wit kalibreren", "E -> Ga verder");
        // Kalibreer waarde wit
        kalibreerReferentiepunt(sensorKalibratieLaag);
    }

</code>
</pre>

## Normalisatie

Nu we zowel voor de waarde op een wit als een zwart oppervlak een referentiewaarde hebben, kunnen we onze metingen normaliseren. Hiervoor passen we de functie <code class="lang-cpp">leesSensorWaarden()</code> aan.

<pre>
<code class="lang-cpp">

    void leesSensorWaarden(){
        // Overloop elke sensor, lees die uit en sla de waarde op.
        for (unsigned char i = 0 ; i < AANTAL_SENSOREN ; ++i){
            sensorWaarden[i] = analogRead(sensorPinnen[i]);
            // Zorg ervoor dat de gemeten waarde nooit hoger is dan de hoge kalibratiewaarde
            if (sensorWaarden[i] > sensorKalibratieHoog[i]){
                sensorWaarden[i] = sensorKalibratieHoog[i];
            }
            // Zorg ervoor dat de gemeten waarde nooit lager is dan de lage kalibratiewaarde
            if (sensorWaarden[i] < sensorKalibratieLaag[i]){
                sensorWaarden[i] = sensorKalibratieLaag[i]; 
            }
            // Normaliseer
            // Trek de lage kalibratiewaarde af van de meting
            sensorWaarden[i] -= sensorKalibratieLaag[i]; 
            // Deel door het verschil van de hoge en lage kalibratiewaarde
            sensorWaarden[i] = (float)sensorWaarden[i]/(float)(sensorKalibratieHoog[i] - sensorKalibratieLaag[i]);
        }
    }

</code>
</pre>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Voeg deze kalibratieprocedure toe aan je lijnvolger code. Probeer het uit. Controleer de referentiepunten door die door te sturen naar de computer.
    </div>
</div>