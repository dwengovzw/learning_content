---
hruid: leerlijn_project_lijnvolger_motoren_aansturen
version: 1
language: nl
title: "Motoren aansturen"
description: "Hoe stuur ik dc-motoren aan."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "motoren", "dc-motor"]
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

# Motoren aansturen

Onze robot is bijna af. We moeten deze enkel nog laten rijden. Hiervoor moeten we de dc-motoren aansturen met de correcte snelheden. Motoren die via de schroefconnector op de Dwenguino verbonden zijn, kunnen we makkelijk een snelheid geven via onze code. Hieronder zie je een voorbeeldprogramma die die snelheid van de twee motoren op 100 zet.

<pre>
<code class="lang-cpp">

    #include <LiquidCrystal.h>
    #include <Wire.h>
    #include <Dwenguino.h>
    #include <DwenguinoMotor.h>

    // Maak voor elke motor een object aan en stel in met welke pinnen die verbonden is.
    DCMotor dcMotor1(MOTOR_1_0, MOTOR_1_1);
    DCMotor dcMotor2(MOTOR_2_0, MOTOR_2_1);

    void setup()
    {
        initDwenguino(); // Initialiseer de basisfuncties van de Dwenguino
    }

    void loop()
    {
        dcMotor1.setSpeed(100); // Zet motor1 op snelheid 100.
        dcMotor2.setSpeed(100); // Zet motor2 op snelheid 100.
    }
</code>
</pre>

De motoren kunnen een snelheid hebben van \\(-255\\) tot en met \\(255\\). Het teken bepaalt in welke richting de motor zal draaien. Het heeft geen zin om hogere snelheden te programmeren, de maximale absolute snelheid zal altijd \\(255\\) zijn.

<div class="dwengo-content sideinfo">
    <h2 class="title">Draairichting</h2>
    <div class="content">
        Je kan de richting waarin een motor draait aanpassen door in je code het teken van de snelheid om te draaien. Er is echter nog een manier om dit te doen. Wanneer je de draadjes van de motor die verbonden zijn met de schroefconnector van de Dwenguino omdraait, zal de motor ook in de andere richting draaien.
    </div>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Pas de code van je lijnvolger aan zodat die rechtdoor kan rijden.
    </div>
</div>