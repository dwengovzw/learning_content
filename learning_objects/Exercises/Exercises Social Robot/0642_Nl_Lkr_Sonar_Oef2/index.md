---
hruid: SR_SonarOef2-v1
version: 3
language: nl
title: "Voorbeeld sonar-sensor 2"
description: "Uitleg sonar-sensor"
keywords: ["StartToDwenguino", "sonar-sensor"]
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', 
    'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso'
]
teacher_exclusive: false
---

## Voorbeeld sonar-sensor
OPGAVE 2
Schrijf een programma dat afhankelijk van de waarde, de boodschap "waarde < 20 cm" of "waarde > 20 cm" teruggeeft.

Hier moet je gebruikmaken van een keuzestructuur: een als - dan of als - dan - anders blok werd hiervoor voorzien. Dit is het moeilijkste dat je nodig hebt voor de sociale robot.

Oplossing:

![blockly](@learning-object/SRM_Sonar2-v1/nl/3)

Bij het programmeren van de sociale robot kan je andere acties koppelen aan deze voorwaarden. Je kan bijvoorbeeld de armen laten zwaaien of ogen laten knipperen wanneer iemand tussen de 0 en 50 cm van de robot verwijderd is.

*Test deze voorbeelden ook zelf uit in de simulator! Als je de werking wat te pakken hebt, kan je zelf aan de slag.*