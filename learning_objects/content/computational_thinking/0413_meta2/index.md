---
hruid: m_ct_cases13b
version: 3
language: nl
title: "Matchen vingerafdrukken"
description: "Matchen vingerafdrukken"
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
Je kent de afstanden in km tussen bepaalde gemeenten langs grote wegen en in vogelvlucht: Gent, Lokeren, Sint-Niklaas, Dendermonde, Willebroek, Mechelen. Bepaal de kortste weg tussen Gent en Mechelen via deze wegen? Hoe kan een computer daarbij helpen?  
</context>
<decomposition>
**Decompositie:**<br>
- Welke wegen zijn er mogelijk? Om dit te zien kan je best op een grafische voorstelling kijken, hier kiezen we voor een graaf.
- Uit welke delen zijn die opgebouwd? M.a.w. welke gemeenten passeer je?
- Totale afstand is de som van de afstanden tussen de gekozen gemeenten.
- Computer kan de afstanden van alle mogelijke wegen berekenen en de kortste eruit halen. 
</decomposition>
<patternRecognition>
**Patroonherkenning:**<br>
    - De wegen tussen de gemeenten vormen een netwerk. Een netwerk kan voorgesteld worden d.m.v. een graaf. Denk bv. aan de voorstelling met een graaf van een sociaal netwerk. 
    - Er is hier wel een bijkomende complexiteit, nl. de lengte van de wegen, die moet ook voorgesteld worden.  
</patternRecognition>
<abstraction>
Tekst
</abstraction>
<algorithms>
    - **Algoritme van Dijkstra** 
    - **A* algoritme** omdat niet alle wegen in aanmerking komen, bv. de wegen langs gemeenten die uit de weg liggen zijn overbodig na te gaan.
    
Algoritme omschrijven in woorden (en eventueel ook programmeren).  
</algorithms>
<implementation>
**Programma:**<br>
    - Python-script van algoritme van Dijkstra
    - Python-script van A* algoritme 
Zie hiervoor de notebooks bij het leerpad ‘Grafen’.
</implementation>
