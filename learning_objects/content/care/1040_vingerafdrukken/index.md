---
hruid: aiz_vingerafdrukken
version: 3
language: nl
title: "Vingerafdrukken"
description: "Vingerafdrukken"
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Vingerafdrukken

**Voorkennis:** De leerlingen weten wat een graaf, knopen en bogen zijn. Hier komt een nieuw type van grafen op de proppen, nl. de gekleurde, gewogen graaf. 

De forensische wetenschap is van groot belang voor het handhaven van de wet. Denk aan DNA technologie, chemische analyses, het onderzoeken van de sporen veroorzaakt door kogels, en het analyseren of identificeren van vingerafdrukken.

In dit onderdeel van het leerpad neem je vingerafdrukken onder de loep. 

Een vingerafdrukken is het lijnenpatroon dat een vingertop achterlaat wanneer hij in contact komt met een oppervlak. Vingerafdrukken zijn uniek voor elke mens en blijven onveranderd tijdens het leven. Ook unieke tweelingen kunnen ermee van elkaar onderscheiden worden. Men moet er wel rekening mee houden dat door het groeien de patronen ook vergoten en dat vingerafdrukken wel kunnen veranderen door een ziekte of een ongeluk. Met ouder worden, kunnen de lijnen ook minder duidelijk worden.  Ongeveer 300 jaar voor Christus gebruikten ze al vingerafdrukken in China om personen te identificeren. In de VS en Europa begon men daar pas mee in de 19de eeuw.

De huid aan de binnenkant en de toppen van de vingers vertoont bepaalde patronen: de lijnen op de huid en de plaatsen ertussen vormen lussen (*loops*), bogen (*arches*) en kringen (*whorls*). Deze patronen worden gevormd in de embryonale en foetale fase van een nieuwe mens.
Door de manier waarop de huid op de vingertoppen gevormd wordt, ontstaan er binnen deze patronen ook herkenningspunten (*minutiae*): delta's, vorken of bifurcaties (*bifurcations*), eilandjes of punten (*islands, dots*), eindigende lijnen (*ridge endings*), crossovers, bifurcaties naar boven en naar beneden (*spurs, hooks*), en ogen op de lijn (*lake, eye*). Deze zijn te zien op vingerafdrukken. Op vingerafdrukken van hoge kwaliteit kan je nog meer in detail kijken en kan je poriën en zweetklieren beschouwen. 

![image](https://user-images.githubusercontent.com/48352335/211288516-0e8ed701-31aa-41da-b22a-979a653cca1a.png)<br>
Figuur: Voorbeeldlesmateriaal project CSI, module f. https://www.slo.nl/thema/meer/doorstroom-vmbo/algemene/werken-algemene/3e-leerjaar/

![image](https://user-images.githubusercontent.com/48352335/211288547-3178d7ad-6604-4df0-84d9-96470929f15a.png)<br>
Figuur: The most common fingerprint minutiae patterns. Inaki Rom, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons.

Dus als men vingerafdrukken bestudeert, bekijkt men op het eerste niveau de lussen, bogen en kringen. Nadien gaat men het gedetaileerder bekijken door de herkenningspunten te observeren. 

### Het gebruik van vingerafdrukken
Vingerafdrukken worden gebruikt om mensen te identificeren, bv. een dader van een misdrijf, of voor authenticatie, toegang tot een smartphone. 

### Computationeel denken
Voorbeeld: Door de grote hoeveelheid aan vingerafdrukken werd het voor de FBI onhaalbaar om een binnenkomende vingerafdruk snel proberen te matchen aan een van de vingerafdrukken in hun database. De noodzaak om te automatiseren drong zich op. De computer was hiervoor de oplossing. 

De digitale bestanden waren best niet te groot naar opslagcapaciteit toe. Bovendien was het ook nodig om de bestanden te kunnen versturen overal ten lande, dus de bestanden mochten ook daarom niet te groot zijn. 

**Unplugged activiteit:** <br>
Bron: https://ccicada.org/education/ccicada-education-modules/#Fingerprint <br>
- Op een vergrote foto van een vingerafdruk de minitiae aanduiden, hun type bepalen, en de afstand in cm meten. 
- Dit omzetten naar een graaf.
- De leerlingen een set geven en daar hetzelfde op laten toepassen.
- Erna een nieuwe vingerafdruk aan de leerlingen geven en kijken of ze een algoritme vinden om te matchen.

![image](https://user-images.githubusercontent.com/48352335/211331634-cc6026fe-76a5-44b1-bdd7-5c0437b1f84a.png)<br>
Bron: https://ccicada.org/education/ccicada-education-modules/#Fingerprint

Gekleurde, gewogen graaf:
- Minutiae zijn de knopen
- Kleur de knopen: bifurcation groen, ridge ending rood, ridge crossing geel, dubbele bifurcation blauw, spurs paars, ...
- Gewogen: verbind de knopen (die met elkaar verbonden zijn door dzelfde lijn) en ken een gewicht toe aan de boog, nl. de afstand tussen de knopen. 
(Andere manieren zijn: de knopen een coördinaat toekennen, als gewicht het aantal gepasseerde lijnen noteren ...)

Nabespreking: Wat zijn de beperkingen van het matching algoritme? Hoe kan het matching algoritme verbeterd worden? 

#### Leerdoelen
- Basisconcepten van grafen toepassen bij het analyseren van vingerafdrukken.
- Leerlingen ontwikkelen een algoritme om vingerafdrukken met elkaar te matchen (gegeven vingerafdruk identificeren a.d.h.v een vingerafdruk dataset).
- Ontdekkend en onderzoekend leren, kritisch en logisch denken.
- Het nut van wiskunde illustreren.

Na dit onderdeel kunnen de leerlingen …
- basisconcepten van grafen binnen deze context gebruiken
- vingerafdrukken karakteriseren
- vingerafdrukken abstraheren naar een graaf
 -vingerafdrukken analyseren a.d.h.v. grafen
- een algoritme ontwikkelen dat een vingerafdruk laat overeenkomen met een graaf 
- een algoritme ontwikkelen om een gegeven vingerafdruk te matchen met een vingerafdruk uit een dataset
- hun kritisch en logisch denken verbeterd hebben

#### Eindtermen
Grafen, computationeel denken, wisselwerking maatschappij en STEM, mediawijsheid, privacy. 
