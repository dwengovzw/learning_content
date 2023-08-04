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

Routeplanners zijn een veelgebruikte digitale toepassing. Ze hebben op meerdere manieren een impact op onze maatschappij.
Alvast een voorbeeld.

## Impact: meer verkeer in woonwijken
Veel mensen gebruiken een navigatiesysteem in de auto, bijvoorbeeld om snel ergens naartoe te rijden waar ze nog nooit geweest zijn, of om files te ontwijken.

In de media vind je tal van berichten die toenemend verkeer in woonwijken wijten aan het wijdverspreid gebruik van navigatiesystemen.

> **Leestips:**<br>
> [Navigatieapp Waze laat Brusselse woonstraten vollopen](https://www.bruzz.be/analyse/navigatieapp-waze-laat-brusselse-woonstraten-vollopen-2019-09-18)<br>
> [Waze Asked to Stop Providing Drivers With Traffic Shortcuts Because of Obvious Reasons](https://www.autoevolution.com/news/waze-asked-to-stop-providing-drivers-with-traffic-shortcuts-because-of-obvious-reasons-215490.html)

## Principes van computationeel denken

![ct-schema](@learning-object/m_ct_impact_2/nl/3)
 
## Bespreking van de impact

-  Een van de redenen dat routeplanners zoveel gebruikt worden en daardoor de mogelijkheid hebben om impact te hebben, is de grote mate van **abstractie** in de routplanner. Indien gewenst, kan je enkel de instructies opvolgen van de weg die je moet volgen (het stappenplan). Je moet je niet bezighouden met het opzoeken van de weg op een kaart, waarbij je rekening zou moeten houden met bv. eenrichtingsverkeer, de oriëntatie van de kaart, enz. <br> Bovendien krijg je er bijkomende informatie zoals files, wegwerkzaamheden, waar je kan tanken, enz. <br> Zo'n routeplanner heeft dus een groot gebruiksgemak.
    - De routeplanner is zo ingeburgerd dat mensen er vaak niet bij stilstaan dat het gebruik ervan niet steeds de beste manier is om de weg te vinden. Soms is het trouwens onmogelijk om een routeplanner te gebruiken, bijvoorbeeld als er geen internetbereik is of als de batterij van je smartphone plat is.
    - Omdat er in routeplanners zoveel geabstraheerd wordt, heb je geen volledig zicht meer op de omgeving. Dat kan ook een nadeel zijn t.o.v. een papieren kaart die veel meer details geven van de omgeving en een bepaalde plaats bovendien situeren in een groter gebied. Routplanners hollen als het ware het ruimtelijk bewustzijn rond een plaats uit. 
    - Teveel afhankelijk zijn van digitale routeplanners, kan ook gevaarlijk zijn. Sommige plaatsen zijn onvoldoende gedetailleerd of onnauwkeurig aanwezig, waardoor mensen bv. een treinspoor of een trap oprijden, temidden van wegenwerken belanden of spookrijden. Digitale routeplanners kunnen ook fouten bevatten, zoals een foute maximale snelheid die op een bepaalde weg is toegelaten of een straat met eenrichtingsverkeer die als tweerichtingsverkeer is aangegeven.
      > [Politie Heusden-Zolder waarschuwt voor gebruik van GPS bij wegenwerken](https://www.vrt.be/vrtnws/nl/2021/09/23/politie-heusden-zolder-waarschuwt-voor-gebruik-van-gps-bij-wegen/)

-  Het gebruik van een routeplanner door zoveel mensen kan ook ongewenste effecten hebben, zoals extra verkeer in woonwijken wanneer een routeplanner het autoverkeer langs woonwijken zou omleiden om files te vermijden.
    - Het kan zijn dat het **algoritme** van de routeplanner met het aspect van de omgeving 'in een woonwijk' rekening houdt, maar mogelijk is dat aspect niet als parameter opgenomen in het algoritme. De routeplanner hoeft bijvoorbeeld om de kortste route te bepalen vooral rekening te houden met de parameter afstand; andere parameters zoals het feit dat een straat in een woonwijk ligt, worden dan mogelijk genegeerd.
    - Het digitaal systeem achter de routeplanner kan bepaalde **patronen** detecteren, zoals een route die doorgaans enkel gekend is door lokale bewoners en door hen courant gebruikt wordt. Als het systeem die route toevoegt als mogelijk traject, dan zal de route ook bekend worden bij niet-lokale autobestuurders en zo mogelijk de drukte in een woonwijk doen toenemen.

- Ethische aspecten:
    - Routeplanners gebruiken algoritmes die de weg berekenen, vaak rekening houdend met real time informatie, zoals files, die ze dan proberen te ontwijken. Real time verkeersinformatie kan afkomstig zijn van meerdere bronnen, bijvoorbeeld de politie of een beheerder van een autosnelweg. Maar het systeem kan ook informatie bekomen via de momentele gebruikers van de routeplanner. Hierbij is het aspect van privacy gemoeid. 
        - Wordt daarbij opgeslagen waar de gebruiker zich bevindt?
        - Als de locaties van de gebruiker worden opgeslagen, dan rijst de vraag wat het bedrijf achter de routeplanner aanvangt met die gegevens.
    - Routeplanners doen ook aan het verstrekken van reclame. 
        - Zo wordt bepaald welke winkels, tankstations ... getoond worden.
        - Zo kan een toerist via de routeplanner bv. te weten komen welke zaken er in de buurt zijn van het hotel.
        - Mogelijk zijn er afspraken met commerciële partners om hen zoeveel mogelijk op de routes te laten aanwezig zijn.
        - De routeplanner heeft daartoe toegang tot **databanken** van restaurants, winkels, bioscopen, enz. Dat zijn andere databanken dan de strikt noodzakelijke om de routeplanner te doen werken. 
    - Routeplanners kunnen ook rekening houden met zaken die je niet zou verwachten.
      > [Navigatie Mercedes ontwijkt criminele buurten](https://www.ad.nl/auto/navigatie-mercedes-ontwijkt-criminele-buurten~a48a4169/)<br>
-------------------------------
## Impact op online shopping en op de zorgsector
Routeplanners leiden tot nieuwe verwachtingen op het gebied van online shoppen, zoals snellere levering van pakjes en levering door rijdende robots of drones. 

Het gebruik van routeplanners kan ervoor zorden dat een bedrijf de kosten en de tijd gebruikt voor transport kan minimaliseren en de werking kan optimaliseren, bv. bij een leveringsbedrijf of taxibedrijf.
> ["Without location technology, delivering packages for Christmas would be a nightmare!"](https://www.here.com/learn/blog/last-mile-holiday-season-2021)

Rijdende robots worden gebruikt om in de buurt van de supermarkt etenswaren en andere boodschappen te bezorgen.
> [GETEST. Wij lieten onze boodschappen leveren door robot van Carrefour: “We geloven onze ogen niet ”](https://www.nieuwsblad.be/cnt/dmf20230726_96924324)

Behalve in de verkoop, is men ook in andere sectoren gaan nadenken over de opportuniteiten van navigatiesystemen.<br> Robots en drones kunnen a.d.h.v. een digitaal navigatiesysteem de weg vinden.

In de zorgsector zag men bv. de mogelijkheid tot het inzetten van medische drones voor het transport tussen ziekenhuizen.  
> [Met Medical Drone Service in minuten heen en weer tussen ziekenhuislocaties](https://www.antoniusziekenhuis.nl/nieuwsoverzicht/met-medical-drone-service-minuten-heen-en-weer-tussen-ziekenhuislocaties-0)<br>

Bij de brandweer van Genk zet men drones in om een betere inschatting te kunnen van een incident.
> [Genks proefproject met safety drones krijgt navolging in het hele land](https://www.vrt.be/vrtnws/nl/2023/03/14/genks-proefproject-met-safety-drones-krijgt-navolging-in-het-hel/)<br>

-----------------------------
### Werking 
In het leerpad 'Grafen' wordt [de werking van een routeplanner](https://staging.dwengo.org/backend/api/learningObject/getWrapped?hruid=aiz_routeplanner&version=3&language=nl) uit de doeken gedaan.

-----------------------------
#### Leestips

[TomTom VIA53: voor navigatie en files omzeilen](https://www.intogadgets.nl/tomtom-via53-voor-navigatie-en-files-omzeilen/)<br>
[TomTom Mapmakers: Meet Leen D’hondt, Product Manager, TomTom Maps](https://developer.tomtom.com/blog/spotlight/tomtom-mapmakers-meet-leen-dhondt-product-manager-tomtom-maps/)<br>
[‘Vermijden, verschuiven en verschonen: hoe kunnen we e-commerce duurzamer organiseren?’](https://www.knack.be/nieuws/vermijden-verschuiven-en-verschonen-hoe-kunnen-we-e-commerce-duurzamer-organiseren/)<br>
[Delivery robots begin to look real](https://www.gpsworld.com/delivery-robots-begin-to-look-real/)<br>
[Autonomous Robots for Industry 4.0](https://starshipdeliveries.com/industry/)

#### Kijktips

[Delivery robotsStarship Completes One Million Autonomous Deliveries](https://youtu.be/tQZWe1JFR9g)<br>
[A Day in the Life of a Starship Robot](https://youtu.be/Z417CncwQsg)<br>
[Presentatie over o.a. werking delivery robots](https://youtu.be/6rq6Hx0PRAc)


