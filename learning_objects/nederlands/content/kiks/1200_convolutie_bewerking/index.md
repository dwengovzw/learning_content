---
hruid: kiks_convolutie_bewerking
version: 3
language: nl
title: "Convolutiebewerking"
description: "Convolutiebewerking"
keywords: ["AI"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 30
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Convolutiebewerking
Bij een ’convolutie’ laat men een ’filter’ over een afbeelding ’glijden’; er wordt daarbij telkens één pixel opgeschoven. 
Zowel de afbeelding als de filter zijn matrices of tensoren. De elementen van de filter en de elementen van de matrix van de afbeelding worden
elementsgewijs vermenigvuldigd en erna worden deze producten opgeteld. 

In deze notebook leer je exact hoe deze bewerking verloopt.

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/hub/tmplogin?id=1751 "Convolutie bewerking")

Deze animatie geeft je alvast een voorproefje:<br>
![animatie convolutiebewerking](embed/convolutie.gif "Convolutiebewerking") 
<br>Bron: Afbeelding van Rob Robinson, MLNotebook. Geraadpleegd op 19 mei 2019 via  https://mlnotebook.github.io
