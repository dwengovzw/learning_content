---
hruid: org-dwengo-waisda-beelden-teachable-machine-example
version: 1
language: nl
title: "Teachable Machine"
description: "Hoe werkt de Teachable Machine van Google."
keywords: ["Neurale netwerken", "Imagenet", "Teachable machine", "fine tuning"]
content_type: "text/markdown"
estimated_time: 20
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY Dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# Google Teachable Machine

Op [https://teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com) stelt Google een applicatie ter beschikking om een *machine learning*-model voor classificatie af te stemmen op jouw eigen doel. Je kan er eigen afbeeldingen uploaden om een AI-systeem te **tunen**. Je kan bijvoorbeeld een aantal afbeeldingen van katten en honden uploaden om zo een systeem te bekomen dat afbeeldingen van alle katten en honden van elkaar kan onderscheiden.

## Misconceptie

Een algemene misconceptie is dat de Teachable Machine een volledig nieuw AI-systeem zal trainen op basis van jouw data. **Dit klopt niet!** Wat het systeem eigenlijk doet is een **bestaand model**, dat al getraind is om heel wat objecten te kunnen detecteren, **bijtrainen** om een zo goed mogelijke classificatie van jouw objecten te maken. Zonder gebruik te maken van een voorgetraind model zou het nooit lukken om een systeem te trainen met maar een beperkt aantal afbeeldingen. Het zou ook nooit lukken in een korte tijdspanne.


<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        <ul>
            <li>Zoek een aantal objecten van twee types. Bijvoorbeeld vijf balpennen en vijf boeken.</li>
            <li>Bezoek <a href="https://teachablemachine.withgoogle.com">https://teachablemachine.withgoogle.com</a>.</li>
            <li>Maak een nieuw project voor afbeeldingen; kies het standaardmodel.</li>
            <li>Voeg een klasse (class) toe voor de afbeeldingen van de balpennen. Gebruik de webcam om van elke balpen een foto te nemen of laad een aantal bestaande afbeeldingen van balpennen op.</li>
            <li>Voeg een tweede klasse toe voor de afbeeldingen van de boeken. Maak opnieuw foto's met de webcam of laad een aantal bestaande afbeeldingen van boeken op.</li>
            <li>Klik op <strong>Model trainen</strong>.</li>
            <li>Zoek ondertussen nog een aantal extra balpennen en boeken.</li>
            <li>Wanneer het model klaar is met trainen, kan je het testen. Gebruik de webcam en toon een van de extra voorwerpen die je bent gaan halen. Kan het systeem de voorwerpen correct classificeren?</li>
            <li>Probeer ook eens een ander soort voorwerp. Wat is het resultaat?</li>
        </ul>
    </div>
</div>
