---
hruid: anm_1301
version: 3
language: nl
title: "Gradient descent"
description: "Gradient descent"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14]
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

# Gradient descent

Bij  _gradient descent_ gaat men op zoek naar het minimum door de gewichten **stap voor stap** aan te passen, en zo dichter en dichter bij het minimum te komen. Geleidelijk aan vindt men zo de meest optimale gewichten waarnaar men op zoek is. De grootte van de stappen wordt bepaald door de zogenaamde *learning rate*; afhankelijk van de waarde van de *learning rate* zullen er grote of kleine aanpassingen plaatsvinden.  

In de volgende notebook word je ingewijd in de methode van _gradient descent_. Voor de eenvoud zal je op zoek gaan naar het minimum van enkele functies die afhankelijk zijn van slechts 1 variabele. Ook de functies worden vrij eenvoudig gehouden, de notebook beperkt zicht tot veeltermfuncties.   

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=1760 "Gradient descent")