---
hruid: ct08_05
version: 3
language: nl
title: "Algoritmisch denken"
description: "Algoritmisch denken"
keywords: [""]
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

# Algoritmisch denken

*Leerlingen bedenken een systematische manier om het (deel)probleem op te lossen. Die systematische manier is een set van opeenvolgende, eenduidige stappen in de nodige volgorde.*

**Voorbeeld**<br>
Bij de automatisatie van een ophaalbrug ziet een mogelijk algoritme er als volgt uit:

* Als de sensor op de brug een inkomende boot waarneemt, dan:

    - moeten de verkeerslichten aan het wegdek voor doorgaand verkeer (auto’s, fietsers…) op rood;
    - moet ‘x’ minuten gewacht worden om verkeer op de brug de kans te geven eraf te geraken;
    - moeten de slagbomen dicht;
    - mag de motor van de brug starten om de brug op te halen;
    - moet de motor stoppen als de brug boven is;
    - moet het sein voor de boot op ‘doorvaren mag’ gezet worden.
    
* Als de boot door is en de sensor de uitgaande boot waarneemt, dan:
    -  ...
