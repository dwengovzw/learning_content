---
hruid: Pr_AttendWGS2-v1
version: 3
language: fr
title: "Attend Example"
description: "Attend Example"
keywords: ["StartToDwenguino", "wacht"]
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
teacher_exclusive: true
---

### Aperçu Attendre

Vous pouvez résoudre ce problème de 2 manières.

**Voie 1**

La première consiste à supprimer le texte. Pour cela, vous utilisez le bloc **CreateLCDClear**.

![blockly](@learning-object/WACHTWGS2-v1/nl/3)

*Testez ces exemples vous-même dans le simulateur !*