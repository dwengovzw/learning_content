---
hruid: wgs_lcd-v1
version: 3
language: fr
title: "Explication lcd"
description: "Explication lcd"
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

## Affichage LCD

Vous pouvez utiliser l'écran LCD pour afficher du texte. Cela peut être utile, par exemple, pour la lecture de capteurs.

L'écran LCD du Dwenguino peut contenir jusqu'à 32 caractères, par exemple des lettres ou des chiffres, répartis sur deux lignes. Vous pouvez donc afficher 16 caractères par ligne. La luminosité et le rétroéclairage de l'écran sont également réglables, mais ils ne sont pas traités ici.

![](embed/Image1.png "Image LCD")