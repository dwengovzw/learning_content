---
hruid: pr_lcdWGS2-v1
version: 3
language: fr
title: "Exemple LCD 2"
description: "Exemple LCD 2"
keywords: ["StartToDwenguino", "lcd", "lcd-scherm"]
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
### Exemple d'écran LCD

QUESTION 2

Assurez-vous que « Bienvenue » et « robot » apparaissent sur des lignes distinctes.

Solution:

![blockly](@learning-object/LCDM2-v1/nl/3)

Pour diviser le texte en 2 lignes, vous avez besoin d'un deuxième bloc *'écran LCD'*.
Si vous remplacez le 0 par un 1 à « dans une rangée : », votre texte apparaîtra sur la deuxième ligne.

*Testez ces exemples vous-même dans le simulateur ! Une fois que vous aurez compris son fonctionnement, vous pourrez commencer vous-même.*