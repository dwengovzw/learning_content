---
hruid: stem5_0
version: 3
language: nl
title: "Rupsenuitbraak modelleren"
description: "Rupsenuitbraak modelleren"
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
# Modelleren van een rupsenuitbraak met een exponentiële functie

## Ecologen modelleren

Ecologen bestuderen hoe levende organismen interageren met andere levende organismen en met hun omgeving. <br>
Een van de meest fundamentele vragen die ze proberen te beantwoorden, is hoe een populatie vandieren, planten, bacteriën of mensen verandert doorheen de tijd. Groeit ze? Daalt ze? Stagneert ze? Gaat depopulatie op en neer? Kan ze plots imploderen? 

Dit soort vragen beantwoorden ecologen aan de hand van groeimodellen: wiskundige vergelijkingen die de (verwachte) groei doorheen de tijd voorstellen. 

## Ontmoet de buxusmot

Vele insecten zijn nuttig, maar vaak zijn ze een plaag wanneer ze de planten opvreten. Zo is de rups van de buxusmot (*Cydalima perspectalis*) een nachtmerrie voor elke tuinier met een mooie buxushaag. De buxusmot is een invasieve soort in Europa met een grote economische kost.

Foto buxusmot in actie

Omdat deze rups zo schadelijk is, zijn ecologen en gewasbeschermers erg geïnteresseerd om de groei van populaties op te volgen en te modelleren. Wiskundige modellen helpen hen in te schatten of de populatie binnen een aanvaardbare grootte blijft of wanneer ze dreigt uit haar voegen te treden en bestrijding nodig is.

## Een wiskundig model

Een wiskundig model is een vereenvoudiging van de werkelijkheid. Hier zal je de rupsenpopulatie modelleren in perfecte, niet-overlappende generaties. 

**Het doel is om een rij te bekomen die te populatiegrootte doorheen de tijd voorstelt:**<br>
<p style="text-align: center;">**x<sub>0</sub>, x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>t-1</sub>, x<sub>t</sub>, ...**</p>

Hierbij geldt:<br>
-  x<sub>0</sub> is de initiële populatiegrootte: het aantal rupsen bij het begin van de metingen.
-  x<sub>t</sub> stelt de populatiegrootte voor op generatie of tijdstip t.
-  t neemt de waarden 0, 1, 2, 3 ... aan.

**Stel dat x<sub>t-1</sub>, het aantal rupsen op het tijdstip t-1, gekend is. Wat is dan x<sub>t</sub>? M.a.w. hoeveel rupsen zijn er dan op tijdstip t?**<br>
Je gaat m.a.w. op zoek naar een regel die vertelt wat de populatiegroote op tijdstip t is, gegeven het aantal rupsen er zijn op tijdstip t-1. 

We maken drie veronderstellingen voor zo'n regel:
We gaan ervan uit dat de regel determistisch is. Als we de grootte kennen op tijdstip
, resulteert ditaltijd in dezelfde grootte op tijdstip
. We houden dus geen rekening met willekeurige fluctuaties.
We nemen aan dat onze populatie groot genoeg is zodat we de kunnen voorstellen aan de hand van reëlegetallen zoals
,
, en
in plaats van natuurlijke getallen zoals
,
en
. Inwerkelijkheid zijn er geen (levende) 'halve' rupsen. Voor de eenvoud nemen we aan dat de populatie grootgenoeg is dat de populatie oneindig deelbaar is zodat kommagetallen een goede benadering zijn. FN: Voorwie zich nog altijd niet helemaal lekker voelt bij fracties van rupsen, je kan ook over
denken als debiomassa van rupsen. Dit is het totaal gewicht van rupsen op tijdstip
.
De populatiegrootte wordt bekeken in een reeks van perfect gescheiden generaties. We zeggen dus de tijddiscreet doortikt. Onze modellen geven de groottes aan op tijdstippen
, maar het houdt geensteek om te kijken naar tijdstip
. Er is niets tussen de generaties!
