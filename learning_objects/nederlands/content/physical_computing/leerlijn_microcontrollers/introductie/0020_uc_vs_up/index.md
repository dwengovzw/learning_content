---
hruid: leerlijn_uc_vs_up
version: 1
language: nl
title: "µController of µProcessor?"
description: "Hier leggen we het verschil uit tussen een microcontroller en een microprocessor."
keywords: ["Microcontroller", "µC", "microprocessor", "processor", "CPU"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16]
difficulty: 1
estimated_time: 25
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Microcontroller of microprocessor?

We kennen nu al heel wat voorbeelden van toepassingen waarin µCs gebruikt worden. Maar wat is nu het fundamentele verschil tussen een µC in bijvoorbeeld een vaatwasmachine en de microprocessor (µP) in je smartphone? Hieronder lijsten we zowel de verschillen als gelijkenissen tussen deze systemen op. Merk op dat er tegenwoordig heel wat complexe computerchips bestaan. Soms combineren deze functionaliteiten van de twee types systemen. De grens tussen de µC en de µP kan in de praktijk dus wat vaag zijn. Het is niet de bedoeling dat je de eigenschappen van deze systemen uit het hoofd kent. Wel moet je bij het ontwikkelen van een toepassing het meest geschikte systeem kunnen kiezen.

## Verschillen

<table>
    <tr>
        <th><h4>Microcontroller</h4></th>
        <th><h4>Microprocessor</h4></th>
    </tr>
    <tr>
        <td colspan="2"><h5>Toepassingen</h5></td>
    </tr>
    <tr>
        <td>Microcontrollers zijn ontworpen om zeer specifieke taken uit te voeren zoals het lezen van een sensorwaarde en op basis daarvan een actuator (bv. motor) aan te sturen. Meestal worden microcontrollers geïntegreerd in een ingebed systeem waar ze de hardware van het systeem controleren (bv. een vaatwasmachine, een auto of een elektrische boormachine). Een specifieke eigenschap van microcontrollers is dat ze goed zijn in realtime toepassingen waarbij exacte timing essentieel is. </td>
        <td>Microprocessoren zijn rekeneenheden voor algemeen gebruik (general-purpose). Bijgevolg kunnen ze veel verschillende taken uitvoeren. Daarom worden ze gebruikt in systemen zoals laptops, desktops en servers.</td>
    </tr>
    <tr>
        <td colspan="2"><h5>Integratie</h5></td>
    </tr>
    <tr>
        <td>Microcontrollers zijn systemen op een chip (SoC) apparaten. Alle hardware die nodig is, wordt op de chip geïntegreerd. Een µC heeft zijn eigen verwerkingseenheid (CPU), geheugen, invoer/uitvoer en randapparaten.</td>
        <td>Microprocessoren zijn gewoonlijk afhankelijk van externe apparaten. Meestal gebruiken ze extern geheugen, externe invoer/uitvoer hardware en externe randapparaten (bv. een GPU). Merk op dat recente microprocessoren steeds meer externe apparaten integreren. Zo heeft de nieuwe M3 chip van Apple zowel een geïntegreerde GPU als geïntegreerd geheugen.</td>
    </tr>
    <tr>
        <td colspan="2"><h5>Stroomverbruik</h5></td>
    </tr>
    <tr>
        <td>Microcontrollers hebben gewoonlijk minder rekenkracht en worden geoptimaliseerd voor een specifieke toepassing. Bijgevolg verbruiken ze ook veel minder energie dan een microprocessor.</td>
        <td>Microprocessoren zijn ontworpen om veel rekenkracht te hebben zodat ze complexe taken kunnen uitvoeren. Bijgevolg verbruiken ze significant meer energie dan een µC.</td>
    </tr>
    <tr>
        <td colspan="2"><h5>Besturingssysteem</h5></td>
    </tr>
    <tr>
        <td>Microcontrollers maken gewoonlijk geen gebruik van een besturingssysteem. De code die je schrijft wordt rechtstreeks op de chip uitgevoerd. Dit zorgt ervoor dat je gemakkelijk energie-efficiënte realtime toepassingen kan ontwikkelen.</td>
        <td>Microprocessoren hebben een besturingssysteem nodig om te kunnen functioneren. Besturingssystemen zoals Linux, Windows of macOS voorzien verschillende functionaliteiten zoals multitasking.</td>
    </tr>
</table>



## Gelijkenissen
- µC en µP bevatten beiden een centrale verwerkingseenheid (CVE of CPU). Deze voert de instructies uit die in een programma staan.
- µC en µP hebben een vastgelegde verzameling van instructies die ze kunnen uitvoeren. Je schrijft een programma door deze instructies achter elkaar te plaatsen (= een programma).
- µC en µP hebben geheugen nodig om zowel programma's als data op te slaan.
- µC en µP hebben verschillende mogelijkheiden om externe invoer te verwerken en bepaalde uitvoer te genereren.
- µC en µP maken gebruik van een klok. Deze legt vast wat de verwerkingssnelheid van het systeem is.


<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        <p>
        Ga online op zoek naar voorbeelden van microcontrollers (bv. ATtiny85) en microprocessoren (bv. Apple M3). Zoek voor elk van de voorbeelden op wat hun kloksnelheid en energieverbruik zijn.
        </p>
    </div>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        <p>
        Microprocessoren kunnen bijna alles wat een microcontroller kan maar vaak op een minder efficiënte manier. Efficiënte toepassingen bouwen is echter van groot belang. Zoek op wat het energieverbruik is van complexe applicaties zoals Google en ChatGPT. Welke impact hebben deze systemen op de maatschappij?
        </p>
    </div>
</div>
