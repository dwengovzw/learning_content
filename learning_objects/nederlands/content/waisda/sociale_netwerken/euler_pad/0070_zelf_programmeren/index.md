---
hruid: org-dwengo-waisda-soc-netwerken-graaf-zelf-programmeren
version: 1
language: nl
title: "Zelf programmeren"
description: "Hoe stel ik een graaf voor op de computer en hoe kan ik het euleriaans pad vinden in die graaf?"
keywords: ["grafen","Euleriaans pad", "koningsbergen", "voorstellingen", "python"]
content_type: "text/markdown"
estimated_time: 50
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# Zelf grafen programmeren

Je weet intussen hoe je een graaf kan voorstellen op de computer en wat een Euleriaans pad is in die graaf. In de volgende notebook ga je zelf aan de slag met verschillende grafen. Je zal ze voorstellen aan de hand van hun adjacentielijst, controleren of ze een euleriaans pad bevatten en je zal dat pad zoeken aan de hand van het algoritme van Fleury.

[![](images/Knop.png "Knop")](https://kiks.ilabt.imec.be/hub/tmplogin?id=waisda_sociale_netwerken_euler "Notebook transfer learning")


<div class="dwengo-content sideinfo">
<h2 class="title">Grafen en AI</h2>
<div class="content">
De link tussen grafen en AI-systemen is misschien nog niet helemaal duidelijk. Toch worden grafen vaak gebruikt in AI-systemen omdat het goede manier is om informatie te structureren. We kunnen informatie en de verbanden ertussen bijvoorbeeld voorstellen met een <strong>kennisgraaf</strong> (<strong>knowledge graph</strong> in het Engels). <br>
Alle informatie op Wikipedia kunnen we bijvoorbeeld voorstellen met zo'n kennisgraaf. De artikels zijn dan de knopen van de graaf en de bogen van de graaf zijn de hyperlinks tussen de artikels. <br>
Ook informatie van sociale netwerken kan je voorstellen aan de hand van een graaf, de **social graph**. In een social graph zijn de knopen bijvoorbeeld personen. Als twee personen bevriend zijn, dan is er een boog in de graaf die hen verbindt. 
</div>
</div>