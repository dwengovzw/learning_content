---
hruid: pc_micro_p1_oef1
version: 3
language: nl
title: "Oefening 1"
description: "Oefening 1"
keywords: ["Microcontroller", "leds", "knoppen", "practicum", "C"]
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
# Practicum 1

## Oefening 1: Leds aanschakelen met de drukknoppen

Analyseer eerst het schema van de dwenguino om te achterhalen hoe de leds met de microcontroller verbonden zijn.

Een deel van de fysieke pinnen van de microcontroller kan je gebruiken om waarden te inputten en outputten (I/O). Het andere deel wordt voor allelei dingen gebruikt, zoals b.v.b. voeding, kloksynchronisatie en USB connectie. Zoek in de datasheet van de microcontroller in sectie 2.2 (pp. 8-10) welke pinnen gebruikt kunnen worden voor I/O.

Merk op dat de I/O pinnen steeds gegroepeerd zijn per 8.

<div class="dwengo-content sideinfo">
    <h2 class="title">De code</h2>
    <div class="content">
        <p>
        Een <strong>I/O-poort</strong> is het geheel van:<br><br>
        </p>
        <p>
            <ul>
                <li>8 fysieke pinnen (de letterlijke stukjes metaal)</li>
                <li>Drie 8-bit registers (DDRx, PINx, PORTx)</li>
                <li>8 pull-up weerstanden</li>
                <li>Een aantal elektrische componenten voor de werking van de poort</li>
    </div>
</div>

Elke poort wordt in de datasheet benoemd met een x die je moet vervangen door een hoofdletter bvb A, B etc. Bij Port A horen dus registers DDRA, PINA en PORTA. Deze registers zal je in dit practicum juist moeten instellen of inlezen om de I/O poort te gebruiken. Om de 8 bits in een register te benoemen, gebruikt de dataset de letter n. n moet je dus vervangen door een getal tussen 0 en 7.

> In hoofdstuk 11 van de datasheet (p. 72) vind je schema 11-2. Dit schema toont een achtste van een I/O-poort, het stuk dat hoort bij 1 fysieke pin. Een hele poort bestaat dus uit 8 keer wat je ziet op het schema. <br><br> Het is normaal dat je momenteel nog niet veel van de figuur begrijpt. De essentie is als volgt. Helemaal links zie je Pxn staan. Pxn is de fysieke pin ("het metaaltje"). Dat metaaltje is verbonden met 3 flipflops: DDxn, PORTxn, PINxn. Een flipflop is een elektrische component die 1 bit opslaat. De DDxn bit is verbonden met een driehoekje (= een tri-state buffer) en bepaalt daarmee of de waarde van de PORTxn bit al dan niet op Pxn ge-output wordt. Daarnaast kan je zien dat Pxn ook verbonden is met de PINxn bit (de tussenliggende compomenten mag je negeren). Dit geeft je de mogelijkheid om de waarde te lezen die op de pin staat.


### Pinnen configureren als input of output

De I/O-pinnen van de microcontroller kan je configureren zodat je ze ofwel kan uitlezen, ofwel er naar kan schrijven. Dit stel je in via het DDRx-register, hierbij vervang je x door de naam van het I/O-register.

> DDR staat voor *Data Direction Register*. Het bepaalt dus de richting waarin de data gaat: ingelezen of uitgeschreven.


#### Pinnen configureren als output

Wil je bijvoorbeeld de eerste en derde en pin van Port A instellen als een output pin, dan doe je in je C code:

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
        DDRA |= 0b00000101

        // of equivalent

        DDRA |= _BV(PA0) | _BV(PA2);
</code>
    </pre>
</div>

_BV(NAAM_VAN_PIN) is een voorgedefinieerde macro uit de AVR bibliotheek. Een macro wordt door de C compiler voor het compileren omgezet in gewone C code. Hieronder zie je de definitie van de _BV macro:

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
        #define_BV(bit) 1 << bit
</code>
    </pre>
</div>

Bijgevolg is dus bijvoorbeeld:

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
        _BV(PA2) == _BV(2) == (1 << 2) == (0b00000001 << 2) == 0b00000100
</code>
    </pre>
</div>

> DDRA, PA2 etc. zijn ook macro's die het voor ons gemakkelijker maken om de juiste registers en bits aan te passen. Dit soort macro's bestaan voor alle bits en registers die je later zal tegenkomen in de datasheet, zoals bv. de WGM10 bit in het TCCR1A register.

