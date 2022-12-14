---
hruid: Attendwgs
version: 3
language: fr
title: "Explication Attend"
description: "Explication Attend"
keywords: ["StartToDwenguino", "wacht"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
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
## Attends

Le bloc *'wait'* est une instruction qui indique à l'ordinateur combien de temps quelque chose doit être exécuté.

![](embed/Image1.png "Aperçu en attente")

Le temps est exprimé en millisecondes. Une milliseconde est un millième de seconde. Un millier de millisecondes peut être fait en une seconde.

**Exemple**

Essayez l'exemple ci-dessous pour voir comment cela fonctionne !

![blockly](@learning-object/WAIT1/fr/3)