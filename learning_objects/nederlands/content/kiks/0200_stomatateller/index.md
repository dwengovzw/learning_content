---
hruid: kiks_stomatateller
version: 3
language: nl
title: "Stomatateller"
description: "Stomatateller"
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
teacher_exclusive: false
---

# Automatisch tellen van huidmondjes

In de volgende notebook wordt er getoond hoe men AI inzet om huidmondjes te tellen op microscopische foto's.

Er is ook in een kleine demonstratie voorzien, zodat je alvast weet waarmee je aan de slag gaat!

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=1710 "Basis")

----------
Er wordt een convolutioneel neuraal netwerk voor gebruikt, nl. een diep neuraal netwerk voor objectherkenning.<br>
In de rest van dit leerpad wordt uitgelegd hoe dit diepe neurale netwerk werd opgebouwd.
