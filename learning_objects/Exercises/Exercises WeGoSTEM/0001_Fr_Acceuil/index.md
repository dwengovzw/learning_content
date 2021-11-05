---
hruid: Acceuil-v1
version: 3
language: fr
title: "StartToDwenguino Base"
description: "Description des pièces du simulateur"
keywords: ["StartToDwenguino"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [10, 11, 12, 13, 14]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', 
    'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso'
]
teacher_exclusive: false
---
# DwenguinoBlockly
# Un environnement de programmation

L'environnement de programmation du simulateur est disponible en ligne sur [https://www.dwengo.org/dwenguinoblockly](https://www.dwengo.org/dwenguinoblockly "link simulator").

Ci-dessous vous voyez une capture d'écran de l'environnement avec la description des différentes parties.

![](embed/Image1.png "Simulateur de pièces")


1. La *boîte à outils* : Dans ce menu, vous trouverez les différents blocs de code. Le menu est divisé en catégories, chacune contenant un type spécifique de blocs. Dans
Par exemple, ![alt](embed/Afb2.png "Image Dwenguino") vous pouvez trouver tous les blocs pour contrôler le robot de dessin.

2. Le *champ de code* : C'est là que vous trouverez le programme que vous êtes en train de créer. Le bloc *'put ready/repeat'* est déjà là.
![alt](embed/Image3.png "Répétition prête pour l'ensemble d'images")

Seul le code placé dans les sections 'set ready' et 'repeat' de ce bloc sera exécuté. Le code à un autre endroit ne s'exécutera pas. Pour programmer, vous faites glisser des blocs de la boîte à outils vers le champ de code et cliquez dessus dans le bloc *'set ready/repeat'*.

3. Le *menu principal* : Avec ce menu, vous pouvez effectuer des actions telles que l'enregistrement de votre code (avec
![alt](embed/Image4.png "Téléchargement d'images")), recharger (avec
![alt](embed/Image5.png "Téléchargement d'images")
), ou ouvrir et fermer l'environnement de simulation (avec
![alt](embed/Image6.png "Environnement de simulation d'images")
).

4. Le *menu simulateur* : Vous trouverez ici les boutons pour démarrer et arrêter la simulation avec les boutons
![alt](embed/Image7.png "Lecture d'images")
 et
![alt](embed/Image8.png "Image Stop")
. Il vous permet également de choisir un scénario spécifique dans lequel vous souhaitez exécuter votre code.

5. La *fenêtre de simulation* : Dans cette fenêtre vous voyez un robot virtuel et souvent aussi une carte de microcontrôleur virtuelle, la Dwenguino, sur laquelle vous pouvez exécuter votre code. Dans l'image, le scénario du robot de dessin est sélectionné. En haut, vous voyez un tableau Dwenguino virtuel, en bas un robot de dessin virtuel que vous pouvez programmer.


Dans la boîte à outils, vous pouvez trouver les blocs dont vous avez besoin pour créer des programmes. Vous devez faire glisser ces blocs, puis cliquer dessus dans l'ordre souhaité.

Tout au long des exercices, il y aura des références pour de nouveaux blocs à l'endroit dans la boîte à outils où vous pouvez les trouver. Un exemple d'une telle référence est ![alt](embed/Image2.png "Image Dwenguino") .