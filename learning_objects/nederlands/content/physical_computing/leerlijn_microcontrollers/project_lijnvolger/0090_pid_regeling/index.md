---
hruid: leerlijn_project_lijnvolger_pid
version: 1
language: nl
title: "PID regeling"
description: "Hoe programmeer ik een pid regeling."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "pid"]
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

# PID regeling

In een laatste stap moeten we de snelheid van onze motoren afhankelijk maken van de gemeten fout op de lijn. Hiervoor gebruiken we een techniek genaamd de **PID regeling**. Dit soort regeling houdt niet enkel rekening met de fout maar ook met de afgeleide en de integraal van deze fout doorheen de tijd. De naam is ook afgeleid van deze verschillende soorten informatie.

* **P** de proportie (proportional): dit is de fout die we op een gegeven tijdstap meten. Het is dus het resultaat van onze <code class="lang-cpp">berekenFout()</code> functie.
* **I** de integraal (integral): dit is de som van alle fouten die we in het verleden gemaakt hebben. Met deze waarde krijg je zicht op de historische fout. Deze informatie kan je gebruiken om te compenseren voor een fout die je over een langere periode blijft maken.
* **D** de afgeleide (differential): dit is het verschil tussen de huidige fout en de vorige fout. Deze waarde geeft aan hoe snel een fout toe- of afneemt. Deze waarde kan je gebruiken om snel bij te sturen wanneer dat nodig is. 

We zullen de snelheid van onze motoren dus laten afhangen van deze drie parameters. Daarvoor gieten we ze in de volgende formule:

\\[
\mathrm{snelheid} = \mathrm{K_p}\cdot \mathrm{P} + \mathrm{K_i}\cdot \mathrm{I} + \mathrm{K_d}\cdot \mathrm{D}    
\\]

waarbij \\(\mathrm{K_p}\\), \\(\mathrm{K_i}\\) en \\(\mathrm{K_d}\\) wegingsfactoren zijn die we zelf moeten kiezen. De waarde hiervan hangt af van de toepassing. Wij zullen deze waarden experimenteel bepalen. 

## De P regeling

Voor we een complexe PID regeling programmeren, kiezen we eerst voor een eenvoudige P regeling. We houden in dit geval dus geen rekening met de integraal en de afgeleide van de fout. Enkel de proportie van de fout wordt hier gebruikt om de motoren van de robot bij te sturen. Hieronder zie je de code die we moeten toevoegen om de snelheid van onze motoren afhankelijk te maken van de gemeten fout.

We voegen de volgende globale variabelen toe:

<pre>
<code class="lang-cpp">

    // Parameters voor PID regeling
    float proportie = 0;
    float Kp = 15;
    float integraal = 0;
    float Ki = 0;
    float derivative = 0;
    float Kd = 0;
    float vorigeFout =  0;
    int basisMotorSnelheid = 65;

</code>
</pre>

Hier zijn \\(\mathrm{K_i}\\) en \\(\mathrm{K_d}\\) gelijk aan \\(0\\). Voor \\(\mathrm{K_i}\\) kiezen we hier de waarde \\(15\\). Deze waarde bepaalt hoe sterk de motoren zullen bijsturen wanneer er een fout gemeten wordt. 

In de lus voegen we de volgende code toe om de nieuwe motorsnelheden te berekenen:

<pre>
<code class="lang-cpp">

    // Bereken P, I and D 
    float meetFout = berekenFout();

    // De proportie is de fout die we gemeten hebben
    proportie = meetFout;
    // De integraal is de som van alle fouten die we al gemeten hebben.
    integraal = integraal + meetFout;
    // De afgeleide is het verschil tussen de huidige en de vorige fout.
    derivative = meetFout - vorigeFout;

    vorigeFout = meetFout;
    
    // Bereken het nieuwe snelheidsverschil
    float snelheidsVerschil = Kp * proportie + Ki * integraal + Kd * derivative;
    // Stel de snelheid van de motoren in
    int snelheidMotor1 = basisMotorSnelheid - (int)snelheidsVerschil;
    int snelheidMotor2 = basisMotorSnelheid + (int)snelheidsVerschil;
    dcMotor1.setSpeed(snelheidMotor1);
    dcMotor2.setSpeed(snelheidMotor2);

</code>
</pre>

<div class="dwengo-content assignment">
<h2 class="title">Opdracht</h2>
<div class="content">
    Programmeer je robot zodat deze een lijn kan volgen. Gebruik hiervoor een P-regeling. Hiervoor kan je de bovenstaande code toevoegen aan je programma. Daarnaast kan je de waarde van \\(\mathrm{K_p}\\) aanpassen zodat de robot de lijn mooi blijft volgen. Wat doet de robot wanneer je de waarde van \\(\mathrm{K_p}\\) groter of kleiner maakt?
</div>
</div>