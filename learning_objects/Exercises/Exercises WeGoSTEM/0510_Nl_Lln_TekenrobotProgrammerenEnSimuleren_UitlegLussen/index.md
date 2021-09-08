---
hruid: UitlegLussen-v1
version: 1
language: nl
title: Uitleg lussen
description: Uitleg lussen
keywords: [WeGoSTEM, lus]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [10, 11, 12, 13, 14]
difficulty: 3
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', 
    'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso'
]
teacher_exclusive: false
---

# 5. Lussen

*Een lus is een structuur waarbij een bepaald stuk code een aantal keer of voortdurend herhaald zal worden.* We spreken van een **herhalingslus**.

Als je code in het ‘**herhaal**’-gedeelte van het ‘zet klaar / herhaal’-blok plaatst, dan maak je eigenlijk gebruik van een lus. De code daar wordt voortdurend herhaald.

Wil je echter dat de code slechts een bepaald aantal keer wordt herhaald, dan gebruik je het blok voor een ‘**beperkte herhaling**’:

![alt](https://scholen.dwengo.org/static/forlus.png "Afb. Lussen")

Met dit blok zal de code die in het blok staat, tien keer uitgevoerd worden. Het aantal keer dat de lus de code uitvoert, kan je aanpassen aan de hand van drie waarden: de beginwaarde (hier 0), de eindwaarde (hier 9) en met hoeveel de waarde zal veranderen telkens de lus één keer doorlopen is (hier 1). 

Hieronder zie je nog een voorbeeld van een beperkte herhaling, deze lus zal de code 5 keer uitvoeren:

![alt](https://scholen.dwengo.org/static/forlus2.png "Afb. Lussen")

We zetten de gepaste code hierin als we LED 5 op het Dwenguino-bord exact vijf keer willen laten knipperen en het knipperen dus moet stoppen:

![alt](https://scholen.dwengo.org/static/forlus3.png "Afb. Lussen")