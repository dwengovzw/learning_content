---
hruid: leerlijn_basis_programmeren_basisstructuur
version: 1
language: nl
title: "Basisstructuur"
description: "Basisstructuur van het programma: de setup en loop functies."
keywords: ["programmeren", "setup", "loop", "microcontroller", "µC", "arduino", "dwenguino"]
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

# Basisstructuur

Om de basisstructuur van een µC-programma uit te leggen, kijken we terug naar ons eerste programma uit het leerpad over invoer, verwerking en uitvoer. Dit programma zorgde ervoor dat led 13 ging branden wanneer de sonarsensor beweging detecteerde. Hieronder zie je die code opnieuw weergegeven. In de commentaar staan de verschillende onderdelen van de code aangeduid.


<div class="dwengo-content dwengo-code-simulator">
<pre>
<code class="language-arduino">

    /*
        ONDERDEEL 1: Het koppelen van bibliotheken.
    */
    #include <Wire.h>
    #include <Dwenguino.h>
    #include <LiquidCrystal.h>
    #include <NewPing.h>

    /*
        ONDERDEEL 2: Definities en globale variabelen.
    */
    #define TRIGGER_PIN 11
    #define ECHO_PIN 12
    #define MAX_DISTANCE 200

    NewPing sonar = NewPing(
        TRIGGER_PIN,
        ECHO_PIN,
        MAX_DISTANCE);
    int afstand;

    /*
        ONDERDEEL 3: De setup() functie,
        deze functie wordt één keer opgeroepen bij de start van je programma.
    */

    void setup(){
        initDwenguino();
        pinMode(13, OUTPUT);
    }

    /*
        ONDERDEEL 4: De loop() functie,
        deze functie wordt telkens opnieuw opgeroepen
        tot wanneer het programma stopt.
    */
    void loop(){
        afstand = sonar.ping_cm();
        if (afstand > 0 && afstand < 100){
            digitalWrite(13, HIGH);
        } else {
            digitalWrite(13, LOW);
        }
        delay(100);
    }
</code>
</pre>
</div><br>


## ONDERDEEL 1: Het koppelen van bibliotheken
 
Bovenaan je programma koppel je de bibliotheken die je wil gebruiken. Op de Dwenguino zal je standaard altijd de Dwenguino bibliotheek (<code class="language-cpp">#include &lt;Dwenguino.h&gt;</code>) en de lcd bibliotheek (<code class="language-cpp">#include &lt;LiquidCrystal.h&gt;</code>) koppelen. Zo kan je makkelijk alle basisfunctionaliteiten van de Dwenguino gebruiken. Op de Arduino UNO moet je in principe geen bibliotheken koppelen. Dit bord heeft standaard immers maar een beperkte functionaliteit. 

Om een bibliotheek te koppelen, gebruik je steeds het <code class="language-cpp">#include</code> commando. Hierna plaats je de naam van de bibliotheek tussen <code class="language-cpp">&lt;</code> en <code class="language-cpp">&gt;</code>. Bijvoorbeeld: <code class="language-cpp">#include &lt;LiquidCrystal.h&gt;</code>.


## ONDERDEEL 2: Definities en globale variabelen.

In dit onderdeel definieer je **globale** **definities** en **globale variabelen**. Ze zijn **globaal** omdat je de waarde ervan overal in je programma kan gebruiken. Van **definities** kan je de waarde overal in je programma opvragen. **Je kan de waarde van een definitie echter niet aanpassen**. Deze behoudt dus altijd de waarde die deze in het begin van het programma kreeg. Van **variabelen** kan je de waarde ook overal in je programma opvragen maar je kan de waarde van een variabele ook **overal in je programma aanpassen**.

Een definitie definieer je aan de hand van een <code class="language-cpp">#define</code>. Erna schrijf je de naam van de definitie in drukletters. Na de naam volgt de waarde die de definitie moet krijgen. Bijvoorbeeld: <pre><code class="language-cpp">#define TRIGGER_PIN 11</code></pre>

Een variabele heeft een type, een naam en een waarde. Het type geeft aan welke soorten waarden je kan opslaan in de variable. Hier gebruiken we een variabele van het type <code class="language-cpp">NewPing</code> met de naam <code class="language-cpp">sonar</code> en een variabele van het type <code class="language-cpp">int</code> met de naam <code class="language-cpp">afstand</code>. Merk op dat het niet verplict is om een variabele ook onmiddelijk een waarde te geven. Dat kan ook later in het programma. In onze code gebruiken we bijvoorbeeld:

<pre>
    <code class="language-cpp">int afstand;</code>
</pre>

om onze variabele aan te maken. Later in het programma geven we de variabele een waarde gelijk aan de gemeten afstand:

<pre>
    <code class="language-cpp">afstand = sonar.ping_cm();</code>
</pre>

## ONDERDEEL 3: De setup() functie

Alle code die in de <code class="language-cpp">setup()</code> functie staat wordt één keer uitgevoerd in het begin van het programma, nadat de globale definities en variabelen zijn aangemaakt. Gebruik deze functie om de starttoestand van je programma in te stellen.

## ONDERDEEL 4: De loop() functie

Alle code in de <code class="language-cpp">loop()</code> functie wordt herhaald tot je het programma stopt (bv. door de stroom uit te trekken of op de reset knop te drukken). Deze functie bevat de belangrijkste logica van je programma.

<div class="dwengo-content important">
<h2 class="title">OPGELET!</h2>
<div class="content">
In C++ eindigt elke lijn op een <code class="language-cpp">;</code>. Vergeet deze <code class="language-cpp">;</code> niet anders zal het niet mogelijk zijn om je programma uit te voeren!
</div>
</div>