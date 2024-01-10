---
hruid: pc_hddclock4
version: 3
language: nl
title: "Van afstand naar geluid"
description: "Van afstand naar geluid"
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# HDD klok

## Van schijf-snelheid tot juiste LED timing

Als we de snelheidssensor willen gebruiken om de verschillende LED-lampjes op de LED strip correct aan te spreken, dan moet je de interrupts die de sensor gebruikt correct gebruiken.
Zoals eerder vermeld zal de snelheidssensor een interrupt sturen zodra de infrarood verbinding onderbroken wordt door een object tussen het onderdeel dat een infraroodsignaal verstuurt en het onderdeel dat dit signaal opvangt.  
Om dit te laten gebeuren is het noodzakelijk dat er voorwerp tussen deze twee objecten beweegt dat afwisselend de verbinding toelaat/verbreekt. In deze oefening is dat de draaiende schijf. De schijf zelf laat geen verbinding toe, maar de smalle gleuf wel. Zodra de gleuf voorbij de sensor is en de infraroodverbinding als gevolg onderbroken wordt, zal de sensor een signaal sturen. 

Zodra dit sensorsignaal ontvangen is en we als gevolg weten dat de schijf eenmaal rondgedraaid heeft, kunnen we beginnen berekenen wanneer de LED's moeten branden. 
Een goede timing van de leds betekend dat de gleuf in de schijf op de juiste positie staat wanneer de LED's branden. Indien dit lukt krijg je namelijk de illusie dat er in de positie van de gleuf een klokwijzer is aangezien het licht enkel hier zichtbaar is. 
Om te bepalen wat de juiste positie is van de gleuf werken we als volgt; we berekenen de verhouding tussen het de tijdseenheden van het huidige tijdstip en het maximum van diezelfde tijdseenheden. Deze verhouding passen we vervolgens toe op de duur van een volledige cyclus van de schijf.  
Concreet zijn dit de berekeningen die gebruiken:
<ul>
    <li>Tijd voor volledige cyclus van schijf / aantal <bmon>uren</b> huidig tijdstip * maximaal aantal <b>uren</b> op een analoge klok</li>
    <li>Tijd voor volledige cyclus van schijf / aantal <b>minuten</b> huidig tijdstip * maximaal aantal <b>minuten</b> op een analoge klok</li>
    <li>Tijd voor volledige cyclus van schijf / aantal <b>seconden</b> huidig tijdstip * maximaal aantal <b>seconden</b> op een analoge klok</li>
</ul>

Toegepast op een voorbeeld zoals 12 uur, 31 minuten en 10 seconden ziet het er als volgt uit:
<ul>
    <li>Tijd voor volledige cyclus van schijf / 12 * 12 : op 12/12 van de cyclus van de schijf zullen de leds met de kleur voor uren branden </li>
    <li>Tijd voor volledige cyclus van schijf / 31 * 60 : op 31/60 van de cyclus van de schijf zullen de leds met de kleur voor minuten branden </li>
    <li>Tijd voor volledige cyclus van schijf / 10 * 60 : op 10/60 van de cyclus van de schijf zullen de leds met de kleur voor seconden branden </li>
</ul>

![](embed/0.png "Stand cyclus schijf voor 12 uur")

![](embed/186.png "Stand cyclus schijf voor 31 minuten")

![](embed/60.png "Stand cyclus schijf voor 10 seconden")

<!-- Toevoegen link timers & interrupts? -->
De tijd voor een volledige cyclus van de schijf wordt uitgedrukt in ticks. Ticks worden gebruikt als tijdseenheid in de CPU van een computer en de concrete duur is afhankelijk van microcontroller tot microcontroller. 

Deze berekening geeft ons dus een aantal ticks dat we moeten wachten voordat de smalle gleuf in een positie staat die overeenkomt met de positie van een analoge wijzer die het huidig aantal seconden, minuten of uren aangeeft. Hierdoor kunnen we de LED lichten exact timen om deze te laten branden om deze vervolgens onmiddelijk weer uit te schakelen. Indien we de LED's niet onmiddelijk zouden uitschakelen, zou correct timen van de LED's weinig nut hebben. 

Zoals vermeld in het voorbeeld hebben de leds ook een verschillende kleur voor seconden, minuten en uren. We kunnen immers geen verschillende lengte's verzien voor de wijzers in de optische illusie. We gebruiken hiervoor namelijk de gleuf en deze heeft een vaste lengte. 



