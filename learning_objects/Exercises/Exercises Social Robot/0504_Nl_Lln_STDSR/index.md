---
hruid: SR_STD-v1
version: 3
language: nl
title: "Onderdelen simulator"
description: "Dwengo simulator"
keywords: ["Sociale Robot", "AI Op School", "STEM", "Computationeel denken", "Grafisch programmeren"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', 
    'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso'
]
teacher_exclusive: false
---
# Simulator
## Onderdelen simulator

Het ontwerpen en programmeren van de robot gebeurt in de Dwengo-simulator. Je vindt de online programmeeromgeving met simulator via de knop 'Simulator' rechtsbovenaan in dit leerpad. Momenteel wordt de simulator ondersteund op de meest recente versies van Google Chrome en Firefox. Het volgende filmpje vat het gebruik van de simulator samen. Onder het filmpje vind je de verschillende aspecten nog eens uitvoerig uitgelegd.

![](@youtube/https://www.youtube.com/embed/PhblfDjUXPQ "Wegwijs in de simulator")


Hieronder zie je een screenshot van de omgeving met de beschrijving van de verschillende onderdelen.  
    

![](embed/Afb1.png "Onderdelen simulator")


1. De *toolbox*: In dit menu vind je de verschillende codeblokken terug. Het menu is opgedeeld volgens categorieën die elk een specifieke soort van blokken bevatten. In 
![alt](embed/Afb2.png "Afb. Dwenguino") vind je bijvoorbeeld het *'wacht'-blok* terug.

2. Het *codeveld*: Hier staat het programma dat je maakt. Het *'zet klaar/herhaal'-blok* staat er al klaar.  
![alt](embed/Afb3.png "Afb. zetklaarherhaal")

Enkel code die in het ‘zet klaar’- of het 'herhaal'-gedeelte van dit blok geplaatst is, wordt uitgevoerd. Code op een andere plaats wordt niet uitgevoerd.  
Om te programmeren sleep je dus blokken uit de toolbox naar het codeveld en klik je deze in de gewenste volgorde vast in het *‘zet klaar/herhaal’-blok*. 

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
. Het laat je ook toe om een specifiek scenario te kiezen waarbinnen je je code wil uitvoeren; op de figuur is het scenario van de tekenrobot geselecteerd.

5. Het *simulatievenster*: In dit venster zie je een virtuele robot en vaak ook een virtueel microcontrollerbord, de Dwenguino, waarop je je code kan uitvoeren. Op de afbeelding is het scenario van de tekenrobot geselecteerd. Bovenaan zie je een virtueel Dwenguino-bord, onderaan een virtuele tekenrobot die je kan programmeren.

Om een programma op te bouwen, zal je dus blokken uit de toolbox gebruiken. Doorheen de oefeningen zal er voor nieuwe blokken telkens worden aangegeven waar in de toolbox je deze terugvindt. Een voorbeeld van zo'n verwijzing is ![alt](embed/Afb2.png "Afb. Dwenguino") .