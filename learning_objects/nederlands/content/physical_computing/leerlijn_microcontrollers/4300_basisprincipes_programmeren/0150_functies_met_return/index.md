---
hruid: leerlijn_basis_programmeren_functies_met_return
version: 1
language: nl
title: "Functies met returnwaarde"
description: "Wat is een functie die een waarde teruggeeft en waarvoor wordt die gebruikt."
keywords: ["programmeren", "functies", "return", "microcontroller", "µC", "arduino", "dwenguino"]
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

# Functies met returnwaarde

Functies kunnen ook een waarde teruggeven nadat de code erin werd uitgevoerd. Dat is bijvoorbeeld nuttig wanneer je een berekening op meerdere plaatsen in je progamma moet uitvoeren met andere waarden. Stel dat we een afstand meten met een sonarsensor en op basis van die afstand een hoorbaare toon willen afspelen. De afstand die de sensor meet zal tussen de \\(0\,\mathrm{cm}\\) en \\(200\,\mathrm{cm}\\) liggen. De frequenties die we kunnen horen liggen tussen de \\(200\,\mathrm{Hz}\\) en \\(12000\,\mathrm{Hz}\\). Om de afstandswaarde om te zetten in een frequentiewaarde, kunnen we een functie schrijven die dit voor gelijk welke afstand doet.



<pre>
<code class="language-cpp">

    float zetAfstandOmNaarFrequentie(float afstandInCm){
        float maximaleAfstand = 200;
        // Is de afstand groter dan de maximale afstand, 
        // geef dan de maximale frequentie terug.
        if (afstandInCm > maximaleAfstand){
            return 12000; 
        }
        // Zet de afstand om naar een waarde tussen 0 en 1
        float afstandTussen0en1 = afstandInCm / maximaleAfstand;
        // Reken om naar frequentie 
        float frequentie = 11800 * afstandTussen0en1 + 200;
        return frequentie;
    }

</code>
</pre>

Deze functie kan je dan overal in je code oproepen om een afstand om te zetten naar een frequentie:
<pre>
<code class="language-cpp">

    float frequentie = zetAfstandOmNaarFrequentie(100);
    
</code>
</pre>






