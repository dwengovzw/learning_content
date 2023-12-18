---
hruid: pc_theremin1
version: 3
language: nl
title: "Een digitaal systeem"
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

# Theremin

## Een digitaal systeem

Dankzij alle handige voorzieningen op de Dwenguino en het gebruiksgemak van de software, kan jij een theremin leren programmeren. En via de simulator van de Dwenguino gaat dat extra gemakkelijk! Je hebt enkel een computer en een browser nodig.

Een theremin is het eerste elektronisch muziekinstrument. Het is uitgevonden door de Russische wetenschapper Leon Theremin in 1919. Wat hem speciaal maakt, is dat de theremin wordt bespeeld zonder hem aan te raken. 

![](embed/theremin.jpg "theremin")<br>
<sub>Gregor Hohenberg. (2009). *Barbara Buchholz die het model TVox van George Pavlov bespeelt*. CC BY-SA 3.0, via Wikimedia Commons.</sub>

Een theremin beschikt over 2 antennes (zie afbeelding) die verbonden zijn met een kistje. Eén antenne regelt de toonhoogte, de andere het volume. De muzikant kan dan de toonhoogte en/of het volume aanpassen door de handen dichter of verder van de respectievelijke antennes te bewegen.

***

Om een eenvoudige theremin te bouwen, gebruik je een Dwenguino die verbonden is met een sonar-sensor; de zoemer is al aanwezig op de Dwenguino. De microcontroller van de Dwenguino zal de waarden die de sonar-sensor meet, verwerken en de zoemer laten zoemen op een bepaalde toonhoogte.  

Een theremin moet zo worden geprogrammeerd dat de afstand van je hand tot de sonar de toonhoogte bepaalt. Dit is dus een digitaal systeem dat interageert met zijn omgeving.
