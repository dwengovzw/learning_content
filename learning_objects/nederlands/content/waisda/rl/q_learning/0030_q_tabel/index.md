---
hruid: org-dwengo-waisda-rl-agent-trainen-q-tabel
version: 1
language: nl
title: "Q-tabel"
description: "Wat is de Q-tabel"
keywords: ["AI", "reïnforcement learning", "versterkend leren", "q-learning", "q-tabel"]
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

# De Q-tabel

De waardefunctie \((Q(T_t, A_t)\)) zegt ons hoe goed actie \\(A_t\\) is in toestand \\(T_t\\). Er zijn verschillende manieren om deze \\(Q\\)-functie voor te stellen. Een van de eenvoudigste manieren is aan de hand van een tabel. Voor elke mogelijk toestand in onze wereld voegen we een rij toe aan de tabel, voor elke mogelijke actie in de wereld voegen we een kolom toe. Op onderstaande figuur zie je een Q-tabel voor 5 acties en 7 toestanden. De waarde in de tabel zegt hoe goed de actie bovenaan de kolom is wanneer de agent in de toestand links van de rij zit.

![](img/q_table_example.png)

 