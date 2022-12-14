---
hruid: ct_cases4
version: 3
language: nl
title: "Zeeniveau - trendlijn"
description: "Zeeniveau - trendlijn"
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
# Evolutie van het Oostendse zeeniveau

### Doel
**Visualiseren van een spreidingsdiagram en een trendlijn.**

*In de context van de klimaatverandering gaan de leerlingen aan de slag met 'echte' data. Ze vertrekken daarbij van een uitdaging. Ze moeten zelf op zoek gaan naar de data, deze visualiseren a.d.h.v. een spreidingsdiagram en op zoek gaan naar een eventuele trendlijn.*

**Doelgoep:** 2de of 3de graad - dubbele finaliteit of finaliteit doorstroom

**Vak:** Wiskunde - Wetenschappen - STEM

### Uitdaging: Analyseer hoe het zeeniveau in Oostende in de toekomst zal evolueren.

Voorkennis: 
* De leerlingen kunnen informatie verzamelen via het internet. 
* De leerlingen weten dat de vorm van het spreidingsdiagram een indicatie is van een mogelijk trendlijn. 
* De leerlingen kunnen in Python een spreidingsdiagram en een trendlijn visualiseren. 

![ct-schema](@learning-object/m_ct_cases4/nl/3)

### Eindtermen (Bron: onderwijsdoelen.be)
<span style="color: yellowgreen">(4.5 Finaliteit doorstroom) De leerlingen ontwerpen algoritmen om problemen digitaal op te lossen.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau creëren

<span style="color: yellowgreen">(4.5 Dubbele finaliteit) De leerlingen lossen een afgebakend probleem digitaal op door een aangereikt algoritme aan te passen. </span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau creëren

<span style="color: yellowgreen">(6.19 Finaliteit doorstroom) De leerlingen onderzoeken het verband tussen twee numerieke grootheden in een dataset met behulp van een spreidingsdiagram.
</span>
&nbsp;&nbsp;&nbsp;&nbsp;Met ICT
&nbsp;&nbsp;&nbsp;&nbsp;Opstellen en interpreteren van een spreidingsdiagram
&nbsp;&nbsp;&nbsp;&nbsp;Bepalen en interpreteren van de trendlijn met bijhorend voorschrift 
&nbsp;&nbsp;&nbsp;&nbsp;Bepalen en interpreteren van de correlatiecoëfficiënt bij een lineair verband

&nbsp;&nbsp;&nbsp;&nbsp;De eindterm wordt zowel met als zonder context gerealiseerd.

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau analyseren

<span style="color: yellowgreen">(6.9.1 Cesuurdoelen Biotechnieken) De leerlingen onderzoeken het verband tussen twee numerieke grootheden in een dataset met behulp van een spreidingsdiagram.
</span>
&nbsp;&nbsp;&nbsp;&nbsp;Met ICT
&nbsp;&nbsp;&nbsp;&nbsp;Opstellen en interpreteren van een spreidingsdiagram
&nbsp;&nbsp;&nbsp;&nbsp;Bepalen en interpreteren van de trendlijn met bijhorend voorschrift 

&nbsp;&nbsp;&nbsp;&nbsp;De eindterm wordt met context gerealiseerd.

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau analyseren


<span style="color: yellowgreen">(6.53 Finaliteit doorstroom) De leerlingen passen een wetenschappelijke methode toe om kennis te ontwikkelen en om vragen te beantwoorden.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau analyseren

<span style="color: yellowgreen">(12.3.1 Cesuurdoelen Biotechnologische wetenschappen) De leerlingen passen een wetenschappelijke methode toe om kennis te ontwikkelen en vragen te beantwoorden.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau toepassen
    
<span style="color: yellowgreen">(6.54 Finaliteit doorstroom; 6.30 Dubbele finaliteit) De leerlingen analyseren natuurlijke en technische systemen aan de hand van verschillende STEM-concepten. </span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau analyseren