Merk ook op dat we de registers niet volledig overschrijven met =, maar dat we de bitwise or |= gebruiken. Dit zorgt ervoor dat we de overige bits in het register niet aantasten.


#### Pinnen configureren als input

Om dezelfde pinnen terug in te stellen als input doe je: 

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
        DDRA &= 0b11111010
        
        // of equivalent:
        
        DDRA &= ~(_BV(PA0) | _BV(PA2))
</code>
    </pre>
</div>

> Tip: het _BV macro gebruiken met de naam van de pin (bv. PA2) maakt je code leesbaarder en voorkomt fouten. Dit wordt beschouwd als good practice en we raden jullie sterk aan dit ook te doen voor de practica en het project.

### Waarde outputten op een pin

Daarnet lezen we hoe we pinnen instellen als output. Nu kunnen we er een **waarde** naar schrijven aan de hand van het PORTx register. Zo kunnen we bv. de laagste bit van PORTA aanschakelen:

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
        PORTA |= 0b00000001;
</code>
    </pre>
</div>


### Waarde inlezen van pinnen

Om een waarde van alle pinnen van een poort x in te lezen gebruiken we het PINx register. Op volgende manier lezen we bijvoorbeeld de 8 pinnen van Port A in:

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
        char my_var = 0;
        my_var = PINA;
</code>
    </pre>
</div>

Bij het configureren van de pinnen zagen jullie al hoe _BV gebruikt kan worden om bitmaskers te creëren. Om te controleren of een bepaalde bit van een register op 1 of 0 staat maak je ook gebruik van een masker. Als we bijvoorbeeld willen controleren of de vierde bit van het PINA register op 1 staat gebruiken we de volgende code:

<div class="dwengo-content dwengo-code-simulator">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">
        if (PINA & _BV(PA3)) {
            // Ja, de vierde bit van het PINA register staat hoog.
        } else {
            // Nee, de vierde bit staat laag.
        }
</code>
    </pre>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht 1</h2>
    <div class="content">
        <p>
            Zoek op het schema van de dwenguino welke pinnen verbonden zijn met de linkse (W = west) en rechtse (E = east) drukknoppen. Schrijf nu code die ervoor zorgt dat:
        </p>
        <p>
            <ul>
                <li>Als de linkse knop ingedrukt is, moet de meest linkse led branden.</li>
                <li>Als de rechtse knop ingedruk is, moet de meest rechtse led branden.</li>
            </ul>
        </p>
        <p>
            Zoek daarna op in sectie 11.2 van de datasheet hoe je een **pull-up weerstand** activeert. In je code:
        </p>
        <p>
            <ul>
                <li>Activeer de pull-up weerstand voor de pin verbonden met de rechtse knop</li>
                <li>Deactiveer de pull-up weerstand voor de pin verbonden met de linkse knop.</li>
            </ul>
        </p>
        <p>
            Upload en test nu je code en vergelijk het gedrag van de rechtse en de linkse knop.
        </p>
    </div>
</div>

### Het belang van pull-up weerstanden

Normaal gezien zou je bij de vorige oefening gemerkt moeten hebben dat de rechtse knop betrouwbaarder werkt dan de linkse. Voor sommige bordjes is het effect meer uitgesproken dan bij andere.

De onderstaande figuur toont de werking van een pull-up weerstand.

![](embed/pullup.jpg "pull-up weerstand")

Wanneer de pull-up weerstand niet gebruikt wordt, is de pin niet verbonden met 5V. Als bovendien de knop niet ingedrukt is, is de pin ook niet verbonden met ground. De pin is dan in een **zwevende** toestand.<br>
In deze toestand kunnen ladingen opbouwen op de pin. Deze ladingen kunnen komen van de externe omgeving, of kunnen overgebleven zijn nadat de pin daarvoor hoog heeft gestaan. Ook kan stroom in een andere geleider van het bordje een spanning induceren in de geleider die met de pin verbonden is.<br>
Zonder pull-up weerstand kan dit alles leiden tot onbetrouwbaar gedrag wanneer de verbonden knop niet ingedrukt is.

Wanneer de pull-up weerstand wel gebruikt wordt, is de pin wel verbonden met 5V. Als de knop niet ingedrukt is, zal de spanning op de pin dus hoog gehouden worden door de voeding.

> Vraag om zelf over te denken: Waarom gebruiken we hier een weerstand en verbinden we de pin niet gewoon met de 5V lijn?