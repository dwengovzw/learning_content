---
hruid: anm_1302
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

In de notebook komen enkele **wiskundige concepten** aan bod: tweedegraadsfunctie en parabool, punt op een grafiek, derde- en vierdegraadsfunctie (optioneel), de richtingscoëfficiënt van een raaklijn aan een functie, m.a.w. de afgeleide in een punt, lokaal en globaal minimum (optioneel).  

De afgeleide in een punt van een parabool is de richtingscoëfficiënt van de raaklijn in dat punt aan de parabool.<br>
Waar de parabool stijgt, is de raaklijn een stijgende rechte en is de richtingscoëfficiënt van de raaklijn positief. Waar de parabool daalt, is ze negatief.
In een top van de parabool is de raaklijn horizontaal en de afgeleide 0.
Hoe steiler de raaklijn, hoe groter de richtingscoëfficiënt van de raaklijn in absolute waarde, dus hoe groter de afgeleide in absolute waarde.

Een functie kan meer dan een minimum hebben. Als er bv. meerdere lokale minima zijn, dan is het de bedoeling om op zoek te gaan naar het globale minimum: het kleinste lokale minimum.