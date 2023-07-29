---
hruid: stem5_2
version: 3
language: nl
title: "Exponentiële groei"
description: "Exponentiële groei"
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
# Modelleren van een rupsenuitbraak volgens de exponentiële groei

## Situatie afhankelijk van de groeifactor <em>a</em>

Het getal <em>a</em> stelt het gemiddeld aantal nakomelingen per rups voor. We werken met gemiddelden, dus kommagetallen zijn toegestaan, maar negatieve getallen houden geen steek.

- Als <em>a < 1</em>, dan brengt elke rups minder dan één rups voort per generatie. In elke tijdstap wordt de populatie kleiner en kleiner tot ze uiteindelijk uitsterft. Je hebt dan te maken met een exponentiële **afname**.
- Als <em>a > 1</em>, dan zal elke rups aanleiding geven tot meer dan één nieuwe rups in de volgende generatie. De populatie zal groeien. Je hebt dan te maken met een exponentiële **toename**.
- In het randgeval waarbij $a = 1$, dan is de populatiegrootte **stabiel**: de geboorte van nieuwe rupsen compenseert de sterfte.

In het geval van de rups van de buxusmot is <em>a > 1</em>, aangezien deze rupsen een plaag vormen.

Het voorschrift is het recursieve voorschrift van een meetkundige rij. Het getal <em>a</em> is niets anders dan het equivalent van de **groeifactor** bij een exponentiële functie (continu model in plaats van discreet). Je hebt dus te maken met **exponentiële groei**. 

## De parameters in het wiskundig model

In de notebook wordt de grafiek geplot van een meetkundige rij aan de hand van het algemene voorschrift.<br>
De index <em>t</em> speelt de rol van **veranderlijke**. Voor bepaalde waarden van <em>t</em> wordt de populatiegrootte berekend en teruggegeven.<br>
De meetkundige rij wordt bepaald door het algemeen voorschrift met daarin twee **parameters**: de groeifactor <em>a</em> en de beginwaarde <em>u<sub>0</sub></em>.

Door de parameters aan te passen kan met het model geëxperimenteerd worden. De leerlingen kunnen het effect van de parameters op het model onderzoeken:

- Wat is het effect van een grotere beginwaarde?
- Wat is het effect van een grotere groeifactor?
- Wat is het effect van een groeifactor kleiner dan 1?

## Draagkracht

In de **notebook** wordt de grafiek getekend van een meetkundige rij die de evolutie van de rupsenpopulatiegrootte modelleert. **Via de grafiek wordt het probleem immers veel duidelijker.** <br>
De plaag groeit erg snel, wat verontrustend is. Als je nog verder in de tijd kijkt, stel je het volgende vast: de populatiegrootte groeit zonder enige belemmering verder aan; na 50 generaties zijn er meer dan 29 000 000 000 000 rupsen. Als je aanneemt dat één rups ongeveer 3 gram weegt, zijn er na 50 generaties meer dan 87 miljoen ton rupsen, het equivalent van 40 miljoen nijlpaarden. Er zijn niet genoeg buxushagen in de wereld om dergelijke populaties te ondersteunen!

In de praktijk heeft elk ecosystem een bepaalde **draagkracht**, de hoeveelheden voedsel, water en ruimte die voorhanden zijn om een bepaalde populatie te ondersteunen. Onze rupsenpopulatie is gelimiteerd door het aantal planten dat beschikbaar is als voedsel. De draagkracht wordt vaak voorgesteld door de letter <em>K</em>. Een waarde <em>K = 1000 </em> zou betekenen dat een tuin genoeg buxussen heeft om 1000 rupsen te voeden, maar niet meer.

In het volgende onderdeel wordt het model aangepast om rekening te houden met de draagkracht.

## Python

Deze notebook maakt, net als de andere, gebruik van Python om berekeningen te doen en grafieken te genereren. Het is als leerkracht belangrijk om:

