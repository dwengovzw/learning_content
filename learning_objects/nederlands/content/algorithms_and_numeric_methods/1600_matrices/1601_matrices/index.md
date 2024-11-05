---
hruid: anm_1601
version: 3
language: nl
title: "Voorbeeld"
description: "Matrices"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Voorbeeld

Beschouw het volgende stelsel van vergelijkingen:
\\[\begin{cases} 3 x + y - 4 z = 3 \\\ 3 y - 5 z = -11 \\\ x - 5 y - 2 z = 11 \end{cases}\\]

De overeenkomstige matrix is:
\\[\begin{bmatrix} 3 & 1 & -4 & 3 \\\ 0 & 3 & -5 & -11 \\\ 1 & -5 & -2 & 11 \end{bmatrix}\\]

## Het stelsel manipuleren 

\\[\begin{cases} 3 x + y - 4 z = 3 \\\ 3 y - 5 z = -11 \\\ x - 5 y - 2 z = 11 \end{cases}\\]

In de derde vergelijking beide leden vermenigvuldigen met 3:
\\[\begin{cases} 3 x + y - 4 z = 3 \\\ 3 y - 5 z = -11 \\\ 3 x - 1 5 y - 6 z = 33 \end{cases}\\]

De eerste vergelijking aftrekken van de derde vergelijking:
\\[\begin{cases} 3 x + y - 4 z = 3 \\\ 3 y - 5 z = -11 \\\ -16 y - 2 z = 30 \end{cases}\\]

In de derde vergelijking beide leden delen door -2:
\\[\begin{cases} 3 x + y - 4 z = 3 \\\ 3 y - 5 z = -11 \\\ 8 y + z = -15 \end{cases}\\]

In de eerste vergelijking beide leden vermenigvuldigen met 3:
\\[\begin{cases} 9 x + 3 y - 12 z = 9 \\\ 3 y - 5 z = -11 \\\ 8 y + z = -15 \end{cases}\\]

De tweede vergelijking aftrekken van de eerste vergelijking:
\\[\begin{cases} 9 x - 7 z = 20 \\\ 3 y - 5 z = -11 \\\ 8 y + z = -15 \end{cases}\\]

Het stelsel ziet er al eenvoudiger uit. Merk op dat in de eerste kolom enkel het getal op de eerste rij verschillend is van nul.

## De matrix manipuleren 
De matrix verandert mee met het stelsel.

\\[\begin{bmatrix} 3 & 1 & -4 & 3 \\\ 0 & 3 & -5 & -11 \\\ 1 & -5 & -2 & 11 \end{bmatrix}\\]
\\[\begin{bmatrix} 3 & 1 & -4 & 3 \\\ 0 & 3 & -5 & -11 \\\ 0 & -16 & -2 & 30 \end{bmatrix}\\]
\\[\begin{bmatrix} 3 & 1 & -4 & 3 \\\ 0 & 3 & -5 & -11 \\\ 0 & 8 & 1 & -15 \end{bmatrix}\\]
\\[\begin{bmatrix} 9 & 0 & -7 & 20 \\\ 0 & 3 & -5 & -11 \\\ 0 & 8 & 1 & -15 \end{bmatrix}\\]

## Voer deze werkwijze verder door
In de derde vergelijking beide leden vermenigvuldigen met 3:
\\[\begin{cases} 9 x - 7 z = 20 \\\ 3 y - 5 z = -11 \\\ 24 y + 3 z = -45 \end{cases}\\]

Een achtvoud van de tweede vergelijking aftrekken van de derde vergelijking:
\\[\begin{cases} 9 x - 7 z = 20 \\\ 3 y - 5 z = -11 \\\ 43 z = 43 \end{cases}\\]

De overeenkomstige matrix:
\\[\begin{bmatrix} 9 & 0 & -7 & 20 \\\ 0 & 3 & -5 & -11 \\\ 0 & 0 & 43 & 43 \end{bmatrix}\\]

Beide leden van de derde vergelijking delen door 43:
\\[\begin{cases} 9 x - 7 z = 20 \\\ 3 y - 5 z = -11 \\\ z = 1 \end{cases}\\]

De overeenkomstige matrix:
\\[\begin{bmatrix} 9 & 0 & -7 & 20 \\\ 0 & 3 & -5 & -11 \\\ 0 & 0 & 1 & 1 \end{bmatrix}\\]

Merk op dat in de tweede kolom enkel het getal op de tweede rij verschillend is van nul.

Een zevenvoud van de derde vergelijking optellen bij de eerste vergelijking:
\\[\begin{cases} 9 x = 27 \\\ 3 y - 5 z = -11 \\\ z = 1 \end{cases}\\]

De overeenkomstige matrix:
\\[\begin{bmatrix} 9 & 0 & 0 & 27 \\\ 0 & 3 & -5 & -11 \\\ 0 & 0 & 1 & 1 \end{bmatrix}\\]

Beide leden van de eerste vergelijking delen door 9:
\\[\begin{cases} x = 3 \\\ 3 y - 5 z = -11 \\\ z = 1 \end{cases}\\]

De overeenkomstige matrix:
\\[\begin{bmatrix} 1 & 0 & 0 & 3 \\\ 0 & 3 & -5 & -11 \\\ 0 & 0 & 1 & 1 \end{bmatrix}\\]

Een vijfvoud van de derde vergelijking optellen bij de tweede vergelijking:
\\[\begin{cases} x = 3 \\\ 3 y = -6 \\\ z = 1 \end{cases}\\]

De overeenkomstige matrix:
\\[\begin{bmatrix} 1 & 0 & 0 & 3 \\\ 0 & 3 & 0 & -6 \\\ 0 & 0 & 1 & 1 \end{bmatrix}\\]

Beide leden van de tweede vergelijking delen door 3:
\\[\begin{cases} x = 3 \\\ y = -2 \\\ z = 1 \end{cases}\\]

De overeenkomstige matrix:
\\[\begin{bmatrix} 1 & 0 & 0 & 3 \\\ 0 & 1 & 0 & -2 \\\ 0 & 0 & 1 & 1 \end{bmatrix}\\]

Merk op dat in derde kolom enkel het getal op de derde rij verschillend is van nul.

De matrix is nu gediagonaliseerd. Het stelsel is opgelost.

De oplossingsverzameling van het stelsel is \\(\{\(3, -2, 1\)\}\\).
