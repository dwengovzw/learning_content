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

## De **OF** schakeling

Wanneer we meerdere invoeren van het type IF in **parallel** schakelen, bouwen we een logisch OF poort. Dit wil zeggen dat het circuit stroom zal doorlaten wanneer er minstens een van de invoerwaarden een logische 1 is. Hieronder zie je een ladder diagram van een logische OF poort met twee invoeren A en B.

| Ladder diagram |
|:---:|
| ![Voorbeeld van een ladder diagram.](images/sample_no_labels.svg "Voorbeeld van een ladder diagram.") | 

Je kan de ze logische schakeling dan beschrijven aan de hand van een logische propositie.

\\[ A \lor B \Leftrightarrow Q\\]

De mogelijke waarde die deze logische expressie kan hebben, kunnen we uitschrijven in een waarheidstabel.

\\[
    \begin{array}{c|c|c}
        A & B & Q \\\\
        \hline 
        0 & 0 & 0 \\\\
        0 & 1 & 1 \\\\
        1 & 0 & 1 \\\\
        1 & 1 & 1 \\\\
    \end{array}
\\]


## De **EN** schakeling

Wanneer we meerdere invoeren van het type IF in **serie** schakelen, bouwen we een logisch EN poort. Dit wil zeggen dat het circuit stroom zal doorlaten wanneer alletwee de invoerwaarden een logische 1 hebben. Hieronder zie je een ladder diagram van een logische EN poort met twee invoeren A en B.

| Ladder diagram |
|:---:|
| ![Voorbeeld van een ladder diagram.](images/and.svg "Voorbeeld van een ladder diagram.") | 

Je kan de ze logische schakeling dan beschrijven aan de hand van een logische propositie.

\\[ A \land B \Leftrightarrow Q\\]

De mogelijke waarde die deze logische expressie kan hebben, kunnen we uitschrijven in een waarheidstabel.

\\[
    \begin{array}{c|c|c}
        A & B & Q \\\\
        \hline 
        0 & 0 & 0 \\\\
        0 & 1 & 0 \\\\
        1 & 0 & 0 \\\\
        1 & 1 & 1 \\\\
    \end{array}
\\]


<div class="dwengo-content assignment">
<h2 class="title">Hier de titel van de opdracht</h2>
<div class="content">
Hieronder zie je de waarheidstabel van de logische XOR operatie. Teken een ladder diagram die deze logica implementeert.

\\[
    \begin{array}{c|c|c}
        A & B & Q \\\\
        \hline 
        0 & 0 & 0 \\\\
        0 & 1 & 1 \\\\
        1 & 0 & 1 \\\\
        1 & 1 & 0 \\\\
    \end{array}
\\]

</div>
</div>