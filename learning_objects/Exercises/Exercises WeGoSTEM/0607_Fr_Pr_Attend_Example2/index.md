---
hruid: Pr_Attendwgs2
version: 3
language: fr
title: "Exemple Attend 2"
description: "Exemple Attend 2"
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

Vous pouvez résoudre ce problème de 2 manières.

**Voie 1**

La première consiste à supprimer le texte. Pour cela, vous utilisez le bloc **CreateLCDClear**.

![blockly](@learning-object/WACHTwgs2/fr/3)

*Testez ces exemples vous-même dans le simulateur !*