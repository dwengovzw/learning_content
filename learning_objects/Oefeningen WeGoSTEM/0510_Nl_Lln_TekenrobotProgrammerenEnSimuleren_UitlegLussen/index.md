---
hruid: Uitleg lussen-v1.0.00
version: 1
language: nl
title: Uitleg lussen
description: Uitleg lussen
keywords: [voorbeeld, voorbeeld2]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [4, 3]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
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