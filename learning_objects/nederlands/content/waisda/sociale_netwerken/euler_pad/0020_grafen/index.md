---
hruid: org-dwengo-waisda-soc-netwerken-graphs-netwerk-grafen
version: 1
language: nl
title: "Grafen"
description: "Wat zijn grafen en wat hebben onze tekeningen ermee te maken?"
keywords: ["grafen","Euleriaans pad"]
content_type: "text/markdown"
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# Grafen

Is het je gelukt? Heb je alle tekeningen kunnen maken zonder je balpen op te heffen? Of is het je bij sommige figuren niet gelukt? Bij veel tekeningen kan het heel moeilijk zijn om een oplossing te vinden door gewoon mogelijkheden uit te proberen. Toch bestaat er een trucje dat je kan helpen om de oplossing gemakkelijker te vinden. Dit trucje komt uit de grafentheorie. 


<div class="dwengo-content sideinfo">
<h2 class="title">Wat is een graaf?</h2>
<div class="content">
Een graaf is een structuur die bestaat uit <strong>knopen</strong> en eventuele verbindingen tussen die knopen, de <strong>bogen</strong>.
</div>
</div>

Hier zie je een voorbeeld van een graaf met **twee knopen** en **één boog** ertussen.

![](img/simple_twonode.svg)

De tekeningen die we probeerden te maken, kunnen we ook voorstellen als grafen. In de volgende tabel zie je links de tekening en rechts de voorstelling als een graaf.

| Tekening | Graaf |
|-|:-:|
| ![](img/euler1.svg) | ![](img/euler1_graph.svg) |
| ![](img/euler2.svg) | ![](img/euler2_graph.svg) |
| ![](img/euler3.svg) | ![](img/euler3_graph.svg) |
| ![](img/euler4.svg) | ![](img/euler4_graph.svg) |


Ons initiële probleem, waarbij we een tekening willen maken zonder onze balpen op te heffen, kunnen we dus vertalen naar een grafenprobleem. Dit probleem formuleren we als volgt. Bestaat er een *wandeling* in de graaf waarbij je elke boog juist een keer oversteekt?

<div class="dwengo-content sideinfo">
    <h2 class="title">Isomorfie</h2>
    <div class="content">
        In tegenstelling tot onze tekeningen, zijn de posities van de knopen van de graaf niet van belang. Je kan de knopen van de graaf op gelijk welke plaats tekenen zolang ze via bogen verbonden blijven met dezelfde knopen. Deze verschillende versies van de graaf zijn <strong>isomorf</strong>. Hieronder zie je bijvoorbeeld een aantal mogelijke graafvoorstellingen voor het huisje.
        <table>
            <tr><td><img src="img/euler1_graph.svg"></img></td></tr>
            <tr><td><img src="img/euler1_graph_var2.svg"></img></td></tr>
            <tr><td><img src="img/euler1_graph_var3.svg"></img></td></tr>
            <tr><td><img src="img/euler1_graph_var4.svg"></img></td></tr>
        </table>
    </div>
</div>


<div class="dwengo-content sideinfo">
<h2 class="title">De Mercedes challenge</h2>
<div class="content">
<p>De Mercedes challenge is een puzzel die viraal is gegaan op TikTok. De uitdaging zou gestart zijn in een Mercedes garage in Dubai. Daar stond een groot Mercedes logo op de grond getekend. Bezoekers van de garage werden uitgedaagd om op over alle lijnen van het logo te lopen zonder twee keer over dezelfde lijn te lopen. Wanneer ze daarin slaagden, wonnen ze een auto. </p>
<p>Ga zelf op zoek naar een filmpje van de <em>Mercedes Challenge</em>. Slaag jij er in om op de correcte manier over de lijnen van het logo te lopen?</p>
</div>
</div>


**Waarom is het nu nuttig om onze tekeningen voor te stellen als een graaf?**


Een graaf is een abstracte voorstelling die we voor heel wat problemen kunnen gebruiken. Daarom zijn er al heel veel slimme wiskundigen en computerwetenschappers die hebben nagedacht over de eigenschappen van die grafen. Hun kennis kunnen we gebruiken om ons tekenprobleem op te lossen.

Je zou het misschien niet verwachten maar ons tekenprobleem komt sterk overeen met het probleem van de zeven bruggen van Koningsbergen.
