---
hruid: pc_micro_p2_oef3
version: 3
language: nl
title: "Oefening 3"
description: "Oefening 3"
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
teacher_exclusive: false
---
# Practicum 2 - Timers en Interrupts

## Oefening 3: Gebruiken van Timers voor het precies meten van de reactietijden wonder busy waiting

In deze oefening gaan we de while loop met de _delay functie voor het meten van de reactietijd vervangen door een timer. Dat zal ons in staat stellen om het LCD scherm aan te sturen ondertussen of andere nuttige dingen te doen, zonder de metingen te beïnvloeden.


### Timers

In de kennisclips zijn timers al uitgebreid aan bod gekomen en we raden je aan om de clip nog eens te herbekijken als het al wat ver zou zitten.

In essentie is een Timer een mechanisme in de microcontroller dat toelaat om bij te houden hoeveel klokcycli al verstreken zijn sinds het moment waarop de timer aangezet werd aan de mogelijkheid biedt om gepast te reageren als bepaalde aantallen bereikt zijn.


### Opdracht 3.1 - Verkennen Datasheet

De microcontroller heeft **4 timers**, in dit practicum gebruiken enkel de 16-bot timers, **Timer 1** en **Timer 3**.

Alle info over de timers die je nodig hebt in dit pracitcum vind je in de datasheet in hoofdstukken **13**, **15**. Initieel zal de datasheet overweldigend zijn, maar ermee werken is een belangrijke vaardigheid die jullie dit semester zullen leren.

* Zorg dat je zeker volgende begrippen aan jezelf kan uitleggen en zoek ze indien nodig op de Ufora pagina:
    * Timer Counter Register (TCNT)
    * Prescaler
    * Timer Operation Mode
    * Normal operation mode

* Ga op zoek op p.140 naar de opties voor de prescaler. Bereken hoelang het duurt vooraleer het TCNT1 register de maximale waarde bereikt bij gebruik van de hoogste prescaler waarde.

* Ga ook eens kijken in sectie 15.8.1 wat er gebeurt met het TCNT register als het zijn maximale waarde heeft bereikt in normal mode.


### Opdracht 3.2 - Visualiseren van het TCNT1 register

Als eerste oefening zullen het timer counter value register (TCNT1) van Timer 1 uitlezen en de waarde op het LCD scherm printen. Je mag daartoe onderstaand snippet kopiëren, compileren en uploaden op de microcontroller.

<div class="highlight highlight-source-c">
<pre>#<span class="pl-k">include</span> <span class="pl-s"><span class="pl-pds">"</span>dwenguinoBoard.h<span class="pl-pds">"</span></span>
#<span class="pl-k">include</span> <span class="pl-s"><span class="pl-pds">"</span>dwenguinoLCD.h<span class="pl-pds">"</span></span>

<span class="pl-c"><span class="pl-c">/*</span> Snippet to print out the 16-bit TCNT1 register to the LCD<span class="pl-c">*/</span></span>
<span class="pl-k">int</span> <span class="pl-en">main</span>() {
    <span class="pl-c1">initLCD</span>();
    <span class="pl-c1">clearLCD</span>();

   <span class="pl-c"><span class="pl-c">//</span> Initialize Timer 1 in normal mode, which is the default.</span>
    <span class="pl-c"><span class="pl-c">//</span> All we have to do is change the prescaler from 0 to a non-zero value</span>
    <span class="pl-c"><span class="pl-c">//</span> TODO: set prescaler here</span>

   <span class="pl-k">while</span>(<span class="pl-c1">1</span>){
        <span class="pl-c"><span class="pl-c">//</span> print the value of the timer to the LCD</span>
        <span class="pl-c"><span class="pl-c">//</span> cannot just combine into INT and print</span>
        <span class="pl-c"><span class="pl-c">//</span> as that would give negative values for large numbers</span>

   <span class="pl-c1">printIntToLCD</span>(TCNT1L,<span class="pl-c1">0</span>,<span class="pl-c1">3</span>);
        <span class="pl-c1">printIntToLCD</span>(TCNT1H,<span class="pl-c1">0</span>,<span class="pl-c1">0</span>);

   <span class="pl-k">if</span> (TCNT1H == <span class="pl-c1">0</span>){
            <span class="pl-c1">clearLCD</span>();
        }
    }

   <span class="pl-k">return</span> <span class="pl-c1">0</span>;
}</pre>
</div>
**
Je zal zien dat de de counter op nul blijft staan. Ga in **Table 15-5. op p.140** op zoek naar de bits die je moet instellen om de prescaler op een niet-nul waarde in te stellen en zo de timer te starten.

* Zet de prescaler op de maximale waarde.
* Check of de TCNTn registers zich inderdaad zo gedragen als je had verwacht en gebruik je smartphone om (ongeveer) te meten of je goed berekend had hoelang het duurt voor het TCNT1 register vol loopt.


### Opdracht 3.3 - Implementatie van het meten van reactietijd met Timer1

In deze opdracht gaan we de code uit de vorige oefening aanpassen zodat de **Timer 1** gebruikt wordt om de reactietijd te meten.

We weten dat de gemiddelde reactietijd tussen het aansturen van de LEDs en het indrukken van de knop ongeveer 200 ms bedraagt, maar we willen zeker voldoende marge nemen en dus zouden we liefst alles tot en met 1 seconde willen kunnen meten. **Bepaal een gepaste prescaler waarde voor Timer 1**.

Pas nu de code aan zodat je de **Timer 1** klok aan zet op het moment dat de de LEDs aan gaan. Wanneer de C-knop ingedrukt wordt lees je nu het TCNT register uit. Daarna reken je uit met hoeveel milliseconden dit overeenstemt.

> Let op voor eventuele impliciete type casting tussen verschillende soorten variabelen. Als je bijvoorbeeld In C moet je typisch iets nauwgezetter zijn dan in dynamische talen zoals Python, zoals jullie wel al gemerkt zullen hebben.


### Waarom ook al weer een timer?

Door een timer te gebruiken:

* Zijn we niet meer beperkt door de onnauwkeurigheden van de _delay functie en andere code overhead.
* Kunnen we tijdens het wachten andere dingen doen, zoals informatie printen naar de LCD of communiceren met de buitenwereld zonder dat dit de meting van de reactijtijd beinvloedt, al moeten we nog steeds voldoende vaak de knop uitlezen. Dit gaan we in de volgende oefening oplossen door gebruik te maken van interrupts.