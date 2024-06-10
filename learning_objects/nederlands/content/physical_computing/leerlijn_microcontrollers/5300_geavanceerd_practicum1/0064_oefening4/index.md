---
hruid: pc_micro_p1_oef4
version: 3
language: nl
title: "Oefening 4"
description: "Oefening 4"
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
estimated_time: 60
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# Practicum 1

## Oefening 4: Cylon

![](embed/cylon.jpg "cylon")

In deze oefening bouwen we verder op de vorige oefeningen om een Cylon-modus te schrijven. Ken je de Cylons uit Battlestar Galactica niet? Neem dan eens een kijkje op Youtube.


### Bit shifts

In C kan je met de >>(of <<) operator alle bits van een variable 1 of meer posities naar rechts (of links) opschuiven. Je bekomt bijvoorbeeld 0b10010000 als je het volgende uitvoert: 0b00110010 << 3. Deze techniek kan je dus gebruiken om de opgelichte LED van links naar rechts te laten verschuiven.

> Voor **unsigned** integers komen bitshifts overeen met vermenigvuldigingen of delingen door machten van 2. Shifts uitvoeren gaat heel snel, dus de meeste compilers zullen vanzelf vermenigvuldigingen of delingen door 2 omzetten naar shifts in machine code.

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 4.1 - Cylon modus met delay</h2>
    <div class="content">
        <p>
          Schrijf nu code voor de Cylon modus. In de Cylon modus brandt steeds 1 led. Zorg ervoor dat:
        </p>
        <p>
          <ul>
            <li>De led die aan staat eerst elke 70 ms naar links beweegt.</li>
            <li>Wanneer de meeste linkse led bereikt is, keert de richting om en beweegt de led naar rechts.</li>
            <li>Wanneer de meest rechtse led weer aan staat, keert de richting opnieuw om.</li>
          </ul>
        </p>
        <p>
          Maak daarna van de onderste knop een "play and pause" knop die de Cylon kan stilleggen.
        </p>
    </div>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 4.2 - Cylon modus zonder delay</h2>
    <div class="content">
        <p>
          In deze laatste opdracht willen we jullie laten zien hoe de assembly code eruit ziet die op microcontroller runt. Verlies hier zeker niet teveel tijd, de bedoeling is dat jullie er ongeveer 30-45 min aan spenderen.
        </p>
        <p>
          In deze opdracht herschrijven we de Cylon modus zodat die de _delay_ms(int) functie niet meer gebruikt. We zullen dit doen door microcontroller bezig te houden met "dummy" berekeningen. Gebruik daarvoor de dummy_function(x, n) uit onderstaand codefragment.
        </p>
        <p>
          <div class="dwengo-content dwengo-code-simulator">
            <pre>
<code class="language-cpp" data-filename="filename.cpp">
                  #include <avr/io.h>

                  attribute((noinline)) unsigned char dummy_function(unsigned char x, unsigned long iterations) {
                    for (unsigned long i = 0; i < iterations; i++) {
                      asm volatile("nop");
                      asm volatile("nop");
                      x *= 2;
                      x += 145;
                      x *= 3;
                      x -= 4;
                      x /= 8;
                      asm volatile("nop");
                      asm volatile("nop");
                    }
                    return x;
                  }

                  int main(void) {
                    DDRA = 0xff;
                    volatile unsigned char x = 7;
                    unsigned long iterations = 1000000L; // 1 million
                    while (1) {
                      x = dummy_function(x, iterations);
                      PORTA ^= 0b11111111;
                    }
                    return 0;
                  }
</code>
            </pre>
          </div>
        </p>
    </div>
</div>

> Merk op dat we voor de definitie van de dummy_function() __attribute__((noinline)) zetten. Daardoor zal de compiler de function niet inlinen en vinden we hem gemakkelijker terug in de assembly. Bovendien hebben we rond de berekeningen ook enkele assembly "nop" instructies gezet, die zal je ook zien in de assembly straks. We gebruiken ook een aantal keer volatile, om te voorkomen dat de compiler delen van de code zou weg-optimaliseren.

De waarde die de functie berekent speelt geen rol, maar wat wel belangrijk is, is de **uitvoeringstijd** van de functie. Het is de bedoeling dat jullie op zoek gaan naar de waarde van n die ervoor zorgt dat de dummy_function() 95 ms uitvoeringstijd nodig heeft. Je zou n kunnen proberen schatten door gebruik te maken van een chronometer, maar we weten dat de microcontroller een klokfrequentie heeft van **16 MHz**. Als we weten hoeveel instructies de dummy_function nodig heeft, en hoeveel **klokcycli** elke instructie nodig heeft, kunnen we berekenen hoe lang de dummy_function() zal duren. Om te weten in welke instructies de compiler de dummy_function() omzet, zal je een kijkje nemen in de assembly code.