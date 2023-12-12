---
hruid: leerlijn_invoer_basisprincipes_spanningsdeler_oplossing
version: 1
language: nl
title: "De spanningsdeler (oplossing)"
description: "Je leert wat een spanningsdeler is en waarvoor je die kan gebruiken."
keywords: ["digitale elektronica", "spanningsdeler", "basisprincipes", "microcontroller", "µC", "arduino", "dwenguino"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16]
difficulty: 1
estimated_time: 8
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# De spanningsdeler (oplossing)


Hieronder zie je hoe we de weerstandswaarde van R1 kunnen berekenen.

Eerst lijsten we de informatie op die we al kennen. Zo weten we dat onze schakeling op 5V werkt.

\\[U_{in} = 5\\,\mathrm{V}\\]

We weten ook dat het spanningsniveau waarop de µC van een logische 0 naar een logische 1 overschakelt 1.3V is.

\\[U_{out} = 1.3\\,\mathrm{V}\\]

Verder kunnen we uit de grafiek met de karakteristiek van de lichtsensor aflezen dat die bij een lichtintensiteit van 10 Lux een weerstand van ongeveer 10KΩ zal hebben.

\\[R_2 = 10\\,\mathrm{K\Omega}\\]

Deze waarden kunnen we nu invullen in de formule.

\\[U_{out} = \frac{R_2}{R_1+R_2} U_{in}\\]

\\[1.3\\,\mathrm{V} = \frac{10\\,\mathrm{K\Omega}}{R_1+10\\,\mathrm{K\Omega}} 5\\,\mathrm{V}\\]

We lossen de vergelijking op om de waarde van R1 te bepalen.

\\[\frac{1.3}{5} = \frac{10\\,\mathrm{K\Omega}}{R_1 + 10\\,\mathrm{K\Omega}}\\]

\\[\frac{1.3}{5}R_1 + \frac{13}{5}\\,\mathrm{K\Omega} = 10\\,\mathrm{K\Omega}\\]

\\[\frac{1.3}{5}R_1 = \frac{50}{5}\\,\mathrm{K\Omega} - \frac{13}{5}\\,\mathrm{K\Omega}\\]

\\[\frac{1.3}{5}R_1 = \frac{37}{5}\\,\mathrm{K\Omega}\\]

\\[R_1 = \frac{5}{1.3} \frac{37}{5}\\,\mathrm{K\Omega}\\]

\\[R_1 = \frac{37}{1.3}\\,\mathrm{K\Omega} \thickapprox 28.46\\,\mathrm{K\Omega}\\]


Merk op dat de verhouding tussen de berekende weerstanden (\\(10\\,\mathrm{K\Omega}\\) en \\(28.46\\,\mathrm{K\Omega}\\)) gelijk is aan de verhouding tussen de spanningsniveau's (\\(1.3\\,\mathrm{V}\\) en \\(3.7\\,\mathrm{V}\\)).

