---
hruid: Problemen-v1.0.0
version: 1
language: nl
title: Problemen
description: Vaak voorkomende problemen
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

## Vaak voorkomende problemen

### Het lcd-scherm toont geen tekst

* Pas het contrast van het lcd-scherm aan via het gele schroefje op de Dwenguino microcontroller (zie **6. Robotassemblage > Bedrading**)

### De sonar-sensor werkt niet

* Het gebeurt af en toe dat een sensor kapot is. Probeer na te gaan of dit het geval is door de aansluitingen van de sonar-sensor na te kijken en de gemeten waarde van de sensor weer te geven op het lcd-scherm. Er zitten extra vervangingssensoren in het pakket.