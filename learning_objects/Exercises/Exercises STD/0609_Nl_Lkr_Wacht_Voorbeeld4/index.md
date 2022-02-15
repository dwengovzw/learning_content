---
hruid: STD_Lkr_Wacht4-v1
version: 3
language: nl
title: "Voorbeeld Wacht 4"
description: "Voorbeeld Wacht 4"
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

OPGAVE 2

Maak een reclamebord voor de UGent en Dwengo. De namen moeten afwisselend verschijnen in een interval van 5 seconden. Zorg er ook voor dat de namen gecentreerd zijn.

Oplossing:

![blockly](@learning-object/WACHTWGS4-v1/nl/3)

Merk op dat het in principe niet nodig is om het *"MaakLCDLeeg"-blok* hier te gebruiken omdat de eerste uitdrukking uit 6 + 5 karakters (6 lege + Ugent) bestaat en de tweede uitdrukking uit 5 + 6 karakters (5 lege + Dwengo).

*Test deze voorbeelden ook zelf uit in de simulator!*
