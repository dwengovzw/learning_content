---
hruid: g_led
version: 3
language: nl
title: "Uitleg Led"
description: "Uitleg led"
keywords: ["oefeningen", "led"]
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
# DwenguinoBlockly
## Led

Links onderaan op het Dwenguino-bord vind je acht leds:

![alt](embed/leds.png "Afb. led")

Deze leds zijn *led 0*, *led 1*, ..., *led 7*, van rechts naar links. De eerste led is dus *led 0*. In computerwetenschappen is het vaak de conventie om te beginnen tellen vanaf 0. Dit heb je misschien ook al gemerkt bij het lcd-scherm.

Links bovenaan is er nog een ledje: *led 13*.
Dit laatste led heeft enkele speciale functionaliteiten en heeft daarom ook een speciale naam.