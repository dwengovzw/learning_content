---
hruid: leerlijn_basis_programmeren_variabelen_toekenning
version: 1
language: nl
title: "Variabelen (toekenning)"
description: "Wat zijn variabelen en hoe kan je het gebruiken."
keywords: ["programmeren", "variabele", "type", "int", "char", "unsigned", "float", "microcontroller", "µC", "arduino", "dwenguino"]
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
estimated_time: 15
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

# Variabelen (toekenning)

De toekenning zorgt ervoor dat de variabele een waarde krijgt.

<pre>
    <code class="language-cpp">
        /*          declaratie            
        <-------------------------------> */
        unsigned char digitaleWaardePin6;
        /*            toekenning
        <------------------------------->*/
        digitaleWaardePin6 = digitalRead(6);
    </code>
</pre> 

De waarde kan, zoals hierboven, een resultaat zijn van een functieoproep. Maar het kan ook een berekening of een constante zijn.

<pre>
    <code class="language-cpp">
        /*        declaratie            
        <------------------------------->*/ 
        unsigned char digitaleWaardePin6;
        /*  toekenning met constante
        <------------------------------->*/
        digitaleWaardePin6 = 210;
    </code>
</pre> 

<pre>
    <code class="language-cpp">
        /*          declaratie            
        <------------------------------->*/
        unsigned char digitaleWaardePin6;
        /*  met berekening toekenning
        <------------------------------->*/
        digitaleWaardePin6 = 15 + 8;
    </code>
</pre> 

Wanneer je in je programma meerdere toekenningen hebt van dezelfde variable, zal een latere toekenning een eerdere waarde overschrijven.

<pre>
    <code class="language-cpp">
        digitaleWaardePin6 = 12;

        // Hier is digitaleWaardePin6 == 12

        digitaleWaardePin6 = 42;

        // Hier is digitaleWaardePin6 == 42
    </code>
</pre> 

<div class="dwengo-content sideinfo">
    <h2 class="title">Interessant!</h2>
    <div class="content">
        Bij een toekenning gebruiken we een <code class="language-cpp">=</code> om een waarde toe te wijzen aan een variabele. Deze heeft een andere betekenis dan de \(=\) uit de wiskunde. In de wiskunde wil \(=\) zeggen dat de delen links en rechts ervan gelijk zijn. In code betekent <code class="language-cpp">=</code> dat we de waarde rechts van de <code class="language-cpp">=</code> toekennen aan de variabele aan de linker kant. We passen dus de waarde van de variabele aan.
    </div>
</div>