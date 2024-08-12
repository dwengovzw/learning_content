---
hruid: leerlijn_basis_programmeren_functies_met_parameters
version: 1
language: nl
title: "Functies met parameters"
description: "Wat is een functie en waarvoor wordt die gebruikt."
keywords: ["programmeren", "functies", "microcontroller", "µC", "arduino", "dwenguino"]
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

# Functies met parameters

We kunnen aan functies ook waarden meegeven die we kunnen gebruiken binnen de functie. Op die manier kunnen we onze functie generieker maken. Hieronder zie je hoe we onze functie <code class="language-cpp">void knipperLed13()</code> generieker maken zodat we een led op gelijk welke pin kunnen laten knipperen.

<pre>
<code class="language-cpp">
    // Niet generieke versie van de functie
    void knipperLed13(){
        pinMode(13, OUTPUT);
        digitalWrite(13, HIGH);
        delay(500);
        digitalWrite(13, LOW);
        delay(500);
    }

    // Generieke versie van de functie
    void knipperLed(unsigned char pin){
        pinMode(pin, OUTPUT);
        digitalWrite(pin, HIGH);
        delay(500);
        digitalWrite(pin, LOW);
        delay(500);
    }
</code>
</pre>



<div class="dwengo-content sideinfo">
    <h2 class="title">Generieke code</h2>
    <div class="content">
        Probeer je code zo generiek mogelijk te maken. Zo zorg je ervoor dat je code niet moet copy-pasten op verschillende plaatsen. Generieke code is makkelijker te onderhouden. 
        Als er in de naam van de functie zoals in onze <code class="language-cpp">void knipperLed13()</code> functie een verwijzing staat naar iets wat een parameter zou kunnen zijn, in dit geval het pin nummer, dan gebruik je beter een parameter. 
    </div>
</div>


<div class="dwengo-content assignment">
    <h2 class="title">Opdracht</h2>
    <div class="content">
        Schrijf een functie die een led op een pin van de µC \(n\) keer laat knipperen. Hierbij zijn zowel het nummer van de pin als \(n\) parameters van de functie.
    </div>
</div>


