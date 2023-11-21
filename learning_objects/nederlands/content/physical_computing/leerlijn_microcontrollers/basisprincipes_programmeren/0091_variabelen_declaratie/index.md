---
hruid: leerlijn_basis_programmeren_variabelen_declaratie
version: 1
language: nl
title: "Variabelen (delcaratie)"
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

# Variabelen (delcaratie)

Bekijk je de declaratie van dichterbij dan zal je zien dat deze uit twee delen bestaat: 1) Het type van de variabele. 2) De naam van de variabele die je in je programma zal gebruiken om ernaar te verwijzen.

<pre>
    <code class="language-cpp">
        /*          declaratie                  toekenning
        <----------------------------------><---------------> 
           type             naam
        <-----------><------------------>*/
        unsigned char digitaleWaardePin6 = digitalRead(6);
    </code>
</pre> 

## Het type van een variabele

Het type van de variabele geeft aan welke soort informatie we erin kunnen opslaan. C++ heeft heel wat ingebouwde types. In onderstaande tabel zie je een overzicht.

<table>
    <tr>
        <th>Code</th>
        <th>Mogelijke waarden</th>
        <th>Aantal bits</th>
        <th>Beschrijving</th>
    </tr>
    <tr>
        <td><code class="language-cpdd">char</code></td>
        <td>\(\left[-127, 127\right]\)</td>
        <td>8</td>
        <td>Het <code class="language-cpdd">char</code> type is het kleinst moegelijke datatype in C++. Het komt van het woord character omdat 8 bits gebruikt werd om karakters/letters in op te slaan.</td>
    </tr>
    <tr>
        <td><code class="language-cpdd">unsigned char</code></td>
        <td>\(\left[0, 255\right]\)</td>
        <td>8</td>
        <td>Het <code class="language-cpdd">unsigned char</code> type heeft evenveel bits als een <code class="language-cpdd">char</code> maar kan enkel positieve getallen bevatten.</td>
    </tr>
</table>


In het bovenstaande voorbeeld gebeuren de **declaratie** en **toekenning** in dezelfde lijn. Je kan deze twee operaties ook uit elkaar trekken:

<pre>
    <code class="language-cpp">
        /*          declaratie              
        <-------------------------------> */
        unsigned char digitaleWaardePin6;
        
        // Hier komt nog andere code.
        /*            toekenning
        <---------------------------------> */
        digitaleWaardePin6 = digitalRead(6);
    </code>
</pre> 

