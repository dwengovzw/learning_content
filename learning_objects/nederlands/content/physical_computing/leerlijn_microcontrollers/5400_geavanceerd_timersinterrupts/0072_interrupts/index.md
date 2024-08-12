---
hruid: pc_micro_interrupts
version: 3
language: nl
title: "Interrupts"
description: "Interrupts"
keywords: ["Microcontroller","interrupts"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# Interrupts

In essentie laten interrupts toe om bepaalde gebeurtenissen (events) tijdig af te handelen, onafhankelijk van de code die ondertussen uitgevoerd wordt op de microcontroller.

Volgende figuur geeft een schematisch overzicht van hoe dit gerealiseerd wordt in de microcontroller: 

![](embed/interrupts.png "interrupts")

Elke interrupt heeft een ID, een beschrijving van waardoor de interrupt getriggerd is en een pointer naar de interrupt service routine (ISR), de code die moet uitgevoerd worden als de interrupt plaatsvindt. Die informatie zit vervat in de Interrupt Vector Table. De interrupt vector table van de Atmel microcontroller kan je terugvinden in de datasheet in sectie 10.1.

Een interrupt request wordt gesignaleerd door een flag (een bit) op 1 te zetten in een Interrupt Flag Register. Vervolgens checkt de microcontroller of interrupts toegelaten zijn én of deze specifieke interrupt ook moet worden afgehandeld. Als dit het geval is wordt alles klaargemaakt om de bijhorende ISR uit te voeren. Na het uitvoeren van de ISR hervat de microcontroller terug de code in de main loop. Meer info over wat er precies gebeurt tijdens het *klaarzetten* vind je in sectie 5.8 van de datasheet.

De bron van een interrupt kan softwarematig of hardwarematig zijn, in het tweede geval spreken we over een externe interrupt. Concreet betekent dit dat de interrupt verbonden is met een fysieke pin van de microcontroller. Hoofdstuk 12 van de datasheet gaat over externe interrupts.

<div class="dwengo-content sideinfo">
    <h2 class="title">Het belang van korte Interrupt Service Routines</h2>
    <div class="content">
        <p>
            Tijdens het uitvoeren van de ISR worden ook alle andere interrupts genegeerd, zoals je kan lezen in sectie 5.8. <strong>Het is daarom zeer belangrijk dat je interrupt routines kort houdt</strong>. Anders dreig je andere signalen te missen tijdens het afhandelen.
        </p>
        <p>
            Zelfs als je geen andere signalen zou kunnen missen kan je nog steeds het algemene programma-verloop beïnvloeden met (te) lange interrupt routines. Microcontrollers worden gebruikt in allerlei systeem- en levenskritische ware-tijd (real-time) toepassingen, dit omwille van hun deterministisch gedrag (er is geen besturingssysteem of interpreter die nog allerlei zaken kan uitvoeren). Met andere woorden <em>what you see</em> in de gecompileerde machine-instructies is <em>what you get</em> (zie de laatste oefening van practicum 1). Echter, wanneer je lange interrupt-routines gebruikt, is het veel moeilijker (of zelfs onmogelijk) om de juiste werking te garanderen.
        </p>
        <p>
            We kunnen het niet genoeg herhalen: <strong>Het is uitvoeren van floating point bewerkingen, delays en andere trage operaties uit te voeren in de interrupt-routine moet je absoluut vermijden!</strong>
        </p>
    </div>
</div>