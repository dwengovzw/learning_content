---
hruid: pc_hddclock3
version: 1
language: nl
title: "Sonar-sensor"
description: "T"
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

## Snelheidssensor

<img src="embed/snelheidssensor_aangeduid.png" alt="Een afbeelding van de onderdelen van een snelheidssensor." title="Een afbeelding van de onderdelen van een snelheidssensor."></img>

Een snelheidssensor meet de snelheid van een motor, maar hoe gebeurt dit? De sensor bestaat hierbij uit twee belangrijke onderdelen; het eerste onderdeel stuurt een infrarood signaal uit, het tweede onderdeel vangt dit signaal dan weer op. Dit zorgt voor een connectie tussen de twee onderdelen. Wanneer een object tussen deze onderdelen komt, dan is deze connectie onderbroken en stuurt de sensor een signaal uit naar de Dwenguino. Door de tijd te meten tussen opeenvolgende signalen, kunnen we nagaan hoe snel het object tussen deze twee onderdelen beweegt. 


***

Hoe je de snelheidssensor gebruikt, leer je in het volgende leerobject.