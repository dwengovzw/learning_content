---
hruid: stem5_13
version: 3
language: nl
title: "Differentiaalvergelijkingen"
description: "Differentiaalvergelijkingen"
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
# Lieveheersbeestjes en luizenplagen: een dynamisch wereldbeeld met differentiaalvergelijkingen

We stelden reeds vast dat de tijd in de praktijk als continu ervaren wordt, waarbij discrete groeimodellen niet lang volstaan. Daarom introduceren we de **differentiaalvergelijking**, die als oplossing een functie oplevert die het systeem beschrijft doorheen de tijd. In dit leerobject geven we een eerste introductie tot differentiaalvergelijkingen, met als doel een populatie bladluizen en lieveheersbeestjes te beschrijven.

## De populatiegrootte als differentiaalvergelijking

Specifiek gericht op het probleem met bladluizen, wordt de groei van de populatiegrootte van luizen als volgt beschreven:

\[\dot{y} = ry \left(1 - \frac{y}{K}\right)\]

Hierbij stellen \(r = a - 1\) het groeipercentage en \(K\) de draagkracht voor en stelt \(y\) de populatiegrootte voor. \(\dot{y}\) is dan de afgeleide van \(y\), die de leerlingen iets vertelt over de verandering van de populatiegrootte:

- wanneer \(\dot{y} > 0\), zal de populatiegrootte stijgen;
- wanneer \(\dot{y} < 0\), zal de populatiegrootte dalen;
- wanneer \(\dot{y} = 0\), zal er geen verandering zijn en blijft de populatiegrootte constant.

Het is belangrijk dat de leerlingen inzien dat \(\dot{y}\) **de verandering (groei/afname) van de populatiegrootte** beschrijft, en **niet de populatiegrootte** zelf!

## Evenwichtswaarden en verloop

Evenwicht wordt bereikt wanneer \(\dot{y} = 0\). Om de evenwichtswaarde te bepalen, moeten de leerlingen volgende vergelijking oplossen:

\[\dot{y} = 0 \iff ry \left(1 - \frac{y}{K}\right) = 0 \iff ry = 0 \lor 1 - \frac{y}{K} = 0 \iff y = 0 \lor y = K\]

In het eerste geval zijn er geen bladluizen, in het tweede geval wordt de draagkracht \(K\) bereikt.

Om het verloop van de populatiegrootte te beschrijven doorheen de tijd, zullen de leerlingen de methode van Euler gebruiken. Hierbij wordt de afgeleide van een functie als volgt benaderd:

