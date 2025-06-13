---
hruid: org-dwengo-waisda-rl-agent-trainen-q-tabel
version: 1
language: nl
title: "Q-tabel"
description: "Wat is de Q-tabel"
keywords: ["AI", "reïnforcement learning", "versterkend leren", "q-learning", "q-tabel"]
content_type: "text/markdown"
estimated_time: 3
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

De waardefunctie \\((Q(T_t, A_t)\\)) zegt ons hoe goed actie \\(A_t\\) is in toestand \\(T_t\\). Er zijn verschillende manieren om deze \\(Q\\)-functie voor te stellen. Een van de eenvoudigste manieren is aan de hand van een tabel. Voor elke mogelijk toestand in onze wereld voegen we een rij toe aan de tabel, voor elke mogelijke actie in de wereld voegen we een kolom toe. Op onderstaande figuur zie je een Q-tabel voor 5 acties en 7 toestanden. De waarde in de tabel zegt hoe goed de actie bovenaan de kolom is wanneer de agent in de toestand links van de rij zit. Op de afbeelding zie je links bovenaan hoe goed actie 2 is in toestand 3.

![](img/q_table_example.png)

Via deze tabel kunnen we een bepaald beleid/policy uitvoeren. Het beleid kan bijvoorbeeld zijn om in elke toestand de actie te kiezen met de hoogst mogelijke Q waarde.

<div class="dwengo-content assignment">
<h2 class="title">Opdracht</h2>
<div class="content">
Gegeven de Q-tabel en het beleid die we hierboven hebben beschreven, welke actie zal de agent uitvoeren wanneer deze in toestand 6 zit?
</div>
</div>

<div class="dwengo-content sideinfo">
<h2 class="title">De <code class="language-python">argmax</code> functie</h2>
<div class="content">
Wanneer we in de Q-tabel de beste actie willen selecteren in de huidige toestand, dan kijken we eerst welke rij overeenkomt met deze toestand. In deze rij gaan we op zoek naar de beste actie. Deze actie komt overeen met de index van de hoogste waarde in de rij. Om deze index te vinden, kan je in Python gebruik maken van de <code class="language-python">argmax()</code> functie. 
</div>
</div>

 