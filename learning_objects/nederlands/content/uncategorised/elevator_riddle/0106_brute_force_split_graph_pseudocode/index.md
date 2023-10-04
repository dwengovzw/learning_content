---
hruid: org-dwengo-elevator-riddle-brute-force-3
version: 1
language: nl
title: "Stap 1: Pseudocode"
description: "Om en algoritme zonder te coderen te beschrijven kunnen we pseudocode gebruiken."
keywords: ["grafen", "algoritme", "computationeel denken", "clustering", "datastructuur", "brute force", "pseudocode"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
difficulty: 5
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---
# Brute kracht

## Pseudocode

In gewone mensentaal is het vaak moeilijk om formele redeneringen eenduidig te beschrijven. Daarom gebruiken informaticawetenschappers vaak pseudocode om de logica van een algoritme te beschrijven. Hieronder zie je de pseudocode voor het genereren van de keuzes. De code maakt gebruik van twee variabelen: k = het aantal keuzes die je mag maken, n = het aantal items waaruit je mag kiezen.

```pseudocode
genereer alle mogelijke keuzes van k items uit een lijst van n items:
	als k = 0 dan mag je uit de rest van de n items geen meer kiezen:
		Geef een lijst terug met n keer de waarde 2
	als k = n dan moet je alle resterende items kiezen:
		Geef een lijst terug met n keer de waarde 1
	als k > n dan is er iets fout, dit geval kan niet voorkomen:
		Geef een lege lijst terug
	als k < n dan moeten we een keuze maken:
		keuzes = een lege lijst
		voor alle subkeuzes sa in (genereer alle mogelijke keuzes van k - 1 items uit een lijst van n items):
			maak een lijst [1, sa] en voeg die toe aan de keuzes lijst
		voor alle subkeuzes sb in (genereer alle mogelijke keuzes van k - 1 items uit een lijst van n-1 items):
			maak een lijst [0, sb] en voeg die toe aan de keuzes lijst
		geef de keuzes lijst terug
```
