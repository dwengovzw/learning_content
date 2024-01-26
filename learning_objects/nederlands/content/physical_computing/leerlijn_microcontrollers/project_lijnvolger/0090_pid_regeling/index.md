---
hruid: leerlijn_project_lijnvolger_pid
version: 1
language: nl
title: "PID regeling"
description: "Hoe programmeer ik een pid regeling."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "pid"]
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
estimated_time: 15
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# PID regeling

In een laatste stap moeten we de snelheid van onze motoren afhankelijk maken van de gemeten fout op de lijn. Hiervoor gebruiken we een techniek genaamd de **PID regeling**. Dit soort regeling houdt niet enkel rekening met de fout maar ook met de afgeleide en de integraal van deze fout doorheen de tijd. De naam is ook afgeleid van deze verschillende soorten informatie.

* **P** de proportie (proportional): dit is de fout die we op een gegeven tijdstap meten. Het is dus het resultaat van onze <code class="lang-cpp">berekenFout()</code> functie.
* **I** de integraal (integral): dit is de som van alle fouten die we in het verleden gemaakt hebben. Met deze waarde krijg je zicht op de historische fout. Deze informatie kan je gebruiken om te compenseren voor een fout die je over een langere periode blijft maken.
* **D** de afgeleide (differential): dit is het verschil tussen de huidige fout en de vorige fout. Deze waarde geeft aan hoe snel een fout toe- of afneemt. Deze waarde kan je gebruiken om snel bij te sturen wanneer dat nodig is. 

We zullen de snelheid van onze motoren dus laten afhangen van deze drie parameters. Daarvoor gieten we ze in de volgende formule:

\\[
\mathrm{snelheid} = \mathrm{K_p}\cdot \mathrm{P} + \mathrm{K_i}\cdot \mathrm{I} + \mathrm{K_d}\cdot \mathrm{D}    
\\]

waarbij \\(\mathrm{K_p}\\), \\(\mathrm{K_i}\\) en \\(\mathrm{K_d}\\) wegingsfactoren zijn die we zelf moeten kiezen. De waarde hiervan hangt af van de toepassing. Wij zullen deze waarden experimenteel bepalen. 

## De P regeling

Voor we een complexe PID regeling programmeren, kiezen we eerst voor een eenvoudige P regeling. We houden in dit geval dus geen rekening met de integraal en de afgeleide van de fout. 