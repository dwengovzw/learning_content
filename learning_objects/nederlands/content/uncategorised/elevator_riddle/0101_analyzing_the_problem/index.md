---
hruid: org-dwengo-elevator-riddle-analyzing-1
version: 1
language: nl
title: "Analyse van het probleem"
description: "Voor we een probleem kunnen oplossen met de computer, gebruiken we computationeel denken om het probleem te vertalen naar een vorm die de computer begrijpt."
keywords: ["grafen", "algoritme", "computationeel denken", "clustering"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
difficulty: 5
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---

# Analyse van het probleem

In een eerste fase proberen we alle overbodige informatie die niet nodig is om het probleem op te lossen, weg te laten. Door deze abstractie kunnen we focussen op de informatie die relevant is om het probleem op te lossen. Hiervoor kijken we naar de vraagstelling:

> Op welke verdiepingen moet elk van de privéliften stoppen om ervoor te zorgen dat zo weinig mogelijk mensen de trap moeten nemen?

In de vraagstelling gaat het enkel over de privéliften, de informatie over de gemeenschappelijke lift is dus niet relevant. In de vraagstelling wordt er ook vanuit gegaan dat er al twee privéliften zijn die elk op hun eigen vier verdiepingen stoppen. We moeten ons dus geen zorgen meer maken over hoe die lift geïnstalleerd moet worden of welke strategie we moeten gebruiken om de liften efficiënt in te zetten. De essentie van het vraagstuk is de opdeling van de verdiepingen in twee groepen. Om dit te doen baseren we ons op het historisch liftgebruik.

Bij het opdelen van de verdiepingen in twee groepen zullen bepaalde verplaatsingen sowieso met de trap moeten gebeuren. Ons doel is om deze verplaatsingen te minimaliseren. Daarvoor baseren we ons op de tabel met verplaatsingen.

| Van verdieping      | Naar verdieping |
| ----------- | ----------- |
| 4      | 8, 10, 10, 8, 6, 6        |
| 5   | 8, 8, 9, 9, 11, 11, 11, 9, 8         |
| 6   | 10, 8, 10, 4         |
| 7   | 10, 10, 11, 11, 11, 5, 11, 5, 9, 9, 5, 10, 10         |
| 8   | 5, 5, 4, 6, 4, 6, 5, 10, 10         |
| 9   | 5, 5, 11, 11, 7, 11, 7, 5         |
| 10   | 6, 8, 8, 7, 6, 7, 6         |
| 11   | 7, 5         |

De volgorde waarin de verplaatsingen gebeuren, is voor ons niet van belang. Wij willen enkel kijken naar hoeveel verplaatsingen er zijn tussen elke verdieping. Daarvoor kunnen we een tabel opstellen:

|  | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** |
| ----------- | ----------- |----------- | ----------- |----------- | ----------- |----------- | ----------- |----------- |
| **4** | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| **5** | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 3 | 
| **6** | 1 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 
| **7** | 0 | **3** | 0 | 0 | 0 | 2 | 4 | 4 | 
| **8** | 2 | 3 | 2 | 0 | 0 | 0 | 2 | 0 | 
| **9** | 0 | 3 | 0 | 2 | 0 | 0 | 0 | 3 | 
| **10** | 0 | 0 | 3 | 2 | 2 | 0 | 0 | 0 |
| **11** | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |

De tabel geeft het aantal verplaatsingen weer van de verdieping in de eerste kolom naar de verdieping0 in de eerste rij van de tabel. De cel in het vet op coordinaat (rij 7, kolom 5) stelt bijvoorbeeld het aantal verplaatsingen tussen verdieping zeven en vijf voor (= 3).
Merk op dat deze verplaatsingen ook de richting aangeven. Er zijn bijvoorbeeld twee verplaatsingen van verdieping zeven naar verdieping negen maar ook twee verplaatsingen van verdieping negen naar zeven. De richting van de verplaatsing is voor ons niet van belang, enkel het aantal verplaatsingen. Deze overbodige informatie laten we weg om het probleem te vereenvoudigen (**abstractie**). We kunnen onze tabel dus omvormen naar een bovendriehoeksmatrix door de verplaatsingen tussen dezelfde verdiepingen op te tellen. Dan krijgen we de volgende tabel:

|  | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** |
| ----------- | ----------- |----------- | ----------- |----------- | ----------- |----------- | ----------- |----------- |
| **4** | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| **5** | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 3 | 
| **6** | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 
| **7** | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 4 | 
| **8** | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 
| **9** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 
| **10** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **11** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |