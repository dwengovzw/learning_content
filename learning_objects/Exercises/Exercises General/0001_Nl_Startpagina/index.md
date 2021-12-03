---
hruid: STD_Startpagina-v1
version: 3
language: nl
title: "StartToDwenguino"
description: "Beschrijving van de onderdelen van de simulator"
keywords: ["StartToDwenguino"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [10, 11, 12]
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
# WIP
# DwenguinoBlockly  
# Een programmeeromgeving

De programmeeromgeving met simulator is online beschikbaar op [https://www.dwengo.org/dwenguinoblockly](https://www.dwengo.org/dwenguinoblockly "link simulator").

Hieronder zie je een screenshot van de omgeving met de beschrijving van de verschillende onderdelen.

![](embed/Afb1.png "Onderdelen simulator")


1. De *toolbox*: In dit menu vind je de verschillende codeblokken terug. Het menu is opgedeeld volgens categorieën die elk een specifieke soort van blokken bevatten. In 
![alt](embed/Afb2.png "Afb. Dwenguino") kan je bijvoorbeeld alle blokken vinden om de tekenrobot te besturen.

2. Het *codeveld*: Hier staat het programma dat je maakt. Het *'zet klaar/herhaal'-blok* staat er al klaar.  
![alt](embed/Afb3.png "Afb. zetklaarherhaal")

Enkel code die in het ‘zet klaar’- en 'herhaal'-gedeelte van dit blok geplaatst is, wordt uitgevoerd. Code op een andere plaats wordt niet uitgevoerd. Om te programmeren sleep je dus blokken uit de toolbox naar het codeveld en klik je deze vast in het *‘zet klaar/herhaal’-blok*. 

3. Het *hoofdmenu*: Met dit menu kan je acties uitvoeren zoals je code opslaan (met 
![alt](embed/Afb4.png "Afb. Download")), terug inladen (met 
![alt](embed/Afb5.png "Afb. Upload")
), of de simulatieomgeving openen en sluiten (met 
![alt](embed/Afb6.png "Afb. Simulatieomgeving")
).

4. Het *simulatormenu*: Hier vind je de knoppen terug om de simulatie te starten en te stoppen met de knoppen 
![alt](embed/Afb7.png "Afb. Play")
 en 
![alt](embed/Afb8.png "Afb. Stop")
. Het laat je ook toe om een specifiek scenario te kiezen waarbinnen je je code wil uitvoeren. 

5. Het *simulatievenster*: In dit venster zie je een virtuele robot en vaak ook een virtueel microcontrollerbord, de Dwenguino, waarop je je code kan uitvoeren. Op de afbeelding is het scenario van de tekenrobot geselecteerd. Bovenaan zie je een virtueel Dwenguino-bord, onderaan een virtuele tekenrobot die je kan programmeren.


In de toolbox kan je dus de blokken terugvinden die je nodig hebt om programma's te maken. Deze blokken moet je hieruit slepen om nadien vast te klikken in de gewenste volgorde.

Doorheen de oefeningen zal er voor nieuwe blokken verwijzingen staan naar de plaats in de toolbox waar je deze kan terugvinden. Een voorbeeld van zo'n verwijzing is ![alt](embed/Afb2.png "Afb. Dwenguino") .