---
hruid: anm_0204
version: 3
language: nl
title: "Algoritme van Dijkstra"
description: "Algoritme van Dijkstra"
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
teacher_exclusive: false
---

# Algoritme van Dijkstra

## Pseudocode

<div class="alert alert-box alert-secondary"><p style=" font-family: 'Courier New', monospace; font-size:12px; ">
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
Zolang lijst ‘onbezocht’ niet leeg is:<br>
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
</p>
</div>


## Toepassen van het algoritme
Aan de hand van een tabel en een boomstructuur ga je op zoek naar de kortste route.

![image](https://user-images.githubusercontent.com/48352335/213934175-be5b3e22-4fc8-49ca-83ad-c73cc8f94298.png)
![M024_Boom_1](https://user-images.githubusercontent.com/48352335/216783699-8bd9beb6-c2d6-4155-909a-a88bdac9524b.png)


## Oefenen met het algoritme
**Oefening 1**
Bron: https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all 

*Vind de kortste weg van A naar E.*

![image](https://user-images.githubusercontent.com/48352335/213934203-9e5f3b11-c9fa-4745-9935-c115d214e584.png)
 
**Oefening 2**
Bron: https://www.bebras.org/sites/default/files/2015%20Bebras%20Solution%20Guide.pdf

Bebras 2015 – Reizen 

Bever Martina gaat elke dag naar het werk met de trein. Er is geen directe lijn, dus ze moet overstappen. De kaart toont de lijnen die ze kan nemen met vermelding van de reistijd. Martines huis staat aangegeven met de letter ‘H’, de plaats waar ze werkt met een ‘W’, en de stations met een ‘S’.

*Welke weg komt overeen met de kortste reistijd?*

![image](https://user-images.githubusercontent.com/48352335/213934241-97b3a82e-8fe4-4407-a09f-0caa52c83b4a.png)
 
**Oefening 3** 
Bron: https://www.curriculumonline.ie/getmedia/da0c349c-d205-47ff-9b43-6c820a62807c/uk-bebras-2016-answers.pdf <br>
Copyright 2016 UK Bebras – Licence: CC-BY-NC-SA 3.0

Bebras 2016 – Fietspaden 

Cleveria is een fietser. Ze verkent de eenrichtingsfietspaden die door de dorpen n haar buurt lopen. Elk dorp heeft een dorpssteen met daarop een letter. Al de dietspaden hebben een fietsrichting en een afstand. De fietsrichting en de afstand zijn aangeduid d.m.v. de gele vlaggen.
 
![image](https://user-images.githubusercontent.com/48352335/213934298-cd8a75f8-ef27-4d77-a20c-140770bf3856.png)

Cleveria laat op haar verkenningstochten blauwe briefjes achter onder de dorpsstenen, met daarop een getal. Dat getal is de kortste afstand van de betreffende dorpssteen tot het dorp A. 

*Welk getal komt onder dorpssteen E?*

**Oefening 4**
Bron: https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all 

*Vind de kortste weg van S naar G.*
 
![image](https://user-images.githubusercontent.com/48352335/213934333-5e062113-f283-490c-bd56-6d4fee4bdee2.png)

------------------------

## Terug naar het routeprobleem - kritisch denken
- Optimalisatie? Opmerking: alle mogelijke routes afgaan is eigenlijk tijdverlies, sommige gemeenten komen door hun ligging niet in aanmerking.

![image](https://user-images.githubusercontent.com/48352335/213933743-2a57ac0f-b76b-4440-96e4-173f275a649b.png)

## Toe te passen techniek 
Zie: https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all

Je maakt gebruik van een schattingsfunctie om een idee te hebben van welke gemeenten meer opportuun zijn om langs te rijden in vergelijking met andere, rekning houdend met de gemeente waar de reis naartoe gaat.<br>
Als schattingsfunctie (f-score) gebruik je de afstand in vogelvlucht (komt voor deze toepassing overeen met de Euclidische afstand).

Je vult de gewogen graaf aan met de afstand in vogelvlucht.
  
![M024_Graaf_2](https://user-images.githubusercontent.com/48352335/216783645-5910a805-f876-4643-82f1-d98c15c2a48b.png)

Aan de hand van een tabel en een boomstructuur ga je op zoek naar de kortste route.
![image](https://user-images.githubusercontent.com/48352335/213934386-9fe136a5-ff13-46b2-9ec0-42a8161da0de.png)
![M024_Boom_2](https://user-images.githubusercontent.com/48352335/216783661-d320583e-1ad3-4d09-b8a4-7180c9335c93.png)

## A* algoritme
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace; font-size:12px;">
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
</p>
</div>

------------

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
