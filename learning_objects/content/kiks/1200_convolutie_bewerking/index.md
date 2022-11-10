---
hruid: KIKS_convolutie_bewerking-v1
version: 3
language: nl
title: "Convolutie bewerking"
description: "Convolutie bewerking"
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Convolutiebewerking
Bij een ’convolutie’ laat men een ’filter’ over een afbeelding ’glijden’; er wordt daarbij telkens één pixel opgeschoven. 
Zowel de afbeelding als de filter zijn matrices of tensoren. De elementen van de filter en de elementen van de matrix van de afbeelding worden
elementsgewijs vermenigvuldigd en erna worden deze producten opgeteld. 

In deze notebook leer je hoe deze bewerking exact verloopt.

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=1751 "Convolutie bewerking")
