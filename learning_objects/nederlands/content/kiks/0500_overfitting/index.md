---
hruid: kiks_overfitting
version: 3
language: nl
title: "Overfitting"
description: "Overfitting"
keywords: [""]
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
estimated_time: 20
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Overfitting
Wanneer een netwerk te gefixeerd geraakt op de trainingdata zal het minder goed presteren op ongeziene data. Het netwerk leert dan als het ware de trainingdata van buiten. Dit wordt **overfitting** genoemd. Wanneer het netwerk nog kan bijleren, door bijvoorbeeld meer lagen toe te voegen, spreekt men van **underfitting**.

![over- en underfitting](embed/overunderfit.png "Balans tussen over- en underfitting") 

Links op de afbeelding is er sprake van underfitting, de rechtse grafiek illustreert overfitting.

In de volgende notebook leer je hiermee rekening te houden.

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=1713 "Overfitting")
