---
hruid: STD_Lkr_Wacht3-v1
version: 3
language: nl
title: "Voorbeeld Wacht 3"
description: "Voorbeeld Wacht 3"
keywords: ["StartToDwenguino", "wacht"]
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
### Voorbeeld Wacht

**Manier 2**

De tweede manier is om alle code te verplaatsen van het *'zet klaar'-deel* naar het *'herhaal'-deel*. Dan zal de computer simpelweg de code opnieuw uitvoeren eens ze allemaal uitgevoerd is.

![blockly](@learning-object/WACHTWGS3-v1/nl/3)

I.p.v. de code eenmalig uit te voeren, zal ze nu herhaald worden.  
  
Zoals je misschien al gemerkt hebt bij het uittesten van de voorbeelden, verwijdert het lcd-scherm tekst niet automatisch. Wanneer je oude tekst door nieuwe tekst vervangt, zonder de oude tekst eerst te verwijderen, worden enkel de gebruikte cellen aangepast:  

"Hallo mensen" (12 karakters) vervangen door "Ik ben Dwenguino" (16 karakters): "Ik ben Dwenguino"  
"Ik ben Dwenguino" (16 karakters) vervangen door "Hallo mensen" (12 karakters): "Hallo mensen**uino**"  

Omdat "Hallo mensen" 4 karakters korter is dan "Ik ben Dwenguino" zullen de laatste 4 cellen in het programma niet veranderen. "Ik ben Dweng" wordt dus overschreven door "Hallo mensen". "uino" blijft echter staan. Om dit probleem te voorkomen, zal je dus steeds het *MaakLCDLeeg-blok* moeten gebruiken.

*Test deze voorbeelden ook zelf uit in de simulator!*