<span style="color: yellowgreen">(6.55 Finaliteit doorstroom; 6.31 Dubbele finaliteit) De leerlingen ontwerpen een oplossing voor een probleem door concepten en praktijken uit verschillende STEM-disciplines geïntegreerd aan te wenden.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Met inbegrip van context
&nbsp;&nbsp;&nbsp;&nbsp;* Elke STEM-discipline komt ten minste één maal geïntegreerd aan bod.

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau creëren

<span style="color: yellowgreen">(6.57 Finaliteit doorstroom)De leerlingen onderzoeken aan de hand van concrete maatschappelijke uitdagingen de wisselwerking tussen STEM-disciplines onderling en tussen STEM-disciplines met de maatschappij.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Met inbegrip van context
&nbsp;&nbsp;&nbsp;&nbsp;* Contexten zoals klimaatverandering, hernieuwbare energie, zorg en gezondheid, onderwijs, watervoorziening, mobiliteit, leefbare en duurzame steden, oceaanvervuiling komen aan bod.
&nbsp;&nbsp;&nbsp;&nbsp;* De duurzame ontwikkelingsdoelen zoals geformuleerd door de internationale gemeenschap worden aangereikt (SDG's, sustainable development goals).

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau analyseren

<span style="color: yellowgreen">(6.33 Dubbele finaliteit)De leerlingen leggen aan de hand van concrete maatschappelijke uitdagingen de wisselwerking tussen STEM-disciplines onderling en tussen STEM-disciplines met de maatschappij uit.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Met inbegrip van context
&nbsp;&nbsp;&nbsp;&nbsp;* Contexten zoals klimaatverandering, hernieuwbare energie, zorg en gezondheid, onderwijs, watervoorziening, mobiliteit, leefbare en duurzame steden, oceaanvervuiling komen aan bod.
&nbsp;&nbsp;&nbsp;&nbsp;* De duurzame ontwikkelingsdoelen zoals geformuleerd door de internationale gemeenschap worden aangereikt (SDG's, sustainable development goals).

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau begrijpen

<span style="color: yellowgreen">(13.3 Finaliteit doorstroom; 13.3 Dubbele finaliteit) De leerlingen zetten een geschikte zoekstrategie in bij het selecteren van digitale en niet-digitale bronnen om een informatievraag te beantwoorden.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau analyseren

<span style="color: yellowgreen">(13.5 Finaliteit doorstroom; 13.5 Dubbele finaliteit) De leerlingen beoordelen digitale en niet-digitale bronnen en informatie op betrouwbaarheid, correctheid en bruikbaarheid in functie van een informatievraag en aan de hand van criteria.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau evalueren

<span style="color: yellowgreen">(13.9 Finaliteit doorstroom; 13.9 Dubbele finaliteit) De leerlingen stellen verwerkte informatie voor volgens een zelf gekozen digitale en een niet-digitale presentatievorm.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau toepassen

<span style="color: yellowgreen">(13.10 Finaliteit doorstroom; 13.10 Dubbele finaliteit) De leerlingen beheren zelf op structurele wijze informatie digitaal en niet-digitaal.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau toepassen


<span style="color: yellowgreen">(13.11 Finaliteit doorstroom; 13.11 Dubbele finaliteit) De leerlingen formuleren, na analyse van een aangereikt probleem, een onderzoeksvraag en een hypothese.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau creëren

<span style="color: yellowgreen">(13.12 Finaliteit doorstroom; 13.12 Dubbele finaliteit) De leerlingen voeren een onderzoekstechniek uit om digitale en niet-digitale gegevens te verwerven in functie van een onderzoeksvraag.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau toepassen

<span style="color: yellowgreen">(13.13 Finaliteit doorstroom; 13.13 Dubbele finaliteit) De leerlingen voeren een zelfgekozen en geschikte oplossingsstrategie uit in functie van een onderzoek of een probleem.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau evalueren

<span style="color: yellowgreen">(13.14 Finaliteit doorstroom; 13.14 Dubbele finaliteit) De leerlingen formuleren een conclusie bij een onderzoeksvraag en een antwoord op een hypothese op basis van eigen onderzoeksresultaten.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Cognitieve dimensie: beheersingsniveau creëren
