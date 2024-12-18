---
hruid: org-dwengo-waisda-soc-netwerken-graaf-de-bruijn-graaf
version: 1
language: nl
title: "De 'De Bruijn' graaf"
description: "Hoe kunnen we het resultaat van shotgun sequencing voorstellen aan de hand van een de Bruijn graaf."
keywords: ["grafen","Euleriaans pad", "DNA", "sequencing", "RNA", "De Bruijn"]
content_type: "text/markdown"
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/vak1/informatica-wetenschappen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen',
    'http://ilearn.ilabt.imec.be/vocab/tref1/ict',

]
copyright: "CC BY dwengo"
target_ages: [14, 15, 16, 17, 18]
teacher_exclusive: False
---

# De "De Bruijn"-graaf

Om de volledige DNA streng te reproduceren op basis van de stukjes DNA die het resultaat zijn van shotgun sequencing, kan je gebruik maken van een De Bruijn graaf. 

Voor we deze graaf opstellen, zetten we onze stukjes DNA eerst om naar een lijst van overlappende **k-meren**. Een **k-meer** is een stukje DNA van k nucleotiden lang? Is k bijvoorbeeld 3 dan maken we een lijst met stukjes DNA van 3 nucleotiden lang (3-meren).

Nemen we bijvoorbeeld de sequentie GAGCTTTTAG, dan kunnen we deze omzetten naar 7 overlappende 3-meren: GAG, AGC, GCT, CTT, TTT, TTT, TTA en TAG. 

![](img/splitting_dna_into_overlapping_sequences.svg)

Op basis van deze k-meren bouwen we de De Bruijn graaf. Daarvoor nemen we elke k-meer. Voegen we de prefix van lengte k-1 toe als knoop aan de graaf. Voegen we de suffix van lengte k-1 toe als knoop aan de graaf. En verbinden die met een boog.

Voor GAG levert dat de volgende graaf op.

![](img/de_bruijn_1.svg)

Zo voegen we elke k-meer toe aan de graaf. 

AGC

![](img/de_bruijn_2.svg)

GCT

![](img/de_bruijn_3.svg)

CTT

![](img/de_bruijn_4.svg)

TTT

![](img/de_bruijn_5.svg)

TTT

![](img/de_bruijn_6.svg)

TTA

![](img/de_bruijn_7.svg)

TAG

![](img/de_bruijn_8.svg)

We voegen niet enkel de k-meren voor deze ene subsequentie (GAGCTTTTAG) toe maar ook voor alle andere subsequenties die we gelezen hebben met shotgun sequencing. Door voldoende stukjes DNA toe te voegen aan de graaf, krijg je een graaf die de structuur van het volledige genoom voorstelt. De volledige DNA sequentie van dat genoom kan je dan vinden door het euleriaans pad te zoeken in die graaf.


