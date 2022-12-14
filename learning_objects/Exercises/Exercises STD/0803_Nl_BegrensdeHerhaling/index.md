---
hruid: STD_BH
version: 3
language: nl
title: "Begrensde Herhaling"
description: "Beperkte Herhaling"
keywords: ["StartToDwenguino", "Lussen"]
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
### Begrensde herhaling

Om een begrensde herhaling uit te voeren, gebruik je het volgende blok:  

![](embed/Beperkteherhaling.png "Beperkte herhaling")  

Je stelt hiermee het aantal herhalingen in, aan de hand van een *teller* die een start- en stopwaarde opgelegd krijgt. Deze teller werd in het voorbeeld 'i' genoemd, begint bij 0 en er wordt per herhaling 1 bij opgeteld. De herhaling stopt zodra de stopwaarde bereikt wordt. 

*Wat is de stopwaarde in het voorbeeld? Hoeveel keer wordt deze lus dus herhaald?*

Voor opgave 3 van de buzzer kan je dus elk deel dat herhaald moet worden, inkorten door een begrensde herhaling te gebruiken. Omdat elk deel 2 keer moet afgespeeld worden (1 herhaling), stel je de stopwaarde in op 1.

Oplossing:

![blockly](@learning-object/STD_Buzzer32/nl/3)  

*Test dit ook eens uit op een echte Dwenguino als dit werkt in de simulator.*