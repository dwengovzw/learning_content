---
hruid: stem5_5
version: 3
language: nl
title: "Logistische groei"
description: "Logistische groei"
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
# Modelleren van een rupsenuitbraak volgens de logistische groei

In het vorige leerobject stelden de leerlingen vast dat de populatiegrootte zonder enige belemmering verder aangroeit wanneer een exponentiële groei beschouwd wordt met groeifactor $a > 1$. We wensen evenwel rekening te houden met de draagkracht van het ecosysteem waarin de populatie voorkomt; deze bepaalt de maximale populatiegrootte die ondersteund kan worden op basis van de hoeveelheden voedsel, water en ruimte die voorhanden zijn om de populatie te ondersteunen.

## Logistische groei

In dit leerobject introduceren we de logistische groei, die rekening houdt met de groeifactor $a$ en de draagkracht $K$:

\\[u_t = \left[1 + (a - 1) \left(1 - \frac{u_{t - 1}}{K}\right)\right] u_{t - 1} = \left[1 + r \left(1 - \frac{u_{t - 1}}{K}\right)\right] u_{t - 1}\\]

De leerlingen kunnen het effect van de parameters op dit model onderzoeken:

- Wat is het effect van een grotere draagkracht?
- Wat is het effect van een grotere populatiegrootte?
- Wat gebeurt er wanneer de populatiegrootte op een gegeven moment groter is dan de draagkracht?

## Creëren van grafieken

In dit leerobject wordt van de leerlingen gevraagd om verschillende grafieken te genereren. Hierbij wordt een vast stramien gehanteerd:

- De nodige bibliotheken (Matplotlib en NumPy) worden ingeladen

- De nodige berekeningen worden gedaan, om de data te genereren die geplot moeten worden

- Een nieuwe figuur wordt aangemaakt

- De eerder gegenereerde data worden geplot

- De assen worden benoemd

- Er wordt voorzien in een titel

- De grafiek wordt getoond

Eigen accenten kunnen hierbij gelegd worden door de leerkracht. Zo kunnen diverse kleurenpaletten gebruikt worden, kunnen verschillende reeksen in dezelfde grafiek gecombineerd worden met behulp van een legende, enzovoort.

## Chaostheorie

Doorheen het leerobject zullen de leerlingen ontdekken dat een zekere willekeur onstaat wanneer bepaalde waarden voor de groeifactor $a$ gebruikt worden. Hierbij wordt verwezen naar de chaostheorie, die stelt dat kleine verschillen in de startcondities van een systeem kunnen leiden tot grote verschillen in de uitkomst. Om dit chaotische gedrag te kaderen, wordt in een apart leerobject voorzien.

## Python

Deze notebook maakt, net als de andere, gebruik van Python om berekeningen te maken en grafieken te genereren. Het is als leerkracht belangrijk om te weten:

- welke [syntax](https://www.w3schools.com/python/python_syntax.asp) Python gebruikt;

- hoe [functies](https://www.w3schools.com/python/python_functions.asp) gedefinieerd worden;

- hoe [lijsten](https://www.w3schools.com/python/python_lists.asp) gebruikt kunnen worden;

- hoe [for-loops](https://www.w3schools.com/python/python_for_loops.asp) werken;

- hoe de [NumPy-bibliotheek](https://www.w3resource.com/numpy/array-creation/arange.php) het mogelijk maakt om een lijst van getallen te generen, en functies uit te voeren die de waarden in deze lijst als inputargument gebruiken;

- hoe de [Matplotlib-bibliotheek](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py) het mogelijk maakt om grafieken te genereren.

Om het voor de leerkracht eenvoudiger te maken om te begrijpen wat er gebeurt, werd in het nodige commentaar voorzien. Ook werden alle functies voorzien van een omschrijving met daarin de werking van de functie, de parameters die als input gebruikt worden en de parameters die als output teruggegeven worden. Wanneer een leerkracht deze omschrijving wil consulteren, volstaat het om `help(<functie_naam>)` op te roepen.

## Minimumdoelen

### WD_06 Wiskunde

#### Algemene minimumdoelen

Alle beschouwde richtingen

<span style="color: yellowgreen">MD 06.19 De leerlingen beschrijven fenomenen uit de realiteit aan de hand van wiskundige concepten uit de derde graad.</span><br>
In deze notebook wordt de groei van de populatiegroottes van de buxusmot uitvoerig besproken, en dit aan de hand van een logistisch groeimodel.

<span style="color: yellowgreen">MD 06.20 De leerlingen lossen vraagstukken en problemen op door te mathematiseren en demathematiseren en door gebruik te maken van heuristieken.</span><br>
In de notebook wordt onder meer gevraagd om te bepalen wanneer het aantal buxusmotten in evenwicht is.<br>
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
In de notebook worden verschillende grafieken gegenereerd die de populatiegrootte doorheen de tijd tonen. De leerlingen stellen hierbij vast dat de populatiegrootte stabiliseert voor bepaalde waarden van \\(a\\).

<span style="color: yellowgreen">06.05.07 De leerlingen lossen vergelijkingen en ongelijkheden grafisch op.</span><br>
De leerlingen bepalen wanneer de populatiegrootte in evenwicht is.

#### Wiskunde B+S'

Biotechnologische en chemische STEM-wetenschappen; Informatica- en communicatiewetenschappen; Mechatronica

<span style="color: yellowgreen">06.04.06 De leerlingen leggen het verband tussen de grafiek van een functie en haar kenmerken.</span><br>
In de notebook worden verschillende grafieken gegenereerd die de populatiegrootte doorheen de tijd tonen. De leerlingen stellen hierbij vast dat de populatiegrootte stabiliseert voor bepaalde waarden van \\(a\\).

<span style="color: yellowgreen">06.04.07 De leerlingen lossen vergelijkingen en ongelijkheden grafisch op.</span><br>
De leerlingen bepalen wanneer de populatiegrootte in evenwicht is.

#### Wiskunde B+S''

Economie-Wiskunde; Grieks-Wiskunde; Latijn-Wiskunde; Technologische wetenschappen en Engineering; Wetenschappen-Wiskunde

<span style="color: yellowgreen">SMD 06.08.07 De leerlingen leggen het verband tussen de grafiek van een functie en haar kenmerken.</span><br>
In de notebook worden verschillende grafieken gegenereerd die de populatiegrootte doorheen de tijd tonen. De leerlingen stellen hierbij vast dat de populatiegrootte stabiliseert voor bepaalde waarden van \\(a\\).

<span style="color: yellowgreen">SMD 06.08.13 De leerlingen lossen eenvoudige veeltermvergelijkingen, rationale vergelijkingen, irrationale vergelijkingen, exponentiële vergelijkingen, logaritmische vergelijkingen en goniometrische vergelijkingen algebraïsch op.</span><br>
De leerlingen bepalen wanneer de populatiegrootte in evenwicht is.

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
