---
hruid: aiz_routeplanner
version: 3
language: nl
title: "Werking routeplanner"
description: "Werking routeplanner"
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# De werking van een routeplanner

**Voorkennis:** De leerlingen weten wat een graaf, knopen en bogen zijn. Hier komt een nieuw type van grafen op de proppen, nl. de gewogen graaf. 

### Opdracht voor de leerlingen
 
### Klassikale brainstorm  - Probleem: Kortste weg van Gent naar Mechelen via grote wegen 
Mogelijke ideeën (→ computationeel denken – decompositie ):
-	Hoe vind je de kortste weg? 
o	Op een kaart kijken wat de ligging is van de steden. Dat kan helpen bij het bepalen van de kortste route.
o	Mogelijke routes een voor een afgaan → hiervoor is een visuele voorstelling nodig 
o	Van elke mogelijke route de afstand berekenen
o	De kortste weg komt overeen met de kleinste afstand
-	Schets maken van de steden en wegen (→ patroonherkenning /abstractie netwerk → graaf)
o	Afstanden aanduiden op de schets (→ gewogen graaf )  
-	Hoe kan een computer helpen? 
o	Dat bestaat al → routeplanner, bv. Google Maps
o	Hoe werkt zo’n routeplanner eigenlijk?    
o	Hoe programmeren dat een computer de afstanden van de mogelijke routes berekent? 
	Computer heeft afstanden nodig tussen de verschillende gemeenten
	Je kan maar in een gemeente geraken als je komt van een gemeente die ermee in verbinding staat
	De wegen zijn in twee richtingen, dus er is ‘symmetrie met gelijke afstand’ (dat is duidelijk door de symmetrie in de gegeven tabel)
	Opmerking: alle mogelijke routes afgaan is eigenlijk tijdverlies, sommige gemeenten komen door hun ligging niet in aanmerking.

### Voor de leerkracht
 

Google Maps  
 



Hoe gaat dit in zijn werk?
Afstanden (in km) tussen gemeenten langs grote wegen:
	Gent	Lokeren	Sint-Niklaas	Willebroek	Dender-monde	Antwerpen	Mechelen	Eeklo
Gent		25						23
Lokeren	25		11		11			
Sint-Niklaas		11		18	12	22		49
Willebroek			18		17	16	14	
Dender-monde		11	12	17				
Antwerpen			22	16			23	62
Mechelen				14		23		
Eeklo	23		49			62		






### Gewogen graaf:  
  
	Leerlingen proberen zelf (manueel) de kortste weg te vinden.
	Welke strategie hebben de leerlingen toegepast?
	Al gauw wat werk
	Computer inzetten is zinvol!
Het zou handig zijn dat de computer alle mogelijkheden afgaat.

Controle Google Maps
 

 
 

### Nadien: algoritme 
	Hebben de leerlingen een algoritme bedacht?
	Algoritme van Dijkstra
	Eventueel implementeren in de computer met Python
o	Python notebook


### Algoritme van Dijkstra

Initialiseer de lijst ‘bezocht’   # lijst bevat knopen waarvan alle buren bezocht zijn
Initialiseer de lijst ‘onbezocht’ # lijst bevat knopen waarvan nog niet alle buren bezocht zijn    

# lijst ‘onbezocht’ opvullen (kost is afstand, tijd … naargelang het probleem)
# alle knopen hebben als vorige knoop geen
# alle knopen behalve startknoop hebben als kost oneindig, startknoop heeft als kost 0
Voor elke knoop in graaf:
Voeg knoop toe aan lijst ‘onbezocht’ met kost oneindig en vorige knoop geen
Stel kost van startknooppunt in de lijst ‘onbezocht’ in op 0

# knopen in lijst ‘onbezocht’ een voor een onderzoeken tot die lijst leeg is
# telkens beginnen met knoop met kleinste kost, noem die huidige knoop
# alle buren beschouwen die nog niet in lijst ‘bezocht’ staan
# voor elke buur kost berekenen en vergelijken met de kost die die al had
# als nieuwe kost kleiner uitvalt, gegevens van buur aanpassen in lijst ‘onbezocht’
# na onderzoek van al zijn buren die huidige knoop verplaatsen naar lijst ‘bezocht’
Zolang lijst ‘onbezocht’ niet leeg is: 
 	Stel huidige knoop in op knoop met laagste kost uit lijst ‘onbezocht’
 	Voeg huidige knoop met zijn gegevens (kost en vorige knoop) toe aan lijst ‘bezocht’
               Voor elk buurknoop van huidige knoop:
               		Indien buurknoop niet in lijst ‘bezocht’ staat:
               			Bereken nieuwe kost buurknoop = kost huidig knooppunt + kost boog
                			Als deze nieuwe kost lager is dan vorige kost buurknoop:
                    			Pas kost buurknoop aan naar nieuwe kost
                    			Pas vorige knoop van buurknoop aan naar huidige knoop
 	Verwijder huidige knoop van lijst ‘onbezocht’

Geef lijst ‘bezocht’ terug

Voor programma, zie notebook ‘Dijkstra’.
Toepassen van het algoritme:
  












### Oefenen met het algoritme
Oefening 1
https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all 
Vind de kortste weg van A naar E.
 
