---
hruid: anm_0103
version: 3
language: nl
title: "Computationeel denken"
description: "Tentje-boompje"
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

# Computationeel denken

### Decompositie
- Het gegeven schema op een digitale manier voorstellen om aan de computer te geven.
- De tenten moeten kunnen worden geteld.
- Het schema bevat uiteindelijk drie soorten velden: velden met een boom, velden met een tent, en velden dieleeg blijven.
- Tijdens het oplossen van de puzzel moet er een onderscheid zijn tussen de velden waarvan nog nietgeweten is wat er komt en de velden die leeg zullen blijven.
- Het oplossen zal iteratief gebeuren: telkens zal moeten nagegaan worden of er velden zijn waarvan zeker isdat ze leeg zullen blijven, of bepaalde rijen of kolommen al het gevraagde aantal tenten hebben.

### Abstractie
- Het schema voorstellen m.b.v. een matrix.
- Elk veld in het schema komt overeen met een element in de matrix en wordt bepaald door zijn indices(overeenkomstig de rij en de kolom).
- Voor het gegeven schema wordt de volgende representatie gebruikt: in de matrix staat er op de plaats vande bomen het getal 100, op de lege plaatsen een 0.
- Als de puzzel opgelost is, zal de matrix drie verschillende elementen bevatten.
- Als de puzzel opgelost is, dan staat er op de plaats van de bomen een 100, op de plaats van de tenten een1, en op de plaatsen waar er niets staat een 10.
- Als de puzzel opgelost is, dan staat er geen 0 meer in de matrix.
- Een functie schrijven voor code die herhaald wordt.

### Patroonherkenning
- Objecten worden weergegeven door getallen. Verschillende objecten door verschillende getallen.
- Wees bij het opstellen van de code alert voor code die herhaald wordt.

### Algoritme
1. In zo'n veld komt zeker geen tent: ofwel niet onder, boven of naast een boom.
2. In zo'n veld komt zeker geen tent: rakend aan een tentveld.
3. In zo'n veld komt zeker geen tent: overblijvende velden in een rij of kolom met reeds het vereiste aantaltenten.
4. Voor elke rij en voor elke kolom: vergelijk het aantal lege velden en het aantal reeds aanwezige tenten methet vereiste aantal tenten. Zijn er net genoeg plaatsen, vul de tenten in.
5. Herhaal stappen 2, 3 en 4 tot elke rij het juiste aantal tenten bevat.
6. Gebruik een keuze- of herhalingsstructuur wanneer dat van toepassing is.
