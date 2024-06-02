---
hruid: anm_1101
version: 3
language: nl
title: "Rij en limiet van een rij"
description: "Limiet rij"
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
# Rijen: terminologie

Met een rij wordt een oneindige rij van getallen bedoeld. De volgorde van de getallen in die rij is van belang en een getal kan meerdere keren in de rij voorkomen. Elk element in de rij heeft een index die overeenkomt met de positie van het element in de rij.

Om in Python met een rij aan de slag te gaan, is het datatype `list` (lijst) geschikt. In een lijst is de volgorde van de elementen immers van belang en wordt er ook met indices gewerkt. 

## Limiet van een rij

Een rij waarvan de termen naderen naar \\(+\infty\\), is <b>divergent</b>; de limiet van de rij is \\(+\infty\\).<br>Een rij waarvan de termen naderen naar \\(-\infty\\), is <b>divergent</b>; de limiet van de rij is \\(-\infty\\).<br> Er zijn ook rijen die naar een bepaald getal naderen; zo'n rij is <b>convergent</b>; de limiet van de rij is dat getal.<br> Rijen die noch naar \\(+\infty\\) of \\(-\infty\\), noch naar een bepaald getal naderen, zijn ook <b>divergent</b>; van deze rijen zegt men dat de limiet niet bestaat.  

## Rekenkundige rij

Beschouw de rij \\(u\\): \\(u = 2, 6, 10, 14, 18, 22, ...\\)<br>
De rij is gegeven door **opsomming** van de eerste zes **termen** van de rij.<br> De eerste term is \\(2\\) en door er telkens het *verschil* \\(4\\) bij op te tellen, worden de volgende termen bekomen. Zo'n rij wordt een **rekenkundige rij** genoemd. <br>
Elke term van de rij heeft een **index**. Zo is bijvoorbeeld \\(u_{0} = 2, u_{1} = 6\\), en \\(u_{3} =14\\).

Je kan de termen van de rij verder aanvullen.<br>
\\(u = 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, ...\\)<br>
Het is duidelijk dat de termen steeds groter worden en allemaal positief zijn. Het is een **stijgende rij**.<br>
Deze rij nadert naar \\(+\infty\\), of anders gezegd: de **limiet** van deze rij is \\(+\infty\\).<br>
Men zegt dat de rij *divergeert* of **divergent** is.

Je kan de rij \\(u\\) ook definiëren a.d.h.v. een **expliciet voorschrift**: 

\\(u_{n} = 2 + n \cdot 4 \\) met \\(n \in 	\mathbb{N}.\\)


De term \\(u_{n}\\) wordt **de algemene term** van de rij genoemd.

Dat deze rij naar \\(+\infty\\) nadert, kan je nu kort neerschrijven als \\(u_{n} \rightarrow +\infty\\).<br>
Men noteert: 

\\(\lim_{n \to +\infty} u_{n} = +\infty.\\)


## Meetkundige rij

Beschouw de rij \\(u\\): \\(u = -3, 6, -12, 24, -48, 96, ...\\)<br>
De rij is gegeven door **opsomming** van de eerste zes **termen** van de rij.<br> De eerste term is \\(-3\\) en door telkens te vermenigvuldigen met de *reden* \\(-2\\), worden de volgende termen bekomen. Zo'n rij wordt een **meetkundige rij** genoemd.

Wanneer je de termen van de rij verder aanvult, merk je dat de termen van de rij afwisselend positief en negatief zijn en steeds groter worden in absolute waarde. In absolute waarde naderen de termen van de rij naar \\(+\infty\\).  Omdat de rij **schommelt**, is het onmogelijk om te bepalen of de termen van de rij naar \\(+\infty\\) of naar \\(-\infty\\) naderen. De **limiet** van deze rij bestaat niet. De rij is **divergent**.

## Recursief voorschrift

In de plaats van een expliciet voorschrift zou je voor het definiëren van een rekenkundige of meetkundige rij ook een **recursief voorschrift** kunnen gebruiken:<br> De rekenkundige rij \\(u\\) waarvoor \\(u_{n} = 2 + n \cdot 4 \\) (met \\(n \in \mathbb{N}\\)) kan je ook als volgt definiëren: 

\\(u_{0} = 2  \\) en \\(u_{n} = u_{n-1} + 4 \\) met \\(n \in \mathbb{N}_{0}\\).


-----

# Notebooks
In de eerste notebook leren de leerlingen hoe ze in Python een rij kunnen definiëren, er enkele termen van laten berekenen en laten zien. Het begrip 'limiet van een rij' wordt er opgefrist. <br>
In de tweede notebook gaan ze aan de slag met deze opdracht:

Beschouw de harmonische rij \\(u_{n}=\frac{1}{n}\\).<br>
Bepaal naar welk getal \\(u_{n}\\) nadert bij heel grote waarden van \\(n\\).

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/hub/tmplogin?id=6510 "Limiet van een rij")
