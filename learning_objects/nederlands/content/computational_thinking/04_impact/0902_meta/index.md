---
hruid: m_ct_impact_2
version: 3
language: nl
title: "Impact routeplanner"
description: "Impact routeplanner"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/ct-schema
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

<context>
Ontwikkelen van een routeplanner.
</div>
</context>
<decomposition>
Verkennen van het probleem. Wat heb je nodig? <br> Subtaken (**decompositie**):<br>
1. De positie van de gebruiker
2. Een voorstelling van het wegennet, wat inhoudt:
    - welke wegen er met elkaar verbonden zijn;
    - de waarde van de parameters van de wegen.
3. Er moet dus beslist worden met welke parameters de routeplanner rekening zal houden en met welke niet, zoals:
    - toegelaten snelheid;
    - verkeersdrukte;
    - lengte;
    - weer;
    - karakter.
    - - Geschiktheid van de wegen voor vrachtwagens.
    - - Lokaal karakter zoals woonwijk of industriepark. 
    - Tot welke databanken heeft de routeplanner toegang? 
       -- Een databank van commerciële partners zoals bepaalde winkels, tankstations, ...
       -- Wegenwerken
    ...
3. Een algoritme om het kortste, snelste of meest optimale pad te bepalen    
4. Vastleggen of en hoe de routeplanner real time aanpassingen kan doen aan de route.
    - Een mobiele internetverbinding
    - Real time positie van de gebruiker 
    - - Global positioning system (gps)
    - Real time verkeersinformatie
    - - Wordt ervoor gekozen om real time informatie over de routes van de gebruikers te communiceren?
</decomposition>
<patternRecognition>
Het systeem kan informatie bekomen via **patroonherkenning**, bijvoorbeeld:
1. De gebruikers die op een bepaald stuk weg alle trager rijden, kunnen door het systeem herkend worden als file of vertraagd verkeer.
2. Het systeem zou een patroon van herhaaldelijke file op een bepaalde plaats kunnen detecteren en aanduiden als te vermijden plaats.
3. Een routes die doorgaans enkel gekend is door lokale bewoners zou door het rijden ervan  als mogelijk traject kunnen opgeslagen worden in het systeem. 
</patternRecognition>
<abstraction>
Zowel in de vormgeving als in de werking van een routeplanner speelt **abstractie** een prominente rol. 
1. Overtollige gegevens over de omgeving zijn verwijderd in de vormgeving. Je krijgt enkel de weg te zien, zonder veel informatie van de omgeving waar je door rijdt.
    - Nochtans worden bepaalde winkels, tankstations ... toch weergegeven.  
2.  De routeplanner houdt voor het bepalen van de route slechts rekening met bepaalde parameters, zoals de afstand. Andere parameters, zoals het feit dat een straat in een woonwijk ligt, worden genegeerd.       
</abstraction>
<algorithms>
Routeplanners gebruiken **algoritmes** die de weg berekenen. 
1. Naargelang de wens van de gebruiker zoeken ze naar de kortste, snelste of meest optimale weg.
2. Mogelijk is er een algoritme dat real time informatie verwerkt.
3. Mogelijk is er ook een algoritme dat de route linkt aan de aanwezigheid van commerciële partners. 
</algorithms>


