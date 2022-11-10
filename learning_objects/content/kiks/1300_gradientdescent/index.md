---
hruid: KIKS_gradient_descent-v1
version: 3
language: nl
title: "Gradient descent"
description: "gradient descent"
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

# Gradient Descent
In de wiskunde wordt veel aandacht besteed aan de afgeleide van een reële functie. Afgeleiden hebben veel toepassingen, bv. in de economie en in de fysica.

Ook voor neurale netwerken zijn afgeleiden belangrijk. Men gebruikt ze om de kostenfunctie te minimaliseren. Men gaat op zoek naar het minimum door de
gewichten stap voor stap aan te passen, gebaseerd op de afgeleide in het ‘huidige’ punt. Deze methode noemt men _gradient descent_.

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=1760 "Gradient descent")
