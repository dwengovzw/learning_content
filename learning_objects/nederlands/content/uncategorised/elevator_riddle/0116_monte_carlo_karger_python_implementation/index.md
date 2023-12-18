---
hruid: org-dwengo-elevator-riddle-monte-carlo-karger-python-3
version: 1
language: nl
title: "Karger in Python (implementatie)"
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
difficulty: 10
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

## Algoritme van Karger: implementatie

Om twee willekeurige knopen te kiezen, gebruiken we onderstaande functie. We kiezen ervoor om de knopen altijd van klein naar groot gesorteerd terug te geven. Dit zal het makkelijker maken om de rijen en kolommen van de matrix samen te voegen.

```python

def kiesWillekeurigPaarInVolgorde(max):
    p1 = np.random.randint(0, max)
    p2 = np.random.randint(0, max)
    while p1 == p2:
        p2 = np.random.randint(0, max)
    if p2 > p1:
        return [p1, p2]
    else:
        return [p2, p1]

```

We maken gebruik van onderstaande functie om de rijen en kolommen van de matrix samen te voegen. Dit doen we aan de hand van de volgende functie:


```python

# Kies twee willekeurige knopen en voeg ze samen.
def kiesEnVoegSamen(bogen_matrix, knoop_labels):
    willekeurig_paar_knopen = kiesWillekeurigPaarInVolgorde(len(bogen_matrix))

    # Als er geen boog is tussen de twee knopen, kies dan een nieuw paar knopen.
    while (bogen_matrix[willekeurig_paar_knopen[0]][willekeurig_paar_knopen[1]] == 0):
        willekeurig_paar_knopen = kiesWillekeurigPaarInVolgorde(len(bogen_matrix))

    # Add rows of willekeurig_paar_knopen
    bogen_matrix[willekeurig_paar_knopen[0]] += bogen_matrix[willekeurig_paar_knopen[1]]
    bogen_matrix = np.delete(bogen_matrix, willekeurig_paar_knopen[1], axis=0)

    # Add columns of willekeurig_paar_knopen
    bogen_matrix[:, willekeurig_paar_knopen[0]] += bogen_matrix[:, willekeurig_paar_knopen[1]]
    bogen_matrix = np.delete(bogen_matrix, willekeurig_paar_knopen[1], axis=1)

    # Update edge labels
    # Voeg het label van de tweede knoop toe aan de eerste knoop
    knoop_labels[willekeurig_paar_knopen[0]].extend(knoop_labels[willekeurig_paar_knopen[1]])

     # Verwijder de tweede knoop
    knoop_labels.pop(willekeurig_paar_knopen[1])
    if (len(bogen_matrix) > 2):
        return kiesEnVoegSamen(bogen_matrix, knoop_labels)
    else:
        return bogen_matrix, knoop_labels

```

De volgende functie gokt wat de knip kost zou kunnen zijn. Merk op dat we de waardes van de bogen en de labels van de knopen hier in twee afzonderlijke variabelen bijhouden. Dit maakt het makkelijker om de twee los van elkaar aan te passen. 
Deze functie blijft zichzelf oproepen tot de graaf maar twee knopen meer over heeft. Dit noemen we recursie (denk terug aan het algoritme om alle mogelijke combinaties van 4 knopen te genereren).

```python

def gokDeKnipKost(bogen_matrix):
    knoop_labels = [[x] for x in range(len(bogen_matrix))]
    gereduceerde_graaf, gereduceerde_knopen = kiesEnVoegSamen(bogen_matrix, knoop_labels)
     # Return the sum of the edges between the two remaining nodes and the labels of the edges that were contracted
    return gereduceerde_graaf[0][1] + gereduceerde_graaf[1][0], gereduceerde_knopen

```

We hebben nu dus code om een knop te gokken. Deze gok herhalen we nu een aantal keer en nemen de beste gok als oplossing.

```python

# Herhaal gokDeKnipKost n keer en onthoud de beste oplossing
def herhaalGokDeKnipKost(bogen_matrix, n=8):
    huidige_minimale_knip_kost = 100000 # Kies een arbitrair grote minimale kost om mee te starten.
    labels_van_minimale_knip = []
    for i in range(n):
        minknipkost, labels = gokDeKnipKost(bogen_matrix.copy())
        # Onthouw enkel de oplossing als deze beter is dan het huidige minimum.
        if minknipkost < huidige_minimale_knip_kost:
            huidige_minimale_knip_kost = minknipkost
            labels_van_minimale_knip = labels
    return huidige_minimale_knip_kost, labels_van_minimale_knip


minimale_knip_kost, labels = herhaalGokDeKnipKost(bogen_matrix, 8)
print("De minimale knip is: ", minimale_knip_kost)
print("De labels van de knopen zijn: ", labels)

```

Als we deze code uitvoeren krijgen we het volgende resultaat:

De minimale knip is:  9
De labels van de knopen zijn:  [[0], [1, 5, 2, 4, 6, 3, 7]] 

**Opmerking**: Je moet hier een offset van 4 bij optellen om tot het label van de originele knoop te komen.

