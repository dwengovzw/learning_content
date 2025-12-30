---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: "Plus grand et plus petit : D\xE9composition et abstraction"
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 1
hruid: ct05_01
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
title: "Plus grand et plus petit: D\xE9composition et abstraction"
version: 3
---
# Exemple 1 : Décomposition et abstraction
Source : [la plateforme en ligne du concours Bebras belge](https://bebras.ugent.be/)<br>
Texte : Pär Söderhjelm, SE, Artem Iglikov, KZ, Jan Berki, CZ<br>
Images : Maiko Shimabuku, JP<br>
Traduction : Kris Coolsaet 

## Plus grand et plus petit (Bebras 2014-SE-04)

Les jeunes castors Anna, Britt, Charlotte, Demi et Emma — tous de tailles différentes — veulent jouer un jeu avec toi. Ils se placent en file, l’un derrière l’autre, tous regardant dans la même direction, dans un ordre qu’ils ont choisi eux-mêmes. Chaque castor compte alors combien de castors plus grands se trouvent devant et derrière lui. Voici les résultats :

|**Nom**|**Nombre de castors plus grands devant**|**Nombre de castors plus grands derrière**|
|---------------|------------------------|----------------------------|
|Anna|1|2|
|Britt|3|1|
|Charlotte|1|0|
|Demi|0|0|
|Emma|2|0|


*Dans quel ordre les castors sont-ils placés ?*

---

#### Solution

Il y a 5 castors. <br>
D’après le tableau, on peut déduire que Demi est la plus grande car aucun castor devant ou derrière n’est plus grand. Ensuite vient Charlotte, avec seulement un castor plus grand (à savoir Demi), puis Emma, puis Anna et enfin Britt. Britt est la plus petite, car les quatre autres castors sont plus grands.

![bebrasdecompositiestap1](embed/bebrasdecompositiestap1.png)

Raisonne maintenant de la manière suivante :<br>
- Demi est plus grande que tout le monde. Il n’y a qu’une seule personne plus grande que Charlotte. Demi est plus grande que Charlotte et se trouve donc devant Charlotte dans la file.   
    - Demi - Charlotte
- Il n’y a que deux castors plus grands qu’Emma et ils sont placés devant Emma. Ces deux castors sont donc Demi et Charlotte.  
    - Demi - Charlotte - Emma
- Comme il n’y a qu’un seul castor plus grand placé devant Anna, ce doit être Demi. Donc Anna vient après Demi et avant Charlotte et Emma. 
    - Demi - Anna - Charlotte - Emma
- Britt a trois castors plus grands devant elle, donc Britt se trouve après Charlotte dans la file. 
    - Demi - Anna - Charlotte - Britt - Emma

![Plus grand et plus petit](embed/bebrasdecompositieabstractieoplossing.png "Bebras Solution Plus grand et plus petit")

#### Discussion

Ceci est un bel exemple de **décomposition**. Dans une première étape, tu détermines pour chaque castor combien de castors sont plus petits que ce castor et donc, en fait, quel est le classement des castors par taille. Ensuite, tu utilises cette information dans une deuxième étape pour déterminer l’ordre des castors dans la file. 

Dans la solution, tu abordes les sous-problèmes un par un. De cette manière, tu obtiens à chaque fois des résultats intermédiaires que tu utilises ensuite pour résoudre un sous-problème suivant.

Dans la première étape, tu fais en outre une **abstraction** de la différence entre « devant » et « derrière ». Tu t’intéresses uniquement au nombre de castors qui sont plus grands qu’un castor donné, pas au fait qu’ils soient devant ou derrière.