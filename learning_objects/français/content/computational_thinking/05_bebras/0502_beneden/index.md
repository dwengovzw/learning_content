---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: 'Vers le bas : Appliquer l''algorithme'
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct05_02
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
title: 'Vers le bas : Appliquer l''algorithme'
version: 3
---
# Exemple 2 : Appliquer un algorithme
Source : [la plateforme en ligne du concours belge Bebras](https://bebras.ugent.be/)<br>
Texte : Mathias Hiron, FR<br>
Images : inconnu<br>
Traduction : Kris Coolsaet 

## Vers le bas (Bebras 2012-FR-10)
Madame Castor a placé un robot en haut d’un labyrinthe. Le robot descend le labyrinthe d’une plate-forme à la suivante en dessous, jusqu’à atteindre l’une des cases tout en bas. Pour ce faire, il se déplace toujours de la même manière : il part d’abord vers la droite et, chaque fois qu’il tombe d’une plate-forme vers le bas, il repart dans la direction opposée.

L’image de gauche ci-dessous montre la trajectoire que le robot suivra dans le labyrinthe n° 1.

![Vers le bas](embed/bebrasalgoritme.png "Algorithme Bebras")

*Si Madame Castor place son robot tout à gauche dans le labyrinthe n° 2, dans quelle case le robot finira-t-il par tomber ?*

---

#### Solution

![Vers le bas](embed/bebrasalgoritmeoplossing.png "Solution Vers le bas de Bebras")

On trouve la solution en exécutant l’**algorithme** donné.

#### Discussion

Le robot se déplace selon un **algorithme** donné. Il faut comprendre cet algorithme et l’appliquer au deuxième labyrinthe. 

L’algorithme peut être décrit comme suit : 

<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace; font-size:12px;">
Répétez les quatre lignes suivantes, tant que vous n’êtes pas arrivé en bas :<br>
&nbsp;&nbsp;&nbsp;&nbsp;Avancez dans la direction actuelle, puis<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tombez vers le bas jusqu’à la prochaine plate-forme, puis<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Inversez la direction actuelle
</p>
</div>

Il existe différentes manières d’appliquer la pensée algorithmique dans un processus de pensée computationnelle. Dans cet exemple, la pensée algorithmique apparaît sous sa forme la plus simple. Dans les autres exemples, vous ferez connaissance avec d’autres formes de pensée algorithmique.

Applications possibles :
- savoir appliquer un algorithme donné (exemple 2, exemple 4) ;
- concevoir soi-même un algorithme pour parvenir à une solution de manière efficace (exemple 5).

Une voie intermédiaire pour laquelle il n’y a (pas encore) d’exemple ici :  
- appliquer un algorithme (généralement) connu pour résoudre un problème.<br>
Cette voie intermédiaire nécessite une forme de reconnaissance de motifs. En sont des exemples : savoir rendre la monnaie en utilisant le moins possible de billets et de pièces, savoir résoudre une équation linéaire à une inconnue...