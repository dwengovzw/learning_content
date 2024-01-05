---
hruid: anm_0202
version: 3
language: nl
title: "Probleem aanpakken"
description: "Brainstorm"
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

# Klassikale brainstorm  - Probleem: Kortste weg van Gent naar Mechelen via grote wegen 

Mogelijke ideeën tijdens de brainstorm (→ computationeel denken – decompositie):<br>
- Hoe vind je de kortste weg? 
	- Op een kaart kijken wat de ligging is van de steden. Dat kan helpen bij het bepalen van de kortste route.
	- Mogelijke routes een voor een afgaan → hiervoor is een visuele voorstelling nodig 
	- Van elke mogelijke route de afstand berekenen
	- De kortste weg komt overeen met de kleinste afstand
- Schets maken van de steden en wegen (→ patroonherkenning /abstractie netwerk → graaf)
	- Afstanden aanduiden op de schets (→ gewogen graaf )  
- Hoe kan een computer helpen? 
	- Dat bestaat al → routeplanner, bv. Google Maps
	- Hoe werkt zo’n routeplanner eigenlijk?    
	- Hoe programmeren dat een computer de afstanden van de mogelijke routes berekent? 
		- Computer heeft afstanden nodig tussen de verschillende gemeenten
		- Je kan maar in een gemeente geraken als je komt van een gemeente die ermee in verbinding staat
		- De wegen zijn in twee richtingen, dus er is ‘symmetrie met gelijke afstand’ (dat is duidelijk door de symmetrie in de gegeven tabel)
		- Opmerking: alle mogelijke routes afgaan is eigenlijk tijdverlies, sommige gemeenten komen door hun ligging niet in aanmerking.

--------------
### De leerkracht vat de brainstorm samen
Voorbeeld:

![image](https://user-images.githubusercontent.com/48352335/213933875-ae28abd8-eacd-4e3b-b5c0-a629119469a2.png)

Situatie bekijken in Google Maps:

![image](https://user-images.githubusercontent.com/48352335/213933904-236a21e1-9be4-4028-b475-b7ec9fec1b33.png)
<center>Bron: Google Maps</center>  
