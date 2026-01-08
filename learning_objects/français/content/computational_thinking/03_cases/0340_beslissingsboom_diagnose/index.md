---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: "Arbre de d\xE9cision"
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct03_40
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
title: "Arbre de d\xE9cision pour le diagnostic m\xE9dical (2,3)"
version: 3
---
# Arbre de décision pour le diagnostic médical

*Dans le projet « IA dans les soins de santé », les élèves, avec l’enseignant, cherchent un moyen d’aider les soignants à poser un diagnostic ou à déterminer un traitement. Ils peuvent s’appuyer pour cela sur des données de patients fournies dans un fichier CSV. Ces données sont étiquetées et contiennent par exemple des caractéristiques des patients, des symptômes et une affection.*  

**Défi : Présentez des données étiquetées du secteur des soins de santé d’une manière appropriée pour prendre des décisions concernant un diagnostic ou un traitement.**

**Public cible** : 2e degré – finalité de transition ; 3e degré – double finalité

**Discipline(s) :** 
* Mathématiques
* STEM 

**Prérequis :**
* Les élèves savent ordonner les nombres réels.
* Les élèves connaissent les fonctions du second degré.
* Les élèves ont vu des exemples d’arbres de décision.

Un déroulement possible de l’étude de cas est le suivant :<br><br>

*Phase 1 : découverte des arbres de décision et de leur structure*<br>
<ol>
    <li>Vous donnez des exemples d’arbres de décision de la vie réelle ou les élèves en recherchent eux-mêmes.
    <li>Reconnaissance de motifs : les élèves identifient la structure à partir des différents exemples. C’est un graphe orienté avec des arcs et des nœuds.
    <li>Les élèves comprennent qu’on peut générer un arbre de décision sur la base d’un paramètre de dispersion et de questions oui/non.
    <li>Les élèves complètent le schéma avec les concepts de base.</li>
</ol>

*Phase 2 : mathématiques*<br>
<ol>
    <li>Les élèves réalisent une tâche sur le paramètre de dispersion.
    <li>Les élèves choisissent le paramètre de dispersion sur la base de quelques critères. Lequel reflète le mieux la réalité ? Lequel est réalisable compte tenu des connaissances préalables ?
    <li>Les élèves établissent une formule pour l’indice de Gini.
    <li>Des exercices montrent que l’on peut représenter des questions oui/non à l’aide d’expressions logiques (inégalités).</li>
</ol>

*Phase 3 : algorithme*<br>
<ol>
    <li>Les élèves rédigent l’algorithme (en mots).
    <li>Les élèves testent l’algorithme (manuellement ou avec des outils numériques, les deux sont possibles) sur un petit jeu de données.</li>
</ol>

*Phase 4 : Python*<br>
<ol>
    <li>Les élèves exécutent l’algorithme en Python sur un jeu de données réel. Ils utilisent un module Python existant pour écrire un programme à cet effet.
    <li>Les élèves doivent prétraiter le jeu de données (nettoyer les données et les rendre numériques si nécessaire).
    <li>Les élèves complètent davantage le schéma avec les concepts de base.</li>
</ol>
 
![ct-schema](@learning-object/m_ct03_40/nl/3)

Pour le développement de ce projet, voir le projet « IA dans les soins de santé ».