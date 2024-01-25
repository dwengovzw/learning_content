---
hruid: leerlijn_project_lijnvolger_data_visualiseren_oplossing
version: 1
language: nl
title: "Data visualiseren (oplossing)"
description: "Hoe kan ik de data die ik ontvang in mijn Python programma weergeven in een grafiek."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "grondsensor", "grafiek", "matplotlib"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16]
difficulty: 1
estimated_time: 25
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Data visualiseren (oplossing)

**Hieronder zie je het verloop van de sensorwaarden van de robot die we bij Dwengo gebouwd hebben. Eerst stonden alle sensoren op een wit oppervlak. Erna werd de robot verschoven naar een zwart oppervlak. Bekijk de waarden goed. Wat merk je op?**

<img src="img/verloop_sensorwaarden.png"></img>

* Je merkt op dat de waarden van de sensoren sterk verschillen wanneer ze allemaal op een wit oppervlak staan. De oorzaken hiervan kunnen het verschil in afstand tot de grond of een variërende lichtinval zijn. Er zal een calibratiestap nodig zijn om deze verschillen weg te werken.
* Je merkt dat er een duidelijke overgang is van het witte naar het zwarte oppervlak.
* Je merkt dat de sensorwaarden minder verschillen wanneer de robot op een zwart oppervlak staat. Hier spelen verschillen in lichtinval minder een rol omdat het zwarte oppervlak het meeste licht absorbeert.