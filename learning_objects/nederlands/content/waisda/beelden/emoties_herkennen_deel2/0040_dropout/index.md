---
hruid: org-dwengo-waisda-beelden-emoties-deel2-dropout
version: 1
language: nl
title: "Dropout"
description: "Wat is max dropout?"
keywords: ["lagen", "AI", "neurale netwerken", "dropout"]
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

# Dropout

De **dropout** laag zal elk element in de invoer met een kans van \\(p\\) op nul zetten. Hieronder zie je een voorbeeld van hoe het effect van de dropout laag eruit kan zien.

!["Voorbeeld van dropout"](img/dropout.png)

Er zijn verschillende redenen waarom je dropout toepast.

- **Beschermt tegen overfitting**: Omdat je tijdens het trainen telkens andere willekeurige pixels op nul zet, zal het moeilijker zijn voor het netwerk om de trainingsverzameling van buiten te leren. Het gaat dus overfitting tegen.
- **Redundantie in geleerde eigenschappen**: Omdat je telkens ander pixels weglaat, zal het netwerk meerdere manieren moeten leren om bepaalde eigenschappen te herkennen. Je creëert als het ware "backup redeneringen" om bepaalde objecten te herkennen.
- **Model generaliseert beter**: Dropout introduceert willekeurige variaties in de invoerafbeeldingen. Daardoor kan het getrainde netwerk beter omgaan met afbeeldingen die het nog niet gezien heeft. 


<div class="dwengo-content important">
<h2 class="title">Dropout</h2>
<div class="content">
Dropout wordt enkel toegepast tijdens het trainen van het netwerk. Eens het netwerk getraind is, zal deze laag geen waarden meer op nul zetten. 
</div>
</div>

