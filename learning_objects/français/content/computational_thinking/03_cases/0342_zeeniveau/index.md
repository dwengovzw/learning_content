---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Niveau de la mer - ligne de tendance
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct03_42
keywords:
- ''
language: fr
licence: dwengo
return_value:
  callback_schema:
    att: test
    att2: test2
  callback_url: callback-url-example
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
target_ages:
- 12
- 13
- 14
teacher_exclusive: true
title: Niveau de la mer - ligne de tendance (2,3)
version: 3
---
# Évolution du niveau de la mer à Ostende

**Visualisation d'un nuage de points et d'une droite de tendance.**

*Dans le contexte du changement climatique, les élèves travaillent avec de « vraies » données. Ils partent d'un défi. Ils doivent rechercher eux-mêmes les données, les visualiser à l'aide d'un nuage de points et rechercher une éventuelle droite de tendance.*

**Public cible :** 
* 2e ou 3e degré - finalité double
* 2e ou 3e degré - finalité de transition

**Discipline :** 
* Mathématiques - Sciences - STEM
* Sciences informatiques

**Prérequis :** 
* Les élèves savent collecter des informations via Internet. 
* Les élèves savent que la forme du nuage de points indique une éventuelle droite de tendance. 
* Les élèves peuvent visualiser en Python un nuage de points et une droite de tendance. 

Un **déroulement** possible de l'étude de cas est le suivant :<br><br>

*Phase 1*<br>
<ul>
    <li>Les élèves font un brainstorming sur le problème.
    <li>Ils complètent déjà en partie le schéma des concepts de base.</li>
</ul>

*Phase 2*<br>
<ul>
    <li>Les élèves rassemblent via Internet des données sur le niveau de la mer à Ostende au cours des dernières décennies.</li>
</ul>

*Phase 3*<br>
<ul>
    <li>Les élèves visualisent les données dans un nuage de points. En raison de la taille du jeu de données, ils utilisent Python pour ce faire.
    <li>Ils complètent davantage le schéma des concepts de base.
    <li>Les élèves constatent que les données reflètent une tendance et que cette tendance peut être approchée par une relation linéaire.
    <li>Les élèves font générer une droite de tendance via une régression linéaire.
</ul>

![ct-schema](@learning-object/m_ct03_42/nl/3)


### Objectifs minimaux (Source : onderwijsdoelen.be)

<span style="color: yellowgreen">(06.06 Finalité de transition) Les élèves appliquent le théorème de Pythagore pour résoudre des problèmes géométriques dans le plan et dans l'espace.</span>

<span style="color: yellowgreen">(04.05 Finalité de transition; Finalité double, Finalité marché du travail) Les élèves analysent l'impact des systèmes numériques sur la société à partir des principes de la pensée computationnelle.</span>

Avec ce cas, vous mettez en pratique les principes de la pensée computationnelle. Vous travaillez donc en partie cet objectif final avec ce cas.

### Objectifs minimaux spécifiques (Source : onderwijsdoelen.be)

<span style="color: yellowgreen"><strong>Algorithmes et programmation</strong></span><br>
<span style="color: yellowgreen">(07.01.01 Finalité de transition) Les élèves programment des solutions conçues par eux-mêmes pour des problèmes concrets.</span><br>
Public cible : Sciences informatiques de soutien aux entreprises, Économie-Mathématiques, Grec-Mathématiques, Sciences de l'informatique et de la communication, Latin-Mathématiques, Sciences et ingénierie technologiques, Sciences-Mathématiques<br>
<span style="color: yellowgreen">(07.02.01) Les élèves programment des solutions conçues par eux-mêmes pour des problèmes concrets.</span>
Public cible : Sciences STEM biotechnologiques et chimiques, Sciences de la construction et du bois, Mécatronique

### Objectifs finaux annulés (Source : onderwijsdoelen.be)
<span style="color: yellowgreen">(4.5 Finalité de transition) Les élèves conçoivent des algorithmes pour résoudre des problèmes de manière numérique.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise créer

<span style="color: yellowgreen">(4.5 Finalité double) Les élèves résolvent numériquement un problème délimité en adaptant un algorithme fourni. </span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise créer

<span style="color: yellowgreen">(6.19 Finalité de transition) Les élèves étudient la relation entre deux grandeurs numériques dans un jeu de données à l'aide d'un nuage de points.
</span>
&nbsp;&nbsp;&nbsp;&nbsp;Avec les TIC
&nbsp;&nbsp;&nbsp;&nbsp;Établir et interpréter un nuage de points
&nbsp;&nbsp;&nbsp;&nbsp;Déterminer et interpréter la droite de tendance avec son équation correspondante 
&nbsp;&nbsp;&nbsp;&nbsp;Déterminer et interpréter le coefficient de corrélation dans le cas d'une relation linéaire

&nbsp;&nbsp;&nbsp;&nbsp;L'objectif final est réalisé avec et sans contexte.

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise analyser