Oefening 2
https://www.bebras.org/sites/default/files/2015%20Bebras%20Solution%20Guide.pdf
Bebras 2015 – Reizen 
Bever Martina gaat elke dag naar het werk met de trein. Er is geen directe lijn, dus ze moet overstappen. De kaart toont de lijnen die ze kan nemen met vermelding van de reistijd. Martines huis staat aangegeven met de letter ‘H’, de plaats waar ze werkt met een ‘W’, en de stations met een ‘S’.
Welke weg komt overeen met de kortste reistijd?
 
Oefening 3 
https://www.curriculumonline.ie/getmedia/da0c349c-d205-47ff-9b43-6c820a62807c/uk-bebras-2016-answers.pdf
Copyright 2016 UK Bebras – Licence: CC-BY-NC-SA 3.0
Bebras 2016 – Fietspaden 
Cleveria is een fietser. Ze verkent de eenrichtingsfietspaden die door de dorpen n haar buurt lopen. Elk dorp heeft een dorpssteen met daarop een letter. Al de dietspaden hebben een fietsrichting en een afstand. De fietsrichting en de afstand zijn aangeduid d.m.v. de gele vlaggen.
 
Cleveria laat op haar verkenningstochten blauwe briefjes achter onder de dorpsstenen, met daarop een getal. Dat getal is de kortste afstand van de betreffende dorpssteen tot het dorp A. 
Welk getal komt onder dorpssteen E?










Oefening 4
https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all 
Vind de kortste weg van S naar G.
 












### Terug naar het routeprobleem
	Optimalisatie? Opmerking: alle mogelijke routes afgaan is eigenlijk tijdverlies, sommige gemeenten komen door hun ligging niet in aanmerking.

Afstanden in vogelvlucht (in km) tussen gemeenten en eindbestemming:
	Gent	Lokeren	Sint-Niklaas	Willebroek	Dender-monde	Antwerpen	Mechelen	Eeklo
Mechelen	54	33	25	11	25	20		66

Tot te passen techniek zie: https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all
Als schattingsfunctie (f-score) gebruik je de afstand in vogelvlucht (komt voor deze toepassing overeen met de Euclidische afstand).
  
  












### A* algoritme
Initialiseer de lijst ‘bezocht’   # lijst bevat knopen waarvan alle buren bezocht zijn
Initialiseer de lijst ‘onbezocht’ # lijst bevat knopen waarvan nog niet alle buren bezocht zijn    

# lijst ‘onbezocht’ opvullen met knopen, kost, f-score en vorige knoop 
# kost is afstand, tijd … naargelang het probleem
# f-score is kost vermeerderd met schatting
# alle knopen hebben als vorige knoop geen
# alle knopen behalve startknoop hebben als kost en als f-score oneindig
# startknoop heeft als kost 0, en als f-score zijn schatting
Voor elke knoop in graaf:
Voeg knoop toe aan lijst ‘onbezocht’ met kost en f-score oneindig, vorige knoop geen
Stel kost van startknooppunt in de lijst ‘onbezocht’ in op 0
Stel f-score van startknooppunt in de lijst ‘onbezocht’ in op zijn schatting (= 0 + schatting)

# knopen in lijst ‘onbezocht’ een voor een onderzoeken totdat huidige knoop eindknoop is
# telkens beginnen met knoop met kleinste f-score, noem die huidige knoop
# alle buren beschouwen die nog niet in lijst ‘bezocht’ staan
# voor elke buur kost en f-score berekenen en vergelijken met de kost die die al had
# als nieuwe kost kleiner uitvalt, gegevens van buur aanpassen in lijst ‘onbezocht’
# na onderzoek van al zijn buren die huidige knoop verplaatsen naar lijst ‘bezocht’
Zolang lijst ‘onbezocht’ niet leeg is:
 	Stel huidige knoop in op knoop met laagste f-score uit lijst ‘onbezocht’
 	Voeg huidige knoop met gegevens (kost, f-score en vorige knoop) toe aan lijst ‘bezocht’
	Als huidige knoop gelijk is aan de eindknoop:
		Stop de while-lus
	Anders:
               Voor elk buurknoop van huidige knoop:
               		Indien buurknoop niet in lijst ‘bezocht’ staat:
               			Bereken nieuwe kost buurknoop = kost huidig knooppunt + kost boog
                		Als deze nieuwe kost lager is dan vorige kost buurknoop:
                    			Pas kost buurknoop aan naar nieuwe kost
Pas f-score aan naar nieuwe kost + schatting
                    			Pas vorige knoop van buurknoop aan naar huidige knoop
 	Verwijder huidige knoop van lijst ‘onbezocht’

Geef lijst ‘bezocht’ terug


#### Leerdoelen
- Basisconcepten van grafen toepassen bij het analyseren van vingerafdrukken.
- Leerlingen ontwikkelen een algoritme om vingerafdrukken met elkaar te matchen (gegeven vingerafdruk identificeren a.d.h.v een vingerafdruk dataset).
- Ontdekkend en onderzoekend leren, kritisch en logisch denken.
- Het nut van wiskunde illustreren.

Na dit onderdeel kunnen de leerlingen …
- basisconcepten van grafen binnen deze context gebruiken
- vingerafdrukken karakteriseren
- vingerafdrukken abstraheren naar een graaf
 -vingerafdrukken analyseren a.d.h.v. grafen
- een algoritme ontwikkelen dat een vingerafdruk laat overeenkomen met een graaf 
- een algoritme ontwikkelen om een gegeven vingerafdruk te matchen met een vingerafdruk uit een dataset
- hun kritisch en logisch denken verbeterd hebben

#### Eindtermen
Grafen, computationeel denken, wisselwerking maatschappij en STEM, mediawijsheid, privacy. 
