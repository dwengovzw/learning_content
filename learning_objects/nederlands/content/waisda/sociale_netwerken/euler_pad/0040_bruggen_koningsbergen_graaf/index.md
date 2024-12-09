---
hruid: org-dwengo-waisda-soc-netwerken-bruggen-van-koningsbergen-graaf
version: 1
language: nl
title: "Graaf van Koningsbergen"
description: "Hoe kunnen we de kaart van koningsbergen voorstellen als een graaf om zo het probleem te kunnen oplossen."
keywords: ["grafen","Euleriaans pad", "koningsbergen"]
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

# Graaf van Koningsbergen

Om dit probleem op te lossen, kunnen we eerst een abstractie maken van de kaart van de stad. Er is immers veel informatie op te zien die we niet nodig hebben. Zo moeten we niet weten waar de huizen in de stad liggen of zelfs waar de rivier en de bruggen juist liggen. De enige info die we nodig hebben is welke eilanden er zijn en welke bruggen de eilanden verbinden. De overbodige informatie laten we weg.

We tekenen op de volgende manier een **graaf** van de stad:

1. Teken voor elk eiland van de stad een knoop.
2. Teken voor elke brug tussen twee eilanden een boog tussen de knopen die overeenkomen met deze twee eilanden.

Hieronder zie je de kaart van Konginsbergen waarbij de eilanden elk een eigen kleur gekregen hebben. Daaronder zie je de graaf. De kleur van de knoop komt overeen met de kleur van het eiland.

![](images/koningsbergen_colored.png)

![](images/koningsbergen_color_graph.svg)

