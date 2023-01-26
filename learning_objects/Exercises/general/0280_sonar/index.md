---
hruid: g_sonar
version: 3
language: nl
title: "Uitleg Sonar"
description: "Uitleg Sonar"
keywords: ["oefeningen", "sonar"]
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
teacher_exclusive: false
---
# DwenguinoBlockly
## Sonar-sensor

### Type
- Invoer
- Digitale sensor

### Werking
De sensor stuurt een ultrasoon geluidssignaal uit. Indien er een voorwerp binnen bereik is, zal deze ultrasone geluidsgolf op dit voorwerp weerkaatsen. Je kan de werking vergelijken met de echolocatie van vleermuizen. Door de tijd te meten tussen het verzenden van het geluidssignaal en het ontvangen van de weerkaatste straal, kan de sensor de afstand tot het object nauwkeurig bepalen. De afstand wordt teruggegeven in cm.

### Werking in de simulator
In de simulator is een schuifbalk voorzien om de afstand tussen de sensor en een object te simuleren. Het getal op de schuifbalk simuleert de afstand tot het object in cm.

***

### In het echt

![](embed/sonar.png "Sonar-sensor")

### In de simulator

![](embed/Sonarsim.png "Sonar-sensor simulator")

Verwijzing sonar blok ![]()

<div class=alert alert-box alert-success>
Voor meer informatie over de sonar-sensor kan je terecht in de leerlingenfiches van de <em>Sociale Robot</em>
</div>