\[f'(t) \approx \frac{f(t + \Delta t) - f(t)}{\Delta t}\]

In het beschouwde geval stelt \(y = f(t)\) de populatiegrootte voor, en \(\dot{y} = f'(t)\) de verandering van deze grootte. In de interactieve notebook zal deze laatste formule gebruikt worden om stap voor stap nieuwe schattingen voor de functie \(f\) te maken.

## Bladluizen en lieveheersbeestjes

Na een eerste praktisch voorbeeld van het gebruik van differentiaalvergelijkingen, wordt een voorbeeld van een stelsel van differentiaalvergelijkingen gegeven. Hierbij worden twee variabelen beschouwd: de populatiegrootte van bladluizen en de populatiegrootte van lieveheersbeestjes. Deze populaties interageren met elkaar, omdat de lieveheersbeestjes (de jagers) bladluizen (de prooien) opeten. De volgende algemene vorm wordt gebruikt om dit voor te stellen:

$$\dot{\mathbf{y}} = f(\mathbf{y}, t)$$

Belangrijk om te benadrukken bij de leerlingen is dat $\mathbf{y}$ en $\mathbf{\dot{y}}$ in het vet geschreven worden, omdat het **vectoren** zijn. Hierbij is $\mathbf{y} = (y_1, y_2)$, met $y_1$ en $y_2$ de respectievelijke populatiegrootte van de bladluizen en de lieveheersbeestjes. Analoog stel je dat $\mathbf{\dot{y}} = (\dot{y_1}, \dot{y_2})$, met $\dot{y_1}$ en $\dot{y_2}$ de respectievelijke groei van beide populaties.

In de notebook worden twee voorbeelden van stelsels gegeven. Zo vinden we volgend stelsel terug, dat de groei van de populaties beschrijft:

$$
\begin{cases}
    \dot{y_1} = (a - 1) y_1 \left(1 - \frac{y_1}{K}\right) - 0.0012 y_1 y_2 \\
    \dot{y_2} = -0.4 y_2 + 0.0005 y_1 y_2
\end{cases}
$$

Dit stelsel wordt een **Lotka-Volterravergelijking** genoemd, dat in de ecologie vaak gebruikt wordt om een dynamisch biologisch systeem te beschrijven waarin zowel een prooi (de bladluis) als een predator (het lieveheersbeestje) voorkomen. Het stelsel bestaat uit twee vergelijkingen, met elk twee termen:

- De verandering van de luizenpopulatie doorheen de tijd $\dot{y_1}$

    - $(a - 1) y_1 \left(1 - \frac{y_1}{K}\right)$ beschrijft de logistische groei van de luizenpopulatie, bepaald door de huidige populatiegrootte $y_1$, de groeifactor $a$ en de draagkracht $K$.
    - $-0.0012 y_1 y_2$ beschrijft de predatie van de lieveheersbeestjes op de luizen. Deze predatie is proportioneel met zowel het aantal luizen als het aantal lieveheersbeestjes: hoe meer luizen er zijn, hoe meer er gevangen kunnen worden, en hoe meer lieveheersbeestjes er zijn, hoe meer zij er kunnen vangen. Merk op dat het model veronderstelt dat deze twee effecten onafhankelijk van elkaar zijn en vermenigvuldigd kunnen worden.
    
- De verandering van de lieveheersbeestjespopulatie doorheen de tijd $\dot{y_2}$

    - $-0.4 y_2$ beschrijft de netto sterfte van lieveheersbeestjes: elke dag sterft 40% van de lieveheersbeestjes door ouderdom of externe factoren.
    - $+0.0005 y_1 y_2$ beschrijft opnieuw de predatie van de lieveheersbeestjes op de luizen. Hier zorgt deze voor een positieve bijdrage: de luizen dienen als voedsel dat de lieveheersbeestjes gebruiken om te groeien en te vermenigvuldigen. Ook hier veronderstelt het model dat deze twee effecten onafhankelijk van elkaar zijn en vermenigvuldigd kunnen worden.

Bovenstaande vraagt enige uitleg, die klassikaal gegeven kan worden. Daarna kunnen de leerlingen met de voorziene code aan de slag, die het mogelijk maakt om de impact van de verschillende parameters te evalueren door middel van grafieken.

In gerichte opdrachten wordt onder meer gevraagd om te bepalen wanneer beide stelsels in evenwicht zijn. Dit evenwicht wordt eerst wiskundig bepaald, en nadien geverifieerd met behulp van Python-code die het mogelijk maakt om een fasediagram van het Lotka-Volterramodel te genereren. In dit diagram worden de populatiegrootte van de jagers en de prooien uitgezet, waarbij een periodisch verloop vastgesteld wordt.

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

<span style="color: yellowgreen">MD 06.03 De leerlingen interpreteren de afgeleide als limiet van een differentiequotiënt en als richtingscoëfficiënt van de raaklijn aan de grafiek.</span><br>
De methode van Euler komt aan bod, die gebruik maakt van het differentiequotiënt.

<span style="color: yellowgreen">MD 06.21 De leerlingen gebruiken ICT om berekeningen uit te voeren en grafische voorstellingen te maken.</span><br>
De notebook berekent de geschatte afgeleide voor verschillende waarden \\(t\\), en laat toe om grafieken te genereren die onder meer de impact van de variabele \\(\Delta t\\) illustreren. De bekomen populatiegroottes worden geplot doorheen de tijd, en een fasediagram van het Lokta-Volterramodel wordt gegenereerd.

#### Wiskunde B+S''

Economie-Wiskunde; Grieks-Wiskunde; Latijn-Wiskunde; Technologische wetenschappen en Engineering; Wetenschappen-Wiskunde

<span style="color: yellowgreen">SMD 06.08.13 De leerlingen lossen eenvoudige veeltermvergelijkingen, rationale vergelijkingen, irrationale vergelijkingen, exponentiële vergelijkingen, logaritmische vergelijkingen en goniometrische vergelijkingen algebraïsch op.</span><br>
Aan de hand van een stelsel van vergelijkingen wordt bepaald wanneer de populatiegroottes van jagers en prooien in evenwicht zijn.

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
