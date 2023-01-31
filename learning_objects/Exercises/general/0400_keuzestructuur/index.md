---
hruid: g_ks
version: 3
language: nl
title: "Uitleg Keuzestructuur"
description: "Uitleg Keuzestructuur"
keywords: ["oefeningen", "keuzestructuur"]
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
teacher_exclusive: false
---
# DwenguinoBlockly
## Keuzestructuren: Als - Dan

Om van je robot een sociale robot te maken, zal die in staat moeten zijn om te reageren op bepaalde prikkels: een persoon die dichter komt, een luide klap... Denk bijvoorbeeld aan schuifdeuren die opengaan wanneer iemand in de buurt komt.

Om je robot te laten reageren op zulke prikkels, gebruik je een keuzestructuur. Keuzestructuren bestaan steeds uit een **voorwaarde**, *ALS*, en een daaraan gekoppelde **actie**, *DAN*. Vaak voorziet men ook een **alternatieve actie**, *ANDERS* die uitgevoerd wordt indien er niet aan de voorwaarde voldaan is.

***

In de simulator vind je de blokken voor een keuzestructuur terug in de categorie ![](embed/cat_logica.png "categorie logica"). De simpelste vorm van dit blok is het *'ALS-DAN'-blok*.

![](embed/keuzestructuur1.png "ALS-DAN-blok")

Je kan dit blok echter zolang maken als je wilt, afhankelijk van het aantal voorwaarden waarmee je robot moet rekening houden. Hoe je dit doet, wordt hieronder kort voorgetoond.

![](embed/keuzestructuur2.png "ALS-DAN-ANDERS")

<div class="alert alert-box alert-danger">
Zoals eerder vermeldt, kan je dit blok zo lang maken als je wilt, maar let er wel op dat je je programma niet onnodig ingewikkeld maakt!
</div>

***

Om voorwaarden voor een keuzestructuur te programmeren, maak je gebruik van de onderstaande blokken:

![](embed/block_and_or.png "blok en-of")
![](embed/block_operations.png "blok wiskundige operaties")

Wanneer je deze combineert, kan je zeer eenvoudige voorwaarden programmeren zoals: 

![](embed/combo_andor_operations.png "combinatie voorwaarden")