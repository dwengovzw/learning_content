---
hruid: STD_BH-v1
version: 3
language: nl
title: "Beperkte Herhaling"
description: "Beperkte Herhaling"
keywords: ["StartToDwenguino", "Lussen"]
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
### Beperkte herhaling

Om een beperkte herhaling uit te voeren, gebruik je de volgende blok:  

![](embed/Beperkteherhaling.png "Beperkte herhaling")  

Je stelt hiermee een voorwaarde in voor het aantal herhalingen, namelijk de waarde van de *teller i*. Deze begint bij 0 en er wordt per herhaling 1 bij opgeteld. De herhaling stopt zodra de stopvoorwaarde bereikt wordt.  

Voor opgave 3 van de buzzer kan je dus elk deel dat herhaald moet worden, inkorten door een beperkte herhaling te gebruiken. Omdat elk deel slechts 1 keer moet herhaald worden, stel je de stopvoorwaarde in op 1.

Oplossing:

![blockly](@learning-object/STD_Buzzer32-v1/nl/3)  

*Test dit ook eens uit op een echte Dwenguino als dit werkt in de simulator.*