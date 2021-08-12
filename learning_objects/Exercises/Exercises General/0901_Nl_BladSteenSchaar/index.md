---
hruid: BladSteenSchaar-v1.0.1
version: 1
language: nl
title: Blad Steen Schaar
description: De leerlingen programmeren de Dwenguino om blad-steen-schaar te spelen.
keywords: [LCD, buttons, ifelse]
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

## Blad-Steen-Schaar

Programmeer 2 Dwenguinos om Blad-Steen-Schaar te spelen. Zorg ervoor dat je programma aan de onderstaande criteria voldoet!

* Op het LCD-scherm verschijnt er een startscherm dat toont welke knoppen overeenkomen met blad, steen en schaar.

* De knoppen zijn als volgt geprogrammeerd: 
Noord: Blad
Midden: Steen
Zuid: Schaar

* Er is een wachttijd van 2 seconden tussen het maken van de keuze en het tonen van die keuze.

* Je kan terugkeren naar het startscherm door de Oost- en Westknop tegelijk in te drukken.