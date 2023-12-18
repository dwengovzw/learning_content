---
hruid: leerlijn_invoer_basisprincipes_meten_is_weten_stroom
version: 1
language: nl
title: "Meten is weten: stroom!"
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

# Meten is weten (stroom)

Om de stroom te kunnen meten moet er ook effectief stroom door onze multimeter lopen. We moeten onze multimeter dus in **serie** aansluiten op onze schakeling. We moeten onze schakeling dus onderbreken en de meetsnoeren van de multimeter verbinden met elk van de kanten van de onderbreking. Om de stroom te kunnen meten moet de schakeling **verbonden zijn met een spanningsbron!**

## Instellen van de multimeter

### Verbinden van de meetsnoeren

Om spanning te meten pluggen we de meetsnoeren in in de volgende poorten op de multimeter.

<span style="color: white; background-color: black; padding: 3px; border-radius: 5px; overflow:hidden">Zwarte meetsnoer</span>: <span style="color: white; background-color: black; padding: 3px; border-radius: 5px; overflow:hidden">COM</span>

Waar je de rode meetsnoer inplugt hangt af van de verwachte stroom die je gaat meten. Is die niet groter dan 400 mA:

<span style="color: white; background-color: red; padding: 3px; border-radius: 5px; overflow:hidden">Rode meetsnoer</span>: <span style="color: white; background-color: red; padding: 3px; border-radius: 5px; overflow:hidden"> 400 mA </span><br>

Is die niet groter dan 10A

<span style="color: white; background-color: red; padding: 3px; border-radius: 5px; overflow:hidden">Rode meetsnoer</span>: <span style="color: white; background-color: red; padding: 3px; border-radius: 5px; overflow:hidden"> 10 A </span><br>


### Modus van de multimeter
We willen graag gelijkstroom meten. Het icoontje voor gelijkstroom of spanning is ⎓, het icoontje voor stroom is A. Kies de instelling die deze icoontjes combineert. Merk op dat de instelling ook afhangt van de geschatte stroom (400 mA of 10A). 

TODO: voeg foto toe.


<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        <p>
            Hieronder zie je een circuit, bouw dit circuit na en meet de stroom door de weerstand R1 (=440 Ω) door de meetsnoeren van de multimeter te verbinden met de punten a en b.
        </p>
        <p>
            <img src="img/diagram_eu.svg"></img>
        </p>
        <ul>
            <li>Wat gebeurt er met de stroom als je de meetsnoeren omwisselt?</li>
            <li>Wat gebeurt er met de stroom als je een weerstand met een andere waarde neemt (bv. 550 Ω)?</li>
        </ul>
    </div>
</div>
