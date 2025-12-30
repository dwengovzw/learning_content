---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: "\xC9quation du second degr\xE9"
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct03_38
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
title: "\xC9quation du second degr\xE9 (2,3)"
version: 3
---
# L'équation du second degré

**Automatiser la résolution d'une équation du second degré.**

Vous souhaitez programmer avec vos élèves en cours de mathématiques ? Ce thème s'y prête.

Avec vos élèves, vous construisez pas à pas une application pour automatiser la résolution d'une équation du second degré. Pas à pas, vous développez davantage l'application. 

Cette application peut ensuite être utilisée pour résoudre des problèmes. L'accent se porte alors davantage sur le problème et moins sur le calcul.

> Réduire un problème à l'équation du second degré à résoudre est une forme d'abstraction.

<div class="alert alert-box alert-warning">
Dans l'étude de cas sur le théorème de Pythagore, vous voyez comment élaborer progressivement une telle application, en partant de la pensée computationnelle.
</div>

Avec la programmation, vous allez aussi loin que vous le souhaitez. Dans cet exemple détaillé, nous abordons les variables, les types de données, les opérateurs, les expressions logiques et la structure conditionnelle, nous demandons une saisie à l'utilisateur et nous utilisons des fonctions intégrées et définies par l'utilisateur. Nous utilisons également des modules Python (bibliothèques) et accordons de l'attention à la rédaction de commentaires. <br>
> Si vous le souhaitez, vous pouvez encore améliorer l'application et travailler aussi avec des structures de répétition. Vous pouvez, par exemple, utiliser une boucle conditionnelle pour vérifier que le coefficient saisi de l'équation du second degré n'est pas nul.

**Public cible :** 2e degré - finalité de transition, 3e degré - double finalité

**Discipline :** Mathématiques

**Prérequis :** 
* Les élèves savent résoudre manuellement une équation du second degré. Ils connaissent les formules du discriminant et des racines.
* Les élèves connaissent une structure conditionnelle (ou elle peut être introduite collectivement ici).

![schéma CT](@learning-object/m_ct03_38/nl/3)

Selon que les élèves ont déjà été initiés à l'utilisation de fonctions dans un programme, la **reconnaissance de motifs et l'abstraction** peuvent être abordées dès le début ou plus tard. On peut travailler pas à pas. On peut d'abord écrire un programme sans appliquer la reconnaissance de motifs et l'abstraction mentionnées. Ce programme peut alors servir de point de départ pour utiliser une **fonction** définie par l'utilisateur et en expliciter les avantages.

---

Sous le thème de cours ['Python en cours de mathématiques'](https://www.dwengo.org/math_with_python/) vous trouverez dans le parcours d'apprentissage ['Paraboles'](https://www.dwengo.org/learning-path.html?hruid=maths_parabolen&language=nl&te=true&source_page=%2Fmath_with_python%2F&source_title=%20Python%20in%20de%20Wiskundeles#pn_voorkennis_parabolen;nl;3) un notebook Python où vous pouvez programmer ceci.

---

### Supplément

Vous pouvez, après coup, mettre les élèves au travail de manière autonome avec l'une des tâches suivantes :
* Écrivez une application analogue pour calculer le sommet d'une parabole.
* Écrivez une application analogue qui indique si une parabole coupe l'axe des x et si les points d'intersection se trouvent à gauche, à droite ou de part et d'autre de l'origine.
* Écrivez une application qui trace la courbe d'une parabole et y indique le sommet. Les paraboles ouvertes vers le haut apparaissent en vert et celles ouvertes vers le bas en bleu.