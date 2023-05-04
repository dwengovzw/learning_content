---
hruid: g_rgb
version: 3
language: en
title: "Uitleg RGB-led"
description: "Uitleg RGB-led"
keywords: ["oefeningen", "RGB-led"]
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
# dwenguinoBlockly
## RGB-led

### Type
- Uitvoer
- Digitale Actuator

### Werking
De RGB-led is een led waarvan je de kleur van het licht zelf kan bepalen door de intensiteit van rood, groen en blauw licht (de primaire kleuren) te programmeren. De intensiteit wordt doorgegeven als een getal tussen 0 en 255 (van lage tot hoge intensiteit). Houd er rekening mee dat niet alle kleuren even goed kunnen wordenweergegeven op de RGB-led via het RGB-kleurenmodel (bv. bruin).

***

### In het echt

![](embed/rgb.png "RGB-led")

### In de simulator

![](embed/rgb_sim.png "RGB-led simulator")

De blokken die je nodig hebt voor het programmeren van de led-matrices vind je terug onder de categorie ![](embed/cat_uitvoer.png "categorie uitvoer").

### Belangrijke combinaties

|**Kleur**|**R (Rood)**|**G (Groen)**|**B (Blauw)**|
|---|---|---|---|
|Wit|255|255|255|
|Zwart|0|0|0|
|Rood|255|0|0|
|Groen|0|255|0|
|Blauw|0|0|255|

> Een <strong>kleurmengsysteem</strong> is een systeem gebaseerd op het idee dat je met een bepaalde set kleuren, <strong>primaire kleuren</strong> genoemd, alle andere kleuren kunt maken.<br><br>Het <strong>subtractieve kleurmengsysteem</strong> is het meest gekende, omdat kinderen dit zelf gemakkellijk kunnen ontdekken tijdens kleuren of verven. Rood + blauw = paars, blauw + geel = groen, geel + rood = oranje, ... Dit gaat uit van de primaire kleuren <strong>cyaan</strong> <em>(hemelsblauw)</em>, <strong>magenta</strong> <em>(een soort roze)</em> en <strong>geel</strong>.<br><br>Het <strong>additieve kleurmengsysteem</strong> is minder intuïtief. Dit wordt gebruikt bij het "mengen" van verschillende kleuren <strong>licht</strong>. De primaire kleuren zijn voor dit kleurmengsysteem <strong>rood</strong>, <strong>groen</strong> en <strong>blauw</strong>.

<div class="alert alert-box alert-success">
Voor meer informatie over de de RGB-led kan je terecht in de leerlingenfiches van de <em>Sociale Robot</em>.
</div>