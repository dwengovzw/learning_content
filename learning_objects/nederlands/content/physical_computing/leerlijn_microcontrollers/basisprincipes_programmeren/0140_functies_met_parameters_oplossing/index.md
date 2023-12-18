---
hruid: leerlijn_basis_programmeren_functies_met_parameters_oplossing
version: 1
language: nl
title: "Functies met parameters (oplossing)"
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Functies met parameters (oplossing)

<pre>
<code class="language-cpp">

    void knipperLed(unsigned char pin, unsigned char aantalKeer){
        pinMode(pin, OUTPUT);
        for (unsigned char i = 0 ; i < aantalKeer ; i++){
            digitalWrite(pin, HIGH);
            delay(500);
            digitalWrite(pin, LOW);
            delay(500);
        } 
    }
</code>
</pre>





