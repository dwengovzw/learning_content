---
hruid: org_dewengo_levenshtein_algorithm_recursive
version: 1
language: nl
title: "Recursieve implementatie"
description: "Een algoritme om de Levenshtein afstand te bepalen."
keywords: ["taaltechnologie", "taal", "afstand", "levenshtein", "algoritme", "python", "recursie"]
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

# Een recursief algoritme

TODO: info over recursie

<code class="lang-python">
    def levenshtein(woord1, woord2):
        if len(woord1) == 0:
            return len(woord2)
        if len(woord2) == 0:
            return len(woord1)
        if woord1[0] == woord2[0]:
            return levenshtein(woord1[1:], woord2[1:])
        else:
            return 1 + min(levenshtein(woord1[1:], woord2),
                        levenshtein(woord1, woord2[1:]),
                        levenshtein(woord1[1:], woord2[1:]))
</code>


