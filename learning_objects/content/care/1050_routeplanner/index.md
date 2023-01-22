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
Je kent de afstanden in kilometer tussen bepaalde gemeenten, zowel langs grote wegen als in vogelvlucht. De gemeenten zijn Gent, Lokeren, Sint-Niklaas, Dendermonde, Antwerpen, Eeklo, Willebroek en Mechelen.<br>
Bepaal de kortste weg tussen Gent en Mechelne via deze wegen. Hoe kan een computer daarbij helpen?

![image](https://user-images.githubusercontent.com/48352335/213933739-10534f75-588b-4817-8463-025524b85009.png)
![image](https://user-images.githubusercontent.com/48352335/213933743-2a57ac0f-b76b-4440-96e4-173f275a649b.png)


### Klassikale brainstorm  - Probleem: Kortste weg van Gent naar Mechelen via grote wegen 
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

### Voor de leerkracht
Samenvatting van de brainstorm in een schema:

![image](https://user-images.githubusercontent.com/48352335/213933875-ae28abd8-eacd-4e3b-b5c0-a629119469a2.png)

Situatie bekijken in Google Maps:
![image](https://user-images.githubusercontent.com/48352335/213933904-236a21e1-9be4-4028-b475-b7ec9fec1b33.png)
<center>Bron: Google Maps</center>  
 
### Hoe gaat dit in zijn werk?
![image](https://user-images.githubusercontent.com/48352335/213933739-10534f75-588b-4817-8463-025524b85009.png)	

#### Gewogen graaf:  
  ![image](https://user-images.githubusercontent.com/48352335/213934005-2721797d-40e0-41e5-839e-2674c4256c64.png)
<center>(Afbeelding moet nog aangevuld worden met enkele afstanden en boog van A naar W)</center>

- Leerlingen proberen zelf (manueel) de kortste weg te vinden.
- Welke strategie hebben de leerlingen toegepast?
- Al gauw wat werk
- Computer inzetten is zinvol!
	- Het zou handig zijn dat de computer alle mogelijkheden afgaat.

#### Controle Google Maps
![image](https://user-images.githubusercontent.com/48352335/213934118-1120ed5a-8dfd-4c2b-8b5d-2e67a6475172.png)

![image](https://user-images.githubusercontent.com/48352335/213934134-7d235d6a-c110-4fe2-a540-ef187417e885.png)

### Nadien: algoritme 
- Hebben de leerlingen een algoritme bedacht?
- Algoritme van Dijkstra
- Eventueel implementeren in de computer met Python
- Python notebook


### Algoritme van Dijkstra

<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
Initialiseer de lijst ‘bezocht’   # lijst bevat knopen waarvan alle buren bezocht zijn<br>
Initialiseer de lijst ‘onbezocht’ # lijst bevat knopen waarvan nog niet alle buren bezocht zijn<br><br>
# lijst ‘onbezocht’ opvullen (kost is afstand, tijd … naargelang het probleem)<br>
# alle knopen hebben als vorige knoop geen<br>
# alle knopen behalve startknoop hebben als kost oneindig, startknoop heeft als kost 0<br>
Voor elke knoop in graaf:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Voeg knoop toe aan lijst ‘onbezocht’ met kost oneindig en vorige knoop geen<br>
Stel kost van startknooppunt in de lijst ‘onbezocht’ in op 0<br><br>
# knopen in lijst ‘onbezocht’ een voor een onderzoeken tot die lijst leeg is<br>
# telkens beginnen met knoop met kleinste kost, noem die huidige knoop<br>
# alle buren beschouwen die nog niet in lijst ‘bezocht’ staan<br>
# voor elke buur kost berekenen en vergelijken met de kost die die al had<br>
# als nieuwe kost kleiner uitvalt, gegevens van buur aanpassen in lijst ‘onbezocht’<br>
# na onderzoek van al zijn buren die huidige knoop verplaatsen naar lijst ‘bezocht’<br>
Zolang lijst ‘onbezocht’ niet leeg is: <br>
&nbsp;&nbsp;&nbsp;&nbsp;Stel huidige knoop in op knoop met laagste kost uit lijst ‘onbezocht’<br>
&nbsp;&nbsp;&nbsp;&nbsp;Voeg huidige knoop met zijn gegevens (kost en vorige knoop) toe aan lijst ‘bezocht’<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Voor elk buurknoop van huidige knoop:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Indien buurknoop niet in lijst ‘bezocht’ staat:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bereken nieuwe kost buurknoop = kost huidig knooppunt + kost boog<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Als deze nieuwe kost lager is dan vorige kost buurknoop:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pas kost buurknoop aan naar nieuwe kost<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pas vorige knoop van buurknoop aan naar huidige knoop<br>
&nbsp;&nbsp;&nbsp;&nbsp;Verwijder huidige knoop van lijst ‘onbezocht’<br><br>
Geef lijst ‘bezocht’ terug
</div>

#### Voor programma, zie notebook ‘Dijkstra’.

#### Toepassen van het algoritme:
![image](https://user-images.githubusercontent.com/48352335/213934175-be5b3e22-4fc8-49ca-83ad-c73cc8f94298.png)


### Oefenen met het algoritme
#### Oefening 1
Bron: https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all 

*Vind de kortste weg van A naar E.*

![image](https://user-images.githubusercontent.com/48352335/213934203-9e5f3b11-c9fa-4745-9935-c115d214e584.png)
 
#### Oefening 2
Bron: https://www.bebras.org/sites/default/files/2015%20Bebras%20Solution%20Guide.pdf

Bebras 2015 – Reizen 

Bever Martina gaat elke dag naar het werk met de trein. Er is geen directe lijn, dus ze moet overstappen. De kaart toont de lijnen die ze kan nemen met vermelding van de reistijd. Martines huis staat aangegeven met de letter ‘H’, de plaats waar ze werkt met een ‘W’, en de stations met een ‘S’.

*Welke weg komt overeen met de kortste reistijd?*

![image](https://user-images.githubusercontent.com/48352335/213934241-97b3a82e-8fe4-4407-a09f-0caa52c83b4a.png)
 
#### Oefening 3 
Bron: https://www.curriculumonline.ie/getmedia/da0c349c-d205-47ff-9b43-6c820a62807c/uk-bebras-2016-answers.pdf <br>
Copyright 2016 UK Bebras – Licence: CC-BY-NC-SA 3.0

Bebras 2016 – Fietspaden 

Cleveria is een fietser. Ze verkent de eenrichtingsfietspaden die door de dorpen n haar buurt lopen. Elk dorp heeft een dorpssteen met daarop een letter. Al de dietspaden hebben een fietsrichting en een afstand. De fietsrichting en de afstand zijn aangeduid d.m.v. de gele vlaggen.
 
![image](https://user-images.githubusercontent.com/48352335/213934298-cd8a75f8-ef27-4d77-a20c-140770bf3856.png)

Cleveria laat op haar verkenningstochten blauwe briefjes achter onder de dorpsstenen, met daarop een getal. Dat getal is de kortste afstand van de betreffende dorpssteen tot het dorp A. 

*Welk getal komt onder dorpssteen E?*

#### Oefening 4
Bron: https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all 

*Vind de kortste weg van S naar G.*
 
![image](https://user-images.githubusercontent.com/48352335/213934333-5e062113-f283-490c-bd56-6d4fee4bdee2.png)


### Terug naar het routeprobleem - kritisch denken
- Optimalisatie? Opmerking: alle mogelijke routes afgaan is eigenlijk tijdverlies, sommige gemeenten komen door hun ligging niet in aanmerking.

![image](https://user-images.githubusercontent.com/48352335/213933743-2a57ac0f-b76b-4440-96e4-173f275a649b.png)

Tot te passen techniek zie: https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all

Als schattingsfunctie (f-score) gebruik je de afstand in vogelvlucht (komt voor deze toepassing overeen met de Euclidische afstand).
  
  ![image](https://user-images.githubusercontent.com/48352335/213934379-44c0f84f-dce4-487f-8583-70744387c894.png)

![image](https://user-images.githubusercontent.com/48352335/213934386-9fe136a5-ff13-46b2-9ec0-42a8161da0de.png)



### A* algoritme
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace;">
Initialiseer de lijst ‘bezocht’   # lijst bevat knopen waarvan alle buren bezocht zijn<br>
Initialiseer de lijst ‘onbezocht’ # lijst bevat knopen waarvan nog niet alle buren bezocht zijn<br><br>    
# lijst ‘onbezocht’ opvullen met knopen, kost, f-score en vorige knoop <br>
# kost is afstand, tijd … naargelang het probleem<br>
# f-score is kost vermeerderd met schatting<br>
# alle knopen hebben als vorige knoop geen<br>
# alle knopen behalve startknoop hebben als kost en als f-score oneindig<br>
# startknoop heeft als kost 0, en als f-score zijn schatting<br>
Voor elke knoop in graaf:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Voeg knoop toe aan lijst ‘onbezocht’ met kost en f-score oneindig, vorige knoop geen<br>
Stel kost van startknooppunt in de lijst ‘onbezocht’ in op 0<br>
Stel f-score van startknooppunt in de lijst ‘onbezocht’ in op zijn schatting (= 0 + schatting)<br><br>
# knopen in lijst ‘onbezocht’ een voor een onderzoeken totdat huidige knoop eindknoop is<br>
# telkens beginnen met knoop met kleinste f-score, noem die huidige knoop<br>
# alle buren beschouwen die nog niet in lijst ‘bezocht’ staan<br>
# voor elke buur kost en f-score berekenen en vergelijken met de kost die die al had<br>
# als nieuwe kost kleiner uitvalt, gegevens van buur aanpassen in lijst ‘onbezocht’<br>
# na onderzoek van al zijn buren die huidige knoop verplaatsen naar lijst ‘bezocht’<br>
Zolang lijst ‘onbezocht’ niet leeg is:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Stel huidige knoop in op knoop met laagste f-score uit lijst ‘onbezocht’<br>
&nbsp;&nbsp;&nbsp;&nbsp;Voeg huidige knoop met gegevens (kost, f-score en vorige knoop) toe aan lijst ‘bezocht’<br>
&nbsp;&nbsp;&nbsp;&nbsp;Als huidige knoop gelijk is aan de eindknoop:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stop de while-lus<br>
&nbsp;&nbsp;&nbsp;&nbsp;Anders:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Voor elk buurknoop van huidige knoop:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Indien buurknoop niet in lijst ‘bezocht’ staat:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bereken nieuwe kost buurknoop = kost huidig knooppunt + kost boog<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Als deze nieuwe kost lager is dan vorige kost buurknoop:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pas kost buurknoop aan naar nieuwe kost<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pas f-score aan naar nieuwe kost + schatting<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pas vorige knoop van buurknoop aan naar huidige knoop<br>
&nbsp;&nbsp;&nbsp;&nbsp;Verwijder huidige knoop van lijst ‘onbezocht’<br><br>
Geef lijst ‘bezocht’ terug
</div>

#### Leerdoelen
- Basisconcepten van grafen toepassen om een route voor te stellen.
- Leerlingen ontwikkelen een algoritme om de kortste weg tussen twee steden te vinden.
- Leerlingen maken kennis met het algoritme van Dijkstra dat daarvoor geschikt is.
- Het nut van wiskunde illustreren.

Na dit onderdeel kunnen de leerlingen …
- basisconcepten van grafen binnen deze context gebruiken
- de kortste route vinden
- het algoritme van Dijkstra toepassen
- eventueel het algoritme van Dijkstra programmeren 
- hun kritisch en logisch denken verbeterd hebben

#### Eindtermen
Grafen, computationeel denken, wisselwerking maatschappij en STEM, mediawijsheid, privacy. 