<span style="color: yellowgreen">(6.9.1 Objectifs de césure Techniques biotechnologiques) Les élèves étudient la relation entre deux grandeurs numériques dans un jeu de données à l'aide d'un nuage de points.
</span>
&nbsp;&nbsp;&nbsp;&nbsp;Avec les TIC
&nbsp;&nbsp;&nbsp;&nbsp;Établir et interpréter un nuage de points
&nbsp;&nbsp;&nbsp;&nbsp;Déterminer et interpréter la droite de tendance avec son équation correspondante 

&nbsp;&nbsp;&nbsp;&nbsp;L'objectif final est réalisé dans un contexte.

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise analyser


<span style="color: yellowgreen">(6.53 Finalité de transition) Les élèves appliquent une méthode scientifique pour développer des connaissances et répondre à des questions.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise analyser

<span style="color: yellowgreen">(12.3.1 Objectifs de césure Sciences biotechnologiques) Les élèves appliquent une méthode scientifique pour développer des connaissances et répondre à des questions.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise appliquer
    
<span style="color: yellowgreen">(6.54 Finalité de transition; 6.30 Finalité double) Les élèves analysent des systèmes naturels et techniques à l'aide de différents concepts STEM. </span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise analyser

<span style="color: yellowgreen">(6.55 Finalité de transition; 6.31 Finalité double) Les élèves conçoivent une solution à un problème en mobilisant de manière intégrée des concepts et des pratiques provenant de différentes disciplines STEM.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Y compris le contexte
&nbsp;&nbsp;&nbsp;&nbsp;* Chaque discipline STEM est abordée au moins une fois de manière intégrée.

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise créer

<span style="color: yellowgreen">(6.57 Finalité de transition)Les élèves étudient, à partir de défis sociétaux concrets, les interactions entre les disciplines STEM entre elles et entre les disciplines STEM et la société.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Y compris le contexte
&nbsp;&nbsp;&nbsp;&nbsp;* Des contextes tels que le changement climatique, les énergies renouvelables, les soins et la santé, l'éducation, l'approvisionnement en eau, la mobilité, des villes vivables et durables et la pollution des océans sont abordés.
&nbsp;&nbsp;&nbsp;&nbsp;* Les objectifs de développement durable tels que formulés par la communauté internationale sont proposés (ODD, sustainable development goals).

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise analyser

<span style="color: yellowgreen">(6.33 Finalité double)Les élèves expliquent, à partir de défis sociétaux concrets, les interactions entre les disciplines STEM entre elles et entre les disciplines STEM et la société.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Y compris le contexte
&nbsp;&nbsp;&nbsp;&nbsp;* Des contextes tels que le changement climatique, les énergies renouvelables, les soins et la santé, l'éducation, l'approvisionnement en eau, la mobilité, des villes vivables et durables et la pollution des océans sont abordés.
&nbsp;&nbsp;&nbsp;&nbsp;* Les objectifs de développement durable tels que formulés par la communauté internationale sont proposés (ODD, sustainable development goals).

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise comprendre

<span style="color: yellowgreen">(13.3 Finalité de transition; 13.3 Finalité double) Les élèves mettent en œuvre une stratégie de recherche appropriée lors de la sélection de sources numériques et non numériques pour répondre à une demande d'information.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise analyser

<span style="color: yellowgreen">(13.5 Finalité de transition; 13.5 Finalité double) Les élèves évaluent des sources et informations numériques et non numériques quant à leur fiabilité, leur exactitude et leur utilité en fonction d'une demande d'information et à l'aide de critères.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise évaluer

<span style="color: yellowgreen">(13.9 Finalité de transition; 13.9 Finalité double) Les élèves présentent l'information traitée selon une forme de présentation numérique et non numérique de leur choix.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise appliquer

<span style="color: yellowgreen">(13.10 Finalité de transition; 13.10 Finalité double) Les élèves gèrent eux-mêmes de manière structurée l'information numérique et non numérique.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise appliquer


<span style="color: yellowgreen">(13.11 Finalité de transition; 13.11 Finalité double) Les élèves formulent, après analyse d'un problème fourni, une question de recherche et une hypothèse.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise créer

<span style="color: yellowgreen">(13.12 Finalité de transition; 13.12 Finalité double) Les élèves mettent en œuvre une technique d'enquête afin d'acquérir des données numériques et non numériques en fonction d'une question de recherche.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise appliquer

<span style="color: yellowgreen">(13.13 Finalité de transition; 13.13 Finalité double) Les élèves mettent en œuvre une stratégie de résolution choisie et pertinente en fonction d'une recherche ou d'un problème.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise évaluer

<span style="color: yellowgreen">(13.14 Finalité de transition; 13.14 Finalité double) Les élèves formulent une conclusion à une question de recherche et une réponse à une hypothèse sur la base de leurs propres résultats de recherche.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive : niveau de maîtrise créer