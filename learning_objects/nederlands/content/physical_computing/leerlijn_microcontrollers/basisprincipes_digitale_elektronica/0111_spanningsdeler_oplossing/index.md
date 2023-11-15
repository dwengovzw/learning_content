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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# De spanningsdeler (oplossing)


Hieronder zie je hoe we de weerstandswaarde van R1 kunnen berekenen.

Eerst lijsten we de informatie op die we al kennen. Zo weten we dat onze schakeling op 5V werkt.

\\[V_{in} = 5V\\]

We weten ook dat het spanningsniveau waarop de µC van een logische 0 naar een logische 1 overschakelt 1.3V is.

\\[V_{out} = 1.3V\\]

Verder kunnen we uit de grafiek met de karakteristiek van de lichtsensor aflezen dat die bij een lichtintensiteit van 10 Lux een weerstand van ongeveer 10KΩ zal hebben.

\\[R_2 = 10K\Omega\\]

Deze waarden kunnen we nu invullen in de formule.

\\[V_{out} = \frac{R_2}{R_1+R_2}\times V_{in}\\]

\\[1.3V = \frac{10K\Omega}{R_1+10K\Omega}\times5V\\]

We lossen de vergelijking op om de waarde van R1 te bepalen.

\\[\frac{1.3}{5} = \frac{10K\Omega}{R_1 + 10K\Omega}\\]

\\[\frac{1.3}{5}R_1 + \frac{13}{5} = 10K\Omega\\]

\\[\frac{1.3}{5}R_1 = \frac{50}{5}K\Omega - \frac{13}{5}K\Omega\\]

\\[\frac{1.3}{5}R_1 = \frac{37}{5}K\Omega\\]

\\[R_1 = \frac{5}{1.3} \times \frac{37}{5}K\Omega\\]

\\[R_1 = \frac{37}{1.3}K\Omega \thickapprox 28.46K\Omega\\]


Merk op dat de verhouding tussen de berekende weerstanden (10KΩ en 28.46KΩ) gelijk is aan de verhouding tussen de spanningsniveau's (1.3V en 3.7V).

