---
hruid: g_startpagina
version: 3
language: nl
title: "Introductie"
description: "Introductie"
keywords: ["oefeningen"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-vaktaal'
]
teacher_exclusive: false
---
# DwenguinoBlockly  
## Een programmeeromgeving

De programmeeromgeving met simulator is online beschikbaar op [https://blockly.dwengo.org](https://blockly.dwengo.org "link simulator").

Hieronder zie je een screenshot van de omgeving met een beschrijving van de verschillende onderdelen.

![](embed/simulator.png "Onderdelen simulator")



1. De *toolbox*: In dit menu vind je de verschillende codeblokken terug. Het menu is opgedeeld volgens categorieën die elk een specifieke soort van blokken bevatten. In ![alt](embed/cat_invoer.png "categorie invoer") kan je bijvoorbeeld alle blokken vinden die iets met invoer (input) te maken hebben.

2. Het *codeveld*: Hier staat het programma dat je maakt. Het *'zet klaar/herhaal'-blok* staat er al klaar. 

![alt](embed/zetklaarherhaal.png "Afb. zet klaar/herhaal")

> Enkel code die in het ‘zet klaar’- en 'herhaal'-gedeelte van dit blok geplaatst is, wordt uitgevoerd. Code op een andere plaats wordt niet uitgevoerd. Om te programmeren sleep je dus blokken uit de toolbox naar het codeveld en klik je deze vast in het *‘zet klaar/herhaal’-blok*. 

3. Het *hoofdmenu*: Met dit menu kan je acties uitvoeren zoals je code opslaan (met ![alt](embed/menu_download.png "menu download")), terug inladen (met ![alt](embed/menu_upload.png "menu upload")), of de simulatieomgeving openen en sluiten (met ![alt](embed/menu_hide.png "menu verbergen")).

4. Het *simulatormenu*: Hier vind je de knoppen terug om de simulatie te starten en te stoppen met de knoppen ![alt](embed/simmenu_play.png "simulator play") en ![alt](embed/simmenu_stop.png "simulator stop"). Het laat je ook toe om een specifiek scenario te kiezen waarbinnen je de code wil uitvoeren. 

5. Het *simulatievenster*: In dit venster zie je een virtuele robot en vaak ook een virtueel microcontrollerbord, de Dwenguino, waarop je de code kan uitvoeren. Op de afbeelding is het scenario van de tekenrobot geselecteerd. Bovenaan zie je een virtueel Dwenguino-bord, onderaan een virtuele tekenrobot die je kan programmeren.


In de toolbox kan je dus de blokken terugvinden die je nodig hebt om programma's te maken. Deze blokken moet je hieruit slepen om nadien vast te klikken in de gewenste volgorde.

Doorheen de oefeningen zullen er voor nieuwe blokken verwijzingen staan naar de plaats in de toolbox waar je deze kan terugvinden. Een voorbeeld van zo'n verwijzing is ![alt](embed/cat_dwenguino.png "categorie dwenguino") .