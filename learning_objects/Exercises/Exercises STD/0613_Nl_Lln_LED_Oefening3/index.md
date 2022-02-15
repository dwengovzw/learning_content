---
hruid: STD_LedOef3-v1
version: 3
language: nl
title: "Oefening Led 3"
description: "Oefening Led 3"
keywords: ["StartToDwenguino", "led"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
### Oefening led
OPGAVE 3

Laat alle leds een halve seconde flikkeren in numerieke volgorde. Dit betekent dat led 0 eerst brandt en dan uitgaat wanneer led 1 gaat branden, led 1 uitgaat wanneer led 2 gaat branden ...