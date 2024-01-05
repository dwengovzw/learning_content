---
hruid: stem5_7
version: 3
language: nl
title: "De chaos verklaard"
description: "De chaos verklaard"
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
# De chaos verklaard

## Transities tussen populatiegroottes

In dit leerobject wordt de schijnbare willekeur voor bepaalde waarden van de groeifactor $a$ onder de loep genomen. Daartoe wordt een nieuwe grafiek geïntroduceerd, die de transities van \\(u_{t - 1}\\) naar \\(u_t\\) weergeeft, samen met de eerste bissector en het evenwichtspunt. In deze grafiek wordt voorzien door middel van een functie, die hergebruikt kan worden om de impact van de parameters \\(u_0\\), \\(a\\) en \\(K\\) te onderzoeken:

- Wat gebeurt er voor verschillende waarden van \\(a > 1\\)?

- Welke impact heeft de startwaarde \\(u_0=\\)? Wat gebeurt er indien \\(u_0 = K\\)?

Aan de hand van de gegeven opdrachten zullen de leerlingen vaststellen dat een periode van twee, een periode van vier, of chaotisch gedrag bekomen wordt.

## Het bifurcatiediagram

Er wordt voorzien in de code om een bifurcatiediagram te genereren, waarbij de logistische vergelijking toegepast wordt voor een groot aantal stappen, voor alle waarden van \\(a\\) van \\(0\\) tot \\(4\\) met tussenstappen van \\(0{,}01\\). Typisch worden alle gehele waarden van 1 tot en met \\(K - 1\\) geplot, maar om rekening te houden met grote waarden van \\(K\\) (die de uitvoeringstijd significant beïnvloeden) wordt ervoor gekozen om 100 willekeurige getallen tussen \\(1\\) en \\(K - 1\\) te trekken met herhaling. Uit het resultaat kan het volgende geconcludeerd worden:

- voor $0 < a < 1$ is er geen groei, de populatie sterft uit;

- voor $1 \le a < 3$ is er convergentie naar $K$;

- voor $3 \le a < 4$ stel je eerst een splitsing (een bifurcatie) in twee vast, die duidt op een periodieke reeks met periode twee. Voor hogere waarden stel je een periodieke reeks van vier vast, om uiteindelijk naar een chaotisch regime over te gaan.

Momenteel wordt de code voor deze grafiek gegeven, met de vraag aan de leerlingen om op basis hiervan een tweede grafiek te maken met verschillende eigenschappen. De leerkracht kan er ook voor kiezen om de voorbeeldcode niet te geven, maar hier een (programmeer)opdracht van te maken.

## Wegschrijven van grafieken

Van de leerlingen wordt gevraagd om een gegenereerd bifurcatiediagram weg te schrijven naar een PDF-bestand. Hiervoor zal gebruikgemaakt worden van de `Matplotlib`-bibliotheek.

## Python

Deze notebook maakt, net als de andere, gebruik van Python om berekeningen te maken en grafieken te genereren. Het is als leerkracht belangrijk om te weten:

- welke [syntax](https://www.w3schools.com/python/python_syntax.asp) Python gebruikt;

- hoe [functies](https://www.w3schools.com/python/python_functions.asp) gedefinieerd worden;

- hoe [lijsten](https://www.w3schools.com/python/python_lists.asp) gebruikt kunnen worden;

- hoe [for-loops](https://www.w3schools.com/python/python_for_loops.asp) werken;

- hoe de [NumPy-bibliotheek](https://www.w3resource.com/numpy/array-creation/arange.php) het mogelijk maakt om een lijst van getallen te generen, en om willekeurige getallen in een gegeven bereik te genereren;

- hoe de [Matplotlib-bibliotheek](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py) het mogelijk maakt om grafieken te genereren, en deze weg te schrijven naar een lokaal bestand.

Om het voor de leerkracht eenvoudiger te maken om te begrijpen wat er gebeurt, werd in het nodige commentaar voorzien. Ook werden alle functies voorzien van een omschrijving met daarin de werking van de functie, de parameters die als input gebruikt worden en de parameters die als output teruggegeven worden. Wanneer een leerkracht deze omschrijving wil consulteren, volstaat het om `help(<functie_naam>)` op te roepen.

## Minimumdoelen

### WD_06 Wiskunde

#### Algemene minimumdoelen

Alle beschouwde richtingen

<span style="color: yellowgreen">MD 06.19 De leerlingen beschrijven fenomenen uit de realiteit aan de hand van wiskundige concepten uit de derde graad.</span><br>
In deze notebook wordt de groei van de populatiegroottes van de buxusmot uitvoerig besproken, en dit aan de hand van een logistisch groeimodel.

<span style="color: yellowgreen">MD 06.21 De leerlingen gebruiken ICT om berekeningen uit te voeren en grafische voorstellingen te maken.</span><br>
De notebook berekent de populatiegrootte na een honderdtal generaties, en dit voor verschillende waarden van de groeifactor \\(a\\) en startwaarden \\(u\\). Dit laat toe om een bifurcatiediagram te genereren, dat de impact van de groeifactor op de finale populatiegrootte illustreert.

#### Natuurwetenschappen B+S

Latijn-Wetenschappen; Wetenschappen-Wiskunde

#### Natuurwetenschappen B+S'

Grieks-Wiskunde; Latijn-Wiskunde

<span style="color: yellowgreen">MD 06.46 De leerlingen analyseren de wisselwerking tussen wetenschappen, technologie, wiskunde en de maatschappij aan de hand van maatschappelijke uitdagingen.</span><br>
Dit minimumdoel kan betrokken worden in deze module, op initiatief van de leerkracht.

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
