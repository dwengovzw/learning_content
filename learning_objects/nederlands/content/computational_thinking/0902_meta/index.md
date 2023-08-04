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
1. Global positioning system (gps)
2. Met welke parameters houdt de routeplanner rekening en met welke niet?
    - Parameters om de snelste weg te kunnen bepalen zoals toegelaten snelheid, verkeersdrukte.
    - Parameters om de kortste weg te kunnen bepalen zoals afstand.
    - Parameters om de meest optimale weg te kunnen bepalen zoals het weer.
    - Geschiktheid van de wegen voor vrachtwagens.
    - Lokaal karakter zoals woonwijk of industriepark. 
    - De aanwezigheid van commerciële partners zoals bepaalde winkels, stations, ...
       -- Heeft de routeplanner toegang tot andere databanken, naast de strikt noodzakelijke om te kunnen werken?
    ...
3. Doet de routeplanner real time aanpassingen aan de route?
    - De routeplanner moet over een mobiele internetverbinding beschikken.
    - De routeplanner moet over real time verkeersinformatie beschikken.
    - Wordt ervoor gekozen om real time informatie over de routes van de gebruikers te communiceren?
</decomposition>
<patternRecognition>
Het systeem kan informatie bekomen via **patroonherkenning**, bijvoorbeeld:
1. De gebruikers die op een bepaald stuk weg alle trager rijden, kunnen door het systeem herkend worden als file of vertraagd verkeer.
2. Het systeem zou een patroon van herhaaldelijke file op een bepaalde plaats kunnen detecteren en aanduiden als te vermijden plaats.
3. Een routes die doorgaans enkel gekend is door lokale bewoners zou door het gebruik ervan  als mogelijk traject kunnen opgeslagen worden in het systeem. 
</patternRecognition>
<abstraction>
Zowel in de vormgeving als in de werking van een routeplanner speelt **abstractie** een prominente rol. 
1. Overtollige gegevens over de omgeving zijn verwijderd in de vormgeving. Je krijgt enkel de weg te zien, zonder veel informatie van de omgeving waar je doorrijdt.
    - Nochtans worden sommige zaken toch weergegeven zoals bepaalde winkels, tankstations ... 
2.  De routeplanner houdt voor het bepalen van de route slechts rekening met bepaalde parameters, zoals de afstand. Andere parameters zoals het feit dat een straat in een woonwijk ligt, worden genegeerd.       
</abstraction>
<algorithms>
Routeplanners gebruiken **algoritmes** die de weg berekenen. 
1. Naargelang de wens van de gebruiker zoeken ze naar de kortste, snelste of meest optimale weg.
2. Mogelijk is er een algoritme dat real time informatie verwerkt.
3. Mogelijk is er ook een algoritme dat de route linkt aan de aanwezigheid van commerciële partners. 
</algorithms>


