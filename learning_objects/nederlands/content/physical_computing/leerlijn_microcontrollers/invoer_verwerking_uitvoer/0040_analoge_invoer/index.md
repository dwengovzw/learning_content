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
estimated_time: 8
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Analoge invoer

De µC heeft speciale schakelingen die in staat zijn om een voltage op een pin om te zetten naar een getal. Deze schakeling zal een voltage tussen 0V en 5V registreren en omzetten naar een binair getal van 10 bits. Dit getal kunnen we in onze code dan lezen met de analogRead() functie van de arduino bibliotheek.

```cpp
unsigned int analogeWaardePinA0 = analogRead(A0);
```

- `analogeWaardePinA0` is de variabele waarin we de analoge waarde opslaan.
- `unsigned int` is het type van de variabele `analogeWaardePinA0`. Variabelen van dit type bevatten getallen tussen **0 en 65535**.
- `analogRead(A0)` is de functie van de Arduino bibliotheek waarmee we de analoge waarde van pin A0 lezen.
- `A0` is een constante gedefinieerd in de Arduino bibliotheek. Deze komt overeen met het nummer van een bepaalde pin. Bij de Arduino UNO is dit `14`. Voor de Dwenguino is dit pin nummer `24`. Op de Arduino Mega is het dan weer pin nummer `54`.

<div class="dwengo-content assignment">
    <h2 class="title">Inzichtsvraag</h2>
    <div class="content">
        <p>
        Waarom gebruiken we bij het lezen van analoge invoer <code class="language-cpp">unsigned int</code> als type van de variabele <code class="language-cpp">analogeWaardePinA0 </code> wanneer we bij het lezen van digitale invoer het type <code class="language-cpp">unsigned char</code> gebruiken?
        </p>
    </div>
</div>

<div class="dwengo-content sideinfo">
    <h2 class="title">Wist je dat!</h2>
    <div class="content">
        <p>
            Het gebruik van constanten zoals <code class="language-cpp">A0</code> maakt de code niet enkel leesbaarder. Deze <strong>abstractie</strong> zorgt er ook voor dat je dezelfde code kan uitvoeren op verschillende microcontrollerplatformen. Gebruik je niet de waarde <code class="language-cpp">A0</code> maar het overeenkomstige pin nummer bv. <code class="language-cpp">24</code> op de Dwenguino, zal je om dezelfde code te kunnen uitvoeren op een Arduino UNO het pin nummer overal in je code moeten aanpassen.
        </p>
    </div>
</div>