---
hruid: leerlijn_microcontrollers_microcontroller_naar_plc_ladder_logische_reductie_oplossing
version: 1
language: nl
title: "Ladder logica: vereenvoudiging (oplossing)"
description: "Wat is Ladder logica?"
keywords: ["microcontroller", "plc", "automatisatie", "programmable logic controller", "µC", "ladder", "latch"]
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
estimated_time: 15
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Ladder logica: vereenvoudiging (oplossing)

* *Hoeveel schakelaars heeft elk diagram?*

**(1): 3 schakelaars**
**(2): 8 schakelaars**

* *Teken de waarheidstabel van elk diagram.*

**(1)**

\\[ \left( A \lor B \right) \land C \Leftrightarrow Q\\]

\\[
    \begin{array}{c|c|c|c|c}
        A & B & C & A \lor B & Q \\\\
        \hline 
        0 & 0 & 0 & 0 & 0 \\\\
        0 & 0 & 1 & 0 & 0 \\\\
        0 & 1 & 0 & 1 & 0 \\\\
        0 & 1 & 1 & 1 & 1 \\\\
        1 & 0 & 0 & 1 & 0 \\\\
        1 & 0 & 1 & 1 & 1 \\\\
        1 & 1 & 0 & 1 & 0 \\\\
        1 & 1 & 1 & 1 & 1 \\\\
    \end{array}
\\]

**(2)**

