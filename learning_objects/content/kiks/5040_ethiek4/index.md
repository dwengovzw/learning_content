---
hruid: kiks_ethiek4
version: 3
language: nl
title: "Drempelwaarde"
description: "Drempelwaarde"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Drempelwaarde

Het KIKS-neuraal netwerk bekijkt voor patches op een gegeven microfoto of er een huidmondje op staat of niet. Het netwerk bepaalt een percentage dat weergeeft hoe zeker het netwerk is dat er een huidmondje te zien is. Bij de ontwikkeling van het neuraal netwerk legt de netwerkarchitect een drempelwaarde vast. Als het bepaalde percentage die drempelwaarde overschrijdt, dan behoort de patch toe tot de klasse 'huidmondje', en anders niet.

Een aanpassing van de drempelwaarde heeft invloed op het aantal vals positieven en vals negatieven.  

De gekozen drempelwaarde is letterlijk van levensbelang in het geval van een diep neuraal netwerk in het domein van de medische beeldvorming als het bv. een systeem betreft voor de herkenning van kwaadaardige gezwellen. 
