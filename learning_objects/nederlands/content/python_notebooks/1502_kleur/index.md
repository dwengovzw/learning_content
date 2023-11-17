---
hruid: pn_db_kleur
version: 3
language: nl
title: "Kleur"
description: "Notebooks over ..."
keywords: ["Python", "STEM", "Wiskunde", "AI Op School", Computationeel denken"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
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
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-getallenleer', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-mediawijsheid', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-algebra-analyse', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-kansrekenen-statistiek'
]
---

# Afbeeldingen in kleur

In deze notebook maak je kennis met de wiskunde achter digitale beelden in kleur. In plaats van matrices worden nu tensoren gebruikt.

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=1502 "Notebooks kleur")

------------
Kleuren komen voor in een spectrum. 
![](embed/spectrum.png "Kleurenspectrum")

De kleuren die mensen zien, kunnen benaderd worden door een combinatie van rode(R), groene(G) en blauwe(B) tinten. <br>
Kleuren kunnen digitaal voorgesteld worden door RGB. Er is dan voor de rode, groen en blauwe tinten telkens een tabel nodig; deze vormen een 3D-raster. 

![](embed/rgb.png "RGB")

![](embed/raster.png "3D-raster")

Ook de kleuren op een televisietoestel zijn bijvoorbeeld opgebouw aan de hand van RGB, zoals je kan zien op de volgende ingezoomde foto van een deel van een televisiebeeld. 

![](embed/RGBtelevisie.jpg "RGB")
