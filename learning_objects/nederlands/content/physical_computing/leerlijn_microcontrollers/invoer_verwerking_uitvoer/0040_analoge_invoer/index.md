---
hruid: leerlijn_invoer_verwerking_uitvoer_analoge_invoer
version: 1
language: nl
title: "Analoge invoer"
description: "Leer hoe je een analoge waarde leest van een pin van de µC."
keywords: ["invoer", "verwerking", "uitvoer", "microcontroller", "µC", "arduino", "dwenguino", "analogRead"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Analoge invoer

De µC heeft speciale schakelingen die in staat zijn om een voltage op een pin om te zetten naar een getal. Deze schakeling zal een voltage tussen 0V en 5V registreren en omzetten naar een binair getal van 10 bits. Dit getal kunnen we in onze code dan lezen met de analogRead() functie van de arduino bibliotheek.

```cpp
unsigned int analoge_waarde_pin_A0 = analogRead(A0);
```

`analoge_waarde_pin_A0` is de variabele waarin we de analoge waarde opslaan.
`unsigned int` is het type van de variabele `analoge_waarde_pin_A0`. Variabelen van dit type bevatten getallen tussen 0 en 65535.
`analogRead(A0)` is de functie van de Arduino bibliotheek waarmee we de analoge waarde van pin A0 lezen.

<div class="dwengo-content assignment">
<h2>Inzichtsvraag</h2>
<p>
Waarom gebruiken we bij het lezen van analoge invoer int als type van de variabele <<code class="language-cpp">unsigned int</code> wanneer we bij het lezen van digitale invoer het type <code class="language-cpp">unsigned char</code> gebruiken?
</p>
</div>