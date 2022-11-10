---
hruid: STD_WachtVB4-v1
version: 3
language: nl
title: "Voorbeeld Wacht 4"
description: "Voorbeeld Wacht 4"
keywords: ["StartToDwenguino", "wacht"]
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
### Voorbeeld Wacht

OPGAVE 2

Maak een reclamebord voor de UGent en Dwengo. De namen moeten afwisselend verschijnen in een interval van 5 seconden. Zorg er ook voor dat de namen gecentreerd zijn.

Oplossing:

![blockly](@learning-object/WACHTwgs4-v1/nl/3)

Merk op dat het in principe niet nodig is om het *"MaakLCDLeeg"-blok* hier te gebruiken omdat beide uitdrukkingen evenveel karakters bevatten; de eerste uitdrukking bestaat uit 6 + 5 karakters (6 lege + UGent) en de tweede uitdrukking bestaat uit 5 + 6 karakters (5 lege + Dwengo).

*Test deze voorbeelden ook zelf uit in de simulator!*
