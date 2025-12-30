---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: "R\xE9seau r\xE9sistant aux temp\xEAtes: Cr\xE9er une abstraction"
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct05_06
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
title: "R\xE9seau r\xE9sistant aux temp\xEAtes : Cr\xE9er une abstraction"
version: 3
---
# Exemple 6 : Créer une abstraction
Source : [la plateforme en ligne du concours Bebras belge](https://bebras.ugent.be/)<br>
Texte : Zoltán Molnár, HU, Zsuzsa Pluhár, HU<br>
Images : Ivo Blöchliger, CH<br>
Traduction : Kris Coolsaet 

## Réseau résistant aux tempêtes (Bebras 2014-HU-02) 

L'opérateur GSM Bever Telecom souhaite installer des antennes-relais GSM sur Windeneiland.<br>
La zone de couverture d'une antenne est un cercle centré sur celle-ci. Deux antennes sont dites reliées l'une à l'autre si leurs zones de couverture se chevauchent. Deux antennes peuvent communiquer entre elles s'il existe une chaîne d'antennes intermédiaires telle que chaque antenne soit reliée à la suivante.<br>
En raison des vents violents sur l'île, il arrive qu'une antenne casse. Si une antenne cesse de fonctionner quelque part, nous voulons que toute paire des antennes restantes puisse encore communiquer entre elles.

Laquelle des configurations ci-dessous devons-nous utiliser pour cela ?

![Réseau résistant aux tempêtes](embed/bebrasabstractie.png "Bebras Créer une abstraction")

---

#### Solution

La bonne réponse est B. 

![Réseau résistant aux tempêtes](embed/bebrasabstractieoplossing.png "Solution du réseau résistant aux tempêtes Bebras")

#### Discussion

Dans les configurations illustrées, les antennes sont représentées par des points et les zones de couverture par des cercles. C'est une première **abstraction** que vous devez interpréter correctement.

Pour parvenir à une solution, vous introduisez une **abstraction supplémentaire** en remplaçant les cercles qui se chevauchent par une arête dans un graphe : vous reliez deux antennes lorsque les cercles correspondants se chevauchent, et vous supprimez les cercles. C'est une étape cruciale du processus de résolution.

L'abstraction peut donc intervenir de deux manières différentes dans la pensée computationnelle :
- savoir interpréter correctement une abstraction donnée ;
- produire vous-même une abstraction pour résoudre un problème plus facilement.