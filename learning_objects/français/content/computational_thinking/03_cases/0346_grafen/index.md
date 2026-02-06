---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: Applications des graphes
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct03_46
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
title: Applications des graphes (2,3)
version: 3
---
# Applications des graphes

**Un graphe comme structure de données pour deux problèmes dans des contextes différents.** 

Ici, vous examinez quelques applications des graphes : le fonctionnement d’un planificateur d’itinéraires et l’appariement des empreintes digitales. Ces exemples font partie d’une série de leçons sur la théorie des graphes.

**Public cible :** Élèves du 2e et 3e degré, finalité de transition et double finalité (filières encore à déterminer).

**Discipline :** /

**Prérequis :** Les élèves connaissent déjà quelques types de graphes (graphe simple, graphe orienté, chemin, marche, cycle).

**Objectif :** Les élèves constatent qu’on peut parfois arriver plus rapidement à la solution d’un problème en abstraisant les données sous forme de graphe. Dans ces exemples, un nouveau type de graphe est nécessaire.

### Le fonctionnement d’un planificateur d’itinéraires

Vous connaissez les distances en km entre certaines communes par les grands axes et à vol d’oiseau : Gand, Lokeren, Saint-Nicolas, Termonde, Willebroek, Malines. Déterminez le plus court chemin entre Gand et Malines via ces routes. Comment un ordinateur peut-il aider ?  
![image](https://user-images.githubusercontent.com/48352335/213927739-9b9c0801-bdb0-4692-af36-eafa8f172864.png)
![image](https://user-images.githubusercontent.com/48352335/213927749-83781385-10f4-43f4-9d28-10bfc20d3700.png)

![ct-schema](@learning-object/m_ct03_46a/nl/3)

Cet exemple est une introduction à l’algorithme de Dijkstra et à sa mise en œuvre pratique. 

### L’appariement des empreintes digitales

![ct-schema](@learning-object/m_ct03_46b/nl/3)



Pour plus d’explications, voir le parcours d’apprentissage ['Graphes'](https://www.dwengo.org/learning-path.html?hruid=aiz2_grafen&language=nl&te=true&source_page=%2Fcare%2F&source_title=%20AI%20in%20de%20Zorg#aiz_sprouts;nl;3) dans le cadre du projet [IA dans les soins de santé](https://www.dwengo.org/care/) ou de [Python en cours de mathématiques](https://www.dwengo.org/math_with_python/).