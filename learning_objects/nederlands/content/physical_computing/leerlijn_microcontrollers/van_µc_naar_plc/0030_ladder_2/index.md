---
hruid: leerlijn_microcontrollers_microcontroller_naar_plc_ladder_2
version: 1
language: nl
title: "Ladder logica (structuur)"
description: "Wat is Ladder logica?"
keywords: ["microcontroller", "plc", "automatisatie", "programmable logic controller", "µC", "ladder"]
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

# Ladder logica (structuur)

Voor je een programma kan schrijven in Ladder logica, is het nuttig om te weten hoe de PLC deze logica zal uitvoeren. We doen dat hier door de analogie te leggen met het c++ programma op de microcontroller.

Een ladder programma wordt op de volgende manier uitgevoerd dooer een PLC:
1. De logische waarde van de schakelaars wordt gelezen.
2. Elke rij (rung) in het ladder diagram wordt in volgorde uitgevoerd.
3. Er wordt een uitvoer gegenereerd.

De PLC zal voorgaande stappen blijven herhalen.

Hieronder zie je een voorbeeld van een ladder diagram.

![Voorbeeld van een ladder diagram.](images/sample.png "Voorbeeld van een ladder diagram.")

Als we de logica van dit diagram willen implementeren op de Dwenguino, dan ziet dat er als volgt uit.

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

            #include <Wire.h>
            #include <Dwenguino.h>

            // Leg vast welke pinnen je gaat gebruiken als schakelaars.
            #define PIN_A 0
            #define PIN_B 1

            // Leg vast welke pin je gaat gebruiken als uitvoer.
            #define PIN_Q 2

            // Maak een variabele om de logische waarde van de pin in op te slaan.
            int A = 0;
            int B = 0;
            int Q = 0;

            // Lees de waarde van de pinnen en sla die op.
            void leesSchakelaars(){
            A = digitalRead(PIN_A);
            B = digitalRead(PIN_B);
            }

            // Deze functie bevat de logica van ons ladder diagram.
            void voerRijLogicaUit(){
                if(A == 1 || B == 1){
                    Q = 1;
                } else {
                    Q = 0;
                }
            }

            // Schrijf de uitvoerwaarden naar de overeenkomstige pinnen.
            void schrijfUitvoerwaarde(){
                digitalWrite(PIN_Q, Q);
            }

            void setup(){
                initDwenguino();
            }

            void loop() {
                leesSchakelaars();
                voerRijLogicaUit();
                schrijfUitvoerwaarde();
            }

</code>
    </pre>
</div>

Merk op dat onze code voor de microcontroller er een stuk complexer uitziet dan het ladder diagram. De programmeertaal C++ biedt heel veel mogelijkheden. Zo kan je heel veel verschillende soorten toepassingen bouwen. Deze flexibiliteit brengt extra complexiteit met zich mee. Heb je deze flexibiliteit niet nodig, kan het een goede keuze zijn om gebruik te maken van een PLC met een programma in ladder logica.