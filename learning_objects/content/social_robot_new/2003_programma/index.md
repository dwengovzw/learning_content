---
hruid: sr2_programma
version: 3
language: nl
title: "Programmeer je eigen robot"
description: "Programmeer je eigen robot"
keywords: ["Sociale Robot", "AI Op School", "STEM", "Computationeel denken", "Grafisch programmeren"]
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
estimated_time: 30
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-technologie-en-technieken'
]
teacher_exclusive: false
---

# Programmeer je eigen robot

Proficiat! Nu je het programmeren wat onder de knie hebt, kan je beginnen met je eigen robot te programmeren.

Overloop nogmaals wat jouw robot moet kunnen en schrijf dit nu op in 'pseudocode'.

**Voorbeeld**  
*Wat moet hij kunnen*  
Als de robot niets ziet, houdt hij zijn armen omhoog en knippert hij met de ogen. 
Als iemand dichter dan 20 cm nadert, begint de robot te zwaaien.  

*pseudocode*  
**ALS** iemand op 20 cm **DAN** zwaaien en ogen knipperen  
**ANDERS** armen omhoog en ogen normaal  

Eens je de pseudocode hebt, schrijf en test je de verschillende deelprogramma's die je nodig hebt om dit te verwezenlijken. Deze deelprogramma's moeten:

- de armen laten stilstaan;
- de ogen laten verschijnen;
- de armen laten zwaaien;
- de ogen laten knipperen;
- de sonar-sensor uitlezen, met een "*Als - Dan - Anders*"-blok om er voorwaarden aan te koppelen.  

Wanneer je dan alle deelprogramma's bij elkaar plaatst, heb je het volledige programma voor de robot!