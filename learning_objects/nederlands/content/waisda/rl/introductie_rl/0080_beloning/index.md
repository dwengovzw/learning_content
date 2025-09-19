---
hruid: org-dwengo-waisda-rl-introductie-beloning-policy-waarde
version: 1
language: nl
title: "Beloning, policy en waardefunctie"
description: "Maak kennis met reïnforcement learning."
keywords: ["AI", "reïnforcement learning", "beloning"]
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

# Beloning

Bij versterkend leren is de beloning het belangrijkste instrument om ervoor te zorgen dat de **agent** iets kan leren. De beloning die de **agent** krijgt, hangt af van de **actie** die deze uitvoerde en de huidige **toestand** van de **omgeving**. We spreken bij versterken leren altijd van een **beloning**. Je kan de **agent** ook bestraffen, dat komt overeen met het geven van een negatieve beloning.

Wanneer we een **agent** trainen met versterkend leren is het hoofddoel van de agent om de beloningen die deze krijgt te maximaliseren. In ons spel komt dit overeen met het halen van een zo hoog mogelijke score. De score is immers de som van alle vorige beloningen.

# De policy / het beleid

De **policy** ofwel het beleid legt vast welke **actie** de **agent** gaat uitvoeren in een bepaalde **toestand**. De **policy** bepaalt dus hoe de **agent** zich gedraagt. Bij versterkend leren willen we een optimale **policy** leren om een bepaalde taak uit te voeren. 

In het spel bedenk jij een **policy** waarmee je een zo hoog mogelijke score probeert te halen. De **policy** kan bijvoorbeeld zijn om ervoor te zorgen dat de twee getallen op het scherm altijd gelijk zijn. Een andere policy zou kunnen zijn om ervoor te proberen zorgen dat de som van de twee getallen steeds 14 is. 

Wanneer je een **policy** toepast, krijg je daarvoor een beloning. Is die beloning positief, dan versterkt dat je overtuiging dat je huidige gedrag goed is. Is de beloning negatief, dan zal dat je aanzetten om je gedrag te veranderen en je **policy** dus aan te passen.

# De waardefunctie

De **waardefunctie** geeft ons een schatting van hoe groot de **beloning** is die je bij het toepassen van een bepaalde **policy** op lange termijn mag verwachten wanneer je een bepaalde **actie** uitvoert in een bepaalde **toestand**. Deze definitie is nogal abstract. Door de koppeling te maken met het Pong spel dat je speelde is het makkelijker om te begrijpen waarvoor de waardefunctie dient.

- Stel we spelen het spel en starten met een score 0.
- We bedenken een **policy** waarbij we ervoor zorgen dat de twee getallen op het scherm steeds dezelfde waarde hebben.
- Elke **actie** die we uitvoeren (naar boven gaan, naar beneden gaan of blijven staan) kan een beloning opleveren. Die beloning is +25 wanneer we de bal raken, -10 wanneer we de bal missen en 0 wanneer de bal zich ergens anders op het veld bevind. 
- Wanneer het palet op positie 5 staat en de bal op coördinaat (6, 4) zullen we het palet naar beneden bewegen. We krijgen in dat geval echter een **beloning** van 0. We weten dus niet of onze **actie** goed of slecht was. De **beloning** komt er immers pas wanneer we de bal raken.
- Om op elk moment toch een inschatting te kunnen maken van hoe goed een **actie** is, gebruiken we de **waardefunctie**. Deze **waardefunctie** zal in elke **toestand** een inschatting maken van hoe goed een **actie** is in die **toestand**. De **waardefunctie** geeft een schatting van de **beloning** die we op lange termijn zullen krijgen door een **actie** uit te voeren, rekening houdende met de **policy** die we gekozen hadden (hier om de getallen gelijk te houden).

De policy en de waardefunctie zijn sterk met elkaar verbonden. De policy zegt **wat de agent moet doen** en de waardefunctie zegt **hoe goed dat is**.
