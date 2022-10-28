---
hruid: Boutonswgs-v1
version: 3
language: fr
title: "Explication Boutons"
description: "Explication Boutons"
keywords: ["StartToDwenguino", "knoppen"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [10, 11, 12]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
## Boutons

Sur le Dwenguino, vous trouverez cinq boutons poussoirs. Les boutons extérieurs ont été nommés NORD, SUD, EST, OUEST, tout comme en géographie. Le bouton du milieu s'appelle CENTRE.

Vous pouvez cliquer sur un bouton avec votre souris. Lorsque vous cliquez dessus, le bouton est enfoncé. Lorsque vous relâchez le bouton, il n'est plus enfoncé.

![](embed/Buttons.png "Boutons d'aperçu")

Bien sûr, vous voulez que le robot de dessin ne commence à dessiner que lorsque vous le souhaitez. C'est pourquoi vous allez entrer ici une condition de départ supplémentaire, comme dans l'exemple ci-dessous :

![blockly](@learning-object/KNOP-v1/fr/3)