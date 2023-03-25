---
hruid: pc_micro_interrupts
version: 3
language: nl
title: "Praktisch voorbeeld"
description: "Praktisch voorbeeld"
keywords: ["Microcontroller"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
# Timers en interrupts

## Een praktisch voorbeeld voor interrupts: reageren op een knopje

In dit voorbeeld tonen we hoe je de LEDs kan laten reageren op de input van een gebruiker via het knopje. We gaan uit van het knopje S die op pin PE5 is aangesloten (zie het Dwenguino schema).

Uiteraard zou je deze toepassing kunnen realiseren door continu in de oneindige while(1)-lus in de main het knopje te bevragen (ook wel *polling* genoemd). Naarmate je programma complexer wordt (en er dus heel wat code in je while(1)-lus komt te staan) zal het echter moeilijk zijn om de toestand van de knop op een vast tijdstip te bevragen. Bijgevolg is het aangewezen om hiervoor een interrupt te gebruiken.


### Inladen bibliotheken

We laden eerst de nodige AVR-bibliotheken in. Merk op dat naast de bibliotheek voor de delay-functie en de standaard IO-funcationaliteit, nu ook een bibliotheek is opgenomen voor de interrupt-functionaliteiten van de microcontroller. Zonder deze bibliotheek zal je geen interrupt handler ISR kunnen aanmaken en gebruiken!

<div class="highlight highlight-source-c">
<pre>#<span class="pl-k">include</span> <span class="pl-s"><span class="pl-pds">&lt;</span>avr/interrupt.h<span class="pl-pds">&gt;</span></span>
#<span class="pl-k">include</span> <span class="pl-s"><span class="pl-pds">&lt;</span>avr/io.h<span class="pl-pds">&gt;</span></span>
#<span class="pl-k">include</span> <span class="pl-s"><span class="pl-pds">&lt;</span>util/delay.h<span class="pl-pds">&gt;</span></span></pre>
</div>


### De interrupt-handler

De interrupt-handler kunnen we aanmaken via de ISR-routine. Aan deze routine geven het (programma)geheugenadres mee dat gekoppeld is aan de interrupt die we willen gebruiken. In dit voorbeeld willen we kunnen reageren op een externe gebeurtenis op pin PE5,die gekoppeld is aan INT5. De parameter die we moeten meegeven aan de ISR macro is INT5_vect (oftwel de naam van de interrupt + _vect) wat in de praktijk overeenkomt met het adres 0x000C van het programmageheugen. In de interrupt vector table van de microcontroller (pagina van de datasheet) kan je een lijst vinden van alle interrupts.

Denk er ook aan dat interrupt routines kort moeten zijn! De LEDs op het Dwenguino-bord zitten gelukkig op dezelfde poort A. Bijgevolg kunnen we ze allemaal tegelijk omklappen in 1 kloktik met behulp van de bitsgewijze XOR-operatie ^:

<div class="highlight highlight-source-c">
<pre><span class="pl-en">ISR</span>(INT5_vect) {
   PORTA ^= <span class="pl-c1">0xFF</span>; <span class="pl-c"><span class="pl-c">//</span> toggle LEDs</span>
}</pre>
</div>


### Configureren van de registers

De interrupt handler zal uiteraard nooit opgeroepen worden wanneer de registers niet juist staan ingesteld. We stellen achtereen volgens de volgende registers in:

* DDRA: de LED-pinnen als uitgang;
* PORTA: initiële toestand LEDs is hoog (arbitrair gekozen), alle LEDs zullen dus branden;
* DDRE: de pin PE5 waarmee knop S verbonden is als hoogimpedante ingang;
* PORTE: bij ontbreken van een elektronische pull-up weerstand, activeren we de interne pull-up weerstand;
* SREG: activeren van interrupt-mogelijkheid via het status-register;
* EIMSK: activeren van de externe interrupt INT5;
* EICRB: het instellen van de externe interrupt INT5 op falling edge, met andere woorden de ISR-routine zal opgeroepen worden wanneer de toestand op pin PE5 van hoog naar laag veranderd.

<div class="highlight highlight-source-c">
<pre><span class="pl-k">int</span> <span class="pl-en">main</span>(<span class="pl-k">void</span>) {
  DDRA = <span class="pl-c1">0xFF</span>;  <span class="pl-c"><span class="pl-c">//</span> Set all PAn pins to output</span>
  PORTA = <span class="pl-c1">0xFF</span>; <span class="pl-c"><span class="pl-c">//</span> Turn all LEDs on</span>

  DDRE &amp;= ~(<span class="pl-c1">1</span>&lt;&lt;PE5); <span class="pl-c"><span class="pl-c">//</span> Set PE5 to input</span>
  PORTE |= (<span class="pl-c1">1</span>&lt;&lt;PE5); <span class="pl-c"><span class="pl-c">//</span> Activate PE5 pull-up</span>

  SREG |= (<span class="pl-c1">1</span>&lt;&lt;SREG_I); <span class="pl-c"><span class="pl-c">//</span> Allow interrupts to occur</span>
  EIMSK |= (<span class="pl-c1">1</span>&lt;&lt;INT5);  <span class="pl-c"><span class="pl-c">//</span> Enable INT5</span>

  <span class="pl-c"><span class="pl-c">//</span> Configure INT5 to occur on falling edge</span>
  EICRB |= (<span class="pl-c1">1</span>&lt;&lt;ISC51); <span class="pl-c"><span class="pl-c">//</span>ISC51 bit set</span>
  EICRB &amp;= ~(<span class="pl-c1">1</span>&lt;&lt;ISC50); <span class="pl-c"><span class="pl-c">//</span> ISC50 bit cleared</span>

  <span class="pl-k">while</span> (<span class="pl-c1">1</span>) {
    <span class="pl-c1">_delay_ms</span>(<span class="pl-c1">1</span>);
  }

  <span class="pl-k">return</span> <span class="pl-c1">0</span>;
}</pre>
</div>

Merk op dat er in de oneindige lus while(1) in feite niets gebeurt. Waarom hebben we toch deze lus nodig? Wordt return ooit opgeroepen?


### Doen!

De oplossing voor het instellen van de externe interrupt INT5 geven we jou cadeau. Het is echter belangrijk dat je dit ook kan terugvinden in de datasheet van de AT90USB646. Kijk daarom na of je de uitleg van de video zelf kan terugvinden in hoofdstuk 12 (External interrupts), i.h.b.z. de sectie 12.0.2 van de datasheet.


### Variabelen in interrupt-routines

Zoals uitgelegd in het filmpje kan je ook variabelen gebruiken in de interrupt-routine. Wanneer je deze variabelen wil gebruiken als een toestandsvariabele in de oneindige lus in je main waarvan de toestand verandert in je interrupt-routine, dan moet deze variabele een **globale variabele** zijn. Dit is een variabele die zichtbaar is voor alle functies en dus gedeclareerd wordt in de namespace van je programma (onder de imports van je main file is een goede plek om dit te doen). Op die manier kan je counter incrementeren tijdens te ISR én ook uitlezen in de main functie om naar de LCD te printen

Bovendien moet je, omdat deze variabele aangepast wordt in de ISR-routine, het keyword **volatile** gebruiken om te verhinderen dat de compiler té veel optimalisaties doorvoort.Een voorbeeld vind je hieronder:

<div class="highlight highlight-source-c">
<pre>...
<span class="pl-k">volatile</span> <span class="pl-k">unsigned</span> <span class="pl-k">char</span> toestand;
...
<span class="pl-en">ISR</span>(EEN_vect) {
   toestand = <span class="pl-c1">1</span>;
}
...
<span class="pl-k">int</span> <span class="pl-en">main</span>(<span class="pl-k">void</span>) {
   ...
   <span class="pl-k">while</span>(<span class="pl-c1">1</span>) {
      <span class="pl-k">if</span>(toestand == <span class="pl-c1">1</span>) { ... } <span class="pl-k">else</span> { ... }
   }
   <span class="pl-k">return</span> <span class="pl-c1">0</span>;
}</pre>
</div>