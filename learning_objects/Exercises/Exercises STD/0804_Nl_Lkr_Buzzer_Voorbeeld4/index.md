---
hruid: STD_BuzzerVB4-v1
version: 3
language: nl
title: "Voorbeeld Buzzer 4"
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
### Voorbeeld buzzer
OPGAVE 4

Schrijf een programma zodat je de dwenguino kunt gebruiken als een pentatonisch (5 tonen) instrument. Dit kan je doen door aan elk van de 5 knoppen (NOORD - OOST - ZUID - WEST - MIDDEN) een noot te binden. Een standaard pentatoniek is *Do (C), Re (D), Mi (E), Fa (F), Sol (G)*.

Oplossing:

![blockly](@learning-object/STD_Buzzer4-v1/nl/3)  

Zoals je misschien merkt, is het niet zo eenvoudig om zoemertonen te binden aan de knoppen. De meest efficiënte manier om dit te doen wordt hierna uitgelegd.

*Test dit ook eens uit op een echte Dwenguino als dit werkt in de simulator.*