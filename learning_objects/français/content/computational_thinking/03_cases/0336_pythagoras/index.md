---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: "Pythagore - hypot\xE9nuse"
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct03_36
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
title: "Pythagore - hypot\xE9nuse (2)"
version: 3
---
# Le théorème de Pythagore: calculer l’hypoténuse

**Automatiser le calcul de l’hypoténuse d’un triangle rectangle à partir de côtés de l’angle droit donnés.**

Vous souhaitez programmer avec vos élèves pendant le cours de mathématiques? Ce thème s’y prête bien.

Avec les élèves, vous construisez pas à pas une application pour automatiser les calculs liés au théorème de Pythagore. Vous partez d’un seul type d’exercice. Un deuxième type peut être réalisé de manière autonome par les élèves; cela permet de voir immédiatement s’ils ont tout compris. 

Un atout du théorème de Pythagore est que vous trouvez facilement des applications du monde réel.

Avec la programmation, vous allez aussi loin que vous le souhaitez. Dans cet exemple détaillé, on aborde les variables, les types de données et les opérateurs, on demande une entrée à l’utilisateur, et on utilise des fonctions intégrées et définies par l’utilisateur. Nous utilisons également des modules Python (bibliothèques) et accordons de l’attention à la rédaction de commentaires. Si souhaité, vous pouvez encore améliorer l’application et travailler aussi avec des structures de choix et de répétition. 

Ce cas est expliqué dans cette vidéo. 

