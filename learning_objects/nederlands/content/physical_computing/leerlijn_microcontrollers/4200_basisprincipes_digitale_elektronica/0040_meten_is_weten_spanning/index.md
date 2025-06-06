---
hruid: leerlijn_invoer_basisprincipes_meten_is_weten_spanning
version: 1
language: nl
title: "Meten is weten: spanning!"
description: "Hoe meet ik spanning, stroom en weerstand?"
keywords: ["spanning", "stroom", "weerstand", "multimeter", "meten", "basisprincipes", "microcontroller", "µC", "arduino", "dwenguino"]
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
estimated_time: 15
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Meten is weten (spanning)

Wanneer we spanning meten, meten we altijd het verschil in spanning tussen twee punten. Vaak is één van deze twee punten de referentiespanning of GND maar dat is niet noodzakelijk. De spanningswaarde die we meten is dus steeds het verschil tussen de spanning op elk van de meetsnoeren van de multimeter. Verbinden we het zwarte meetsnoer van de multimeter met een draad waar 5 V op staat en het rode meetsnoer met een draad waar 2 V op staat, dan zal de multimeter de waarde -3 V (= 2 V - 5 V) tonen. Om de spanning te kunnen meten moet de schakeling **verbonden zijn met een spanningsbron!**

## Instellen van de multimeter

### Verbinden van de meetsnoeren

Om spanning te meten pluggen we de meetsnoeren in in de volgende poorten op de multimeter.

<span style="color: white; background-color: red; padding: 3px; border-radius: 5px; overflow:hidden">Rood meetsnoer</span>: <span style="color: white; background-color: red; padding: 3px; border-radius: 5px; overflow:hidden"> V </span><br><br>
<span style="color: white; background-color: black; padding: 3px; border-radius: 5px; overflow:hidden">Zwart meetsnoer</span>: <span style="color: white; background-color: black; padding: 3px; border-radius: 5px; overflow:hidden">COM</span>

### Modus van de multimeter
We willen graag gelijkspanning meten. Het icoontje voor gelijkstroom of -spanning is ⎓, het icoontje voor voltage is V. Kies de instelling die deze icoontjes combineert. Hieronder zie je een voorbeeld van de instelling op onze multimeter. Het is mogelijk dat je niet exact dezelfde multimeter hebt. Kijk goed naar de icoontjes op het toestel om te weten hoe je die correct kan instellen.

<img src="img/mm_voltage.png"></img>
Dit apparaat kan je gebruiken om spanning, weerstand en stroomsterkte te meten. 

<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        <p>
            Hieronder zie je een circuit, bouw dit circuit na en meet de spanning over de weerstand R1 (=440 Ω) door de meetsnoeren van de multimeter te verbinden met de punten a en b.
        </p>
        <img src="img/diagram_eu.svg"></img>
        <ul>
            <li>Wat gebeurt er met de spanning als je de meetsnoeren omwisselt?</li>
            <li>Wat gebeurt er met de spanning als je een weerstand met een andere waarde neemt?</li>
        </ul>
    </div>
</div>
