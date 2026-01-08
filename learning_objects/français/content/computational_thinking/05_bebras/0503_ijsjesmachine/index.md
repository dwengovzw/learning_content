---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: "Machine \xE0 glaces: reconna\xEEtre des motifs"
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct05_03
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
title: "Machine \xE0 glaces: Reconnaissance de motifs"
version: 3
---
# Exemple 3 :  Reconnaître un motif
Source : [la plateforme en ligne du concours belge Bebras](https://bebras.ugent.be/)<br>
Texte : Opráné Vecsei Éva, HU, Zsuzsa Pluhár, HU, Sébastien Combéfis, BE<br>
Images : inconnues<br>
Traduction : Kris Coolsaet

## Machine à glaces (Bebras 2013-HU-01)

Une machine à glace produit des boules colorées d'une manière systématique particulière. Pour chaque cornet, quatre boules sont servies. Ci-dessous, voici à quoi ressemblaient les trois derniers cornets de glace fabriqués par la machine :

![Machine à glaces](embed/bebraspatroon.png "Reconnaissance de motifs Bebras")

*À quoi ressemble la glace suivante fabriquée par la machine ?*

---

#### Solution

![Machine à glaces](embed/bebraspatroonoplossing.png "Solution Machine à glaces Bebras")

#### Discussion
Dans cet exercice, on demande explicitement de reconnaître un **motif** et de l'extrapoler. Cet exercice est destiné à de très jeunes enfants et est donc facile à comprendre pour tout le monde.

La machine à glace produit des boules en quatre couleurs différentes et, de plus, dans un ordre fixe qui se répète sans cesse. Après quatre boules, une couleur est donc répétée. Ainsi, la boule du bas d'une glace a toujours la même couleur que la boule du haut de la glace précédente.

Les couleurs des boules des trois dernières glaces étaient les suivantes :<br>
vert - rouge - violet - bleu - bleu - vert - rouge - violet - violet - bleu - vert - rouge<br>
Ainsi, l'ordre 'vert - rouge - violet - bleu' se répète continuellement et se poursuit d'une glace à l'autre. 

La glace suivante doit donc d'abord recevoir une boule rouge, puis 'violet - bleu - vert'.