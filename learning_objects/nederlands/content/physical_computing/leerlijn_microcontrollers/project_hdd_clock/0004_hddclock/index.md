---
hruid: pc_hddclock4
version: 1
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# HDD klok

## Van schijf-snelheid tot juiste LED timing

Als we de snelheidssensor willen gebruiken om de verschillende LED-lichten op de LED-strip correct aan te spreken, dan moet je de signalen die de sensor stuurt verstandig gebruiken.
Zoals eerder vermeld zal de snelheidssensor een signaal sturen zodra de infrarood verbinding onderbroken wordt tussen het onderdeel dat een infraroodsignaal verstuurt en het onderdeel dat dit signaal opvangt. 
Om dit te laten gebeuren is het noodzakelijk dat er een voorwerp tussen deze twee objecten beweegt dat afwisselend de verbinding toelaat/verbreekt. In deze oefening is dat de draaiende schijf. De schijf zelf laat geen verbinding toe, maar de smalle gleuf wel. Zodra de gleuf voorbij de sensor is en de infraroodverbinding als gevolg onderbroken wordt, zal de sensor een signaal sturen. 

Zodra dit sensorsignaal ontvangen is en we als gevolg weten dat de schijf eenmaal rondgedraaid heeft, kunnen we beginnen met berekenen wanneer de LED-lichten moeten branden. 
Een goede timing van de LED-lichten wilt zeggen dat de gleuf in de schijf op de juiste positie staat wanneer deze branden. Indien dit lukt krijg je namelijk de illusie dat er in de positie van de gleuf een klokwijzer is aangezien het licht enkel hier zichtbaar is. 
Om te bepalen wat de juiste positie is van de gleuf werken we als volgt; we berekenen de verhouding tussen de tijdseenheden van het huidige tijdstip en het maximum van diezelfde tijdseenheden. Deze verhouding passen we vervolgens toe op de duur van een volledige cyclus van de schijf. De verhouding om bijvoorbeeld 31 minuten aan te duiden is dus 31/60. Dit omdat het huidige aantal minuten 31 is en omdat het maximum aantal minuten op een klok 60 is. 

Concreet zijn dit de berekeningen die gebruiken:
<ul>
    <li>Aantal <b>uren</b> huidig tijdstip / maximaal aantal <b>uren</b> op een analoge klok * tijd voor volledige cyclus van schijf</li>
    <li>Aantal <b>minuten</b> huidig tijdstip / maximaal aantal <b>minuten</b> op een analoge klok * tijd voor volledige cyclus van schijf</li>
    <li>Aantal <b>seconden</b> huidig tijdstip / maximaal aantal <b>seconden</b> op een analoge klok * tijd voor volledige cyclus van schijf</li>
</ul>

Toegepast op een voorbeeld zoals 12 uur, 31 minuten en 10 seconden ziet het er als volgt uit:
<ul>
    <li>12 / 12 * tijd voor volledige cyclus van schijf : op 12/12 van de cyclus van de schijf zullen de LED-lichten met de kleur voor uren branden </li>
    <li>31 / 60 * tijd voor volledige cyclus van schijf : op 31/60 van de cyclus van de schijf zullen de LED-lichten met de kleur voor minuten branden </li>
    <li>10 / 60 * tijd voor volledige cyclus van schijf : op 10/60 van de cyclus van de schijf zullen de LED-lichten met de kleur voor seconden branden </li>
</ul>
Merk op dat we als maximum aantal uren 12 in plaats van 24 gebruiken, een analoge klok gebruikt namelijk maar 12 standen om de uren uit te drukken. 

Door gebruik te maken van deze berekeningen, staat de gleuf op deze locaties wanneer de LED-lichten branden.

<table>
    <tr>
        <td>
            <img alt="Stand schijf voor 12 uur." src="embed\0.png"/>
        </td>
        <td>
            <img alt="Stand schijf voor 31 minuten." src="embed\186.png"/>
        </td>
        <td>
            <img alt="Stand schijf voor 10 seconden." src="embed\60.png"/>
        </td>
    </tr>
    <tr>
        <td>Stand gleuf voor 12 uur.</td>
        <td>Stand gleuf voor 31 minuten.</td>
        <td>Stand gleuf voor 10 seconden.</td>
    </tr>
</table>

De tijd voor een volledige cyclus van de schijf wordt uitgedrukt in ticks. Ticks worden gebruikt als tijdseenheid in de CPU van een computer. 

Deze berekening geeft ons dus een aantal ticks dat we moeten wachten voordat de smalle gleuf in een positie staat die overeenkomt met de positie van een analoge wijzer die het huidig aantal seconden, minuten of uren aangeeft. Hierdoor kunnen we de LED-lichten exact timen om deze te laten branden en vervolgens onmiddelijk weer uit te schakelen. Indien we de LED-lichten niet onmiddelijk zouden uitschakelen, zou correct timen weinig nut hebben. 

Zoals je in het voorbeeld kan zien, hebben de LED-lichten ook een verschillende kleur voor seconden, minuten en uren. We kunnen in de optische illusie immers geen verschillende lengte voorzien voor elke wijzer. We gebruiken hiervoor namelijk de gleuf en deze heeft een vaste lengte. Door verschillende kleuren te gebruiken kunnen we alsnog onderscheid maken tussen de verschillende tijdseenheden.





