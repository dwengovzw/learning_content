---
hruid: org_dewengo_levenshtein_algorithm_dynamic
version: 1
language: nl
title: "Implementatie dynamisch programmeren"
description: "Een algoritme om de Levenshtein afstand te bepalen."
keywords: ["taaltechnologie", "taal", "afstand", "levenshtein", "algoritme", "python", "dynamisch programmeren"]
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

# Een algoritme met dynamisch programmeren.

We kunnen nu code schrijven die de tabel van de Levenshtein afstand voor ons invult. Daarvoor schreven we een functie in Python die als parameters de twee woorden waartussen we de afstand willen bepalen meekrijgt. En als resultaat de afstand tussen deze woorden teruggeeft. Merk om dat, omdat we nu de twee woorden opslaan in afzonderlijke variabelen (<code class="lang-python">woord1</code> en <code class="lang-python">woord1</code>), het niet meer nodig is om de woorden ook in de eerste rij en eerste kolom van de tabel op te slaan. In de code zal onze tabel dus enkel de berekende afstanden tussen de prefixes van de woorden bevatten.

```python
import numpy as np

def levenshtein(woord1, woord2):
    # Maak een tabel waarbij het aantal rijen gelijk is aan de lengte van woord1 + 1
    # en het aantal kolommen gelijk is aan de lengte van woord2 + 1.
    # We doen de lengte + 1 om plaats te maken voor het lege woord.
    afstands_matrix = np.zeros((len(woord1)+1, len(woord2)+1))
    # vul de eerste rij en kolom met de afstanden van en naar het lege woord.
    for i in range(len(woord1)+1):
        afstands_matrix[i][0] = i
    for j in range(len(woord2)+1):
        afstands_matrix[0][j] = j
    # Overloop de matrix kolom per kolom
    for j in range(1, len(woord2)+1):
        for i in range(1, len(woord1)+1):
            # In de meeste gevallen zal de kost om een letter te vervangen gelijk zijn aan 1.
            # Dit wil zeggen dat de twee letters niet gelijk zijn
            substitutie_kost = 1
            # Als de letters op positie i en j toch gelijk zijn, dan is de substitutie_kost 0
            if woord1[i-1] == woord2[j-1]:
                substitutie_kost = 0
            # Neem de kost als het minimum van de volgende opties:
            # 1. De kost om een extra letter toe te voegen aan woord1
            # 2. De kost om een letter te verwijderen uit woord1
            # 3. De kost om een letter te vervangen in woord1
            afstands_matrix[i][j] = min(afstands_matrix[i-1][j] + 1, # Kijk naar het vakje boven het huidige vakje en doe het +1
                                        afstands_matrix[i][j-1] + 1, # Kijk naar de waarde links van het huidige vakje en doe het +1
                                        afstands_matrix[i-1][j-1] + substitutie_kost) # Kijk naar de waarde diagonaar linksboven en doe deze waarde + substitutie_kost.
    # Geef de waarde van het vakje rechtsonder terug.
    return afstands_matrix[len(woord1)][len(woord2)] 
```


