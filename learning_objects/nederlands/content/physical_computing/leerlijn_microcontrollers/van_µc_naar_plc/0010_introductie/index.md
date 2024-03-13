---
hruid: leerlijn_microcontrollers_µc_naar_plc
version: 1
language: nl
title: "Introductie"
description: "Hoe stuur je gegevens over een seriële connectie vanop de Dwenguino?"
keywords: ["microcontroller", "plc", "automatisatie", "programmable logic controller", "µC"]
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# De PLC

TODO: foto van PLC die opengevezen is.

In deze leerlijn heb je geleerd hoe je fysische systemen kan besturen aan de hand van een microcontroller. Je hebt gezien dat een microcontroller tal van functies heeft en in verschillende contexten ingezet kan worden. Toch kan het programmeren van een microcontroller soms complex worden en is het af en toe moeilijk om het overzicht te houden over hoe de verschillende componenten aangesloten zijn. Deze exta complexiteit zorgt ervoor dat de kans op bugs (fouten) in je systeem hoger wordt. 
In vele industriële toepassingen is het zeer belangrijk dat er zich geen fouten voordoen. Een fout in een industriële productielijn kan een bedrijf immers miljoenen euro's kosten. Om ervoor te zorgen dat de kans op fouten in een productielijn zo klein mogelijk wordt, werd de PLC (programmable logic controller) uitgevonden. Een PLC is eigenlijk een microcontrollerplatform, gelijkaardig aan de Dwenguino, dat specifiek ontworpen is voor het gebruik in een industriële toepassing.

De PLC onderscheid zich in de volgende eigenschappen van de microcontroller:
* **Betrouwbaarheid**: Een PLC is zodanig gemaakt dat het onder verschillende omstandigheden betrouwbaar kan werken. Zo moet een PLC correct blijven functioneren bij verschillende temperaturen, extreme luchtvochtigheid of vibraties. Een PLC heeft bijvoorbeeld speciale connectoren om componenten aan te sluiten. Deze connectoren zijn veel steviger en betrouwbaarder dan de pinnen op de Dwenguino.
* **Eenvoudig te programmeren**: Een PLC maakt gebruik van een eenvoudige programmeertaal (bv. ladder logic). Deze programmeertaal is, voor eenvoudige controletoepassingen, gemakkelijker in gebruik dan een taal zoals C++. Omdat de taal eenvoudiger is, is de kans dat de programmeur fouten maakt ook kleiner.
* **Flexibiliteit**: Een PLC is robuust en kan eenvoudig geprogrammeerd worden. Daartegenover staat dat een PLC minder flexibel is dan een microcontroller. De PLC is specifiek gericht op industriële controletoepassingen. De microcontroller kan zeer flexibel ingezet worden in verschillende situaties (bv. auto's, huishoudelectronica, industriële robots, ...).

Buiten deze verschillen hebben de PLC en de µC ook veel gemeen. 
* Je kan ze alletwee gebruiken om physieke systemen te besturen. 
* Ze hebben alletwee verschillende manieren om met externe apparaten te communiceren.
* Ze kunnen alletwee ingezet worden in ware-tijd toepassingen. Dit zijn toepassingen waarbij de exacte timing belangrijk is. 
* Ze kunnen in gelijkaardige toepassingen worden ingezet. 



