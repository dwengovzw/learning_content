---
hruid: PN_Epidemie3-v1
version: 3
language: nl
title: "Sociale netwerken"
description: "Epidemie"
keywords: ["voorbeeld", "voorbeeld2"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
content_type: text/markdown
available: true
target_ages: [14, 15, 16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-digitale-media-en-toepassingen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-kansrekenen-statistiek',
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek', 
    http://ilearn.ilabt.imec.be/vocab/curr1/s-stem-onderzoek
]
---

# Sociale netwerken

Het standaard SIR-model maakt de onrealistische veronderstelling dat twee willekeurige individuen telkens dezelfde kans hebben om met elkaar in contact te komen 
en zo mogelijks een ziekte door te geven. In werkelijkheid gaat natuurlijk niet iedereen met dezelfde mensen om. 
We hebben allemaal mensen waar we meer mee omgaan (meer in contact mee komen) dan met anderen. 
Het geheel van wie met wie in contact staat, wordt een *sociaal netwerk* genoemd (denk aan Facebook). Het lijkt evident dat de structuur van zo'n netwerk een sterke invloed zal hebben op de dynamiek van de ziekteverspreiding.

Ook sociale netwerken worden wiskundig gemodelleerd. Men steunt daarvoor op de zogenaamde 'grafen'.  
Een graaf bestaat uit een verzameling knopen waarvan sommige verbonden zijn door bogen. 
In het voorbeeld hieronder vertegenwoordigen de knopen de leerlingen. 
De contacten tussen leerlingen worden weergegeven door lijnsegmenten tussen knopen, en worden *bogen* genoemd. 

![Voorbeelden van gekleurde grafen die netwerken tussen kinderen van verschillende leeftijden voorstellen ([bron](https://royalsocietypublishing.org/doi/full/10.1098/rspb.2010.1807)).](embed/netwerkkinderen.png)
<sub>Bron: https://royalsocietypublishing.org/doi/pdf/10.1098/rspb.2010.1807</sub>

Een figuur is nuttig om te bekijken hoe het netwerk eruitziet. Om er berekeningen mee te doen, zijn er echter andere voorstellingen nodig. 
Een graaf kan wiskundig voorgesteld worden in een matrix die een *verbindingsmatrix* (Engels: adjacency matrix) genoemd wordt.

## Ziekteverspreidingsmodellen in de praktijk

Epidemieën komen voortdurend voor en daarom gebruiken volksgezondheidsorganisaties over de hele wereld modellen om interventiestrategieën te ontwikkelen 
en te evalueren. Met behulp van simulaties kunnen ze snel de situatie beoordelen en belangrijke beslissingen nemen. 

Om een ​​epidemie te herkennen en erop te reageren, hebben gezondheidswerkers informatie nodig die inherent onvoorspelbaar 
is (wat, waar, hoeveel gevallen, hoeveel zullen sterven, waar zal het zich verspreiden). 
De interacties die tot het uitbreken van een ziekte leiden, zijn zeer complex, zodat de resultaten soms onverwacht of contra-intuïtief zijn. 
Er zijn modellen nodig om deze interacties te begrijpen en om de kwantitatieve voorspellingen te maken die volksgezondheidswerkers nodig hebben 
om te beslissen over interventiestrategieën.

Menselijk gedrag tijdens ziekte-uitbraken verandert vaak drastisch. 
Mensen vermijden drukke plaatsen of haasten zich naar drukke plaatsen zoals luchthavens of treinstations als ze proberen te ontsnappen aan de epidemie. 
Modellering kan gezondheidswerkers helpen dit soort effecten te voorzien en te begrijpen.

Modellen kunnen ook gebruikt worden om te bepalen hoe bestaansmiddelen toegewezen moeten worden om de beste kans te hebben 
om de verspreiding van de ziekte te stoppen - bijvoorbeeld, als vaccins beperkt zijn, welke groep mensen moet dan prioritair worden gevaccineerd? 
Wetenschappers kunnen modellen gebruiken om de uitkomsten van verschillende controlestrategieën te vergelijken. 
Modellen kunnen ook worden gekoppeld aan langetermijngegevens over het klimaat en klimaatvoorspellingen, om voorspellingen van uitbraken vele maanden 
in de toekomst te maken. Deze benadering wordt gebruikt om vaccinatiecampagnes te bepalen, bijvoorbeeld tegen influenza of mazelen.

Wetenschappers ontwikkelen hun begrip van ziekteverspreiding met behulp van gegevens zoals gedrags-, demografische en epidemische trends, 
maar het is vaak moeilijk om betrouwbare gegevens te verzamelen, en voor veel ziekten missen we nog steeds belangrijke informatie over hoe ze zich verspreiden. 
Modellering kan ook in deze gevallen helpen, omdat wetenschappers verschillende hypotheses kunnen testen om te proberen de hiaten in hun kennis in te vullen.

***

In deze notebooks wordt o.a. het SIR-model toegepast op een netwerk en ga je zelf bepaalde situaties simuleren in het model.

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=1221 "Notebooks Epidemie")
