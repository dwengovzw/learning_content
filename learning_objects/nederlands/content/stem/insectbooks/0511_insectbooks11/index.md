---
hruid: stem5_11
version: 3
language: nl
title: "De eindige differentiemethode"
description: "De eindige differentiemethode"
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
# De eindige differentiemethode

In dit leerobject wordt de eindige differentiemethode uitgelegd, die gebruikmaakt van het differentiequotiënt om de afgeleide van een functie voor een gegeven waarde te schatten:

\\[f'(t) = \frac{\text{d}f(t)}{\text{d}t} \approx \frac{f(t + \Delta t) - f(t)}{\Delta t}\\]

Een concreet voorbeeld wordt gegeven voor de functie \\(f\\) met voorschrift \\(f(t) = t sin (t)\\), al zijn andere voorbeelden uiteraard ook mogelijk.

## De impact van het tijdsinterval \\(\Delta t\\)

Een functie `plot_afgeleide` wordt gegeven, die het mogelijk maakt om de afgeleide van de functie \\(f\\) te plotten in een grafiek, samen met een schatting van de functiewaarden op basis van de eindige differentiemethode. Deze Pythonfunctie heeft het tijdsinterval \\(\Delta t\\) als input, wat het mogelijk maakt om te experimenteren met verschillende waarden voor deze parameter; hierdoor kan de leerling de impact van een groter/kleiner tijdsinterval onderzoeken.

Bij wijze van uitbreiding kan de leerkracht alternatieve functies laten onderzoeken, of de leerlingen vragen om een tijdsinterval \\(\Delta t\\) te zoeken waarvoor de afwijking ten opzichte van de werkelijke waarden een gegeven drempelwaarde niet overschrijdt. Ook kan gevraagd worden om in een enkele grafiek te voorzien, waarin de bekomen resultaten geplot worden voor verschillende waarden van het tijdsinterval, en dit met een bijbehorende legende.

## Python

Deze notebook maakt, net als de andere, gebruik van Python om berekeningen te maken en grafieken te genereren. Het is als leerkracht belangrijk om te weten:

- welke [syntax](https://www.w3schools.com/python/python_syntax.asp) Python gebruikt;

- hoe [functies](https://www.w3schools.com/python/python_functions.asp) gedefinieerd worden;

- hoe [for-loops](https://www.w3schools.com/python/python_for_loops.asp) werken;

- hoe de [NumPy-bibliotheek](https://www.w3resource.com/numpy/array-creation/arange.php) het mogelijk maakt om een lijst van getallen te genereren;

- hoe de [Matplotlib-bibliotheek](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py) het mogelijk maakt om grafieken te genereren.

Om het voor de leerkracht eenvoudiger te maken om te begrijpen wat er gebeurt, werd in het nodige commentaar voorzien. Ook werden alle functies voorzien van een omschrijving met daarin de werking van de functie, de parameters die als input gebruikt worden en de parameters die als output teruggegeven worden. Wanneer een leerkracht deze omschrijving wil consulteren, volstaat het om `help(<functie_naam>)` op te roepen.

## Minimumdoelen

### WD_06 Wiskunde

#### Algemene minimumdoelen

Alle beschouwde richtingen

<span style="color: yellowgreen">MD 06.03 De leerlingen interpreteren de afgeleide als limiet van een differentiequotiënt en als richtingscoëfficiënt van de raaklijn aan de grafiek.</span><br>
De eindige differentiatiemethode komt aan bod, waarbij het differentiequotiënt besproken wordt.

<span style="color: yellowgreen">MD 06.04 De leerlingen leggen grafisch het verband tussen een functie en haar afgeleide functie.</span><br>
De leerlingen stellen vast dat de functiewaarden toenemen wanneer de afgeleide positief is, en afnemen wanneer deze negatief is.

<span style="color: yellowgreen">MD 06.21 De leerlingen gebruiken ICT om berekeningen uit te voeren en grafische voorstellingen te maken.</span><br>
De notebook berekent de geschatte afgeleide voor verschillende waarden \\(t\\), en laat toe om grafieken te genereren die de impact van de variabele \\(\Delta t\\) illustreren.

#### Wiskunde B+S

Bedrijfsondersteunende informaticawetenschappen

<span style="color: yellowgreen">06.05.06 De leerlingen leggen het verband tussen de grafiek van een functie en haar kenmerken.</span><br>
In de notebook wordt de grafiek van een functie geplot, waarbij periodiciteit vastgesteld wordt. De link tussen het stijgen en dalen van de functie en de afgeleide van de functie wordt besproken.

#### Wiskunde B+S'

Biotechnologische en chemische STEM-wetenschappen; Informatica- en communicatiewetenschappen; Mechatronica

<span style="color: yellowgreen">06.04.06 De leerlingen leggen het verband tussen de grafiek van een functie en haar kenmerken.</span><br>
In de notebook wordt de grafiek van een functie geplot, waarbij periodiciteit vastgesteld wordt. De link tussen het stijgen en dalen van de functie en de afgeleide van de functie wordt besproken.

#### Wiskunde B+S''

Economie-Wiskunde; Grieks-Wiskunde; Latijn-Wiskunde; Technologische wetenschappen en Engineering; Wetenschappen-Wiskunde

<span style="color: yellowgreen">SMD 06.08.07 De leerlingen leggen het verband tussen de grafiek van een functie en haar kenmerken.</span><br>
In de notebook wordt de grafiek van een functie geplot, waarbij periodiciteit vastgesteld wordt. De link tussen het stijgen en dalen van de functie en de afgeleide van de functie wordt besproken.

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
