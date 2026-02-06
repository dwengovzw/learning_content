---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: 'Impressions de hasard: Abstraction et algorithme'
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct05_07
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
title: 'Estampes du hasard: Abstraction et algorithme'
version: 3
---
# Exemple 7 : Abstraction et algorithme
Source : [la plateforme en ligne du concours belge Bebras](https://bebras.ugent.be/)<br>
Texte : Michael Weigend, DE<br>
Images : Michael Weigend, DE<br> 
Traduction : Kris Coolsaet

## Images aléatoires (Bebras 2013-DE-02)

Les castors ont une petite entreprise qui conçoit des cartes de vœux et du papier cadeau personnalisés. Les différents modèles sont réalisés selon les instructions suivantes :

1. Créer un cercle C d'une couleur aléatoire.
2. Répéter les étapes suivantes un nombre aléatoire de fois.<br>
&nbsp;&nbsp;&nbsp;&nbsp;1. Créer un carré V d'une couleur et d'une taille aléatoires.<br>
&nbsp;&nbsp;&nbsp;&nbsp;2. Choisir une taille aléatoire pour C : soit *petite*, soit *grande*.<br>
&nbsp;&nbsp;&nbsp;&nbsp;3. Imprimer C à un endroit aléatoire.<br>
&nbsp;&nbsp;&nbsp;&nbsp;4. Imprimer V à un endroit aléatoire.<br>

(Pour information : créer une forme signifie que la forme est créée dans la mémoire de l'ordinateur, mais cela ne veut pas dire qu'elle est également imprimée ou dessinée sur papier.)

*Lequel des modèles suivants n'a pas été conçu par cette entreprise ?*

![Images aléatoires](embed/bebrasabstractie2.png "Image aléatoire Bebras")

---

#### Solution

Le modèle suivant ne peut pas avoir été réalisé par cette entreprise :

![Images aléatoires](embed/bebrasabstractie2oplossing.png "Solution de l'image aléatoire Bebras")

#### Discussion

Cette image contient deux cercles de tailles différentes et de couleurs différentes. Dans l'algorithme, la couleur du cercle n'est déterminée qu'une seule fois, à savoir tout au début ; ensuite, les cercles peuvent encore changer de taille, mais pas de couleur.<br>
Toutes les autres réponses sont des conceptions possibles, même si cela n'est pas forcément évident. Il faut imprimer autant de cercles que de carrés, mais il est tout à fait possible qu'un carré soit imprimé par-dessus un cercle et le cache ainsi ! N'oubliez pas non plus qu'un cercle ou un carré peut par hasard avoir la même couleur que l'arrière-plan.

Il faut être capable d'appliquer l'**algorithme** de manière suffisante. Si vous voyez que tous les cercles doivent avoir la même couleur, vous avez fait une **abstraction** des instructions de l'**algorithme**. Savoir que tous les cercles doivent avoir la même couleur est la seule chose qui importe pour pouvoir répondre à la question posée. En fait, vous n'utilisez qu'une partie de l'algorithme.