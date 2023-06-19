---
hruid: pc_theremin1
version: 3
language: nl
title: "T"
description: "T"
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

# De Theremin, een digitaal systeem

Dankzij alle handige voorzieningen op de Dwenguino en het gebruiksgemak van de software, kan jij een theremin leren programmeren. En via de simulator van de Dwenguino gaat dat extra gemakkelijk! Je hebt enkel een computer en een browser nodig.

Een theremin is het eerste elektronisch muziekinstrument. Het is uitgevonden door de Russische wetenschapper Leon Theremin in 1919. Wat hem speciaal maakt, is dat de theremin wordt bespeeld zonder hem aan te raken. 
Om een eenvoudige theremin te bouwen, gebruik je een Dwenguino die verbonden is met een sonar-sensor; de zoemer is al aanwezig op de Dwenguino. De microcontroller van de Dwenguino zal de waarden die de sonar-sensor meet, verwerken en de zoemer laten zoemen op een bepaalde toonhoogte.  
Je theremin moet zo worden geprogrammeerd dat de afstand van je hand tot de sonar de toonhoogte bepaalt. Een theremin is dus een digitaal systeem dat interageert met zijn omgeving.