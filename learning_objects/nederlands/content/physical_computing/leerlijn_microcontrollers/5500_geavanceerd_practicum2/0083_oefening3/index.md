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
estimated_time: 30
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

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 3.1</h2>
    <div class="content">
        <h3>Verkennen Datasheet</h3>
        <p>
            De microcontroller heeft <strong>4 timers</strong>, in dit practicum gebruiken enkel de 16-bot timers, <strong>Timer 1</strong> en <strong>Timer 3</strong>.
        </p>
        <p>
            Alle info over de timers die je nodig hebt in dit pracitcum vind je in de datasheet in hoofdstukken <strong>13</strong>, <strong>15</strong>. Initieel zal de datasheet overweldigend zijn, maar ermee werken is een belangrijke vaardigheid die jullie dit semester zullen leren.
        </p>
        <p>
            <ul>
                <li>Zorg dat je zeker volgende begrippen aan jezelf kan uitleggen en zoek ze indien nodig op de Ufora pagina:
                    <ul>
                        <li>Timer Counter Register (TCNT)</li>
                        <li>Prescaler</li>
                        <li>Timer Operation Mode</li>
                        <li>Normal operation mode</li>
                    </ul>
                </li>
                <li>Ga op zoek op p.140 naar de opties voor de prescaler. Bereken hoelang het duurt vooraleer het TCNT1 register de maximale waarde bereikt bij gebruik van de hoogste prescaler waarde.</li>
                <li>Ga ook eens kijken in sectie 15.8.1 wat er gebeurt met het TCNT register als het zijn maximale waarde heeft bereikt in normal mode.</li>
            </ul>
        </p>
    </div>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 3.2</h2>
    <div class="content">
        <h3>Visualiseren van het TCNT1 register</h3>
        <p>
            Als eerste oefening zullen het timer counter value register (TCNT1) van Timer 1 uitlezen en de waarde op het LCD scherm printen. Je mag daartoe onderstaand snippet kopiëren, compileren en uploaden op de microcontroller.
        </p>
        <p>
            <div class="dwengo-content dwengo-code-simulator">
                <pre>
<code class="language-cpp" data-filename="filename.cpp">
                        #include "dwenguinoBoard.h"
                        #include "dwenguinoLCD.h"

                        // Snippet to print out the 16-bit TCNT1 register to the LCD/
                        int main() {
                            initLCD();
                            clearLCD();

                            // Initialize Timer 1 in normal mode, which is the default.
                            // All we have to do is change the prescaler from 0 to a non-zero value
                            // TODO: set prescaler here

                            while(1){
                                // print the value of the timer to the LCD
                                // cannot just combine into INT and print
                                // as that would give negative values for large numbers

                                printIntToLCD(TCNT1L,0,3);
                                printIntToLCD(TCNT1H,0,0);

                                if (TCNT1H == 0){
                                    clearLCD();
                                }
                            }
                            return 0;
                        }
</code>
                </pre>
            </div>
        </p>
    </div>
</div>

Je zal zien dat de de counter op nul blijft staan. Ga in **Table 15-5. op p.140** op zoek naar de bits die je moet instellen om de prescaler op een niet-nul waarde in te stellen en zo de timer te starten.

* Zet de prescaler op de maximale waarde.
* Check of de TCNTn registers zich inderdaad zo gedragen als je had verwacht en gebruik je smartphone om (ongeveer) te meten of je goed berekend had hoelang het duurt voor het TCNT1 register vol loopt.

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 3.3</h2>
    <div class="content">
        <h3>Implementatie van het meten van reactietijd met Timer1</h3>
        <p>
            In deze opdracht gaan we de code uit de vorige oefening aanpassen zodat de <strong>Timer 1</strong> gebruikt wordt om de reactietijd te meten.
        </p>
        <p>
            We weten dat de gemiddelde reactietijd tussen het aansturen van de leds en het indrukken van de knop ongeveer 200 ms bedraagt, maar we willen zeker voldoende marge nemen en dus zouden we liefst alles tot en met 1 seconde willen kunnen meten. <strong>Bepaal een gepaste prescaler waarde voor Timer 1<</strong>>.
        </p>
        <p>
            Pas nu de code aan zodat je de <strong>Timer 1</strong> klok aan zet op het moment dat de de leds aan gaan. Wanneer de C-knop ingedrukt wordt lees je nu het TCNT register uit. Daarna reken je uit met hoeveel milliseconden dit overeenstemt.
        </p>
    </div>
</div>

<div class="dwengo-content important">
    <h2 class="title">LET OP!</h2>
    <div class="content">
        Let op voor eventuele impliciete type casting tussen verschillende soorten variabelen. Als je bijvoorbeeld In C moet je typisch iets nauwgezetter zijn dan in dynamische talen zoals Python, zoals jullie wel al gemerkt zullen hebben.
    </div>
</div>

<div class="dwengo-content sideinfo">
    <h2 class="title">Waarom ook al weer een timer?</h2>
    <div class="content">
        <p>
            Door een timer te gebruiken:
        </p>
        <p>
            <ul>
                <li>Zijn we niet meer beperkt door de onnauwkeurigheden van de _delay functie en andere code overhead.</li>
                <li>Kunnen we tijdens het wachten andere dingen doen, zoals informatie printen naar de LCD of communiceren met de buitenwereld zonder dat dit de meting van de reactijtijd beinvloedt, al moeten we nog steeds voldoende vaak de knop uitlezen. Dit gaan we in de volgende oefening oplossen door gebruik te maken van interrupts.</li>
            </ul>
        </p>
    </div>
</div>