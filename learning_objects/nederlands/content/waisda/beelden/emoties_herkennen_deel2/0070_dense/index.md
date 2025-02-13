---
hruid: org-dwengo-waisda-beelden-emoties-deel2-dense
version: 1
language: nl
title: "Dense lagen"
description: "Wat is zijn dense lagen?"
keywords: ["lagen", "AI", "neurale netwerken", "dense"]
content_type: "text/markdown"
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# Dense lagen

Dense lagen, anders gezegd fully connected layers, zijn lagen waarin alle elementen in deze laag via neuronen verbonden zijn met alle elementen in de volgende laag. Voor elk element in de volgende laag wordt een gewogen som genomen van de elementen in de huidige laag, daarna wordt een activatiefunctie toegepast op het resultaat van de som (bv. relu). Hieronder zie je een voorbeeld van zo'n dense laag met drie invoerwaarden en één uitvoerwaarde.

!["Voorbeeld van een dense laag."](img/dense.png)