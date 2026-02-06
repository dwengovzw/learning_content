---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Empreintes digitales
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: aiz_vingerafdrukken
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
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: true
title: Empreintes digitales
version: 3
---
# Empreintes digitales

**Prérequis:** Les élèves savent ce qu’est un graphe, des nœuds et des arêtes. Un nouveau type de graphes est introduit ici, à savoir le graphe coloré et pondéré. 

### Science forensique
La science forensique est d’une grande importance pour l’application de la loi. Pensez à la technologie ADN, aux analyses chimiques, à l’examen des traces provoquées par des balles, et à l’analyse ou l’identification des empreintes digitales.

Dans cette partie du parcours d’apprentissage, tu examines de près les empreintes digitales. 

### Empreinte digitale
Une empreinte digitale est le motif de lignes qu’un bout de doigt laisse lorsqu’il entre en contact avec une surface. Les empreintes digitales sont uniques à chaque personne et restent inchangées tout au long de la vie. Même des jumeaux identiques peuvent être distingués grâce à elles. Il faut toutefois tenir compte du fait qu’avec la croissance les motifs s’agrandissent également et que les empreintes peuvent changer à la suite d’une maladie ou d’un accident. Avec l’âge, les lignes peuvent aussi devenir moins nettes. Environ 300 ans avant J.-C., on utilisait déjà les empreintes digitales en Chine pour identifier des personnes. Aux États-Unis et en Europe, on ne s’y est mis qu’au XIXe siècle.

La peau à l’intérieur et au bout des doigts présente certains motifs: les lignes de la peau et les espaces entre elles forment des boucles (loops), des arches (arches) et des tourbillons (whorls). Ces motifs se forment pendant les phases embryonnaire et fœtale d’un nouvel être humain.
En raison de la manière dont la peau des bouts des doigts se forme, il apparaît au sein de ces motifs des points caractéristiques (minutiae): deltas, fourches ou bifurcations (bifurcations), îlots ou points (islands, dots), terminaisons de crêtes (ridge endings), croisements (crossovers), bifurcations vers le haut et vers le bas (spurs, hooks), et yeux sur la ligne (lake, eye). Ceux-ci sont visibles sur les empreintes digitales. Sur des empreintes de haute qualité, on peut regarder encore plus en détail et observer les pores et les glandes sudoripares. 

![image](https://user-images.githubusercontent.com/48352335/211288516-0e8ed701-31aa-41da-b22a-979a653cca1a.png)<br>
Figure: Matériel de cours d’exemple du projet CSI, module f. https://www.slo.nl/thema/meer/doorstroom-vmbo/algemene/werken-algemene/3e-leerjaar/

![Fingerprints_Minutiae_Patterns_Representation](https://user-images.githubusercontent.com/48352335/211396289-098e5e5a-516c-41ea-9f83-b86935676b56.jpg)<br>
Figure: Les motifs de minuties d’empreintes digitales les plus courants. Inaki Rom, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons.

Ainsi, lorsqu’on étudie des empreintes digitales, on examine d’abord les boucles, arches et tourbillons. Ensuite, on analyse plus en détail en observant les points caractéristiques. 

### L’utilisation des empreintes digitales
Les empreintes digitales sont utilisées pour identifier des personnes, p. ex. l’auteur d’un délit, ou pour l’authentification, l’accès à un smartphone. 

### Pensée computationnelle
Exemple: En raison de la grande quantité d’empreintes digitales, il est devenu impossible pour le FBI d’essayer d’associer rapidement une empreinte entrante à l’une des empreintes de sa base de données. La nécessité d’automatiser s’est imposée. L’ordinateur a été la solution.<br>
Il valait mieux que les fichiers numériques ne soient pas trop volumineux en termes de capacité de stockage. En outre, il fallait aussi pouvoir envoyer les fichiers partout dans le pays; ils ne devaient donc pas être trop volumineux non plus. 

![vingerafdrukschema](https://user-images.githubusercontent.com/48352335/211395837-e8001d34-f79f-49f3-8e43-d6d824601976.png)

**Activité sans ordinateur:** <br>
Source: https://ccicada.org/education/ccicada-education-modules/#Fingerprint <br>
- Sur une photo agrandie d’une empreinte digitale, indiquer les minuties, déterminer leur type et mesurer la distance en cm. 
- Convertir cela en un graphe.
- Donner un ensemble aux élèves et leur faire appliquer la même démarche.
- Ensuite, donner une nouvelle empreinte aux élèves et voir s’ils trouvent un algorithme d’appariement.

![image](https://user-images.githubusercontent.com/48352335/211331634-cc6026fe-76a5-44b1-bdd7-5c0437b1f84a.png)<br>
Source: https://ccicada.org/education/ccicada-education-modules/#Fingerprint

Graphe coloré et pondéré:
- Les minuties sont les nœuds
- Colorer les nœuds: bifurcation verte, fin de crête rouge, croisement de crêtes jaune, double bifurcation bleue, spurs violet, ...
- Pondération: relier les nœuds (qui sont reliés entre eux par la même ligne) et attribuer un poids à l’arête, à savoir la distance entre les nœuds. 
(Autres possibilités: attribuer des coordonnées aux nœuds, noter comme poids le nombre de lignes traversées ...)

Débriefing: Quelles sont les limites de l’algorithme d’appariement? Comment l’améliorer? 

#### Objectifs d’apprentissage
- Appliquer les concepts de base des graphes à l’analyse des empreintes digitales.
- Développer par les élèves un algorithme pour faire correspondre des empreintes digitales (identifier une empreinte donnée à l’aide d’un jeu de données d’empreintes).
- Apprentissage par découverte et investigation, pensée critique et logique.
- Illustrer l’utilité des mathématiques.

Après cette partie, les élèves pourront …
- utiliser les concepts de base des graphes dans ce contexte
- caractériser des empreintes digitales
- abstraire des empreintes digitales en un graphe
 -analyser des empreintes digitales à l’aide de graphes
- développer un algorithme qui fasse correspondre une empreinte digitale à un graphe 
- développer un algorithme pour apparier une empreinte donnée avec une empreinte d’un jeu de données
- avoir amélioré leur pensée critique et logique

#### Objectifs finaux
Graphes, pensée computationnelle, interaction entre la société et les STEM, éducation aux médias, vie privée.