---
hruid: leerlijn_microcontrollers_microcontroller_naar_plc_ladder_4
version: 1
language: nl
title: "Ladder logica: logica"
description: "Wat is Ladder logica?"
keywords: ["microcontroller", "plc", "automatisatie", "programmable logic controller", "µC", "ladder"]
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
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Ladder logica: logische schakelingen

We zagen dat er twee soorten invoer zijn in een ladder diagram: de IF invoer en de IF NOT invoer. Met deze twee soorten invoer kunnen we logische schakelingen bouwen.

## De of poort

Wanneer we meerdere invoeren van het type IF in parallel schakelen, bouwen we een logisch OF poort. Dit wil zeggen dat het circuit stroom zal doorlaten wanneer er minstens een van de invoerwaarden een logische 1 is. Hieronder zie je een ladder diagram van een logische of poort met twee invoeren A en B.

![Voorbeeld van een ladder diagram.](images/sample.png "Voorbeeld van een ladder diagram.")

Je kan de ze logische schakeling dan beschrijven aan de hand van een logische propositie.

\\[Q \Leftrightarrow A \lor B\\]

De mogelijke waarde die deze logische expressie kan hebben, kunnen we uitschrijven in een waarheidstabel.

| \\(A\\) | \\(B\\) | \\(Q\\) |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |