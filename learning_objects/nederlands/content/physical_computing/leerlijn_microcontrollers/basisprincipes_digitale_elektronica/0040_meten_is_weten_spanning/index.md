---
hruid: leerlijn_invoer_basisprincipes_meten_is_weten_spanning
version: 1
language: nl
title: "Meten is weten!"
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Meten is weten (spanning)

Wanneer we spanning meten, meten we altijd het verschil in spanning tussen twee punten. Vaak is één van deze twee punten de referentiespanning of GND maar dat is niet noodzakelijk. De spanningswaarde die we meten is dus steeds het verschil tussen de spanning op elk van de probes van de multimeter. Verbinden we de zwarte probe van de multimeter met een draad waar 5V op staat en de rode probe met een draad waar 2V op staat, dan zal de multimeter de waarde -3V (2V - 5V) tonen. 

## Instellen van de multimeter

### Verbinden van de probes

Om spanning te meten pluggen we de probes in in de volgende poorten op de multimeter.

<span style="color: white, background-color: red">Rode probe: V \\(\Omega\\) </span><br>
<span style="color: white, background-color: black">Zwarte probe: COM </span>

### Modus van de multimeter
We willen graag gelijkspanning meten. Het icoontje voor gelijkstroom of spanning is ⎓, het icoontje voor voltage is V. 

TODO: voeg foto toe.


<div class="dwengo-content assignment">
    <h2>Opdracht</h2>
    <p>
        Hieronder zie je een circuit, bouw dit circuit na en meet de spanning over de weerstand R1 = \\(440\Omega\\) door de probes van de multimeter te verbinden met de punten a en b.
    </p>
    <p>
        <img src="img/diagram.svg"></img>
    </p>
    <p>
        Wat gebeurd er als je de probes omwisselt?
        Wat gebeurd er als je een weerstand met een andere waarde neemt?
    </p>
</div>