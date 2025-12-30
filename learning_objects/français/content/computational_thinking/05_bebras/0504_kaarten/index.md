---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: "Retourner des cartes: Appliquer un algorithme et reconna\xEEtre un motif"
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct05_04
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
title: "Retourner les cartes: Appliquer un algorithme et reconna\xEEtre un motif"
version: 3
---
# Exemple 4 : Appliquer un algorithme et reconnaître un motif
Source : [la plateforme en ligne du concours belge Bebras](https://bebras.ugent.be/)<br>
Texte : Kris Coolsaet, BE<br>
Images : Kris Coolsaet, BE
 
## Retourner des cartes (Bebras 2018-BE-01a)
Nous jouons au 'petit jeu' suivant. Devant toi se trouve une rangée de cartes. Une carte est soit avec le côté image vers le haut, soit avec le côté image vers le bas.

Une étape dans le 'jeu' se déroule de la manière suivante :<br>
Tu regardes les cartes de droite à gauche.<br>
Si la carte actuelle a le côté image vers le bas, alors tu retournes la carte côté image vers le haut et tu t'arrêtes.<br>
Si la carte actuelle a le côté image vers le haut, alors tu la retournes côté image vers le bas et tu continues avec la carte à sa gauche.<br>
Si tu as passé toutes les cartes, tu t'arrêtes.

L'image ci-dessous montre l'effet des étapes successives : tu retournes d'abord la carte tout à droite, puis la carte à sa gauche et ensuite la carte à la gauche de celle-ci. Et là tu dois t'arrêter, car la troisième carte est maintenant avec le côté image vers le haut.

![Retourner des cartes](embed/bebrasalgoritmepatroon.png "Algorithme Bebras et reconnaissance de motifs")

Le jeu commence avec 32 cartes, toutes avec le côté image vers le bas :

![Retourner des cartes](embed/bebrasalgoritmepatroonopgave.png "Algorithme Bebras et reconnaissance de motifs")

*Combien de cartes ont le côté image **vers le haut** après exactement 32 étapes du jeu ? (Répondez par un nombre.)*

---

#### Solution

![Retourner des cartes](embed/bebrasalgoritmepatroonoplossing.png "Bebras Retourner des cartes solution")

Remarque qu'après 1 étape, après 2, 4, 8 étapes, il y a chaque fois 1 carte avec le côté image vers le haut. Ce sont les étapes 2<sup>0</sup>, 2<sup>1</sup>, 2<sup>2</sup>, 2<sup>3</sup>, toutes des puissances de 2. 32 est aussi une puissance de 2. Après 32 étapes, il y a 1 carte avec le côté image vers le haut. 

#### Discussion

Remarque qu'ici encore tu exécutes un algorithme et ne l'inventes pas toi-même, comme dans l'exemple 2.
Outre le fait que tu dois exécuter un **algorithme**, il est aussi question ici de **reconnaissance de motifs**. Pendant l'exécution de l'algorithme, tu dois remarquer qu'il y a exactement une carte avec le côté image vers le haut après 1 étape, après 2 étapes, après 4 étapes, puis chaque fois après le double du nombre d'étapes de la fois précédente. Le nombre d'étapes est donc toujours une puissance de 2. 32 est 2 à la puissance cinq, donc là aussi il y a une carte avec le côté image vers le haut. 

À l'intérieur d'un ordinateur, les nombres sont représentés dans ce qu'on appelle la notation binaire : un nombre est 'écrit' uniquement avec des uns et des zéros (appelés bits).<br>
Par ex. 1 est représenté comme 0...00001, 2 comme 0...00010, 3 comme 0...00011, 4 comme 0...00100, 5 comme 0...00101, 6 comme 0...00110, etc. (Les ordinateurs modernes utilisent souvent 32 bits pour représenter un nombre.)<br>
Reconnais-tu ces motifs ? Lorsque tu places pour le bit 0 une carte avec le côté image vers le bas, et pour le bit 1 avec le côté image vers le haut, tu obtiens les mêmes motifs que lors des 6 premières étapes de notre jeu. Si tu sais que la représentation binaire de 32 n'est rien d'autre que 0...01000000, alors tu vois qu'après 32 étapes il y a exactement une carte avec le côté image vers le haut.<br>
Ce que nous appelons une 'étape' dans cette énigme correspond à ce que l'électronique d'un ordinateur utilise pour augmenter un nombre binaire de 1.