---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: "Pens\xE9e algorithmique"
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct08_05
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
- 15
- 16
- 17
- 18
teacher_exclusive: true
title: "Pens\xE9e algorithmique"
version: 3
---
# Pensée algorithmique

*Les élèves conçoivent une méthode systématique pour résoudre le (sous-)problème. Cette méthode systématique consiste en un ensemble d’étapes successives, sans ambiguïté, dans l’ordre nécessaire.*

**Exemple**<br>
Pour l’automatisation d’un pont-levis, un algorithme possible est le suivant :

* Si le capteur sur le pont détecte un bateau entrant, alors :

    - les feux de circulation sur la chaussée pour le trafic de transit (voitures, cyclistes…) doivent passer au rouge ;
    - il faut attendre ‘x’ minutes afin de permettre au trafic sur le pont de quitter celui-ci ;
    - les barrières doivent se fermer ;
    - le moteur du pont peut démarrer pour lever le pont ;
    - le moteur doit s’arrêter lorsque le pont est levé ;
    - le signal pour le bateau doit être réglé sur « passage autorisé ».
    
* Lorsque le bateau est passé et que le capteur détecte le bateau sortant, alors :
    -  ...