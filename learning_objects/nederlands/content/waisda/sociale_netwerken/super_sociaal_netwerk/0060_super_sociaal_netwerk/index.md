---
hruid: org-dwengo-waisda-sociale-netwerken-super-sociaal-netwerk-notebook
version: 1
language: nl
title: "Super sociaal netwerk"
description: "Leer hoe je informatie kan halen uit een sociaal netwerk."
keywords: ["Sociale netwerken", "grafen", "AI", "Unsupervised learning"]
content_type: "text/markdown"
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# Het super sociaal netwerk

In de volgende notebook verken je zelf een "super" sociaal netwerk. Het netwerk bevat immers een overzicht van alle superhelden die ooit deel uitgemaakt hebben van een Marvel strip. In het netwerk is er een link tussen twee personages wanneer die samen in een strip voorgekomen zijn. Komen die personages in meerdere strips samen voor, dan krijgt die link een sterker gewicht. Hieronder zie je een voorbeeld van hoe een eenvoudige versie van het super sociaal netwerk eruit zou kunnen zien.

!["Voorbeeld super sociaal netwerk"](img/voorbeeld_sociale_graaf_min_dist.svg)

In de knopen van deze graaf staan de superhelden. Wanneer er een boog tussen twee helden staat, komen die één of meerdere keren samen voor in een strip. Het getal naast de boog geeft weer in hoeveel strips ze samen voorkomen. 