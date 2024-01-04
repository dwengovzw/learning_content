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

Je kan de afstand ook nog op andere manieren berekenen. Een ander soort algoritme, dat vaak in de computerwetenschappen wordt gebruikt, zijn de recursieve algoritmes. Een recursief algoritme bestaat uit een functie met een aantal parameters. Deze functie zal een deel van de oplossing berekenen en dan zichzelf oproepen om de rest te berekenen. Hieronder zie je een voorbeeld van een recursief algoritme voor de Levenshtein afstand.

```python

def levenshtein(woord1, woord2):
    # Als woord1 geen letters meer bevat
    # dan moeten we nog alle letters van woord2 toevoegen.
    # De kost daarvan is het aantal letters in woord2 (= de lengte van het woord).
    if len(woord1) == 0:
        return len(woord2)
    # Als woord2 geen letters meer bevat
    # dan moeten we de rest van de letters van woord1 verwijderen.
    # D kost daarvan is het aantal letters in woord1
    if len(woord2) == 0:
        return len(woord1)
    # Als de eerste letter van woord1 gelijk is aan de eerste letter van woord2
    # dan is de afstand tussen deze woorden dezelfde als de afstand tussen 
    # woord1 waarin de eerste letter wordt weggelaten 
    # en woord2 waarin de eerste letter wordt weggelaten.
    if woord1[0] == woord2[0]:
        return levenshtein(woord1[1:], woord2[1:])
    # Als de eerste letter verschillend is
    # dan is de afstand het minimum van de volgende gevallen
    else:
        return 1 + min(levenshtein(woord1[1:], woord2), # De afstand tussen woord1 zonder eerste letter en woord2
                    levenshtein(woord1, woord2[1:]), # De afstand tussen woord1 en woord2 zonder de eerste letter
                    levenshtein(woord1[1:], woord2[1:])) # De afstand tussen woord1 zonder eerste letter en woord2 zonder eerste letter.

```


