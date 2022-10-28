---
hruid: pr_wgs_lcd1-v1
version: 3
language: fr
title: "Exemple LCD 1"
description: "Exemple LCD 1"
keywords: ["StartToDwenguino", "lcd", "lcd-scherm"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
### Exemple d'écran LCD

QUESTION 1

Faites apparaître 'Welcome Robot' sur l'écran LCD.

Solution:

![blockly](@learning-object/LCDM1-v1/fr/3)

Vous pouvez modifier le texte 'Bienvenue robot'. Les deux zéros signifient : première ligne, premier caractère.

*Testez ces exemples vous-même dans le simulateur ! Une fois que vous aurez compris son fonctionnement, vous pourrez commencer vous-même.*