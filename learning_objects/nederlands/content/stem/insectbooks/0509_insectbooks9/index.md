---
hruid: stem5_9
version: 3
language: nl
title: "De Lesliematrix"
description: "De Lesliematrix"
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
# Modelleren van de levensloop van een kever met de Lesliematrix

In dit leerobject zullen de leerlingen vertrouwd worden met de Lesliematrix, die het mogelijk maakt om het aantal individuen in een specifieke levensfase van een populatie te berekenen. Deze matrix wordt geïntroduceerd aan de hand van de levensvormen van de kever: het eitje, de larve en de volwassen kever. Deze volgorde van levensfases leidt tot een cyclus, die in een graaf gegoten kan worden:

![Graaf](embed/graph.png "https://www.wisfaq.nl/pagina.asp?nummer=1883")

Op basis van de waarden van de knopen in de graaf, kan de volgende toestand berekend worden. Om dit proces te vereenvoudigen, zullen de leerlingen matrices gebruiken.

## De Lesliematrix

Om aan matrixvermenigvuldiging te kunnen doen, wordt de toestand op tijdstip \\(0\\) gelijkgesteld aan een vector \\(v_0\\), die het aantal eitjes, larven en kevers bevat. Het volgende voorbeeld wordt gebruikt:

\\[v_0 = \begin{bmatrix} 1000 \\\ 100 \\\ 60 \end{bmatrix}\\]

Om dan de toestand \\(v_{1}\\) op tijdstip \\(1\\) te bepalen, wordt de Lesliematrix \\(L\\) gebruikt. In bovenstaand voorbeeld ziet deze er als volgt uit:

\\[L = \begin{bmatrix} 0 & 0 & 100 \\\ 0.05 & 0 & 0 \\\ 0 & 0.75 & 0 \end{bmatrix}\\]

Vertrekkend van de toestand \\(v_0\\), kan \\(v_{1}\\) berekend worden als volgt:

\\[v_{1} = L v_0 = \begin{bmatrix} 0 & 0 & 100 \\\ 0.05 & 0 & 0 \\\ 0 & 0.75 & 0 \end{bmatrix} \begin{bmatrix} 1000 \\\ 100 \\\ 60 \end{bmatrix} = \begin{bmatrix} 6000 \\\ 50 \\\ 75 \end{bmatrix}\\]

## Matrices in Python

Het leerobject voorziet eerst in een inleiding tot matrices, waarmee gewerkt kan worden met behulp van de `NumPy`-bibliotheek. Enkele voorbeelden worden gegeven, waarbij gevraagd wordt om enkele eenvoudige berekeningen eerst met de hand te maken. Het volgende wordt uitgelegd:

- Hoe matrices gedefinieerd kunnen worden

- Hoe matrixvermenigvuldigingen gedaan kunnen worden

- Dat Numpy het mogelijk maakt om een matrix rechts te vermenigvuldigen met een rijmatrix, ook al is deze berekening wiskundig gezien niet mogelijk

- Hoe machten van een matrix berekend kunnen worden met behulp van de functie `linalg.matrix_power`

Op basis hiervan worden de nodige berekeningen gemaakt omtrent de populatiegrootte van de kevers. Daarnaast wordt onder meer gevraagd om een grafiek te genereren, waarbij in de nodige data voorzien moet worden.

## Sterftetabellen

Als tweede voorbeeld wordt er gewerkt met sterfte- en reproductiecijfers bij vrouwen. Hierbij worden vrouwen ingedeeld volgens leeftijd, per periode van tien jaar.

Om de kans te berekenen dat een willekeurige vrouw van de ene fase overgaat naar de volgende, wordt gebruikgemaakt van een sterftetabel met officiële gegevens voor België. Van de leerlingen wordt gevraagd om deze te raadplegen, en op basis van de gegevens (per jaar) de kansen op overleven (na tien jaar) te berekenen en deze in te vullen in de Lesliematrix.

Daarnaast worden ook fictieve data aangeleverd, die de verwachtingswaarde van het aantal dochters die een vrouw krijgt in een zekere levensfase bevatten. Door ook deze in te vullen in de Lesliematrix, kan het aantal vrouwen in een bepaalde fase bepaald worden over perioden van tien jaar heen.

## Wegschrijven naar CSV-bestanden

Van de leerlingen wordt gevraagd om de berekende gegevens voor de volgende 20 generaties vrouwen weg te schrijven naar een CSV-bestand. Om de data weg te schrijven wordt gebruikgemaakt van de `Pandas`-bibliotheek.

## Python

Deze notebook maakt, net als de andere, gebruik van Python om berekeningen te maken en grafieken te genereren. Het is als leerkracht belangrijk om te weten:

