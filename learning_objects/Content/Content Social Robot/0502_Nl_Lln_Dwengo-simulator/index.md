---
hruid: Dwengo_simulator-v1
version: 3
language: nl
title: Dwengo simulator
description: Dwengo simulator
keywords: [sociale robot]
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

## Dwengo-simulator

Het ontwerpen en programmeren van de robot gebeurt in de Dwengo-simulator. De nieuwste versie van de programmeeromgeving met simulator is online beschikbaar op [https://blockly-backend.dwengo.org/](https://blockly-backend.dwengo.org/ "link naar simulator"). Momenteel wordt de simulator ondersteund op de meest recente versies van Google Chrome en Firefox.

![](@youtube/https://www.youtube.com/embed/PhblfDjUXPQ "Wegwijs in de simulator")


Hieronder zie je een screenshot van de omgeving met de beschrijving van de verschillende onderdelen.


**Afbeelding simulator**


### Onderdelen

1. **Toolbox**. In dit menu vind je de verschillende codeblokken terug. Het menu is opgedeeld volgens categorieën die elk een specifieke soort van blokken bevatten.

De belangrijkste categorieën zijn **AfbeeldingDwenguino** en **Afbeelding Sociale robot**. In deze categorieën kan je alle blokken vinden om de specifieke sensoren en actuatoren van de sociale robot te programmeren. Daarnaast kan je blokken uit de andere categorieën gebruiken voor extra functionaliteit.

2. **Codeveld**. Hierstaat het programma dat je maakt. Het *'zet klaar/herhaal'-blok* staat er al klaar. Je breidt het programma uit door blokken uit de toolbox naar het codeveld te slepen. Alle code komt ofwel in het 'zet klaar'-gedeelte van dit blok ofwel in het 'herhaal'-gedeelte. Code op een andere plaats wordt niet uitgevoerd. Dus om te programmeren sleep je blokken uit de toolbox naar het codeveld en klik je deze vast in het *'zet klaar/herhaal'-blok*.

3. **Hoofdmenu** Met dit menu kan je acties uitvoeren zoals je code opslaan (met **knop download**) of terug inladen (met **knop upload**) of de simulatieomgeving openen of sluiten (met **knop snelheidsmeter?**). Als je Dwenguino verbonden is met de computer, kan je het programma ook uploaden naar het bordje via de knop **knop uploaden dwenguino**.

4. **Simulatormenu**. Dit menu gebruik je om je code uit te voeren in de simulatieomgeving, door hier te drukken op de afspeelknop **knop play**. De simulatie stoppen doe je met **knop stop**. Het laat je ook toe om een specifiek scenario te kiezen waarbinnen je je code wil uitvoeren. Op de afbeelding is het scenario van de tekenrobot geselecteerd. Klik op **knop SR** om het scenario van de sociale robot te openen en op **knop RR** voor het scenario met de rijdende robot.

5. **Simulatieveld**. In dit venster zie je telkens de simulatie die bij het geselecteerde scenario hoort.