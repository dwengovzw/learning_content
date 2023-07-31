---
hruid: ct9_2
version: 3
language: nl
title: "Routeplanner"
description: "Routeplanner"
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
# Routeplanner

### Principes van computationeel denken bij een routeplanner
- Decompositie:
  - Bij het ontwerp van de routeplanner kan al dan niet rekening gehouden worden met bepaalde parameters. Men kan ervoor kiezen een variabele in rekening te brengen die aangeeft of een bepaalde straat tot een woonwijk behoort of niet.
  - De routeplanner kan bij gebruik verbonden zijn met het internet om in real time aanpassingen te doen. Wordt daarbij opgeslagen waar de gebruiker zich bevindt?
  - Heeft de routeplanner toegenag tot andere databanken, naast het strikt noodzakelijke om te kunnen werken?
- Abstractie:
  - Overtollige gegevens over de omgeving zijn verwijderd.
  - Nochtans worden sommige zaken toch weergegeven zoals bepaalde winkels, tankstations ...
- Patroonherkenning:
  - Real time verkeersinformatie: Als een aantal gebruikers op een bepaald stuk weg alle trager rijden, wordt dit door het systeem herkend als files of vertraagd verkeer.   
- Algoritme:
  - Routeplanners gebruiken algoritmes die de weg berekenen, vaak rekening houdend met real time informatie.

### Impact op de maatschappij

-  Een van de redenen dat routeplanners zoveel gebruikt worden en dus zoveel impact hebben, is de grote mate van abstractie in de routplanner. <br> Indien gewenst, kan je enkel de instructies opvolgen van de weg die je moet volgen (het stappenplan of algoritme). Je moet je niet bezighouden met het opzoeken van de weg op een kaart, waarbij je rekening zou moeten houden met bv. eenrichtingsverkeer, de oriëntatie van de kaart, enz.
-  Zo'n routeplanner heeft dus een groot gebruiksgemak.
-  Bovendien krijg je er bijkomende informatie zoals files, wegwerkzaamheden, waar je kan tanken, enz.
-  Het gebruik van een routeplanner door zoveel mensen kan ook ongewenste effecten hebben, zoals extra verkeer in woonwijken wanneer een routeplanner het autoverkeer langs woonwijken omleidt om files te vermijden. De vraag is met hoeveel aspecten van de omgeving het algoritme in de routeplanner rekening houdt. In de invoer is het misschien weggeabstraheerd dat een bepaalde omgeving een woonwijk is, of in het programma wordt er met die variabele geen rekening gehouden.  
-  Omdat er in routeplanners zoveel geabstraheerd wordt, heb je geen volledig zicht meer op de omgeving. Dat kan ook een nadeel zijn t.o.v. een papieren kaart die veel meer details geven van de omgeving en een bepaalde plaats bovendien situeren in een groter gebied. Routplanners hollen als het ware het ruimtelijk bwustzijn rond een plaats uit.
-  Teveel afhankelijk zijn van digitale routeplanners kan daarom ook gevaarlijk zijn, mensen rijden bv. een treinspoor op of op een trap. Of je kan in een gebied terechtkomen waar er geen mobiel bereik is, of de batterij van je smartphone kan plat zijn. Sommige gebieden zijn ook onvoldoende gedetailleerd of onnauwkeurig aanwezig. Digitale routeplanners kunnen dus fouten bevatten, zoals een foute maximale snelheid die op een bepaalde weg is toegelaten of een straat met eenrichtingsverkeer die als tweerichtingsverkeer is aangegeven.
-  Als de locaties van de gebruiker worden opgeslagen, dan rijst de vraag wat de verstrekker van de routeplanner aanvangt met die gegevens.
-  Hoe wordt bepaald welke winkels, tankstations ... getoond worden in de routeplanner? Dit is een vorm van reclame.
-  Routeplanners worden ook gebruikt door robots die boodschappen naar huis brengen of door medische drones; a.d.h.v. de routeplanner vinden ze de weg.
-  Het gebruik van routeplanners kan ervoor zorden dat een bedrijf de kosten en de tijd gebruikt voor transport kan minimaliseren en de werking kan optimaliseren, bv. bij een leveringsbedrijf of taxibedrijf.
-  Als de routeplanner toegang krijgt tot databanken van restaurants, winkels, bioscopen, enz. dan kan een toerist via de routeplanner bv. te weten komen welke zaken er in de buurt zijn van het hotel. 

-------------------------------
#### Leestips
[Met Medical Drone Service in minuten heen en weer tussen ziekenhuislocaties](https://www.antoniusziekenhuis.nl/nieuwsoverzicht/met-medical-drone-service-minuten-heen-en-weer-tussen-ziekenhuislocaties-0)<br>
[Genks proefproject met safety drones krijgt navolging in het hele land](https://www.vrt.be/vrtnws/nl/2023/03/14/genks-proefproject-met-safety-drones-krijgt-navolging-in-het-hel/)<br>
[GETEST. Wij lieten onze boodschappen leveren door robot van Carrefour: “We geloven onze ogen niet ”](https://www.nieuwsblad.be/cnt/dmf20230726_96924324)<br>
[Autonomous Robots for Industry 4.0](https://starshipdeliveries.com/industry/)
