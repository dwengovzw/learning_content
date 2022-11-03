---
hruid: aiz_etstemzorg-v1
version: 3
language: nl
title: "Verwerking in het project"
description: "Verwerking in het project"
keywords: [""]
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
# STEM
# Eindtermen STEM en het '*AI in de Zorg*'-project 

*Eindtermen - STEM-concepten* 

In ziekenhuizen worden patiënten steeds vaker automatisch gemonitord, met grote hoeveelheden digitale data als gevolg. Elektronische patiëntendossiers bevatten een schat aan data. Uit deze big data kan men veel informatie inwinnen (informatie).<br>
Veel beschikbare data over COVID-19 laat toe de pandemie te controleren en de gevolgen van eventuele maatregelen te simuleren (oorzaak en gevolg - systemen en modellen).<br>
Lerende systemen gaan op zoek naar patronen in data en stellen aan de hand daarvan bv. een beslissingsboom op om een diagnose te stellen afgaand op bepaalde gegevens van de betrokken patiënt. Radiologen kunnen een beroep doen op AI-systemen om bv. subtiele effecten van medicatie op tumoren te detecteren; ook deze systemen werken met patroonherkenning (patronen - systemen).<br>
De noden in de maatschappij kunnen de ontwikkelingen op het vlak van technologie versnellen (stabiliteit en verandering).<br>
Geautomatiseerde EWS-systemen kunnen de dagdagelijkse werking in het ziekenhuis grondig beïnvloeden en leiden tot aanpassingen (veranderingen) in hun werking.<br>
Het regelgebaseerd systeem dat gebruikt wordt om automatisch beslissingsbomen te genereren baseert zich op de aangeleverde data. Onvoldoende of niet kwalitatieve data leiden tot een beslissingsboom die niet effectief is. Te grote beslissingsbomen zijn in de praktijk niet bruikbaar; zo’n beslissingsbomen zullen worden ingeperkt; een te grote inperking kan de accuraatheid verminderen. Leerlingen zien in dat het AI-systeem dat zij gebruiken om beslissingsbomen automatisch te genereren een groot voordeel heeft, nl. de transparantie waarmee een ontwikkeld model tot zijn voorspellingen komt. Leerlingen zien anderzijds ook in dat het gebruikte AI-systeem beperkingen heeft: het is bv. niet geschikt als er rekening moet worden gehouden met heel veel parameters, daarvoor is een lerend systeem beter geschikt, maar dat heeft dan als nadeel dat de transparantie verloren gaat (verhouding en hoeveelheid). 

Omdat de leerlingen de voordelen en beperkingen van sommige AI-systemen kennen, kunnen ze argumenteren waarom in een bepaald geval bv. beter gekozen wordt voor een beslissingsboom, dan wel een lerend systeem. 

De leerlingen gaan aan de slag met een dataset om inzicht te krijgen in een medisch probleem: welke parameters zijn van belang voor (de evolutie van) dat medisch probleem? Een beslissingsboom biedt een oplossing voor dat probleem. Eens die beslissingsboom is opgesteld, beschikken de leerlingen over een systeem dat hen toelaat om bij een nieuwe patiënt de waarden van de parameters in te geven en bv. te voorspellen in welke diagnose die parameters zich vertalen of hoe een medische situatie zal evolueren.<br>
Om tot een beslissingsboom te kunnen komen, zullen de leerlingen eerst vertrouwd moeten worden met de concepten die concreet zullen worden toegepast. De nood aan deze concepten zal naar voren komen bij het aanpakken van deelproblemen: de opbouw van zo’n beslissingsboom met knopen en bogen, de opeenvolgende vragen die worden gesteld in de knopen, de minimale spreiding van de parameters over de verschillende categorieën die de uitkomst van de boom vormen, de gini-index, en hoe men ervoor zorgt dat dit alles kan geïmplementeerd worden in een computerprogramma.<br>
Ze zullen concepten uit de computerwetenschappen leren kennen, zoals een verdeel-en-heersalgoritme en abstractie, en geconfronteerd worden met het feit dat computers werken met getallen, waardoor ze aan de slag moeten gaan met datatypes. Ze zullen werken met wiskundige concepten, zoals grafen, verzamelingen, parabolen, verbanden tussen grootheden, de ‘p’ en ‘q’ uit de kansrekening, en eventueel logische uitdrukkingen.<br>
Het algoritme dat de leerlingen ontwerpen en eerst manueel toepassen, implementeren ze vervolgens op de computer. Ze schrijven daartoe een programma in Python dat het hele proces automatiseert. Ze gebruiken daarvoor de ingebouwde functies van bestaande Python-modules, waardoor ze inzien dat de samenwerking tussen computerwetenschappen en wiskunde tot mooie toepassingen voor de zorgsector kunnen leiden. De leerlingen komen tot een zelfgeschreven programma door bestaande programma’s aan te passen en met elkaar te combineren.<br>
Het is belangrijk dat men met de leerlingen bespreekt dat ook de inbreng van zorgverstrekkers en patiënten vereist is, zodat men tot bruikbare en ethisch aanvaardbare toepassingen komt. Bruikbaar en ethisch aanvaardbaar zijn, naast de effectiviteit, criteria die zeker moeten meegenomen worden bij het ontwerpen. De leerlingen kunnen een gegenereerde beslissingsboom testen met niet eerder geziene data en de omvang van de boom beoordelen op de bruikbaarheid. 

De leerlingen zien in dat een beslissingsboom in een medische context kan aangewend worden voor een betere zorg, bv. het sneller bekomen van een diagnose of gen twijfel over de te volgen remedie. De leerlingen zien in dat er een wisselwerking is tussen de groeiende aanwezigheid van AI-systemen enerzijds, en de maatschappij, waaronder de economische belangen, en hoe met ethische aspecten wordt omgegaan anderzijds.