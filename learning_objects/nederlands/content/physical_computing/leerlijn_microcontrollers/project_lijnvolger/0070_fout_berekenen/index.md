---
hruid: leerlijn_project_lijnvolger_fout_berekenen
version: 1
language: nl
title: "Afstand lijn meten"
description: "Hoe meet ik de afstand tot de lijn."
keywords: ["lijnvolger", "dwenguino", "robot", "project", "µC", "grondsensor", "fout"]
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

# Afstand meten tot de lijn

Nu we onze sensoren gekalibreerd hebben en kunnen uitlezen, moeten we deze meting kunnen omzetten naar een waarde die aangeeft hoe ver de robot afwijkt van de lijn op de grond. We weten dat we een \\(1\\) meten wanneer een sensor op de lijn staat en een \\(0\\) wanneer die op een wit vlak staat. Wanneer de middelste twee grondsensoren een lijn detecteren, is de afwijking nog klein. Hoe verder een sensor van het midden van de robot verwijderd is, hoe meer de robot afwijkt van de lijn. Deze informatie gebruiken we om te berekenen hoe ver de robot afwijkt van de lijn. 

We kennen aan elke sensor een waarde toe. Deze waarde stelt de afstand van de sensor tot het midden van de robot voor. We slaan deze waarden op in een lijst.

<pre>
<code class="lang-cpp">

int afwijking[AANTAL_SENSOREN] = {-3.0, -2.0, -1.0, 1.0, 2.0, 3.0};

</code>
</pre>

Om de totale afwijking te berekenen kunnen we elke gemeten sensorwaarde vermenigvuldigen met de overeenkomstige afwijking en al deze waarden optellen.

<pre>
<code class="lang-cpp">

    float berekenFout(){
        float fout = 0; // Veronderstel fout = 0
        float afwijking[AANTAL_SENSOREN] = {-3.0, -2.0, -1.0, 1.0, 2.0, 3.0};
        // Overloop de sensoren, vermenigvuldig de gemeten waarde met de overeenkomstige afwijking en tel op.
        for (char i = 0 ; i <= AANTAL_SENSOREN ; ++i){
            fout += afwijking[i] * sensorWaarden[i];
        }
        return fout
    }

</code>
</pre>