---
hruid: ct_10_6
version: 3
language: nl
title: "Stormbestendig netwerk: Abstractie maken"
description: "Stormbestendig netwerk: Abstractie maken"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
# Voorbeeld 6:  Abstractie maken
Bron: [het online platform van de Belgische Bebras-wedstrijd](https://bebras.ugent.be/)<br>
Tekst: Zoltán Molnár, HU, Zsuzsa Pluhár, HU<br>
Afbeeldingen: Ivo Blöchliger, CH<br>
Vertaling: Kris Coolsaet 

## Stormbestendig netwerk (Bebras 2014-HU-02) 

De GSM-maatschappij Bever Telecom wil GSM-masten plaatsen op Windeneiland.<br>
Het dekkingsgebied van een mast is een cirkel die errond is gecentreerd. Twee masten heten *verbonden* met elkaar als hun dekkingsgebieden overlappen. Twee masten kunnen met elkaar *communiceren* als er een rij tussenliggende masten bestaat zodat elke mast met elke volgende is verbonden.<br>
Door de sterke wind op het eiland gebeurt het af en toe dat een mast breekt. Als er ergens één mast niet meer functioneert, willen we toch nog dat elke twee van de overblijvende torens met elkaar kunnen blijven communiceren.

*Welke van de opstellingen hieronder moeten we hiervoor gebruiken?*

![Stormbestendig netwerk](embed/bebrasabstractie.png "Bebras Abstractie maken")

##### Oplossing

Het juiste antwoord is B. 

![Stormbestendig netwerk](embed/bebrasabstractieoplossing.png "Bebras Stormbestendig netwerk oplossing")

##### Bespreking

In de afgebeelde opstellingen worden masten voorgesteld door punten en dekkingsgebieden door cirkels. Dit is een eerste **abstractie** die je correct moet interpreteren.

Om tot een oplossing te komen, voer je een **bijkomende abstractie** in door de overlappende cirkels te vervangen door een boog in een graaf: je verbindt twee masten met elkaar wanneer de overeenkomstige cirkels overlappen, en je verwijdert de cirkels. Dit is een cruciaal deel van het oplossingsproces.

Abstractie kan dus op twee verschillende manieren voorkomen in computationeel denken:
- een gegeven abstractie correct kunnen interpreteren;
- zelf tot een abstractie komen om een probleem gemakkelijker op te lossen.
