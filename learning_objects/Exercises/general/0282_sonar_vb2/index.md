---
hruid: g_sonar_vb2
version: 3
language: nl
title: "Voorbeeld Sonar-sensor 2"
description: "Voorbeeld Sonar-sensor 2"
keywords: ["oefeningen", "sonar-sensor"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
## Sonar-sensor

OPGAVE 2  

Schrijf een programma dat afhankelijk van de waarde, de boodschap "waarde < 20 cm" of "waarde > 20 cm" teruggeeft.

Hier moet je gebruikmaken van een keuzestructuur.

Oplossing:  

![blockly](@learning-object/sonar_m2/nl/3)

Bij het programmeren van de sociale robot kan je andere acties koppelen aan deze voorwaarden. Je kan bijvoorbeeld de armen laten zwaaien of de ogen laten knipperen wanneer iemand tussen de 0 en 50 cm van de robot verwijderd is.

<div class="alert alert-box alert-danger">
De sonar-sensor heeft een bereik van 200 cm. Wanneer er zich niets bevindt binnen dit bereik, geeft de sonar-sensor de waarde 0 terug. Dit geeft als gevolg dat wanneer er niets te zien is binnen 2 m, de sensor dit interpreteert alsof er iets vlak voor de sensor staat.

Programmeer daarom altijd <em>"Afstand groter dan 0"</em> als voorwaarde voor de kleinste afstand, zodat er hier geen problemen bij optreden.
</div>