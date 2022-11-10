---
hruid: STD_BuzzerVB3-v1
version: 3
language: nl
title: "Voorbeeld Buzzer 3"
description: "Voorbeeld Buzzer"
keywords: ["StartToDwenguino", "led"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
### Voorbeeld buzzer
OPGAVE 3 

Schrijf een programma zodat de zoemer *broeder Jacob* afspeelt. Hiervoor zal je eerst de partituur van het liedje en de frequenties van de tonen moeten opzoeken. 


Oplossing:

![blockly](@learning-object/STD_Buzzer31-v1/nl/3)  

Zoals je kunt zien, wordt dit een vrij lang programma. Er zijn gelukkig een aantal plaatsen die je wat kunt inkorten met behulp van een **begrensde herhaling**. Dit wordt verder uitgelegd in het volgende onderdeel.

*Test dit ook eens uit op een echte Dwenguino als dit werkt in de simulator.*