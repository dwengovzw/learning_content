---
hruid: leerlijn_fiches_arduino_geluid
version: 1
language: nl
title: "Geluidssensor"
description: "Hoe stel ik de geluidssensor af?"
keywords: ["geluid", "geluidssensor", "fiche", "dwenguino"]
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

<div class="dwengo_content fiche">
    <h1 class="title">Geluidssensor</h1>
    <h2 class="subtitle">Geluid detecteren</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">In het echt</h3>
            <p class="info_item_content">
                <img src="img/geluidssensor.png" alt="Een afbeelding van een geluidssensor." title="Een afbeelding van de geluidssensor."></img>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Type</h3>
            <p class="info_item_content">
                Invoer, digitale sensor 
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Pinnen</h3>
            <p class="info_item_content">
                <table>
                    <tr><td>A</td><td>Een analoge output pin die ons een directe analoge uitlezing van de geluidssensor verschaft.</td></tr>
                    <tr><td>GND</td><td>De referentiespanning of de grond, soms ook aangeduid met een -.</td></tr>
                    <tr><td>VCC</td><td>De 5 V-voeding, soms ook aangeduid met een +.</td></tr>
                    <tr><td>D</td><td>Een digitale pin die aangeeft of er al dan niet geluid gedetecteerd wordt op basis van hoge of lage output.</td></tr>                
                </table>
            </p>
        </div>
        <div class="info_item item">
            <h3 class="info_item_title">Werking</h3>
            <p class="info_item_content">
                Gebruik deze sensor om geluid te detecteren. Bij geluid geeft de sensor 1 terug indien er geluid is en 0 bij stilte. Idealiter wordt deze sensor gebruikt in een stille omgeving.<br>
                <br>
                Wanneer je de geluidssensor aansluit (en voorziet van stroom), kan je 2 leds onderscheiden. De ene led laat je weten dat de geluidssensor aan staat, de andere led dat je geluidssensor geluid hoort. Wanneer de geluidssensor geluid hoort, staat het ledje aan, anders staat het uit.<br>
                <br>
                Het afstellen van de geluidssensor (meer of minder gevoelig maken) gebeurt met de kleine schroef bovenaan de sensor.<br>
                <br>
                - Wijzerzin: De geluidssensor wordt gevoeliger voor geluid.
                - Tegenwijzerzin: De geluidssensor wordt minder gevoelig voor geluid.<br>
                <br>
                Wanneer een geluidssensor voor de eerste keer wordt gebruikt, is deze zeer gevoelig voor geluid. Om de sensor af te stellen, ga je als volgt te werk:<br>
                Zorg ervoor dat het geluidsniveau op dit moment het niveau is waarop de sensor zal werken. Als het nu muisstil is, maar dit zal niet zo zijn wanneer de sensor in gebruik is, zal je deze opnieuw moeten afstellen.<br>
                <br>
                1. Draai de schroef in <em>tegenwijzerzin</em> tot een led uit gaat.
                2. Draai nu de schroef <em>voorzichtig</em> in <em>wijzerzin</em> tot de led terug aan gaat.
                3. Draai de schroef <strong>voorzichtig</strong> terug in <em>tegenwijzerzin</em> en stop zodra de led terug uit gaat.
                4. Tik nu met je vinger op de sensor. Als de led brandt tijdens de tik, dan is je sensor correct afgesteld. Anders ga je terug naar stap 2. 
            </p>
        </div>
        <div class="example_item item">
            <h3 class="example_item_title">Voorbeeld: Op het lcd-scherm laten verschijnen of er geluid gedetecteerd wordt.</h3>
            <p class="example_item_content">
<pre>
<code class="language-cpp">
    
    // Arduino's pin connected to OUT pin of the sound sensor
    #define SENSOR_PIN 5

    int lastState = HIGH;  // the previous state from the input pin
    int currentState;      // the current reading from the input pin

    void setup() {
        // initialize serial communication at 9600 bits per second:
        Serial.begin(9600);
        // initialize the Arduino's pin as an input
        pinMode(SENSOR_PIN, INPUT);
    }

    void loop() {
        // read the state of the the input pin:
        currentState = digitalRead(SENSOR_PIN);

        if (lastState == HIGH && currentState == LOW)
            Serial.println("The sound has been detected");
        else if (lastState == LOW && currentState == HIGH)
            Serial.println("The sound has disappeared");

        // save the the last state
        lastState = currentState;
    }

</code>
</pre> 
            </p>
        </div>
    </div>
</div>



