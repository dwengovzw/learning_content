---
hruid: stem5_2
version: 3
language: nl
title: "Exponentiële groei"
description: "Exponentiële groei"
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
# Rupsenuitbraak modelleren met een exponentiële functie

## Situatie afhankelijk van de waarde van de groeifactor

De groeifactor $a$ stelt het gemiddeld aantal nakomelingen per rups voor. We werken met gemiddelden, dus kommagetallen zijn toegestaan, maar negatieve getallen houden geen steek.

-  Als $a<1$, dan brengt elke rups minder dan één rups voort per generatie. In elke tijdstap wordt de populatie kleiner en kleiner tot ze uiteindelijk uitsterft. Je hebt dan te maken met een exponentiële **afname**.
-  Als $a>1$, zal elke rups aanleiding geven tot meer dan één nieuwe rups in de volgende generatie. De populatie zal groeien. Je hebt dan te maken met een exponentiële **toename**.
-  In het randgeval waarbij $a = 1$, dan is de populatiegrootte **stabiel**: de geboorte van nieuwe rupsen compenseert de sterfte.

-----------------------------
## Draagkracht 

In de **notebook** wordt de grafiek getekend van de exponentiële functie die de evolutie van de grootte van de rupsenpopulatie modelleert. <br>
De plaag groeit erg snel, wat verontrustend is. Als ze nog verder in de tijd kijken, stellen ze het volgende vast: de populatiegrootte groeit zonder enige belemmering verder aan. Na 50 generaties zijn er meer dan 29 000 000 000 000 rupsen. Als je aanneemt dat één rups ongeveer 3 gram weegt, zijn er na 50 generaties meer dan 87 miljoen ton rupsen, het equivalent van 40 miljoen nijlpaarden. Er zijn bijlange niet genoeg buxushagen in de wereld om dergelijke populaties te ondersteunen!

In de praktijk heeft elk ecosystem een bepaalde **draagkracht**, de hoeveelheden voedsel, water en ruimte die voorhanden zijn om een bepaalde populatie te ondersteunen. Onze rupsenpopulatie is gelimiteerd door het aantal planten dat beschikbaar is als voedsel. De draagkracht wordt vaak voorgesteld door de letter $K$.<br>
$K = 1000$ zou betekenen dat een tuin genoeg buxussen heeft om 1000 rupsen te voeden, maar niet meer. <br>
In het volgende onderdeel wordt het model aangepast om rekening te houden met de draagkracht.
