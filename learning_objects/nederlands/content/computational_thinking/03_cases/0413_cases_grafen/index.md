---
hruid: ct_cases13
version: 3
language: nl
title: "Toepassingen grafen"
description: "Toepassingen grafen"
keywords: [""]
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
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
# Toepassingen grafen
Hier bekijk je enkele toepassingen van grafen: de werking van een routeplanner en het matchen van vingerafdrukken. Deze voorbeelden maken onderdeel uit van een lessenreeks over grafentheorie.

**Doelgroep:** Leerlingen 2de en 3de graad finaliteit doorstroom en dubbele finaliteit (richtingen nog te bepalen).

**Voorkennis:** De leerlingen kennen reeds enkele types van grafen (simpele graaf, gerichte graaf, pad, wandeling, cykel).

**Doel:** De leerlingen zien in dat men soms sneller tot de oplossing van een probleem komt als men de gegevens abstraheert tot een graaf. Bij deze voorbeelden is er nood aan een nieuw type graaf.

### De werking van een routeplanner

Je kent de afstanden in km tussen bepaalde gemeenten langs grote wegen en in vogelvlucht: Gent, Lokeren, Sint-Niklaas, Dendermonde, Willebroek, Mechelen. Bepaal de kortste weg tussen Gent en Mechelen via deze wegen? Hoe kan een computer daarbij helpen?  
![image](https://user-images.githubusercontent.com/48352335/213927739-9b9c0801-bdb0-4692-af36-eafa8f172864.png)
![image](https://user-images.githubusercontent.com/48352335/213927749-83781385-10f4-43f4-9d28-10bfc20d3700.png)

![ct-schema](@learning-object/m_ct_cases13/nl/3)

Dit voorbeeld is een inleiding op het algoritme van Dijkstra en hoe dit praktisch toegepast wordt. 

### Het matchen van vingerafdrukken

![ct-schema](@learning-object/m_ct_cases13b/nl/3)



Voor meer uitleg, zie het leerpad ['Grafen'](https://www.dwengo.org/learning-path.html?hruid=aiz2_grafen&language=nl&te=true&source_page=%2Fcare%2F&source_title=%20AI%20in%20de%20Zorg#aiz_sprouts;nl;3) bij het project [AI in de Zorg](https://www.dwengo.org/care/) of bij [Python in de Wiskundeles](https://www.dwengo.org/math_with_python/).