![](@youtube/https://www.youtube.com/embed/ZUl27Ek9zHo "vidéo cas pythagore") 

### Objectif

**Automatiser le calcul de l’hypoténuse à partir de côtés de l’angle droit connus.** 

Une fois que les élèves disposent du programme, ils peuvent l’utiliser pour résoudre des problèmes complexes qui se ramènent au problème résolu ci-dessus. L’accent de la leçon peut alors être mis sur la modélisation mathématique du problème, après quoi la solution peut être déterminée à l’aide de l’ordinateur.

**Public cible:** 2e degré, double finalité ou finalité de transition

**Cours**: Mathématiques

### Étape 1: automatiser le calcul.

**Prérequis:** Les élèves connaissent le théorème de Pythagore sous forme de formule. À l’aide du théorème de Pythagore, ils peuvent calculer manuellement l’hypoténuse d’un triangle rectangle. 

![schéma-ct](@learning-object/m_ct03_36d/nl/3)

Dans cette vidéo, vous voyez pas à pas la partie programmation. 

![](@youtube/https://www.youtube.com/embed/oMFW-0mnAUU "démo cas pythagore") 

### Étape 2: demander une saisie à l’utilisateur.

**Prérequis:** Les élèves savent comment demander une entrée à l’utilisateur, ou ils peuvent l’apprendre ici. 

![schéma-ct](@learning-object/m_ct03_36a/nl/3)

<div class="alert alert-box alert-success">
    <strong>Objectif d’apprentissage en fonction de MD 04.05:</strong><br>
    Les élèves comprennent qu’il est important de rendre une application conviviale si l’on veut qu’elle soit utilisée. Des applications numériques plus conviviales auront un impact plus important.
</div>

### Étape 3: appliquer la reconnaissance de motifs et l’abstraction.

**Prérequis:** Les élèves ont éventuellement déjà appris à définir une fonction en Python, ou cela peut être introduit ici.

![schéma-ct](@learning-object/m_ct03_36b/nl/3)

### Application: distance à vol d’oiseau

**Prérequis:** Les élèves utilisent la fonction définie par l’utilisateur dans un exercice avec contexte.

**Défi: "New York. Quelle est la distance à vol d’oiseau de Times Square à l’Empire State Building, exprimée en kilomètres?"**

*Les élèves imaginent eux-mêmes qu’ils peuvent utiliser un planificateur d’itinéraire et le théorème de Pythagore.*

![schéma-ct](@learning-object/m_ct03_36c/nl/3)

<div class="alert alert-box alert-success">
<strong>Objectif d’apprentissage en fonction de MD 04.05:</strong><br> 
<ul>
    <li>Une des raisons pour lesquelles les planificateurs d’itinéraire sont autant utilisés et ont donc un tel impact est leur convivialité. Si un planificateur d’itinéraire est si convivial, c’est grâce au haut degré d’abstraction dans le planificateur: l’itinéraire est abstrait en nombre de kilomètres et en changements de direction à temps; si vous le souhaitez, vous pouvez simplement suivre les instructions de la route à emprunter (le plan par étapes ou l’algorithme). Vous ne devez pas vous soucier de chercher la route sur une carte, en tenant compte par exemple du sens unique, de l’orientation de la carte, etc. </li>
    <li>De plus, vous obtenez des informations supplémentaires sur, p. ex., les embouteillages, les travaux routiers, où faire le plein, etc. </li>  
    <li>Parce que tant de choses sont abstraites dans les planificateurs d’itinéraire, vous n’avez plus une vision complète de l’environnement. Cela peut aussi être un inconvénient par rapport à une carte papier qui donne beaucoup plus de détails sur l’environnement et situe en outre un lieu donné dans une zone plus vaste. Les planificateurs d’itinéraire érodent en quelque sorte la conscience spatiale autour d’un lieu. Être trop dépendant des planificateurs d’itinéraire numériques peut donc aussi être dangereux: par exemple, des gens montent sur une voie ferrée ou sur un escalier. </li>
    <li>Lors de l’utilisation d’un planificateur d’itinéraire, vous devez tenir compte du fait que vous pouvez vous retrouver dans une zone sans couverture mobile, ou que la batterie de votre smartphone peut se décharger. </li>
    <li>Vous devez également tenir compte du fait que certaines zones peuvent être insuffisamment détaillées ou imprécises. Et que les planificateurs d’itinéraire numériques peuvent contenir des erreurs, comme une vitesse maximale erronée autorisée sur une route donnée ou une rue à sens unique indiquée comme étant à double sens. </li>
    <li>Les planificateurs d’itinéraire ont un impact sur la société: L’utilisation d’un planificateur d’itinéraire par tant de personnes peut avoir des effets indésirables, comme un trafic supplémentaire dans les quartiers résidentiels lorsqu’un planificateur détourne la circulation automobile par ces quartiers pour éviter les embouteillages. La question est de savoir combien d’aspects de l’environnement l’algorithme du planificateur d’itinéraire prend en compte. Il est peut-être abstrait dans les données d’entrée qu’un certain environnement est un quartier résidentiel, ou cette variable n’est pas prise en compte dans le programme. Les planificateurs d’itinéraire peuvent contenir de la publicité: Comment est déterminé, en effet, quelles boutiques, quelles stations-service... sont affichées dans le planificateur? Les planificateurs d’itinéraire ont conduit à de nouvelles applications dans la société, comme des robots qui livrent des courses à domicile et des drones médicaux; à l’aide de techniques de planification spécifiquement conçues pour les drones, ils trouvent leur chemin. L’utilisation d’un planificateur d’itinéraire peut également soulever des questions de confidentialité: Si les emplacements des utilisateurs sont enregistrés, la question se pose de savoir ce que le fournisseur du planificateur fait de ces données. </li>
</ul>
</div>

### Étape suivante: appliquer la reconnaissance de motifs et l’abstraction

Les élèves du deuxième degré sont initiés, en cours de mathématiques, au théorème de Pythagore. Deux types d’exercices se distinguent:<br> 
-  soit les côtés de l’angle droit d’un triangle rectangle sont donnés et il faut calculer l’hypoténuse;
-  soit l’hypoténuse et un côté de l’angle droit sont donnés et il faut calculer l’autre côté de l’angle droit.

Les élèves ont construit une application pour effectuer les calculs dans un exercice du premier type. Dans l’application, une fonction définie par l’utilisateur `pythagoras1()` est utilisée.<br>  
Un complément à ce cas serait que les élèves ajoutent une deuxième fonction `pythagoras2()`, de sorte que l’application puisse effectuer les calculs des deux types.
À partir de ce moment, une série de problèmes peut être proposée aux élèves, qui devront surtout faire de la reconnaissance de motifs et utiliser chaque fois l’application pour les calculs.

<div class="alert alert-box alert-info">
<strong>Remarque concernant la dénomination des fonctions définies par l’utilisateur:</strong><br>
Il est préférable d’adapter les noms des fonctions afin qu’ils indiquent directement ce que font les fonctions. Au lieu de <code>pythagoras1()</code>, il vaut mieux utiliser <code>bereken_schuine_zijde_uit_rechthoekszijden()</code> comme nom de fonction. Par analogie, adaptez le nom <code>pythagoras2()</code> en <code>bereken_rechthoekszijde_uit_schuine_zijde_en_rechthoekszijde()</code>.<br>
Si vous souhaitez que la fonction soit également utilisable pour ceux qui ne sont pas familiers avec les notations standard <em>a, b</em> et <em>c</em> du cours de mathématiques, il est préférable d’adapter aussi les paramètres des fonctions. De meilleurs noms encore pour les fonctions sont donc <code>bereken_schuine_zijde(rechthoekszijde_1, rechthoekszijde_2)</code> et <code>bereken_rechthoekszijde(schuine_zijde, rechthoekszijde)</code>.
</div>

----------------------------------------------------
### Objectifs minimaux (Source: onderwijsdoelen.be)

<span style="color: yellowgreen">(06.06 Finalité de transition) Les élèves appliquent le théorème de Pythagore pour résoudre des problèmes géométriques dans le plan et dans l’espace.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Note: <br>
&nbsp;&nbsp;&nbsp;&nbsp;‘Dans l’espace’: p. ex. une diagonale de l’espace dans un cube ou un pavé où les élèves doivent choisir deux fois le plan adéquat.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Il est recommandé de travailler à la fois avec et sans contexte. Travailler avec des contextes peut en effet motiver les élèves. Apprendre les mathématiques avec et sans contextes est important pour transférer connaissances et compétences vers des situations similaires et nouvelles.

<span style="color: yellowgreen">(06.06 Double finalité) Les élèves appliquent le théorème de Pythagore pour résoudre des problèmes géométriques dans le plan.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Note: <br>
&nbsp;&nbsp;&nbsp;&nbsp;La résolution de problèmes géométriques dans le plan peut également concerner des situations spatiales, à savoir celles dans lesquelles les élèves doivent choisir une fois le plan adéquat. P. ex. l’échelle posée contre un mur, l’armoire IKEA qui doit rentrer dans un espace. <br>
&nbsp;&nbsp;&nbsp;&nbsp;Il est recommandé de travailler à la fois avec et sans contexte. Travailler avec des contextes peut en effet motiver les élèves. Apprendre les mathématiques avec et sans contextes est important pour transférer connaissances et compétences vers des situations similaires et nouvelles.

<span style="color: yellowgreen">(06.52 Finalité de transition) Les élèves conçoivent une solution à un problème en mobilisant de façon intégrée les sciences, la technologie ou les mathématiques.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Note:<br>
&nbsp;&nbsp;&nbsp;&nbsp;STEM signifie par définition que vous pensez de manière intégrée. Le degré d’intégration dépend du problème. <br>
&nbsp;&nbsp;&nbsp;&nbsp;Des disciplines non-STEM peuvent également être abordées.<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;Note de bas de page: En tenant compte des concepts du deuxième degré et du contexte dans lequel cet objectif minimal est abordé.

<span style="color: yellowgreen">(06.36 Double finalité) Les élèves conçoivent une solution à un problème en mobilisant de façon intégrée les sciences, la technologie ou les mathématiques.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Note:<br>
&nbsp;&nbsp;&nbsp;&nbsp;STEM signifie par définition que vous pensez de manière intégrée. Le degré d’intégration dépend du problème. <br>
&nbsp;&nbsp;&nbsp;&nbsp;Des disciplines non-STEM peuvent également être abordées.<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;Note de bas de page: En tenant compte des concepts du deuxième degré et du contexte dans lequel cet objectif minimal est abordé.

<span style="color: yellowgreen">(04.05 Finalité de transition; Double finalité, Finalité marché du travail) Les élèves analysent l’impact des systèmes numériques sur la société à partir des principes de la pensée computationnelle.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Note:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Principes de la pensée computationnelle tels que la décomposition, la reconnaissance de motifs, l’abstraction et les algorithmes.<br>
&nbsp;&nbsp;&nbsp;&nbsp;L’impact des systèmes numériques sur la société à partir des principes de la pensée computationnelle tels que les algorithmes que les plateformes numériques utilisent pour
la sélection et la présentation d’informations aux utilisateurs;
la collecte d’informations personnelles des utilisateurs et leur (mauvaise)(bonne) utilisation à des fins propres;
l’influence sur les choix des utilisateurs (p. ex. offre personnalisé, publicité personnalisée);
l’influence sur la vision du monde/opinion des utilisateurs;
la prise de décisions à propos des utilisateurs (p. ex. demandes de crédit, candidatures, assurances);
la création d’interactions langagières à l’aide de l’intelligence artificielle (chatbot);
la création d’art (images, musique, poésie, autres formes d’art) à l’aide de l’intelligence artificielle;
l’imagerie médicale pour signaler aux médecins, sur base d’un premier scan, d’éventuelles anomalies.

### Attentes finales annulées (Source: onderwijsdoelen.be)

<span style="color: yellowgreen">(4.5 Finalité de transition) Les élèves conçoivent des algorithmes pour résoudre numériquement des problèmes.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive: niveau de maîtrise créer

<span style="color: yellowgreen">(4.5 Double finalité) Les élèves résolvent numériquement un problème délimité en adaptant un algorithme fourni. </span>

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive: niveau de maîtrise créer

<span style="color: yellowgreen">(Attente finale annulée 6.4 Finalité de transition, Double finalité) Les élèves appliquent des concepts géométriques appropriés et des propriétés de figures planes pour résoudre des problèmes plans et spatiaux:
* critères de similitude des triangles;
* le théorème de Thalès;
* le théorème de Pythagore;
* nombres trigonométriques dans un triangle rectangle;
* droites remarquables dans les triangles.
</span>

&nbsp;&nbsp;&nbsp;&nbsp; L’attente finale est réalisée tant avec que sans contexte.

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive: niveau de maîtrise appliquer

<span style="color: yellowgreen">(6.4 Double finalité) Les élèves appliquent, dans des situations significatives, des concepts géométriques appropriés et des propriétés de figures planes pour résoudre des problèmes plans et spatiaux:
* similitude de triangles;
* le théorème de Pythagore;
* nombres trigonométriques dans un triangle rectangle.
</span>

&nbsp;&nbsp;&nbsp;&nbsp;L’attente finale est réalisée tant avec que sans contexte.

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive: niveau de maîtrise appliquer

<span style="color: yellowgreen">(6.55 Finalité de transition; 6.31 Double finalité) Les élèves conçoivent une solution à un problème en mobilisant de façon intégrée des concepts et pratiques issus de différentes disciplines STEM.</span>

&nbsp;&nbsp;&nbsp;&nbsp;Y compris le contexte<br>
&nbsp;&nbsp;&nbsp;&nbsp;* Chaque discipline STEM est abordée au moins une fois de manière intégrée.

&nbsp;&nbsp;&nbsp;&nbsp;Dimension cognitive: niveau de maîtrise créer