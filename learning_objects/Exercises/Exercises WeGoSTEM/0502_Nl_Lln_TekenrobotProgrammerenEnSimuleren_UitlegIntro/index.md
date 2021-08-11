---
hruid: Uitleg programmeren in de simulatie-v1.0.00
version: 1
language: nl
title: Uitleg programmeren in de simulatie
description: Uitleg
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

# 1. DwenguinoBlockly, een programmeeromgeving

De programmeeromgeving met simulator is online beschikbaar op [https://www.dwengo.org/dwenguinoblockly](https://www.dwengo.org/dwenguinoblockly "link simulator").

Hieronder zie je een screenshot van de omgeving met de beschrijving van de verschillende onderdelen.

![alt](https://scholen.dwengo.org/static/screenshotspirograafgenummerd.png "Onderdelen simulator")


1. De *toolbox*: In dit menu vind je de veerschillende codeblokken terug. Het menu is opgedeeld volgens categorieën die elk een specifieke soort van blokken bevatten. De belangrijkste categorie is 
![alt](https://scholen.dwengo.org/static/dwenguino.png "Afb. Dwenguino"). In deze categorie kan je alle blokken vinden om de tekenrobot te besturen.

2. Het *codeveld*: Hier staat het programma dat je maakt. Het 'zet klaar/herhaal'-blok staat er al klaar.

[alt](https://scholen.dwengo.org/static/zetklaarherhaal.png "Afb. zetklaarherhaal")

Alle code komt ofwel in het ‘zet klaar’-gedeelte van dit blok ofwel in het ‘herhaal’-gedeelte. Code op een andere plaats wordt niet uitgevoerd. Dus om te programmeren sleep je blokken uit de toolbox naar het codeveld en klik je deze vast in het ‘zet klaar / herhaal’-blok. 

3. Het *hoofdmenu*: Met dit menu kan je acties uitvoeren zoals je code opslaan (met 
![alt](https://scholen.dwengo.org/static/download.png "Afb. Download")
), terug inladen (met 
![alt](https://scholen.dwengo.org/static/upload.png "Afb. Upload")
of de simulatieomgeving openen of sluiten (met 
![alt](https://scholen.dwengo.org/static/dashboard.png "Afb. Simulatieomgeving")
.

4. Het *simulatormenu*: Dit menu gebruik je om je code uit te voeren in de simulatieomgeving, door hier te drukken op de afspeelknop
![alt](https://scholen.dwengo.org/static/play.png "Afb. Play")
. De simulatie stoppen doe je met 
![alt](https://scholen.dwengo.org/static/stop.png "Afb. Stop")
. Het laat je ook toe om een specifiek scenario te kiezen waarbinnen je je code wil uitvoeren. 

5. Het *simulatieveld*: In dit venster zie je een virtuele robot en vaak ook een virtueel microcontrollerbord, de Dwenguino, waarop je je code kan uitvoeren. Op de afbeelding is het scenario van de tekenrobot geselecteerd. Bovenaan zie je een virtueel Dwenguino-bord, onderaan een virtuele tekenrobot die je kan programmeren.