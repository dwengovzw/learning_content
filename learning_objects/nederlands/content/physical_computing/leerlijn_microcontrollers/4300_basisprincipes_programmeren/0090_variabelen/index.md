---
hruid: leerlijn_basis_programmeren_variabelen
version: 1
language: nl
title: "Variabelen"
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

# Variabelen

In het leerpad over invoer-verwerking-uitvoer zagen we al hoe we een digitale en analoge waarde van een pin konden opslaan in een variabele, bijvoorbeeld:

<pre>
    <code class="language-cpp">
        unsigned char digitaleWaardePin6 = digitalRead(6);
    </code>
</pre> 

Bovenstaande lijn code is relatief kort maar ze bevat wel heel wat programmeerconcepten die we onder de knie moeten krijgen. Eerst en vooral bestaat de lijn uit twee delen: 1) Het aanmaken van de variabele ofwel de **declaratie**. 2) Een waarde geven aan de variabele ofwel de **toekenning**.

<pre>
    <code class="language-cpp">
        /*          declaratie               toekenning
        <-------------------------------><---------------> */
        unsigned char digitaleWaardePin6 = digitalRead(6);
    </code>
</pre> 

In het bovenstaande voorbeeld gebeuren de **declaratie** en **toekenning** in dezelfde lijn. Je kan deze twee operaties ook uit elkaar trekken:

<pre>
    <code class="language-cpp">
        /*          declaratie              
        <-------------------------------> */
        unsigned char digitaleWaardePin6;
        
        // Hier komt nog andere code.
        /*            toekenning
        <----------------------------------> */
        digitaleWaardePin6 = digitalRead(6);
    </code>
</pre> 

