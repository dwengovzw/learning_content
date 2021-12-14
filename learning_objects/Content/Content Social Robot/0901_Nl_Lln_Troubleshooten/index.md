---
hruid: SR_Programmeren3-v1
version: 3
language: nl
title: "Testen en debuggen"
description: "T"
keywords: ["Sociale Robot"]
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
estimated_time: 30
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', 
    'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso'
]
teacher_exclusive: false
---
# Programmeren van de robot

## Testen en debuggen
Tijdens het testen en debuggen, zal je simpelweg dingen moeten uitproberen tot je bekomt wat je wilt (*trial and error*).  
Doe dit echter niet lukraak. Denk eerst na over wat er fout gaat en probeer hier een oplossing voor te bedenken. Daarna test je deze oplossing uit en begint het proces opnieuw.

**Voorbeeld 1**  
Je hebt 2 ledmatrices gebruikt als ogen voor de robot, maar de ogen zijn omgewisseld van plaats.

*Optie 1*  
Je verwisselt de ledmatrices in de fysieke robot zodat ze overeenkomen met het programma.  


*Optie 2*  
Je verwisselt de ogen in het programma, zodat ze overeenkomen met de fysieke robot.  


*Optie3*  
Je programmeert de ogen opnieuw, maar nu voor de juiste plaats.  


**Voorbeeld 2**  
De armpjes van de fysieke robot bewegen niet, terwijl dit in de simulator wel goed functioneerde.  

*Optie 1*
Je controleert de bedrading. Misschien waren er draden verwisseld of losgekomen.


*Optie 2*
Je controleert of er geen onderdeel van je robot in de weg zit waardoor de armen niet kunnen bewegen.  


*Optie 3*
Je maakt de armen los en controleert of de servomotoren nu wel werken. Misschien waren de armen te zwaar?  


Tijdens het testen en debuggen is het vooral belangrijk dat je eerst vaststelt wat de fout veroorzaakt vooraleer je een oplossing gaat bedenken. Zo kan je gericht op zoek naar een oplossing en kan je dit onderdeel efficiënt doorlopen!  

Indien je nog tijd overhebt, kan je je robot nog extra zaken laten doen. Had je nog iets in gedachten tijdens de brainstorm?