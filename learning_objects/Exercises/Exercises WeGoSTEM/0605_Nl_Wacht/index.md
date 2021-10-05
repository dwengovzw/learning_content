---
hruid: WachtWGS-v1
version: 3
language: nl
title: "Wacht"
description: "Wacht"
keywords: ["StartToDwenguino", "wacht"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [10, 11, 12, 13, 14]
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', 
    'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso'
]
teacher_exclusive: false
---
## Wacht

Het *'wacht'-blok* is een instructie die de computer laat weten hoelang iets moet uitgevoerd worden. 

![](embed/Afb1.png "Voorbeeld wacht")

De tijd wordt uitgedrukt in milliseconden. Eén milliseconde is een duizendste van een seconde. In één seconde kunnen dus duizend milliseconden.

**Voorbeeld**

Probeer onderstaand voorbeeld eens uit zodat je ziet hoe het werkt!

![blockly](@learning-object/WACHT1-v1/nl/3)