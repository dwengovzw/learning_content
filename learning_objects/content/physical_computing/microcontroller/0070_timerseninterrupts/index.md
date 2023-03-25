---
hruid: pc_micro_tei
version: 3
language: nl
title: "Timers en interrupts"
description: "Timers en interrupts"
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

![](@youtube/https://www.youtube.com/embed/5PnCgXMj7E4 "Timers en interrupt")

In de beschrijving hieronder gaan we dieper in op de basisconcepten timers en interrupts, en werken we een praktisch voorbeeld uit.


## Het basisconcept timers

Alle info over de timers is ook terug te vinden in de hoofdstukken 13 tot 16 in de datasheet, maar die kunnen nogal overweldigend zijn. In de volgende paragrafen worden een aantal belangrijke concepten nog eens kort uitgelegd met een link naar de corresponderende delen van de datasheet.

In essentie is een Timer niet meer of minder dan een mechanisme in de microcontroller dat toelaat om bij te houden hoeveel klokcycli al verstreken zijn sinds het moment waarop de timer aangezet werd. Dat aantal wordt bijgehouden in een counter register waarvan de naam TCNTn is(waarbij n staat voor het nummer van de klok). Onze microcontroller heeft 4 Timers: Timer0 en Timer2 zijn 8-bit timers, wat wil zeggen dat zij maar tot 2^8 kunnen tellen, Timer1 en Timer3 zijn 16-bit timers, wat wil zeggen dat zij maximaal 2^16 ticks kunnen tellen. Info over de counter unit vind je bv. in sectie 15.4 voor de 16-bit timers.

Naast de counter unit zijn er extra functionaliteiten voorzien die het makkelijker maken om te reageren op bepaalde intervallen, bvb om een pin hoog te zetten telkens als er 100 ticks verstreken zijn. Dit zijn de zogenaamde *Modes of operation*. Hierover vind je meer in sectie 15.8 van de datasheet.

De *normal mode* is de standaard modus van de timer, m.a.w. je hoeft dus geen bits te configureren om deze mode te gebruiken. Lees sectie 15.8.1 van de datasheet om uit te vissen wat die modus precies inhoudt, al kan je het waarschijnlijk wel al afleiden uit de naam en de uitleg in de vorige paragraaf.

De CPU / IO klok van de microcontroller loopt aan 16MHz, zoals je weet. Een 16-bit timer kan daarom maar ongeveer 4µs tellen voor het TCNT register vol zit. Dat is niet bepaald lang en aarom is er ook nog de *prescaler* waarmee je de timers kan vertragen: het TCNTn register zal nu pas elke N klokcycli incrementeren. Meer over prescalers lees je op pagina 140 van de datasheet.


## Het basisconcept interrupts

In essentie laten interrupts toe om bepaalde gebeurtenissen (events) tijdig af te handelen, onafhankelijk van de code die ondertussen uitgevoerd wordt op de microcontroller.

Volgende figuur geeft een schematisch overzicht van hoe dit gerealiseerd wordt in de microcontroller: 

![](embed/interrupts.png "interrupts")

Elke interrupt heeft een ID, een beschrijving van waardoor de interrupt getriggerd is en een pointer naar de interrupt service routine (ISR), de code die moet uitgevoerd worden als de interrupt plaatsvindt. Die informatie zit vervat in de Interrupt Vector Table. De interrupt vector table van de Atmel microcontroller kan je terugvinden in de datasheet in sectie 10.1.

Een interrupt request wordt gesignaleerd door een flag (een bit) op 1 te zetten in een Interrupt Flag Register. Vervolgens checkt de microcontroller of interrupts toegelaten zijn én of deze specifieke interrupt ook moet worden afgehandeld. Als dit het geval is wordt alles klaargemaakt om de bijhorende ISR uit te voeren. Na het uitvoeren van de ISR hervat de microcontroller terug de code in de main loop. Meer info over wat er precies gebeurt tijdens het *klaarzetten* vind je in sectie 5.8 van de datasheet.

De bron van een interrupt kan softwarematig of hardwarematig zijn, in het tweede geval spreken we over een externe interrupt. Concreet betekent dit dat de interrupt verbonden is met een fysieke pin van de microcontroller. Hoofdstuk 12 van de datasheet gaat over externe interrupts.


## Het belang van korte Interrupt Service Routines

Tijdens het uitvoeren van de ISR worden ook alle andere interrupts genegeerd, zoals je kan lezen in sectie 5.8. **Het is daarom zeer belangrijk dat je interrupt routines kort houdt**. Anders dreig je andere signalen te missen tijdens het afhandelen.

Zelfs als je geen andere signalen zou kunnen missen kan je nog steeds het algemene programma-verloop beïnvloeden met (te) lange interrupt routines. Microcontrollers worden gebruikt in allerlei systeem- en levenskritische ware-tijd (real-time) toepassingen, dit omwille van hun deterministisch gedrag (er is geen besturingssysteem of interpreter die nog allerlei zaken kan uitvoeren). Met andere woorden *what you see* in de gecompileerde machine-instructies is *what you get* (zie de laatste oefening van practicum 1). Echter, wanneer je lange interrupt-routines gebruikt, is het veel moeilijker (of zelfs onmogelijk) om de juiste werking te garanderen.

We kunnen het niet genoeg herhalen: **Het is uitvoeren van floating point bewerkingen, delays en andere trage operaties uit te voeren in de interrupt-routine moet je absoluut vermijden!**