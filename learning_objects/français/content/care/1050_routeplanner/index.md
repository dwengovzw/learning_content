---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: "Fonctionnement du planificateur d'itin\xE9raire"
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: aiz_routeplanner
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
title: "Fonctionnement du planificateur d'itin\xE9raire"
version: 3
---
# Le fonctionnement d’un planificateur d’itinéraire

**Prérequis :** Les élèves savent ce qu’est un graphe, des nœuds et des arcs. Un nouveau type de graphe entre en jeu, à savoir le graphe pondéré. 

### Consigne pour les élèves
*Tu connais les distances en kilomètres entre certaines communes, tant via les grandes routes qu’à vol d’oiseau. Les communes sont Gand, Lokeren, Saint-Nicolas, Termonde, Anvers, Eeklo, Willebroek et Malines.<br>
Détermine le plus court chemin entre Gand et Malines via ces routes. Comment un ordinateur peut-il aider ?*

![image](https://user-images.githubusercontent.com/48352335/213933739-10534f75-588b-4817-8463-025524b85009.png)
![image](https://user-images.githubusercontent.com/48352335/213933743-2a57ac0f-b76b-4440-96e4-173f275a649b.png)


### Brainstorm en classe - Problème : Plus court chemin de Gand à Malines via les grandes routes 
Idées possibles durant le brainstorm (→ pensée computationnelle – décomposition) :<br>
- Comment trouver le plus court chemin ?
	- Regarder sur une carte la position des villes. Cela peut aider à déterminer l’itinéraire le plus court.
	- Passer en revue les itinéraires possibles un par un → une représentation visuelle est nécessaire 
	- Calculer la distance de chaque itinéraire possible
	- Le plus court chemin correspond à la plus petite distance
- Faire un schéma des villes et des routes (→ reconnaissance de motifs/abstraction réseau → graphe)
	- Indiquer les distances sur le schéma (→ graphe pondéré)  
- Comment un ordinateur peut-il aider ?
	- Cela existe déjà → planificateur d’itinéraire, p. ex. Google Maps
	- Comment fonctionne un tel planificateur d’itinéraire ?
	- Comment programmer pour que l’ordinateur calcule les distances des itinéraires possibles ?
		- L’ordinateur a besoin des distances entre les différentes communes
		- On ne peut atteindre une commune qu’en venant d’une commune qui y est reliée
		- Les routes sont bidirectionnelles, il y a donc une « symétrie avec distance égale » (c’est clair grâce à la symétrie du tableau donné)
		- Remarque : passer en revue toutes les routes possibles est en fait une perte de temps ; certaines communes ne sont pas pertinentes en raison de leur localisation.

### L’enseignant résume le remue-méninges
Exemple :

![image](https://user-images.githubusercontent.com/48352335/213933875-ae28abd8-eacd-4e3b-b5c0-a629119469a2.png)

Examiner la situation dans Google Maps :

![image](https://user-images.githubusercontent.com/48352335/213933904-236a21e1-9be4-4028-b475-b7ec9fec1b33.png)
<center>Source : Google Maps</center>  
 
### Technique pour déterminer le plus court chemin
#### Tableau des distances données en km
![image](https://user-images.githubusercontent.com/48352335/213933739-10534f75-588b-4817-8463-025524b85009.png)	

#### Transformer le tableau en un graphe pondéré
![M024_Graaf_1](https://user-images.githubusercontent.com/48352335/216783604-7ba61dcf-4e7f-41ba-a05f-017c715fb4d5.png)

#### Les élèves essaient eux-mêmes (manuellement) de trouver le plus court chemin
- Quelle stratégie les élèves ont-ils appliquée ?
- Très vite, cela représente pas mal de travail
        - Recourir à l’ordinateur est pertinent !
	- Il serait utile que l’ordinateur passe en revue toutes les possibilités.

#### Vérification Google Maps
![image](https://user-images.githubusercontent.com/48352335/213934118-1120ed5a-8dfd-4c2b-8b5d-2e67a6475172.png)

![image](https://user-images.githubusercontent.com/48352335/213934134-7d235d6a-c110-4fe2-a540-ef187417e885.png)

#### Ensuite : algorithme 
- Les élèves ont-ils conçu un algorithme ?
- Algorithme de Dijkstra
- Éventuellement l’implémenter à l’ordinateur avec Python
- Notebook Python


### Algorithme de Dijkstra

<div class="alert alert-box alert-secondary"><p style=" font-family: 'Courier New', monospace; font-size:12px; ">
Initialiser la liste ‘visités’   # la liste contient les nœuds dont tous les voisins ont été visités<br>
Initialiser la liste ‘non visités’ # la liste contient les nœuds dont tous les voisins n’ont pas encore été visités<br><br>
# remplir la liste ‘non visités’ (le coût est la distance, le temps… selon le problème)<br>
# tous les nœuds n’ont pas de nœud précédent<br>
# tous les nœuds sauf le nœud de départ ont un coût infini ; le nœud de départ a un coût 0<br>
Pour chaque nœud du graphe :<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ajouter le nœud à la liste ‘non visités’ avec un coût infini et sans nœud précédent<br>
Définir le coût du nœud de départ dans la liste ‘non visités’ à 0<br><br>
# examiner les nœuds de la liste ‘non visités’ un par un jusqu’à ce que cette liste soit vide<br>
# commencer à chaque fois par le nœud au coût le plus faible, appelé nœud actuel<br>
# considérer tous les voisins qui ne figurent pas encore dans la liste ‘visités’<br>
# pour chaque voisin, calculer le coût et le comparer à son coût actuel<br>
# si le nouveau coût est plus faible, mettre à jour les données du voisin dans la liste ‘non visités’<br>
# après avoir examiné tous ses voisins, déplacer le nœud actuel vers la liste ‘visités’<br>
Tant que la liste ‘non visités’ n’est pas vide :<br>
&nbsp;&nbsp;&nbsp;&nbsp;Définir le nœud actuel comme le nœud au coût le plus faible de la liste ‘non visités’<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ajouter le nœud actuel avec ses données (coût et nœud précédent) à la liste ‘visités’<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pour chaque nœud voisin du nœud actuel :<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Si le nœud voisin ne figure pas dans la liste ‘visités’ :<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculer le nouveau coût du nœud voisin = coût du nœud actuel + coût de l’arête<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Si ce nouveau coût est inférieur à l’ancien coût du nœud voisin :<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mettre à jour le coût du nœud voisin avec le nouveau coût<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mettre à jour le nœud précédent du nœud voisin avec le nœud actuel<br>
&nbsp;&nbsp;&nbsp;&nbsp;Supprimer le nœud actuel de la liste ‘non visités’<br><br>
Renvoyer la liste ‘visités’
</p>
</div>

#### Pour le programme, voir le notebook ‘Dijkstra’.

#### Application de l’algorithme
À l’aide d’un tableau et d’une structure arborescente, tu recherches l’itinéraire le plus court.

![image](https://user-images.githubusercontent.com/48352335/213934175-be5b3e22-4fc8-49ca-83ad-c73cc8f94298.png)
![M024_Boom_1](https://user-images.githubusercontent.com/48352335/216783699-8bd9beb6-c2d6-4155-909a-a88bdac9524b.png)


#### S’exercer avec l’algorithme
**Exercice 1**
Source : https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all 

*Trouve le plus court chemin de A vers E.*

![image](https://user-images.githubusercontent.com/48352335/213934203-9e5f3b11-c9fa-4745-9935-c115d214e584.png)
 
**Exercice 2**
Source : https://www.bebras.org/sites/default/files/2015%20Bebras%20Solution%20Guide.pdf

Bebras 2015 – Voyages 

Le castor Martina prend le train tous les jours pour aller travailler. Il n’y a pas de ligne directe, elle doit donc changer. La carte montre les lignes qu’elle peut emprunter avec indication du temps de trajet. La maison de Martina est indiquée par la lettre ‘H’, son lieu de travail par un ‘W’, et les gares par un ‘S’.

*Quel trajet correspond au temps de trajet le plus court ?*

![image](https://user-images.githubusercontent.com/48352335/213934241-97b3a82e-8fe4-4407-a09f-0caa52c83b4a.png)
 
**Exercice 3** 
Source : https://www.curriculumonline.ie/getmedia/da0c349c-d205-47ff-9b43-6c820a62807c/uk-bebras-2016-answers.pdf <br>
Copyright 2016 UK Bebras – Licence: CC-BY-NC-SA 3.0

Bebras 2016 – Pistes cyclables 

Cleveria est cycliste. Elle explore les pistes cyclables à sens unique qui traversent les villages de sa région. Chaque village possède une borne portant une lettre. Toutes les pistes cyclables ont un sens de circulation et une distance. Le sens de circulation et la distance sont indiqués au moyen des drapeaux jaunes.
 
![image](https://user-images.githubusercontent.com/48352335/213934298-cd8a75f8-ef27-4d77-a20c-140770bf3856.png)

Lors de ses explorations, Cleveria laisse des petits papiers bleus sous les bornes des villages, avec un nombre inscrit. Ce nombre correspond à la plus courte distance de la borne en question jusqu’au village A. 

*Quel nombre figure sous la borne du village E ?*

**Exercice 4**
Source : https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all 

*Trouve le plus court chemin de S vers G.*
 
![image](https://user-images.githubusercontent.com/48352335/213934333-5e062113-f283-490c-bd56-6d4fee4bdee2.png)


### Retour au problème d’itinéraire - pensée critique
- Optimisation ? Remarque : passer en revue toutes les routes possibles est en fait une perte de temps ; certaines communes ne sont pas pertinentes en raison de leur localisation.

![image](https://user-images.githubusercontent.com/48352335/213933743-2a57ac0f-b76b-4440-96e4-173f275a649b.png)

#### Technique à appliquer 
Voir : https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all

Vous utilisez une fonction d’estimation pour avoir une idée des communes plus opportunes par rapport à d’autres, en tenant compte de la commune vers laquelle on se dirige.<br>
Comme fonction d’estimation (f-score), vous utilisez la distance à vol d’oiseau (qui, pour cette application, correspond à la distance euclidienne).

Vous complétez le graphe pondéré avec la distance à vol d’oiseau.
  
![M024_Graaf_2](https://user-images.githubusercontent.com/48352335/216783645-5910a805-f876-4643-82f1-d98c15c2a48b.png)

À l’aide d’un tableau et d’une structure arborescente, tu recherches l’itinéraire le plus court.
![image](https://user-images.githubusercontent.com/48352335/213934386-9fe136a5-ff13-46b2-9ec0-42a8161da0de.png)
![M024_Boom_2](https://user-images.githubusercontent.com/48352335/216783661-d320583e-1ad3-4d09-b8a4-7180c9335c93.png)


### Algorithme A*
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace; font-size:12px;">
Initialiser la liste ‘visités’   # la liste contient les nœuds dont tous les voisins ont été visités<br>
Initialiser la liste ‘non visités’ # la liste contient les nœuds dont tous les voisins n’ont pas encore été visités<br><br>    
# remplir la liste ‘non visités’ avec nœuds, coût, f-score et nœud précédent <br>
# le coût est la distance, le temps… selon le problème<br>
# la f-score est le coût majoré de l’estimation<br>
# tous les nœuds n’ont pas de nœud précédent<br>
# tous les nœuds sauf le nœud de départ ont un coût et une f-score infinis<br>
# le nœud de départ a un coût 0, et pour f-score son estimation<br>
Pour chaque nœud du graphe :<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ajouter le nœud à la liste ‘non visités’ avec un coût et une f-score infinis, sans nœud précédent<br>
Définir le coût du nœud de départ dans la liste ‘non visités’ à 0<br>
Définir la f-score du nœud de départ dans la liste ‘non visités’ sur son estimation (= 0 + estimation)<br><br>
# examiner les nœuds de la liste ‘non visités’ un par un jusqu’à ce que le nœud actuel soit le nœud final<br>
# commencer à chaque fois par le nœud ayant la f-score la plus faible, appelé nœud actuel<br>
# considérer tous les voisins qui ne figurent pas encore dans la liste ‘visités’<br>
# pour chaque voisin, calculer le coût et la f-score et les comparer avec son coût actuel<br>
# si le nouveau coût est plus faible, mettre à jour les données du voisin dans la liste ‘non visités’<br>
# après avoir examiné tous ses voisins, déplacer le nœud actuel vers la liste ‘visités’<br>
Tant que la liste ‘non visités’ n’est pas vide :<br>
&nbsp;&nbsp;&nbsp;&nbsp;Définir le nœud actuel comme le nœud à la f-score la plus faible de la liste ‘non visités’<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ajouter le nœud actuel avec ses données (coût, f-score et nœud précédent) à la liste ‘visités’<br>
&nbsp;&nbsp;&nbsp;&nbsp;Si le nœud actuel est égal au nœud final :<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Arrêter la boucle while<br>
&nbsp;&nbsp;&nbsp;&nbsp;Sinon :<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pour chaque nœud voisin du nœud actuel :<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Si le nœud voisin ne figure pas dans la liste ‘visités’ :<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculer le nouveau coût du nœud voisin = coût du nœud actuel + coût de l’arête<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Si ce nouveau coût est inférieur à l’ancien coût du nœud voisin :<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mettre à jour le coût du nœud voisin avec le nouveau coût<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mettre à jour la f-score à nouveau coût + estimation<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mettre à jour le nœud précédent du nœud voisin avec le nœud actuel<br>
&nbsp;&nbsp;&nbsp;&nbsp;Supprimer le nœud actuel de la liste ‘non visités’<br><br>
Renvoyer la liste ‘visités’
</p>
</div>

#### Objectifs d’apprentissage
- Appliquer les concepts de base des graphes pour représenter un itinéraire.
- Les élèves développent un algorithme pour trouver le plus court chemin entre deux villes.
- Les élèves découvrent l’algorithme de Dijkstra, adapté à cet objectif.
- Illustrer l’utilité des mathématiques.

À l’issue de cette partie, les élèves pourront…
- utiliser les concepts de base des graphes dans ce contexte
- trouver l’itinéraire le plus court
- appliquer l’algorithme de Dijkstra
- éventuellement programmer l’algorithme de Dijkstra 
- avoir amélioré leur pensée critique et logique

#### Attentes finales
Graphes, pensée computationnelle, interaction entre société et STEM, éducation aux médias, protection de la vie privée.