- welke [syntax](https://www.w3schools.com/python/python_syntax.asp) Python gebruikt;

- hoe [functies](https://www.w3schools.com/python/python_functions.asp) gedefinieerd worden;

- hoe [lijsten](https://www.w3schools.com/python/python_lists.asp) gebruikt kunnen worden;

- hoe [for-loops](https://www.w3schools.com/python/python_for_loops.asp) werken;

- hoe de [NumPy-bibliotheek](https://www.w3resource.com/numpy/array-creation/arange.php) het mogelijk maakt om een lijst van getallen te generen, matrices te definiëren, matrixvermenigvuldigingen en machtsverheffingen uit te voeren, en matrices te hervormen;

- hoe de [Matplotlib-bibliotheek](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py) het mogelijk maakt om grafieken te genereren;

- hoe de [Pandas-bibliotheek](https://pythonbasics.org/read-csv-with-pandas/) het mogelijk maakt om gegevens uit een dataframe, dat de gegevens in tabelvorm bevat, weg te schrijven naar een CSV-bestand.

Om het voor de leerkracht eenvoudiger te maken om te begrijpen wat er gebeurt, werd in het nodige commentaar voorzien. Ook werden alle functies voorzien van een omschrijving met daarin de werking van de functie, de parameters die als input gebruikt worden en de parameters die als output teruggegeven worden. Wanneer een leerkracht deze omschrijving wil consulteren, volstaat het om `help(<functie_naam>)` op te roepen.

## Minimumdoelen

### WD_06 Wiskunde

#### Algemene minimumdoelen

Alle beschouwde richtingen

<span style="color: yellowgreen">MD 06.19 De leerlingen beschrijven fenomenen uit de realiteit aan de hand van wiskundige concepten uit de derde graad.</span><br>
In deze notebook wordt de groei van de populatiegroottes van de kever (in de vorm van eitjes, larven en kevers) uitvoerig besproken, en dit aan de hand van de Lesliematrix.

<span style="color: yellowgreen">MD 06.20 De leerlingen lossen vraagstukken en problemen op door te mathematiseren en demathematiseren en door gebruik te maken van heuristieken.</span><br>
In de notebook wordt onder meer gevraagd om te bepalen wanneer het aantal nieuwgeboren meisjes voor het eerst een gegeven waarde overschrijdt.<br>
Wenken uit het leerplan van Katholiek Onderwijs Vlaanderen: *Voorbeelden van heuristieken die aan bod kunnen komen: het gegeven en gevraagde expliciteren, het probleem herformuleren of opdelen in deelproblemen, een schets of tekening maken, bijzondere gevallen onderzoeken, tijdelijk één van de voorwaarden laten vallen, van achter naar voor werken, alle mogelijkheden opschrijven en dan elimineren. Het demathematiseren kan gebeuren via een antwoordzin. Controleren of een antwoord realistisch kan zijn, hoort ook bij deze stap van het oplossingsproces.*

<span style="color: yellowgreen">MD 06.21 De leerlingen gebruiken ICT om berekeningen uit te voeren en grafische voorstellingen te maken.</span><br>
De notebook berekent de populatiegrootte na een aantal tijdstappen, en dit voor de verschillende levensfasen van de kever. Dit laat toe om een grafiek te genereren die het aantal individuen in elke levensfase illustreert.

#### Natuurwetenschappen B+S

Latijn-Wetenschappen; Wetenschappen-Wiskunde

#### Natuurwetenschappen B+S'

Grieks-Wiskunde; Latijn-Wiskunde

<span style="color: yellowgreen">MD 06.46 De leerlingen analyseren de wisselwerking tussen wetenschappen, technologie, wiskunde en de maatschappij aan de hand van maatschappelijke uitdagingen.</span><br>
Dit minimumdoel kan betrokken worden in deze module, op initiatief van de leerkracht.

#### Wiskunde B+S

Bedrijfsondersteunende informaticawetenschappen

<span style="color: yellowgreen">06.05.01 De leerlingen voeren bewerkingen uit met matrices: optelling, scalaire vermenigvuldiging, matrixvermenigvuldiging, machtsverheffing en transpositie.</span><br>
Vermenigvuldigingen van de Lesliematrix met een kolommatrix worden toegepast om de toestand in de volgende tijdstap te bepalen, en machtsverheffing van de Lesliematrix wordt toegepast om de toestand verder in de tijd te bepalen.

<span style="color: yellowgreen">06.05.02 De leerlingen gebruiken matrixmodellen om evoluties te beschrijven.</span><br>
De Lesliematrix wordt gebruikt om de evolutie van het aantal eitjes, larven en kevers doorheen de tijd te beschrijven. De link wordt gelegd met de matrixvoorstelling van een graaf.

#### Wiskunde B+S'

Biotechnologische en chemische STEM-wetenschappen; Informatica- en communicatiewetenschappen; Mechatronica

<span style="color: yellowgreen">06.04.01 De leerlingen voeren bewerkingen uit met matrices: optelling, scalaire vermenigvuldiging, matrixvermenigvuldiging, machtsverheffing en transpositie.</span><br>
Vermenigvuldigingen van de Lesliematrix met een kolommatrix worden toegepast om de toestand in de volgende tijdstap te bepalen, en machtsverheffing van de Lesliematrix wordt toegepast om de toestand verder in de tijd te bepalen.

<span style="color: yellowgreen">06.04.02 De leerlingen gebruiken matrixmodellen om evoluties te beschrijven.</span><br>
De Lesliematrix wordt gebruikt om de evolutie van het aantal eitjes, larven en kevers doorheen de tijd te beschrijven. De link wordt gelegd met de matrixvoorstelling van een graaf.

#### Wiskunde B+S''

Economie-Wiskunde; Grieks-Wiskunde; Latijn-Wiskunde; Technologische wetenschappen en Engineering; Wetenschappen-Wiskunde

<span style="color: yellowgreen">06.08.01 De leerlingen voeren bewerkingen uit met matrices: optelling, scalaire vermenigvuldiging, matrixvermenigvuldiging, machtsverheffing en transpositie.</span><br>
Vermenigvuldigingen van de Lesliematrix met een kolommatrix worden toegepast om de toestand in de volgende tijdstap te bepalen, en machtsverheffing van de Lesliematrix wordt toegepast om de toestand verder in de tijd te bepalen.

<span style="color: yellowgreen">06.08.02 De leerlingen gebruiken matrixmodellen om evoluties te beschrijven.</span><br>
De Lesliematrix wordt gebruikt om de evolutie van het aantal eitjes, larven en kevers doorheen de tijd te beschrijven. De link wordt gelegd met de matrixvoorstelling van een graaf.

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