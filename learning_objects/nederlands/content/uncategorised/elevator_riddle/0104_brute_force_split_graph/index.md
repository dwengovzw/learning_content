---
hruid: org-dwengo-elevator-riddle-brute-force-2
version: 1
language: nl
title: "Stap 1: De graaf splitsen"
description: "Hoe splitsen we onze graaf in twee delen?"
keywords: ["grafen", "algoritme", "computationeel denken", "clustering", "datastructuur", "brute force"]
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---

# Alle mogelijke manieren om de graaf in twee gelijke delen te splitsen

Onze graaf bestaat uit acht knopen (de verdiepingen). We kunnen deze in twee verdelen door vier knopen uit te kiezen en deze toe te kennen aan lift 1. De vier knopen die overblijven kennen we toe aan lift 2.  
We kunnen het aantal keuzes van vier items uit acht opties berekenen met onze kennis van combinatoriek \\[\mathrm{C}^4_8 = 70\\].

Om alle 70 combinaties te genereren kunnen we een eenvoudig algoritme bedenken.

We starten zonder verdeling. We hebben nog geen enkele verdieping gekozen om toe te kennen aan lift 1:

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| x | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |



