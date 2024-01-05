---
hruid: stem5_3
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
target_ages: [16, 17, 18]
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

## Situatie afhankelijk van de groeifactor \\(a\\)

Het getal \\(a\\) stelt het gemiddeld aantal nakomelingen per rups voor. We werken met gemiddelden, dus kommagetallen zijn toegestaan, maar negatieve getallen houden geen steek.

- Als \\(a < 1\\), dan brengt elke rups minder dan één rups voort per generatie. In elke tijdstap wordt de populatie kleiner en kleiner tot ze uiteindelijk uitsterft. Je hebt dan te maken met een exponentiële **afname**.
- Als \\(a > 1\\), dan zal elke rups aanleiding geven tot meer dan één nieuwe rups in de volgende generatie. De populatie zal groeien. Je hebt dan te maken met een exponentiële **toename**.
- In het randgeval waarbij \\(a = 1\\), is de populatiegrootte **stabiel**: de geboorte van nieuwe rupsen compenseert de sterfte.

In het geval van de rups van de buxusmot is \\(a > 1\\), aangezien deze rupsen een plaag vormen.

Het voorschrift is het recursieve voorschrift van een meetkundige rij. Het getal \\(a\\) is niets anders dan het equivalent van de **groeifactor** bij een exponentiële functie (continu model in plaats van discreet). Je hebt dus te maken met **exponentiële groei**. 

## De parameters in het wiskundig model

In de notebook wordt de grafiek geplot van een meetkundige rij aan de hand van het algemene voorschrift. De index \\(t\\) speelt hierbij de rol van **veranderlijke**. Voor bepaalde waarden van \\(t\\) wordt de populatiegrootte berekend en teruggegeven.

De meetkundige rij wordt bepaald door het algemene voorschrift met daarin twee **parameters**: de groeifactor \\(a\\) en de beginwaarde \\(u_0\\). Door de parameters aan te passen kan met het model geëxperimenteerd worden. De leerlingen kunnen het effect van de parameters op het model onderzoeken:

- Wat is het effect van een grotere beginwaarde?
- Wat is het effect van een grotere groeifactor?
- Wat is het effect van een groeifactor kleiner dan 1?

## Draagkracht

In de notebook wordt de grafiek getekend van een meetkundige rij die de evolutie van de rupsenpopulatiegrootte modelleert. **Via de grafiek wordt het probleem immers veel duidelijker.**

De plaag groeit erg snel, wat verontrustend is. Als je nog verder in de tijd kijkt, stel je het volgende vast: de populatiegrootte groeit zonder enige belemmering verder aan; na 70 generaties zijn er meer dan 971.000.000.000.000 rupsen. Er zijn niet genoeg buxushagen in de wereld om dergelijke populaties te ondersteunen!

In de praktijk heeft elk ecosysteem een bepaalde **draagkracht**, de hoeveelheden voedsel, water en ruimte die voorhanden zijn om een bepaalde populatie te ondersteunen. Onze rupsenpopulatie is gelimiteerd door het aantal planten dat beschikbaar is als voedsel. De draagkracht wordt vaak voorgesteld door de letter \\(K\\). Een waarde \\(K = 1000 \\) zou betekenen dat een tuin genoeg buxussen heeft om 1000 rupsen te voeden, maar niet meer.

In het volgende leerobject wordt het model aangepast om rekening te houden met deze draagkracht.

## Besmettingen met COVID-19

Bij wijze van illustratie, worden gegevens ingelezen vanuit een CSV-bestand, die het aantal besmettingen en het aantal dodelijke slachtoffers door COVID-19 in België beschrijft in de eerste weken van de lockdown in maart 2020. Aan de hand van enkele grafieken wordt het gevaar van onbeperkte groei geïllustreerd. Om de data in te lezen wordt gebruikgemaakt van de `Pandas`-bibliotheek.

