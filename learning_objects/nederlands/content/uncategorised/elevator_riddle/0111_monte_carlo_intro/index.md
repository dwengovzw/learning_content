---
hruid: org-dwengo-elevator-riddle-monte-carlo
version: 1
language: nl
title: "Statistische methodes"
description: "Op basis van statistische methodes kunnen we op een snelle manier en met een hoge kans de correct oplossing vinden."
keywords: ["grafen", "algoritme", "computationeel denken", "clustering", "datastructuur", "monte carlo", "python"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
difficulty: 5
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 2
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---

# Monte Carlo

Onze eerste oplossing voor het probleem maakte gebruik van een brute kracht algoritme. Deze soort algoritmes proberen alle mogelijke combinaties uit en nemen dan de beste. Ondanks dat computers tegenwoordig heel snel, heel veel berekeningen kunnen uitvoeren, is het voor veel problemen toch onmogelijk om die met brute kracht op te lossen. Dat is ook zo voor het graaf knip probleem. Voor dergelijke problemen gaan informaticawetenschappers vaak op zoek naar alternatieve algoritmes. Deze alternatieve algoritmes offeren de zekerheid dat je een exacte oplossing bekomt op in ruil voor een sneller algoritme. Deze algoritmes worden **heuristieken** genoemd.

Een type **heuristiek** dat op verschillende problemen kan toegepast worden, is **Monte Carlo algoritmes**. De naam voor dit soort algoritmes is geïnspireerd op de gelijknamige wijk in de stadsstaat Monaco. In de wijk staat het bekende Monte Carlo Casino waar veel mensen graag hun geld verspelen. Monte Carlo algoritmes kregen deze naam omdat ze, net zoals de speler in een casino, gokken wat een correcte oplossing zou kunnen zijn. De kans dat het algoritme correct gokt, is klein maar door meerdere keren na elkaar te gokken en de beste oplossing te onthouden kunnen deze algoritmes toch goede resultaten opleveren.

