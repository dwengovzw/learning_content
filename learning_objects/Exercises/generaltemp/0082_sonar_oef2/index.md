---
hruid: g_sonar_oef2
version: 3
language: nl
title: "Oefening Sonar-sensor 2"
description: "Oefening Sonar-sensor 2"
keywords: ["oefeningen", "sonar-sensor"]
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---
## Sonar-sensor

OPGAVE 2

Schrijf een programma dat afhankelijk van de waarde, de boodschap "waarde < 20 cm" of "waarde > 20 cm" teruggeeft.

Hier moet je gebruikmaken van een keuzestructuur: een als - dan of als - dan - anders blok werd hiervoor voorzien. Dit is het moeilijkste dat je nodig hebt voor de sociale robot.


Bij het programmeren van de sociale robot kan je andere acties koppelen aan deze voorwaarden. Je kan bijvoorbeeld de armen laten zwaaien of ogen laten knipperen wanneer iemand tussen de 0 en 50 cm van de robot verwijderd is.

*Test deze voorbeelden ook zelf uit in de simulator! Als je de werking wat te pakken hebt, kan je zelf aan de slag.*