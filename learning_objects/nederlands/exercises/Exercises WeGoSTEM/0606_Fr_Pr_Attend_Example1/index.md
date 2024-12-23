---
hruid: Pr_Attendwgs1
version: 3
language: fr
title: "Exemple Attend 1"
description: "Exemple Attend 1"
keywords: ["StartTodwenguino", "wacht"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

### Aperçu Attendre

QUESTION 1

ShWrite un programme qui effectue les opérations suivantes :

* Faire apparaître "Bonjour les gens" sur l'écran LCD pendant 1 seconde (1000 ms).
* Faire apparaître "Je suis dwenguino" sur l'écran LCD pendant 2 secondes (2000 ms).

Solution:

![blockly](@learning-object/WACHTwgs1/fr/3)

Le bloc *'wait'* qui apparaît **après** une instruction particulière indique combien de temps l'ordinateur doit **attendre** avant de pouvoir lancer l'instruction suivante.

Le problème maintenant est que "Je suis dwenguino" reste à l'écran. *Pensez à ce qui causerait cela.*

*Testez ces exemples vous-même dans le simulateur !*