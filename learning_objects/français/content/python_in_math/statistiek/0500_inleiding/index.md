---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Introduction
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: pim_statistiek_inleiding
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
- 15
- 16
- 17
- 18
teacher_exclusive: true
title: Introduction
version: 3
---
# Introduction

Prérequis pour ce parcours d'apprentissage : le parcours ['Travailler avec des notebooks'](https://www.dwengo.org/learning-path.html?hruid=pn_werking&language=nl&te=true&source_page=%2Fmath_with_python%2F&source_title=%20Python%20in%20de%20Wiskundeles#pn_werkingnotebooks;nl;3).

**Ce parcours d'apprentissage s'inscrit bien dans le nouvel objectif minimal spécifique concernant la statistique en troisième degré en lien avec les grands ensembles de données.**

Les trois premières parties relèvent de la statistique descriptive. La dernière partie établit un lien entre la statistique descriptive et la statistique explicative.

------

Un **complément** à ce parcours d'apprentissage est la statistique bivariée : la visualisation d'un **diagramme de dispersion ou nuage de points** et l'éventuelle détermination de la **droite de régression** associée. Voir à cet effet les parcours ['Diagramme de dispersion'](https://www.dwengo.org/learning-path.html?hruid=maths_spreidingsdiagrammen&language=nl&te=true&source_page=%2Fmath_with_python%2F&source_title=%20Python%20in%20de%20Wiskundeles#pn_inleiding_spreidingsdiagram;nl;3), ['Régression linéaire'](https://www.dwengo.org/learning-path.html?hruid=maths_lineaireregressie&language=nl&te=true&source_page=%2Fmath_with_python%2F&source_title=%20Python%20in%20de%20Wiskundeles#pn_inleiding_lineaireregressie;nl;3), ['Lignes de régression'](https://www.dwengo.org/learning-path.html?hruid=pn_regressie&language=nl&te=true&source_page=%2Fmath_with_python%2F&source_title=%20Python%20in%20de%20Wiskundeles#pn_voorkennis_regressielijnen;nl;3).

Une introduction au travail avec des listes NumPy dans le cadre de cours de statistique se trouve dans le deuxième notebook de cette [série](https://dwengo.org/backend/api/learningObject/getWrapped?hruid=pn_nplijsten&version=3&language=nl). Vous y travaillerez notamment avec la variance et l'écart-type.

Le prétraitement des données dans un DataFrame s'apprend dans ce [cet élément du parcours d'apprentissage 'Types de données'](https://dwengo.org/backend/api/learningObject/getWrapped?hruid=aiz_dataframe&version=3&language=nl).

------

### Objectif minimal grands ensembles de données

**Statistique**<br>
*Ces objectifs spécifiques sont valables dans les filières d'études suivantes : pédagogie Freinet, sciences humaines*

*06.01.05 Les élèves analysent de grands ensembles de données à l'aide de logiciels statistiques dans le cadre d'une recherche statistique.* <br>
*Note : Les grands ensembles de données sont soit fournis, soit construits par eux-mêmes (par exemple dans le cadre d'un projet). L'ensemble de données est suffisamment grand pour pouvoir formuler une réponse à la question de recherche.*

### Autres objectifs minimaux

#### Objectifs minimaux mathématiques deuxième degré - Finalité de transition

*06.18 Les élèves analysent des données statistiques à l'aide de modes de représentation et de mesures de tendance centrale et de dispersion.* <br>
*Éléments (de connaissance) sous-jacents : Modes de représentation : tableau de fréquences absolues et relatives, diagramme en barres, diagramme circulaire, diagramme linéaire, histogramme et boîte à moustaches. Mesures de tendance centrale et de dispersion : moyenne arithmétique, médiane, mode, étendue, écart interquartile et écart-type. Présentations trompeuses.*

*06.21 Les élèves décrivent des phénomènes de la réalité à l'aide de concepts mathématiques du deuxième degré.*

#### Objectifs minimaux mathématiques deuxième degré - Double finalité

*06.16 Les élèves analysent des données statistiques à l'aide de modes de représentation et de mesures de tendance centrale et de dispersion.* <br>
*Éléments (de connaissance) sous-jacents : Modes de représentation : tableau de fréquences absolues et relatives, diagramme en barres, diagramme circulaire, diagramme linéaire, histogramme et boîte à moustaches. Mesures de tendance centrale et de dispersion : moyenne arithmétique, médiane, étendue, écart interquartile. Présentations trompeuses.*

*06.17 Les élèves décrivent des phénomènes de la réalité à l'aide de concepts mathématiques du deuxième degré.*

#### Objectifs minimaux mathématiques troisième degré - Finalité de transition

*06.15 Les élèves expliquent, dans des situations concrètes, la différence entre corrélation et causalité.*

*06.16 Les élèves utilisent la loi normale comme modèle continu pour des données fournies.* <br>
*Éléments (de connaissance) sous-jacents : Évaluation graphique de l'applicabilité du modèle. La moyenne arithmétique et l'écart-type des données fournies comme estimation des paramètres du modèle. Interprétation graphique de la moyenne et de l'écart-type d'une variable aléatoire suivant une loi normale en termes de courbe de Gauss.*

*06.19 Les élèves décrivent des phénomènes de la réalité à l'aide de concepts mathématiques du troisième degré.*

*06.21 Les élèves utilisent les TIC pour effectuer des calculs et réaliser des représentations graphiques.* <br>
*Note de bas de page : en tenant compte des concepts du troisième degré.*

#### Objectifs minimaux mathématiques troisième degré - Double finalité

*06.08 Les élèves expliquent, dans des situations concrètes, la différence entre corrélation et causalité.*

*06.09 Les élèves utilisent la loi normale comme modèle continu pour des données fournies.* <br>
*Éléments (de connaissance) sous-jacents : Évaluation graphique de l'applicabilité du modèle. La moyenne arithmétique et l'écart-type des données fournies comme estimation des paramètres du modèle. Interprétation graphique de la moyenne et de l'écart-type d'une variable aléatoire suivant une loi normale en termes de courbe de Gauss.*

*06.11 Les élèves décrivent des phénomènes de la réalité à l'aide de concepts mathématiques du troisième degré.*

*06.13 Les élèves utilisent les TIC pour effectuer des calculs et réaliser des représentations graphiques.* <br>
*Note de bas de page : en tenant compte des concepts du troisième degré.*