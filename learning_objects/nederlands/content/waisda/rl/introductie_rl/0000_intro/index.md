---
hruid: org-dwengo-waisda-rl-introductie-rl-intro
version: 1
language: nl
title: "Introductie"
description: "Maak kennis met reïnforcement learning."
keywords: ["AI", "reïnforcement learning"]
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

# Leren uit gegevens

AI-systemen leren meestal door in gegevens op zoek te gaan naar regels en patronen. In het [leerpad over het herkennen van emoties](https://dwengo.org/learning-path.html?hruid=org-dwengo-waisda-beelden-emoties-herkennen&language=nl&te=true&source_page=%2Fwaisda%2F&source_title=%20wAIsda?#org-dwengo-waisda-beelden-emoties-herkennen-intro;nl;1) leert de computer bijvoorbeeld regels om lachende en verbaasde smileys van elkaar te kunnen onderscheiden. In het [leerpad waarin je het murder mystery oplost](https://dwengo.org/learning-path.html?hruid=org-dwengo-waisda-taal-murder-mistery&language=nl&te=true&source_page=%2Fwaisda%2F&source_title=%20wAIsda?#org-dwengo-waisda-taal-murder-mystery-intro;nl;1), zoekt de computer naar patronen in de schrijfstijl van de personages. In beide leerpaden maakte het algoritme gebruik van een dataset, bij het herkennen van emoties waren dat afbeeldingen, bij het detecteren van schrijfstijlen waren dat verschillende teksten. Veel van de AI-systemen die we vandaag de dag gebruiken, werken omdat ze geleerd hebben uit grote hoeveelheden data. Maar hoeveel data is dat dan? Hieronder zie je de grootte van de datasets die nodig waren om bepaalde AI-systemen te trainen.

- Het ImageNet model dat achter de Teachable Machine van Google zit, werd getraind met 1 281 167 trainingsafbeeldingen, 50 000 validatieafbeeldingen en 100 000 testafbeeldingen. ([https://www.image-net.org/download.php](https://www.image-net.org/download.php))
- GPT-3, de voorloper van ChatGPT werd onder andere getraind aan de hand van de CommonCrawl dataset. Dit is een open source dataset die de tekst bevat van meer dan 2,7 miljard websites ([https://commoncrawl.org/overview](https://commoncrawl.org/overview)). 
- Dall-e, het model van OpenAI dat afbeeldingen kan genereren, werd getraind met een dataset waarin ongeveer 650 miljoen afbeeldingen zitten ([zie OpenAI paper](https://arxiv.org/pdf/2204.06125)).

Je merkt dat AI-systemen enorme hoeveelheden gegevens nodig hebben om een taak te leren. Dat staat in sterk contrast met hoe wij als mens leren. Mensen slagen erin om te leren zonder miljoenen tot miljarden voorbeelden te moeten zien. Denk bijvoorbeeld aan een baby die leert kruipen. De baby is in staat om zelfs zonder ooit voorbeelden gezien te hebben te leren kruipen<sup>(1)</sup>. Als mens gebruiken we dus andere technieken om te leren dan de technieken die de meeste AI-systemen gebruiken. 

De manier waarop mensen leren, heeft computerwetenschappers geïnspireerd om AI-systemen te ontwikkelen die niet leren op basis van grote hoeveelheden gegevens, maar wel op basis van de interactie met hun omgeving. Deze systemen maken gebruik van **versterkend leren**. In dit leerpad maak je kennis met de basisprincipes van het **versterkend leren**.




(1) Adolph, Karen E., and John M. Franchak. "The development of motor behavior." Wiley Interdisciplinary Reviews: Cognitive Science 8.1-2 (2017): e1430.