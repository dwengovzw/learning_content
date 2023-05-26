---
hruid: ct_10_7
version: 3
language: nl
title: "Toevalsprenten: Abstractie en algoritme"
description: "Toevalsprenten: Abstractie en algoritme"
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
# Voorbeeld 7:  Abstractie en algoritme
Bron: [het online platform van de Belgische Bebras-wedstrijd](https://bebras.ugent.be/)<br>
Tekst: Kris Coolsaet, BE<br>
Afbeeldingen: Kris Coolsaet, BE 

## Toevalsprenten (Bebras ...)

De bevers hebben een klein bedrijfje dat gepersonaliseerde wenskaarten en geschenkpapier ontwerpt. De verschillende modellen worden gemaakt aan de hand van de volgende instructies:

1. Maak een cirkel C aan van een willekeurige kleur.
2. Herhaal de volgende stappen een willekeurig aantal keer.<br>
&nbsp;&nbsp;&nbsp;&nbsp;1. Maak een vierkant V aan van een willekeurige kleur en grootte.<br>
&nbsp;&nbsp;&nbsp;&nbsp;2. Kies een willekeurige grootte voor C: ofwel *klein*, ofwel *groot*.<br>
&nbsp;&nbsp;&nbsp;&nbsp;3. Druk C af, ergens op een willekeurige plaats.<br>
&nbsp;&nbsp;&nbsp;&nbsp;4. Druk V af, ergens op een willekeurige plaats.<br>

(Ter informatie: een vorm aanmaken betekent dat de vorm in het computergeheugen wordt aangemaakt, maar niet dat hij ook op papier wordt afgedrukt of getekend.)

*Welke van de volgende modellen werd niet door dit bedrijfje ontworpen?*

![Toevalsprenten](embed/bebrasabstractie2.png "Bebras Toevalsprent")

##### Oplossing

Het volgende model kan niet door dit bedrijfje zijn gemaakt:

![Toevalsprenten](embed/bebrasabstractie2oplossing.png "Bebras Toevalsprent oplossing")

##### Bespreking

Deze afbeelding bevat twee cirkels van verschillende grootte en van een verschillende kleur. In het algoritme wordt de kleur van de cirkel slechts één keer bepaald, namelijk helemaal in het begin; nadien kunnen de cirkels nog wel van grootte veranderen, maar niet van kleur.<br>
Alle andere antwoorden zijn mogelijke ontwerpen, ook al is dat misschien niet meteen duidelijk. Er moeten evenveel cirkels als vierkanten worden afgedrukt, maar het is best mogelijk dat een vierkant bovenop een cirkel wordt gedrukt en deze op die manier verbergt! Hou er ook rekening mee dat een cirkel of een vierkant toevallig dezelfde kleur kan hebben als de achtergrond.

Je moet het **algoritme** in voldoende mate kunnen toepassen. Als je inziet dat alle cirkels dezelfde kleur moeten hebben, dan heb je **abstractie** gemaakt van de instructies in het **algoritme**. Weten dat alle cirkels dezelfde kleur moeten hebben, is het enige dat van belang is om het antwoord te kunnen geven op de gestelde vraag. Je gebruikt eigenlijk slechts een deel van het algoritme. 
