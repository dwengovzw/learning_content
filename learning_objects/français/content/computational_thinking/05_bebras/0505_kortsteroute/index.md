---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: T
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct05_05
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
title: 'Plus court chemin : Concevoir un algorithme'
version: 3
---
# Exemple 5 : Concevoir un algorithme
Source : [la plateforme en ligne du concours belge Bebras](https://bebras.ugent.be/)<br>
Texte : Yukio Idosaka, JP, Yasushi Kuno, JP, Elena Sutkute, LT, Juha Vartiainen, FI, Barbara Müllner, AT<br>
Illustrations : Maiko Shimabuku, JP, Javier Bilbao, ES<br>
Traduction : Kris Coolsaet et Natacha Gesquière

## Chemin le plus court (Bebras 2013-JP-10)

Le petit castor aime jouer dans le parc. Sa maison (H) et le parc (P) sont reliés par des ponts, faits de troncs d’arbres de même longueur, comme tu peux le voir sur la carte ci-dessous:

![Chemin le plus court](embed/bebrasalgoritmebedenken.png "Concevoir un algorithme Bebras")

Il y a cependant quelques endroits sur la carte, indiqués par une croix rouge, qu’il ne peut pas franchir.

*Combien d’itinéraires différents de la maison vers le parc peut-il suivre ayant la même longueur minimale ?*

---

#### Solution

Il y a 18 itinéraires de même longueur minimale (à savoir 9 déplacements, 6 vers la droite et 3 vers le haut).

![Chemin le plus court](embed/bebrasalgoritmebedenkenoplossing.png "Solution du chemin le plus court Bebras")

Le nombre d’itinéraires possibles jusqu’à un certain carrefour est la somme du nombre d’itinéraires qui viennent de la gauche et de ceux qui viennent du bas. (Tu ne peux pas venir de la droite ni du haut, car il faudrait alors rebrousser chemin à un moment donné et le trajet ne serait plus de longueur minimale.)<br>
C’est pourquoi, en partant d’en bas à gauche, tu notes à chaque carrefour les nombres, et tu avances pas à pas vers la droite et vers le haut. Le nombre que tu écris alors en haut à droite est la réponse finale.

#### Discussion

La solution comporte deux étapes de réflexion :
- premièrement, réaliser que, dans un chemin le plus court, tu ne te déplaces jamais vers la gauche ni vers le bas ;
- deuxièmement, il suffit donc de ne considérer que de tels trajets.

Contrairement aux exemples 2 et 4, tu dois ici élaborer toi-même un **algorithme** pour arriver à la solution : il te faut imaginer une méthode systématique pour y parvenir. <br>
L’*approche brute*, c.-à-d. essayer toutes les possibilités en espérant n’en oublier aucune, ne fonctionne pas ; il est vraiment nécessaire de concevoir une méthode systématique pour résoudre ce problème (autrement dit, un algorithme).<br>
Dans cet exemple : travailler de l’angle inférieur gauche vers l’angle supérieur droit, et noter à chaque tronc combien de chemins y mènent.

Remarque que tu as ici besoin d’une pensée algorithmique, mais que tu n’as pas besoin de programmer !

La technique que tu utilises pour résoudre cet exercice s’appelle la *programmation dynamique* : tu divises ton problème en plus petits sous-problèmes faciles à résoudre. Dans ce cas, le sous-problème est « combien de chemins mènent au carrefour sur lequel nous travaillons ? ». Ce nombre dépend du nombre de chemins vers le carrefour d’où tu viens. Tu commences donc en bas à gauche et tu avances pas à pas vers la droite et vers le haut, en notant à chaque carrefour les nombres jusqu’à arriver en haut à droite.<br>
*Peut-être avais-tu déjà de l’expérience avec ce genre de problèmes et as-tu reconnu que la programmation dynamique pourrait rapidement mener à la solution ici.*