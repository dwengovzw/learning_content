---
hruid: pc_theremin7
version: 3
language: nl
title: "Van afstand naar geluid"
description: "Van afstand naar geluid"
keywords: ["Microcontroller"]
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
teacher_exclusive: true
---

# Theremin

## Van afstand naar geluid

Bekijk onderstaande code en probeer te achterhalen wat deze doet.

![blockly](@learning-object/theremin_7a/nl/3)

Dit is een zeer basische theremin, die je uiteraard zal moeten finetunen. Je hebt het misschien al gehoord: als er geen object voor de sonar-sensor staat, klinkt er een lage bromtoon. Dit komt omdat de sonar-sensor een 0 teruggeeft als hij geen obstakel ziet. Wijzig het programma zodat het stil blijft wanneer er geen obstakel gedetecteerd wordt (tip: je zal hiervoor het als-blok moeten gebruiken).

![blockly](@learning-object/theremin_7b/nl/3)

Indien je iets meer controle over de theremin wilt bewaren, kan je het 100 ms wacht-blok laten staan bij de frequentie.