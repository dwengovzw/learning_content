---
hruid: org-dwengo-elevator-riddle-monte-carlo-karger
version: 1
language: nl
title: "Algoritme van Karger"
description: "Het algoritme van Karger gebruikt de Monte Carlo methode om tot een oplosing te komen."
keywords: ["grafen", "algoritme", "computationeel denken", "clustering", "datastructuur", "monte carlo", "python", "karger"]
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
]
teacher_exclusive: false
---
# Monte Carlo

## Algoritme van Karger

Voor het bepalen van de minimale knip van een graaf bestaat ook een Monte Carlo algoritme. Dit wordt het algoritme van Karger genoemd (naar de uitvinder David Karger). Hieronder leggen we stap voor stap uit hoe dit algoritme werkt.

Het algoritme van Karger zal de graaf die in stukken geknipt moet worden, reduceren tot een graaf met maar twee knopen. De kost om die graaf in twee te knippen is dan de som van alle bogen die die twee knopen verbinden. Deze som is wat het algoritme gokt dat de minimale kost is. Deze procedure wordt een aantal keer herhaald waarna de beste gok gekozen wordt als finaal resultaat. Hieronder zie je een voorbeeld van hoe de graaf gereduceerd kan worden.

|  | <div style="min-width:450px"></div> |
| - | -- |
| We starten met de volledige graaf. | ![Karger stap 1](embed/karger1.png "Stap 1") |
|  |  |
| We kiezen een willekeurige boog en de twee knopen die aan die boog grenzen. | ![Karger stap 2](embed/karger2.png "Stap 2.") |
|  |  |
| We voegen de twee knopen samen door de boog die ze verbindt, weg te laten. Alle andere bogen die uit een van de twee knopen vertrokken, vertrekken nu uit de gecombineerde knoop. | ![Karger stap 3](embed/karger3.png "Stap 3.") |
|  |  |
| Als er knopen zijn waartussen er meerdere bogen lopen, vervangen we deze bogen door één boog. Het gewicht van deze boog is gelijk aan de som van de gewichten van de bogen die we vervangen. Tussen knoop (4, 8) en knoop (6) zijn er bijvoorbeeld twee bogen met gewicht 3. Deze vervangen we door één boog met gewicht 6. | ![Karger stap 4](embed/karger4.png "Stap 4.") |
|  |  |
| Daarna kiezen we opnieuw een willekeurige boog. | ![Karger stap 5](embed/karger6.png "Stap 5.") |
|  |  |
| De aangrenzende knopen van deze boog voegen we opnieuw samen. | ![Karger stap 6](embed/karger7.png "Stap 6.") |
|  |  |
| En we reduceren weer dubbele bogen tussen twee dezelfde knopen. | ![Karger stap 7](embed/karger8.png "Stap 7.") |
|  |  |
| Dit blijven we herhalen tot er slechts 2 knopen over blijven. Boog selecteren. | ![Karger stap 8](embed/karger9.png "Stap 8.") |
|  |  |
| Knopen samenvoegen. | ![Karger stap 9](embed/karger10.png "Stap 9.") |
|  |  |
| Bogen reduceren. | ![Karger stap 10](embed/karger11.png "Stap 10.") |
|  |  |
| Boog selecteren. | ![Karger stap 11](embed/karger12.png "Stap 11.") |
|  |  |
| Knopen samenvoegen en bogen reduceren. | ![Karger stap 12](embed/karger13.png "Stap 12.") |
|  |  |
| Boog selecteren. | ![Karger stap 13](embed/karger14.png "Stap 13.") |
|  |  |
| Knopen samenvoegen en bogen reduceren. | ![Karger stap 14](embed/karger15.png "Stap 14.") |
|  |  |
| Boog selecteren. | ![Karger stap 15](embed/karger16.png "Stap 15.") |
|  |  |
| Knopen samenvoegen en bogen reduceren. | ![Karger stap 16](embed/karger17.png "Stap 16.") |


Na deze reductie is onze gok voor de minimale knip het gewicht van de boog tussen de twee resterende nodes. In dit geval dus 22. **Merk op dat dit algoritme er niet voor zorgt dat de verdeling van de knopen in te twee delen van de knip gelijk is.** In ons geval zitten er 6 knopen in de ene graaf en twee knopen in de andere. 


