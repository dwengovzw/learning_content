---
hruid: pc_hddclock5
version: 1
language: nl
title: "Fysieke versie HDD klok"
description: "Fysieke versie HDD klok"
keywords: ["Microcontroller"]
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# HDD klok

## HDD klok bouwen

Nu we weten hoe een HDD klok werkt en hoe dit gerealiseerd kan worden, is het bouwen van een fysieke versie de logische volgende stap. 
Om een HDD klok te bouwen hebben we de eerder vermelde componenten nodig en een constructie om het af te werken en mooier te presenteren. We hangen de schijf vast aan de spindelmotor, zorgen dat de schijf door de snelheidssensor gaat en voorzien een ledstrip achter de draaiende schijf. Dit kan allemaal gebeuren in de voorziene constructie, die gebouwd kan worden met onderdelen gesneden door een lasercutter. Om deze onderdelen op maat te maken kan je <a href="https://github.com/dwengovzw/learning_content/blob/staging/learning_objects/nederlands/content/physical_computing/leerlijn_microcontrollers/4610_project_hdd_clock/0005_hddclock/embed/hdd_clock.dxf" download><strong>dit bestand</strong></a> gebruiken (tip: dit gaat uit van een materiaaldikte van 2.5mm). 
Ten slotte verbinden we alles met de Dwenguino zodat deze de componenten kan besturen en we de klok daadwerkelijk kunnen gebruiken! 

Programmeer de code op de Dwenguino en test de HDD klok eens uit, als alles goed verlopen is dan zou de klok als volgt moeten werken:

<img src="embed/FysiekeHDDClock.gif" alt="Werkende HDD klok." title="Werkende HDD klok."></img>  
