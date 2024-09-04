---
hruid: leerlijn_invoer_verwerking_uitvoer_digitale_uitvoer
version: 1
language: nl
title: "Digitale uitvoer"
description: "Leer hoe je een digitale waarde schrijft naar een pin van de µC."
keywords: ["invoer", "verwerking", "uitvoer", "microcontroller", "µC", "arduino", "dwenguino", "digitalWrite"]
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
estimated_time: 3
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Digitale uitvoer

Naar digitale pinnen kan je ook een waarde schrijven (1 of 0). Zo stel je het spanningsniveau op de pin in op 5 V of 0 V. Hieronder zie je hoe je met de Arduino/Dwenguino-bibliotheek de waarde 1 (= HIGH) naar pin 12 kan schrijven.

```cpp
digitalWrite(12, HIGH)
```

Merk op dat de waarde `HIGH` gedefinieerd wordt in de Arduino/Dwenguino-bibliotheek. De waarde van `HIGH` is gelijk aan 1. Je kan de code dus ook op de volgende manier schrijven.

```cpp
digitalWrite(12, 1)
```

De eerste manier heeft de voorkeur omdat dit de **leesbaarheid** van de code beter maakt. In professionele omgevingen is leesbare code zeer belangrijk.

Ook de waarde `LOW` wordt gedefinieerd in de Arduino/Dwenguino-bibliotheek. De waarde van `LOW` is gelijk aan 0.

<div class="dwengo-content sideinfo">
    <h2 class="title">Wist je dat!</h2>
    <div class="content">
        <p>
            Uit wetenschappelijk onderzoek blijkt dat professionele programmeurs heel veel belang hechten aan leesbaarheid en begrijpbaarheid van code. Wanneer je professionele programmeurs vraagt naar de eigenschappen van kwaliteitsvolle code, dan brengt ongeveer 80 % de leesbaarheid ervan in rekening. Om dit in perspectief te plaatsen, van diezelfde groep zal maar ongeveer 50 % zeggen dat de code functioneel correct moet zijn.
        </p>
        <p>
            Börstler, J., Störrle, H., Toll, D., Van Assema, J., Duran, R., Hooshangi, S., ... & MacKellar, B. (2018, January). "I know it when I see it" Perceptions of Code Quality: ITiCSE'17 Working Group Report. <em>In Proceedings of the 2017 iticse conference on working group reports</em> (pp. 70-85).
        </p>
    </div>
</div>
