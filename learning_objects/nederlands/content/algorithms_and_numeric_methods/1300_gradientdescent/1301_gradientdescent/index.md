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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Gradient descent

Bij  _gradient descent_ gaat men op zoek naar het minimum door de gewichten **stap voor stap** aan te passen, en zo dichter en dichter bij het minimum te komen. Geleidelijk aan vindt men zo de meest optimale gewichten waarnaar men op zoek is. De grootte van de stappen wordt onder andere bepaald door de zogenaamde *learning rate*; afhankelijk van de waarde van de *learning rate* zullen er grote of kleine aanpassingen plaatsvinden. Maar elke stap hangt ook af van de richtingscoëfficiënt van de raaklijn. 

Dit wordt geillustreerd in het volgende voorbeeld waar met gradient descent op zoek gegaan wordt naar het minimum van een tweedegraadsfunctie (te vinden in de top van de dalparabool).<br>
![Gradient descent parabool](embed/gradientdescent.jpg "Gradient descent")



