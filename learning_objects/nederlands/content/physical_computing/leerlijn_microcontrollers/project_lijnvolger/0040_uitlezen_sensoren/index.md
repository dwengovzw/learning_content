---
hruid: leerlijn_project_lijnvolger_uitlezen_sensoren
version: 1
language: nl
title: "Uitlezen sensoren"
description: "Hoe kan ik de grondsensoren op de lijvolger uitlezen."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "grondsensor"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Uitlezen sensoren

Eerder in dit project hebben we de grondsensoren aangesloten op de pinnen (\\(\mathrm{A0}\\), \\(\mathrm{A1}\\), \\(\mathrm{A2}\\), \\(\mathrm{A3}\\), \\(\mathrm{A4}\\) en \\(\mathrm{A5}\\)) van de µC. Dit zijn analoge pinnen en lezen dus een continue spanningswaarde tussen \\(0\mathrm V\\) en \\(5\mathrm V\\). We kunnen in onze code de <code class="lang-cpp">analogRead(pin)</code> functie gebruiken om de analoge waarde van een pin te lezen. De <code class="lang-cpp">analogRead(pin)</code> functie zet de spanning tussen \\\\(0\mathrm V\\) en \\(5\mathrm V\\) om naar een getal tussen \\(0\\) en \\(1024\\). Dit getal stelt de gemeten sensorwaarde voor en kunnen we opslaan in een variabele van het type <code class="lang-cpp">int</code>.