---
hruid: leerlijn_basis_programmeren_conditie
version: 1
language: nl
title: "Conditie: waar of vals?"
description: "Wat is een conditie en hoe kan je het gebruiken."
keywords: ["programmeren", "waar", "vals", "true", "false", "microcontroller", "µC", "arduino", "dwenguino"]
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
teacher_exclusive: true
---

# Selectie: conditie (waar of vals)

Een conditie is een stukje code dat als resultaat de waarde waar (<code class="language-cpp">true</code>) of vals (<code class="language-cpp">false</code>) heeft. Een conditie kan een vergelijking zijn tussen waarden maar ook het resultaat van een functieoproep. Hieronder zie je een aantal voorbeelden van condities.

<pre>
    <code class="language-cpp">
        // Controlleer of een afstand kleiner of gelijk is aan 100.
        afstand <= 100
        // Controleer of de waarde van pin 12 hoog is.
        digitalRead(12) == HIGH
        // Roep een functie op die controleert of er licht wordt gedetecteerd.
        isErLicht()
    </code>
</pre>

### Operatoren

Meestal zie je een conditie onder de vorm van een vergelijking tussen twee waarden. Je wil bijvoorbeeld weten of een afstand **kleiner of gelijk** is aan 100. Deze **kleiner of gelijk** noemen we in een programmeertaal een vergelijkingsoperator. In de tabel hieronder zie je een overzicht van de vergelijkingsoperatoren in C++.

<table>
    <tr>
        <th>Operator</th>
        <th>Naam</th>
        <th>Voorbeeld</th>
    </tr>
    <tr>
        <th><code class="language-cpp">==</code></th>
        <th>Gelijk</th>
        <th><code class="language-cpp">afstand == 100</code></th>
    </tr>
    <tr>
        <th><code class="language-cpp"></code>!=</th>
        <th>Niet gelijk</th>
        <th><code class="language-cpp"></code>digitalRead(sw_S) != HIGH</th>
    </tr>
    <tr>
        <th><code class="language-cpp">&gt;</code></th>
        <th>Groter dan</th>
        <th><code class="language-cpp">afstand > 0</code></th>
    </tr>
    <tr>
        <th><code class="language-cpp">&lt;</code></th>
        <th>Kleiner dan</th>
        <th><code class="language-cpp">afstand < 200</code></th>
    </tr>
    <tr>
        <th><code class="language-cpp">>=</code></th>
        <th>Groter of gelijk aan</th>
        <th><code class="language-cpp">afstand >= 10</code></th>
    </tr>
    <tr>
        <th><code class="language-cpp"><=</code></th>
        <th>Kleiner of gelijk aan</th>
        <th><code class="language-cpp">afstand <= 150</code></th>
    </tr>
</table>