Leerlingen die vroeger klaar zijn met dit leerobject, of een sterke interesse vertonen in dit onderwerp, kunnen [dit gerelateerde leerobject](https://www.dwengo.org/learning-path.html?hruid=maths_epidemie&language=nl&te=true&source_page=%2F&source_title=%20Ga%20aan%20de%20slag%20met%20uniek%20lesmateriaal%20over%20AI%20en%20STEM!#pn_expogroei;nl;3) volgen.

## De logaritmische as

Als laatste voorbeeld van exponentiële groei wordt de wet van Moore besproken. Om deze te illustreren wordt een grafiek gebruikt met een logaritmische as; het gebruik van een dergelijke as wordt besproken aan de hand van concrete voorbeelden in Python.

## Python

Deze notebook maakt, net als de andere, gebruik van Python om berekeningen te maken en grafieken te genereren. Het is als leerkracht belangrijk om te weten:

- welke [syntax](https://www.w3schools.com/python/python_syntax.asp) Python gebruikt;

- hoe [functies](https://www.w3schools.com/python/python_functions.asp) gedefinieerd worden;

- hoe [lijsten](https://www.w3schools.com/python/python_lists.asp) gebruikt kunnen worden;

- hoe [for-loops](https://www.w3schools.com/python/python_for_loops.asp) werken;

- hoe [while-loops](https://www.w3schools.com/python/python_while_loops.asp) werken;

- hoe de [NumPy-bibliotheek](https://www.w3resource.com/numpy/array-creation/arange.php) het mogelijk maakt om een lijst van getallen te generen, en functies uit te voeren die de waarden in deze lijst als inputargument gebruiken;

- hoe de [Matplotlib-bibliotheek](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py) het mogelijk maakt om grafieken te genereren;

- hoe de [Pandas-bibliotheek](https://pythonbasics.org/read-csv-with-pandas/) het mogelijk maakt om CSV-bestanden uit te lezen naar een dataframe, dat gegevens in tabelvorm bevat.

Om het voor de leerkracht eenvoudiger te maken om te begrijpen wat er gebeurt, werd in het nodige commentaar voorzien. Ook werden alle functies voorzien van een omschrijving met daarin de werking van de functie, de parameters die als input gebruikt worden en de parameters die als output teruggegeven worden. Wanneer een leerkracht deze omschrijving wil consulteren, volstaat het om `help(<functie_naam>)` op te roepen.

## Minimumdoelen

### WD_06 Wiskunde

#### Algemene minimumdoelen

Alle beschouwde richtingen

<span style="color: yellowgreen">MD 06.06 De leerlingen gebruiken modellen voor exponentiële groei.</span><br>
In deze notebook wordt de groei van de populatiegroottes van de buxusmot uitvoerig besproken, en dit aan de hand van een exponentieel groeimodel.<br>
Duiding uit het leerplan van Katholiek Onderwijs Vlaanderen: *Dit doel omvat enerzijds het modelleren (opstellen van het voorschrift vanuit een verwoording) en anderzijds het oplossen van vragen aan de hand van het model, bijvoorbeeld de waarde bepalen bij een gegeven tijdstip of het tijdstip bij een gegeven waarde bepalen. Alhoewel "exponentiële groei" een toename suggereert, kan je ook dalende processen beschrijven.*

<span style="color: yellowgreen">MD 06.12 De leerlingen gebruiken rekenkundige en meetkundige rijen om patronen te beschrijven.</span><br>
Het gaat hier om een meetkundige rij, waarbij initieel het recursieve voorschrift wordt gehanteerd. Voor het model, het voorschrift van de exponentiële functie, wordt de formule voor de algemene term gebruikt.

<span style="color: yellowgreen">MD 06.19 De leerlingen beschrijven fenomenen uit de realiteit aan de hand van wiskundige concepten uit de derde graad.</span><br>
In deze notebook wordt de groei van de populatiegroottes van de buxusmot uitvoerig besproken, en dit aan de hand van een exponentieel groeimodel.

<span style="color: yellowgreen">MD 06.20 De leerlingen lossen vraagstukken en problemen op door te mathematiseren en demathematiseren en door gebruik te maken van heuristieken.</span><br>
In de notebook wordt onder meer gevraagd om te bepalen wanneer het aantal buxusmotten voor het eerst een gegeven waarde overschrijdt.<br>
Wenken uit het leerplan van Katholiek Onderwijs Vlaanderen: *Voorbeelden van heuristieken die aan bod kunnen komen: het gegeven en gevraagde expliciteren, het probleem herformuleren of opdelen in deelproblemen, een schets of tekening maken, bijzondere gevallen onderzoeken, tijdelijk één van de voorwaarden laten vallen, van achter naar voor werken, alle mogelijkheden opschrijven en dan elimineren. Het demathematiseren kan gebeuren via een antwoordzin. Controleren of een antwoord realistisch kan zijn, hoort ook bij deze stap van het oplossingsproces.*

<span style="color: yellowgreen">MD 06.21 De leerlingen gebruiken ICT om berekeningen uit te voeren en grafische voorstellingen te maken.</span><br>
De notebook berekent de populatiegrootte op verschillende momenten in de tijd, en laat toe om grafieken te genereren die de groei van de populatie illustreert.

#### Natuurwetenschappen B+S

Latijn-Wetenschappen; Wetenschappen-Wiskunde

#### Natuurwetenschappen B+S'

Grieks-Wiskunde; Latijn-Wiskunde

<span style="color: yellowgreen">MD 06.46 De leerlingen analyseren de wisselwerking tussen wetenschappen, technologie, wiskunde en de maatschappij aan de hand van maatschappelijke uitdagingen.</span><br>
Dit minimumdoel kan betrokken worden in deze module, op initiatief van de leerkracht.

#### Wiskunde B+S

Bedrijfsondersteunende informaticawetenschappen

<span style="color: yellowgreen">06.05.06 De leerlingen leggen het verband tussen de grafiek van een functie en haar kenmerken.</span><br>
In de notebook worden verschillende grafieken gegenereerd die de populatiegrootte doorheen de tijd tonen. De leerlingen stellen hierbij vast dat de populatiegrootte steeds verder blijft toenemen indien \\(a > 1\\). Ook wordt uitgelegd hoe de logaritmische as gebruikt kan worden in een grafiek.

#### Wiskunde B+S'

Biotechnologische en chemische STEM-wetenschappen; Informatica- en communicatiewetenschappen; Mechatronica

<span style="color: yellowgreen">06.04.06 De leerlingen leggen het verband tussen de grafiek van een functie en haar kenmerken.</span><br>
In de notebook worden verschillende grafieken gegenereerd die de populatiegrootte doorheen de tijd tonen. De leerlingen stellen hierbij vast dat de populatiegrootte steeds verder blijft toenemen indien \\(a > 1\\). Ook wordt uitgelegd hoe de logaritmische as gebruikt kan worden in een grafiek.

#### Wiskunde B+S''

Economie-Wiskunde; Grieks-Wiskunde; Latijn-Wiskunde; Technologische wetenschappen en Engineering; Wetenschappen-Wiskunde

<span style="color: yellowgreen">SMD 06.08.07 De leerlingen leggen het verband tussen de grafiek van een functie en haar kenmerken.</span><br>
In de notebook worden verschillende grafieken gegenereerd die de populatiegrootte doorheen de tijd tonen. De leerlingen stellen hierbij vast dat de populatiegrootte steeds verder blijft toenemen indien \\(a > 1\\). Ook wordt uitgelegd hoe de logaritmische as gebruikt kan worden in een grafiek.

<span style="color: yellowgreen">SMD 06.08.09 De leerlingen lossen vergelijkingen en ongelijkheden grafisch op.</span><br>
De leerlingen berekenen de populatiegrootte op een gegeven moment in de tijd, en aan de hand van een while-loop controleren ze wanneer de populatiegrootte voor het eerst een gegeven waarde zal overschrijden.

### WD_07 Informaticawetenschappen

#### Informaticawetenschappen

Economie-Wiskunde; Grieks-Wiskunde; Latijn-Wiskunde; Wetenschappen-Wiskunde

#### Informaticawetenschappen S''

Bedrijfsondersteunende informaticawetenschappen

#### Informatica- en communicatiewetenschappen B+S

Informatica- en communicatiewetenschappen

#### Technologische wetenschappen en Engineering B+S

Technologische wetenschappen en Engineering

#### Bedrijfswetenschappen S (GO!)

Bedrijfswetenschappen (GO!)

<span style="color: yellowgreen">SMD 07.01.01 De leerlingen programmeren zelfontworpen oplossingen voor concrete problemen.</span><br>
Er wordt een gestructureerde programmeertaal gebruikt, namelijk Python. Er komt een begrensde herhaling aan bod. Er wordt in de notebook gebruikgemaakt van variabelen, gegevenstypes, datastructuren, operatoren, functies en softwarebibliotheken. Er wordt voorzien in het nodige commentaar, zodat leerlingen begrijpen wat de verschillende codefragmenten doen.

#### Biotechnologische en chemische STEM-wetenschappen B+S

Biotechnologische en chemische STEM-wetenschappen

#### Mechatronica B+S

Mechatronica

<span style="color: yellowgreen">SMD 07.02.01 De leerlingen programmeren zelfontworpen oplossingen voor concrete problemen.</span><br>
Er wordt een gestructureerde programmeertaal gebruikt, namelijk Python. Er komt een begrensde herhaling aan bod. Er wordt in de notebook gebruikgemaakt van variabelen, gegevenstypes, datastructuren, operatoren, functies en softwarebibliotheken. Er wordt voorzien in het nodige commentaar, zodat leerlingen begrijpen wat de verschillende codefragmenten doen.
