---
hruid: pc_micro_teivoorbeeld
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
target_ages: [16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 15
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# Timers en interrupts

## Een praktisch voorbeeld voor interrupts: reageren op een knopje

In dit voorbeeld tonen we hoe je de LEDs kan laten reageren op de input van een gebruiker via het knopje. We gaan uit van het knopje S die op pin PE5 is aangesloten (zie het dwenguino schema).

Uiteraard zou je deze toepassing kunnen realiseren door continu in de oneindige while(1)-lus in de main het knopje te bevragen (ook wel *polling* genoemd). Naarmate je programma complexer wordt (en er dus heel wat code in je while(1)-lus komt te staan) zal het echter moeilijk zijn om de toestand van de knop op een vast tijdstip te bevragen. Bijgevolg is het aangewezen om hiervoor een interrupt te gebruiken.


### Inladen bibliotheken

We laden eerst de nodige AVR-bibliotheken in. Merk op dat naast de bibliotheek voor de delay-functie en de standaard IO-funcationaliteit, nu ook een bibliotheek is opgenomen voor de interrupt-functionaliteiten van de microcontroller. Zonder deze bibliotheek zal je geen interrupt handler ISR kunnen aanmaken en gebruiken!

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
        #include <avr/interrupt.h>
        #include <avr/io.h>
        #include <util/delay.h>
</code>
    </pre>
</div>

### De interrupt-handler

De interrupt-handler kunnen we aanmaken via de ISR-routine. Aan deze routine geven het (programma)geheugenadres mee dat gekoppeld is aan de interrupt die we willen gebruiken. In dit voorbeeld willen we kunnen reageren op een externe gebeurtenis op pin PE5,die gekoppeld is aan INT5. De parameter die we moeten meegeven aan de ISR macro is INT5_vect (oftwel de naam van de interrupt + _vect) wat in de praktijk overeenkomt met het adres 0x000C van het programmageheugen. In de interrupt vector table van de microcontroller (pagina van de datasheet) kan je een lijst vinden van alle interrupts.

Denk er ook aan dat interrupt routines kort moeten zijn! De LEDs op het dwenguino-bord zitten gelukkig op dezelfde poort A. Bijgevolg kunnen we ze allemaal tegelijk omklappen in 1 kloktik met behulp van de bitsgewijze XOR-operatie ^:

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
        ISR(INT5_vect) {
          PORTA ^= 0xFF; // toggle LEDs
        }
</code>
    </pre>
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

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
        int main(void) {
          DDRA = 0xFF;  // Set all PAn pins to output
          PORTA = 0xFF; // Turn all LEDs on

          DDRE &= ~(1<<PE5); // Set PE5 to input
          PORTE |= (1<<PE5); // Activate PE5 pull-up

          SREG |= (1<<SREG_I); // Allow interrupts to occur
          EIMSK |= (1<<INT5);  // Enable INT5

          // Configure INT5 to occur on falling edge
          EICRB |= (1<<ISC51); //ISC51 bit set
          EICRB &= ~(1<<ISC50); // ISC50 bit cleared

          while (1) {
            _delay_ms(1);
          }

          return 0;
        }
</code>
    </pre>
</div>

Merk op dat er in de oneindige lus while(1) in feite niets gebeurt. Waarom hebben we toch deze lus nodig? Wordt return ooit opgeroepen?


### Doen!

De oplossing voor het instellen van de externe interrupt INT5 geven we jou cadeau. Het is echter belangrijk dat je dit ook kan terugvinden in de datasheet van de AT90USB646. Kijk daarom na of je de uitleg van de video zelf kan terugvinden in hoofdstuk 12 (External interrupts), i.h.b.z. de sectie 12.0.2 van de datasheet.


### Variabelen in interrupt-routines

Zoals uitgelegd in het filmpje kan je ook variabelen gebruiken in de interrupt-routine. Wanneer je deze variabelen wil gebruiken als een toestandsvariabele in de oneindige lus in je main waarvan de toestand verandert in je interrupt-routine, dan moet deze variabele een **globale variabele** zijn. Dit is een variabele die zichtbaar is voor alle functies en dus gedeclareerd wordt in de namespace van je programma (onder de imports van je main file is een goede plek om dit te doen). Op die manier kan je counter incrementeren tijdens te ISR én ook uitlezen in de main functie om naar de LCD te printen

Bovendien moet je, omdat deze variabele aangepast wordt in de ISR-routine, het keyword **volatile** gebruiken om te verhinderen dat de compiler té veel optimalisaties doorvoort.Een voorbeeld vind je hieronder:

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
        ...
        volatile unsigned char toestand;
        ...
        ISR(EEN_vect) {
          toestand = 1;
        }
        ...
        int main(void) {
          ...
          while(1) {
            if(toestand == 1) { ... } else { ... }
          }
          return 0;
        }
</code>
    </pre>
</div>