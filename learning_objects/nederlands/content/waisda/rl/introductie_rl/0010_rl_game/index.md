---
hruid: org-dwengo-waisda-rl-introductie-rl-explore-game
version: 1
language: nl
title: "Introductie"
description: "Maak kennis met reïnforcement learning."
keywords: ["AI", "reïnforcement learning"]
content_type: "text/markdown"
estimated_time: 2
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# Versterkend leren

Wanneer we het hebben over AI-systemen, hebben we het gewoonlijk over systemen die gebruik maken van de technieken van het machinaal leren. Bij machinaal leren gaat de computer zelf op zoek naar de regels om een bepaalde taak uit te voeren. In het [leerpad over het herkennen van emoties](https://dwengo.org/learning-path.html?hruid=org-dwengo-waisda-beelden-emoties-herkennen&language=nl&te=true&source_page=%2Fwaisda%2F&source_title=%20wAIsda?#org-dwengo-waisda-beelden-emoties-herkennen-intro;nl;1) leer je de computer bijvoorbeeld de regels om lachende en verbaasde smileys van elkaar te kunnen onderscheiden. In het [leerpad waarin je het murder mystery oplost](https://dwengo.org/learning-path.html?hruid=org-dwengo-waisda-taal-murder-mistery&language=nl&te=true&source_page=%2Fwaisda%2F&source_title=%20wAIsda?#org-dwengo-waisda-taal-murder-mystery-intro;nl;1) zoekt de computer de regels om de schrijfstijl van een persoon te detecteren. In alle twee de leerpaden maakte het algoritme gebruik van een dataset, bij het herkennen van emoties waren dat afbeeldingen, bij het detecteren van schrijfstijlen waren dat verschillende teksten. Veel van de AI-systemen die we vandaag de dag gebruiken, werken omdat ze geleerd hebben van grote hoeveelheden data. Maar hoeveel data is dat dan. Hieronder zie je de grootte van de datasets die nodig waren om bepaalde AI-systemen te trainen.

- Het ImageNet model dat achter de Teachable Machine van Google zit werd getraind met 1 281 167 trainingsafbeeldingen, 50 000 validatieafbeeldingen en 100 000 testafbeeldingen. ([https://www.image-net.org/download.php](https://www.image-net.org/download.php))
- GPT-3, de voorloper van ChatGPT werd onder andere getraind aan de hand van de CommonCrawl dataset. Dit is een open source dataset die de tekst bevat van meer dan 2,7 miljard websites ([https://commoncrawl.org/overview](https://commoncrawl.org/overview)). 
- Dall-e het model van OpenAI dat afbeeldingen kan genereren werd getraind met een dataset waarin ongeveer 650 miljoen afbeeldingen zitten ([zie OpenAI paper](https://arxiv.org/pdf/2204.06125)).