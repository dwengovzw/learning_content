---
hruid: leerlijn_project_lijnvolger_uitlezen_sensoren
version: 1
language: nl
title: "Uitlezen sensoren"
description: "Hoe kan ik de grondsensoren op de lijvolger uitlezen."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "grondsensor"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Uitlezen sensoren

Eerder in dit project hebben we de grondsensoren aangesloten op de pinnen (\\(\mathrm{A0}\\), \\(\mathrm{A1}\\), \\(\mathrm{A2}\\), \\(\mathrm{A3}\\), \\(\mathrm{A4}\\) en \\(\mathrm{A5}\\)) van de µC. Dit zijn analoge pinnen en lezen dus een continue spanningswaarde tussen \\(0\mathrm V\\) en \\(5\mathrm V\\). We kunnen in onze code de <code class="lang-cpp">analogRead(pin)</code> functie gebruiken om de analoge waarde van een pin te lezen. De <code class="lang-cpp">analogRead(pin)</code> functie zet de spanning tussen \\(0\mathrm V\\) en \\(5\mathrm V\\) om naar een getal tussen \\(0\\) en \\(1024\\). Dit getal stelt de gemeten sensorwaarde voor en kunnen we opslaan in een variabele van het type <code class="lang-cpp">int</code>.

Hieronder zie je een voorbeeld van hoe je de grondsensoren kan uitlezen. 

<div class="dwengo-content dwengo-code-simulator">
<pre>
<code class="language-cpp" data-filename="sensoren_uitlezen.cpp">

    #include <Dwenguino.h>

    // Definieer het aantal sensoren
    #define AANTAL_SENSOREN 6

    // Sla op op welke pinnen de sensoren zijn aangesloten.
    unsigned char sensorPinnen[AANTAL_SENSOREN] = {A0, A1, A2, A3, A4, A5};
    
    // Maak een array om de waarden van de sensoren in op te slaan.
    int sensorWaarden[AANTAL_SENSOREN] = {0, 0, 0, 0, 0, 0};

    void leesSensorWaarden(){
        // Overloop elke sensor, lees die uit en sla de waarde op.
        for (unsigned char i = 0 ; i < AANTAL_SENSOREN ; ++i){
            sensorWaarden[i] = analogRead(sensorPinnen[i]);
        }
    }

    void setup()
    {
        initDwenguino(); 
    }

    void loop()
    {
        // Lees elke halve seconde de waarden van de sensoren.
        leesSensorWaarden();
        delay(500);
    }

</code>
</pre>
</div>



<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Je zal merken dat het met bovenstaand programma onmogelijk is om te controleren wat de uitgelezen waarden zijn. Pas de code aan zodat de gelezen sensorwaarden via Bluetooth verstuurd worden naar de computer. Stuur de waarden van de zes sensoren door in csv formaat. Druk de waarden af op de computer. 
        Bekijk de waarden goed. Wat gebeurd er met de waarden wanneer het oppervlak onder de robot lichter of donkerder wordt?
    </div>
</div>