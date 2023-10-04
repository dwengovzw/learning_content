---
hruid: org-dwengo-elevator-riddle-brute-force-2
version: 1
language: nl
title: "Stap 1: De graaf splitsen"
description: "Hoe splitsen we onze graaf in twee delen?"
keywords: ["grafen", "algoritme", "computationeel denken", "clustering", "datastructuur", "brute force"]
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
# Brute kracht

## Alle mogelijke manieren om de graaf in twee gelijke delen te splitsen

Onze graaf bestaat uit acht knopen (de verdiepingen). We kunnen deze in twee verdelen door vier knopen uit te kiezen en deze toe te kennen aan lift 1. De vier knopen die overblijven, kennen we toe aan lift 2.  
We kunnen het aantal keuzes van vier items uit acht opties berekenen met onze kennis van combinatoriek \\(\mathrm{C}^4_8 = 70\\).

Om alle 70 combinaties te genereren, kunnen we een eenvoudig algoritme bedenken.

We starten zonder verdeling. We hebben nog geen enkele verdieping gekozen om toe te kennen aan lift 1:

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| x | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

Voor de eerste verdieping in de lijst hebben we twee opties, ofwel kennen we die toe aan lift 1 ofwel niet. In het geval dat we deze verdieping niet kiezen voor lift 1, wordt deze automatisch toegekend aan lift 2. Dat geeft de volgende opties voor de eerste keuze:


|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 1 | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 2 | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

We kunnen deze twee gevallen nu in detail bekijken.

#### Geval 1: De eerste verdieping in de lijst werd toegekend aan lift 1.

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 1 | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

In dat geval zijn er nog zeven verdiepingen die we moeten toekennen aan een lift. Daarvan mogen we er nog 3 toekennen aan lift 1. Er zijn voor deze overige zeven verdiepingen dus nog \\(\mathrm{ C }^3_7 = 35\\) mogelijkheden. Om deze te verdelen over de liften kunnen we opnieuw een keuze maken voor de eerste van de zeven overgebleven verdiepingen. Zo krijgen we de volgende twee mogelijkheden.


|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 1 | 1 | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 1 | 2 | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

#### Geval 2: De eerste verdieping in de lijst werd toegekend aan lift 2.

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 2 | x | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

In dit geval mogen we uit de overgebleven verdiepingen er nog vier kiezen om toe te kennen aan lift 1. Er zijn voor de overige zeven verdiepingen nog \\(\mathrm{ C }^4_7 = 35\\) mogelijkheden. Ook hier kunnen we het algoritme verder zetten door een selectie te maken voor de tweede verdieping in de lijst.

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 2 | 1 | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| 2 | 2 | x | x | x | x | x | x |
|   |   |   |   |   |   |   |   |

#### Geval 1 en geval 2 veralgemenen

Als we goed naar de twee hierboven beschreven gevallen kijken, zien we een patroon opduiken (**patroonherkenning**).
- We nemen telkens een keuze voor de eerste nog niet toegekende verdieping in de lijst. 
- Kennen we die verdieping toe aan lift 1 dan verlagen we het aantal keer dat we lift 1 nog mogen toekennen met 1 en kennen die hoeveelheid van de resterende verdiepingen toe aan lift 1.
- Kennen we die verdieping niet toe aan lift 1 dan mogen we van de resterende verdiepingen er nog evenveel toekennen aan lift 1.
