---
hruid: ct03_51
version: 3
language: nl
title: "Vierkantsvergelijking"
description: "Vierkantsvergelijking"
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
# De vierkantsvergelijking

**Het oplossen van een vierkantsvergelijking automatiseren.**

Wil je met je leerlingen programmeren in de wiskundeles? Dit onderwerp leent er zich toe.

Samen met de leerlingen bouw je stap voor stap een applicatie om het oplossen van een vierkantsvergelijking te automatiseren. Stap voor stap werk je de applicatie verder uit. 

Deze applicatie kan vervolgens gebruikt worden bij het oplossen van vraagstukken. Dan gaat de focus meer naar het vraagstuk en minder naar het rekenen.

> Een vraagstuk herleiden tot de vierkantsvergelijking die opgelost moet worden, is een vorm van abstractie.

<div class="alert alert-box alert-warning">
In de case over de stelling van Pythagoras zie je hoe je zo'n applicatie geleidelijk aan uitwerkt, vertrekkend vanuit computationeel denken.
</div>

Met het programmeren ga je zo ver als je zelf wilt. In dit uitgewerkt voorbeeld komen variabelen, datatypes, operatoren, logische uitdrukkingen en de keuzestructuur aan bod, vragen we input aan de gebruiker, en gebruiken we ingebouwde en zelfgedefinieerde functies. We maken ook gebruik van Python-modules (bibliotheken) en besteden aandacht aan het schrijven van commentaar. <br>
> Indien gewenst, dan kan je de applicatie nog verder verbeteren en ook aan de slag gaan met herhalingsstructuren. Je kan bv. een voorwaardelijke herhaling gebruiken om te laten controleren of de ingevoerde coëfficiënt van de tweedegraadsvergelijking niet nul is.

**Doelgroep:** 2de graad - finaliteit doorstroom, 3de graad - dubbele finaliteit

**Vak:** Wiskunde

**Voorkennis:** 
* De leerlingen kunnen een vierkantsvergelijking manueel oplossen. Ze kennen de formules voor de discriminant en de wortels.
* De leerlingen kennen een keuzestructuur (of het kan hier klassikaal aangebracht worden).

![ct-schema](@learning-object/m_ct03_51/nl/3)

Afhankelijk van het feit of leerlingen reeds kennis maakten met het gebruik van functies in een programma, kan de **patroonherkenning en abstractie** van in het begin, dan wel later aan bod komen. Er kan stap voor stap gewerkt worden. Er kan eerst een programma geschreven worden, zonder toepassing van de vermelde patroonherkenning en abstractie. Dat programma kan dan de aanleiding zijn om aan de slag te gaan met een zelfgedefinieerde **functie** en de voordelen ervan te duiden.

---

Onder het lesthema ['Python in de Wiskundeles'](https://www.dwengo.org/math_with_python/) vind je in het leerpad ['Parabolen'](https://www.dwengo.org/learning-path.html?hruid=maths_parabolen&language=nl&te=true&source_page=%2Fmath_with_python%2F&source_title=%20Python%20in%20de%20Wiskundeles#pn_voorkennis_parabolen;nl;3) een Python notebook waar je dit kan programmeren.

---

### Extra

Je kan leerlingen na afloop zelfstandig aan het werk zetten met een van de volgende opdrachten:
* Schrijf een analoge applicatie om de top te berekenen van een parabool.
* Schrijf een analoge applicatie die geeft of een parabool de x-as snijdt en of de snijpunten links, rechts of aan weerszijden van de oorsprong liggen.
* Schrijf een applicatie die de grafiek tekent van een parabool en er de top op aanduidt. Dalparabolen verschijnen in het groen en bergparabolen in het blauw. 
