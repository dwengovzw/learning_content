---
hruid: sr3_troubleshooting
version: 3
language: nl
title: "Testen en debuggen"
description: "T"
keywords: ["Sociale Robot"]
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
estimated_time: 30
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek'
]
teacher_exclusive: false
---
# Programmeren van de fysieke robot
## Testen en debuggen
Wanneer je bezig bent met testen en debuggen, kan het nodig zijn om verschillende dingen uit te proberen, voordat je het gewenste resultaat bereikt. Dit vereist echter wel een doordachte aanpak. Probeer eerst te achterhalen wat er precies fout gaat en bedenk vervolgens een oplossing. Test deze oplossing en herhaal het proces indien nodig.

**Voorbeeld 1**  
Stel dat je 2 ledmatrices als ogen hebt gebruikt voor de robot, maar ze zijn per ongeluk omgewisseld van plaats.

*Optie 1*  
Je verwisselt de ledmatrices in de fysieke robot, zodat ze overeenkomen met het programma.  

*Optie 2*  
Je programmeert de ogen opnieuw, maar nu voor de juiste plaats.  


**Voorbeeld 2**  
De armpjes van de fysieke robot bewegen niet, terwijl ze in de simulator wel goed functioneerden.

*Optie 1*
Controleer de bedrading om te zien of er draden verwisseld of losgekomen zijn.

*Optie 2*
Controleer of er geen onderdelen van de robot in de weg zitten, waardoor de armen niet kunnen bewegen.

*Optie 3*
Maak de armen los en controleer of de servomotoren werken. Misschien zijn de armen te zwaar om te bewegen?

<div class="alert alert-box alert-success">
Tijdens het testen en debuggen is het belangrijk om de oorzaak van de fout vast te stellen, voordat je een oplossing bedenkt. Op deze manier kun je gericht naar een oplossing zoeken en het proces efficiënter maken. 
</div>

Indien je nog tijd over hebt, kan je je robot nog extra zaken laten doen. Had je nog iets in gedachten tijdens de brainstorm?