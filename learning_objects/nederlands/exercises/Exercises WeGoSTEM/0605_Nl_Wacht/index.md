---
hruid: wgs_Wacht
version: 3
language: nl
title: "Uitleg Wacht"
description: "Uitleg Wacht"
keywords: ["StartTodwenguino", "wacht"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [10, 11, 12]
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
## Wacht

Het *'wacht'-blok* is een instructie die de computer laat weten hoelang iets moet uitgevoerd worden. 

![](embed/Afb1.png "Voorbeeld wacht")

De tijd wordt uitgedrukt in milliseconden. Eén milliseconde is een duizendste van een seconde. In één seconde kunnen dus duizend milliseconden.

**Voorbeeld**

Probeer onderstaand voorbeeld eens uit zodat je ziet hoe het werkt!

![blockly](@learning-object/WACHT1/nl/3)