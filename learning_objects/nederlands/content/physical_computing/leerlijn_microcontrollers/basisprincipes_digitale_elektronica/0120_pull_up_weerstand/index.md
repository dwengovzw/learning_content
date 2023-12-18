---
hruid: leerlijn_invoer_basisprincipes_pull_up_weerstand
version: 1
language: nl
title: "De pull-up weerstand"
description: "De pull-up weerstand zorgt ervoor dat de spanning op een pin steeds voorspelbaar is."
keywords: ["digitale elektronica", "weerstand", "pull-up", "basisprincipes", "microcontroller", "µC", "arduino", "dwenguino"]
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# De pull-up weerstand

Een pull-up weerstand wordt gebruikt om ervoor te zorgen dat een pin van de µC zeker een hoge waarde krijgt zolang die niet actief naar beneden geschakeld wordt. Dit is van belang omdat pinnen van de µC die niet op een gekende spanning zijn aangesloten “**zweven**”. Van die “zwevende” pinnen kunnen we niet voorspellen welke waarde de µC zal detecteren. Als je met je vinger in de buurt van de pin komt, kan het bijvoorbeeld voorkomen dat er ladingen van je vinger overspringen op de pin waardoor die hoog komt te staan.  


| Schema |  |
| - | - |
| !["Schema van de pull-up weerstand"](img/pullup.svg "Schema van de pull-up weerstand") | Deze figuur toont de werking van een pull-up weerstand. De verbinding met 5V via weerstand R1 zorgt ervoor dat, in het geval de de schakelaar niet ingedrukt is, de waarde van de input pin hoog is. Als de knop wordt ingedrukt, verbinden we de pin met de GND dus krijgt die automatisch de waarde 0. |


<div class="dwengo-content assignment">
    <h2 class="title">Inzichtsvraag</h2>
    <div class="content">
        <p>
            Waarom gebruiken we hier een weerstand en verbinden we de pin niet gewoon met de 5V lijn?
        </p>
    </div>
</div>

<div class="dwengo-content assignment">
    <h2 class="title">Inzichtsvraag</h2>
    <div class="content">
        <p>
            Er bestaat ook een pull-down weerstand. Deze zorgt ervoor dat de waarde van de pin laag is tot de knop wordt ingedrukt. Kan jij het schema tekenen van een pull-down weerstand?
        </p>
    </div>
</div>

<div class="dwengo-content sideinfo">
<h2 class="title">Interessant om te weten!</h2>
    <div class="content">
        In het schema van de pull-up weerstand zie je een voorbeeld van een <strong>externe</strong> pull-up weerstand. De µC heeft op elke pin ook een <strong>interne</strong> pull-up weerstand. Deze kan je activeren aan de hand van code. Wanneer je werkt met een µC is het dus meestal niet nodig om een externe pull-up weerstand op een pin aan te sluiten.
    </div>
</div>