- te weten welke [syntax](https://www.w3schools.com/python/python_syntax.asp) Python gebruikt

- te weten hoe [functies](https://www.w3schools.com/python/python_functions.asp) gedefinieerd worden

- te weten hoe [lijsten](https://www.w3schools.com/python/python_lists.asp) gebruikt kunnen worden

- te weten hoe [for-loops](https://www.w3schools.com/python/python_for_loops.asp) werken

- te weten hoe de [NumPy-bibliotheek](https://www.w3resource.com/numpy/array-creation/arange.php) het mogelijk maakt om een lijst van getallen te generen, en functies uit te voeren die de waarden in deze lijst als inputargument gebruiken

- te weten hoe de [Matplotlib-bibliotheek](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py) het mogelijk maakt om grafieken te genereren

Om het voor de leerkracht en de leerlingen eenvoudiger te maken om te begrijpen wat er gebeurt, werd het nodige commentaar voorzien. Ook werden alle functies voorzien van een omschrijving met daarin de werking van de functie, de parameters die als input gebruikt worden en de parameters die als output teruggegeven worden. Wanneer een leerkracht deze omschrijving wil consulteren, volstaat het om `help(<functie_naam>)` op te roepen.

## Minimumdoelen (derde graad doorstroom)

### Economie-Wiskunde; Grieks-Wiskunde; Latijn-Wiskunde; Technologische wetenschappen en Engineering; Wetenschappen-Wiskunde

TODO de andere richtingen met deze specifieke informaticadoelen: Bedrijfsondersteunende informaticawetenschappen(GO!), Informatica- en communicatiewetenschappen, Bedrijfswetenschappen (GO!), Mechatronica, Biotechnologische en chemische STEM-wetenschappen

<span style="color: yellowgreen">SMD 07.01.01 De leerlingen programmeren zelf ontworpen oplossingen voor concrete problemen.</span><br>
Er wordt een gestructureerde programmeertaal gebruikt, namelijk Python.  Er komt een begrensde herhaling aan bod. Er wordt in de notebook gebruikgemaakt van variabelen, gegevenstypes, datastructuren, operatoren, functies en softwarebibliotheken.

<span style="color: yellowgreen">MD 06.06 De leerlingen gebruiken modellen voor exponentiële groei.</span> <br>
Duiding uit het leerplan van Katholiek Onderwijs Vlaanderen: *Dit doel omvat enerzijds het modelleren (opstellen van het voorschrift vanuit een verwoording) en anderzijds het oplossen van vragen aan de hand van het model, bijvoorbeeld de waarde bepalen bij een gegeven tijdstip of het tijdstip bij een gegeven waarde bepalen. Alhoewel "exponentiële groei" een toename suggereert, kan je ook dalende processen beschrijven.*

<span style="color: yellowgreen">SMD 06.08.07	De leerlingen leggen het verband tussen de grafiek van een functie en haar kenmerken.</span> <br>

<span style="color: yellowgreen">SMD 06.08.13	De leerlingen lossen eenvoudige veeltermvergelijkingen, rationale vergelijkingen, irrationale vergelijkingen, exponentiële vergelijkingen, logaritmische vergelijkingen en goniometrische vergelijkingen algebraïsch op.</span><br> 

<span style="color: yellowgreen">MD 06.12	De leerlingen gebruiken rekenkundige en meetkundige rijen om patronen te beschrijven.</span><br>
Het gaat hier om een meetkundige rij waarbij initieel het recursief voorschrift wordt gehanteerd. Voor het model, het voorschrift van de exponentiële functie, wordt de formule voor de algemene term gebruikt.   

<span style="color: yellowgreen">MD 06.19	De leerlingen beschrijven fenomenen uit de realiteit aan de hand van wiskundige concepten uit de derde graad. </span>

<span style="color: yellowgreen">MD 06.20	De leerlingen lossen vraagstukken en problemen op door te mathematiseren en demathematiseren en door gebruik te maken van heuristieken.</span><br> 
Wenken uit het leerplan van Katholiek Onderwijs Vlaanderen: *Voorbeelden van heuristieken die aan bod kunnen komen: het gegeven en gevraagde expliciteren, het probleem herformuleren of opdelen in deelproblemen, een schets of tekening maken, bijzondere gevallen onderzoeken, tijdelijk één van de voorwaarden laten vallen, van achter naar voor werken, alle mogelijkheden opschrijven en dan elimineren. Het demathematiseren kan gebeuren via een antwoordzin. Controleren of een antwoord realistisch kan zijn, hoort ook bij deze stap van het oplossingsproces.*

<span style="color: yellowgreen">MD 06.21	De leerlingen gebruiken ICT om berekeningen uit te voeren en grafische voorstellingen te maken. </span>
