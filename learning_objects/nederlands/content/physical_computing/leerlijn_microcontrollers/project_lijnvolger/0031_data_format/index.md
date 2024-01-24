---
hruid: leerlijn_project_lijnvolger_data_format
version: 1
language: nl
title: "Dataformaat"
description: "Hoe stuur ik telemetrie van de robot naar de computer."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "bluetooth", "telemetrie", "dataformaat"]
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

# Dataformaat

We kunnen nu tekst sturen vanop de Dwenguino en deze ontvangen op de computer. Nu moeten we nog een manier bedenken om de gegevens die we willen doorsturen op een gestructureerde manier voor te stellen als tekst. Hier zullen we dit doen in een csv formaat (comma-separated values). In dit formaat wordt data op een lijn van elkaar gescheiden aan de hand van een , of ;. Wij kiezen voor een ;. Hieronder zie je een voorbeeld van gegevens in een csv formaat.

<pre>
<code class="lang-cpp">

"193.23;453.15;456.33;213.11;23.12;78.12"

</code>
</pre>

Op die manier kunnen we in één lijn meerdere gegevens doorsturen naar de computer. We kunnen deze gegevens in Python gemakkelijk terug van elkaar splitsen. De volgende functie zal een pakket opsplitsen in afzonderlijke waarden en deze teruggeven als een lijst van kommagetallen.


<pre>
<code class="lang-python">

def parse_data_pakket(pakket):
    data = pakket.strip().split(';')
    return [float(getal) for getal in data]

</code>
</pre>

