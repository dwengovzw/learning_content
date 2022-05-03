---
hruid: STD_VH-v1
version: 3
language: nl
title: "Voorwaardelijke herhaling"
description: "Voorbeeld Buzzer"
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
teacher_exclusive: true
---
### Voorwaardelijke herhaling
Om een voorwaardelijke herhaling uit te voeren, gebruik je het volgende blok:  

![](embed/vh.png "Voorwaardelijke herhaling")  

In tegenstelling tot de begrensde herhaling, stellen we hier, i.p.v. een start- en stopwaarde, een startconditie in. Als aan de startconditie voldaan is, zal de lus opstarten. Eens opgestart, zal de inhoud van de lus herhaald worden tot er niet langer aan de startconditie wordt voldaan.

Voor opgave 4 van de buzzer, zullen we als startconditie instellen dat een knop moet ingedrukt zijn. Zolang dit het geval is, zal de buzzer de gewenste toon produceren. Zodra je de knop loslaat moet deze toon stoppen.

Oplossing:

![blockly](@learning-object/STD_Buzzer4-v1/nl/3)  

*Test dit ook eens uit op een echte Dwenguino als dit werkt in de simulator.*