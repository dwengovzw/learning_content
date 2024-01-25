---
hruid: leerlijn_project_lijnvolger_kalibratie
version: 1
language: nl
title: "Calibratie"
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
\mathrm{genormaliseerde_waarde} = \frac{\mathrm{originele_waarde} - \mathrm{gemiddelde_wit}}{\mathrm{gemiddelde_zwart} - \mathrm{gemiddelde_wit}}
\\]

In onze code berekenen we de gemiddelde waarden aan de hand van een exponentieel gemiddelde. We doen dit omdat we dan geen lijst van metingen moeten bijhouden. Een exponentieel gemiddelde neemt een weging tussen de nieuwe waarde en het vorige exponentieel gemiddelde.

\\[
\mathrm{exp_gemiddelde} = 0.05\mathrm{nieuwe_waarde} + 0.95\mathrm{exp_gemiddelde}
\\]

De Coëfficiënten \\(0.05\\) en \\(0.95\\) bepalen voor hoeveel procent je de nieuwe waarde in rekening brengt bij het berekenen van het gemiddelde. Je kan deze waarden zelf kiezen maar de som moet altijd gelijk zijn aan \\(1\\).

Hieronder zie je de code voor de kalibratieprocedure. Deze zal aan de gebruiker vragen om voor de start de robot eerst een tijd op een zwart en daarna een tijd op een wit oppervlak te plaatsen. Je kan de procedure starten door de <code class="lang-cpp">kalibreer</code> functie op te roepen.

<pre>
<code class="lang-cpp">

    unsigned char sensorPinnen[AANTAL_SENSOREN] = {A0, A1, A2, A3, A4, A5};
    float sensorCalibratieHoog[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};
    float sensorCalibratieLaag[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};

    void printStringsToLCD(String lijn1, String lijn2){
        dwenguinoLCD.clear();
        dwenguinoLCD.setCursor(0,0);
        dwenguinoLCD.print(lijn1);
        dwenguinoLCD.setCursor(0,1);
        dwenguinoLCD.print(lijn2);
    }

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

    void kalibreer(){
        printStringsToLCD("Naar zwart", "E -> Ga verder");
        while (digitalRead(SW_E) == HIGH){
            // Wacht tot de oost knop wordt ingedrukt.
        }
        delay(500); // Debounce knop

        printStringsToLCD("Zwart kalibreren", "E -> Ga verder");
        // Kalibreer waarde zwart
        kalibreerReferentiepunt(sensorCalibratieHoog);

        printStringsToLCD("Naar wit", "E -> Ga verder");
        while (digitalRead(SW_E) == HIGH){
            // Wacht tot de oost knop wordt ingedrukt.
        }
        delay(500); // Debounce

        printStringsToLCD("Wit kalibreren", "E -> Ga verder");
        // Kalibreer waarde wit
        kalibreerReferentiepunt(sensorCalibratieLaag);
    }

</code>
</pre>

