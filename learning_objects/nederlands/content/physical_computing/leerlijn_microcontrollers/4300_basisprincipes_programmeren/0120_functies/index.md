---
hruid: leerlijn_basis_programmeren_functies
version: 1
language: nl
title: "Functies"
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

# Functies

Je hebt intussen al meerdere keren gebruik gemaakt van functies. Je schreef bijvoorbeeld een waarde naar een pin aan de hand van de functie <code class="language-cpp">digitalWrite(13, HIGH)</code> of las de afstand van een sonarsensor aan de hand van de functie <code class="language-cpp">ping_cm()</code>. In deze gevallen gebruikte je functies die iemand anders voor jou geschreven heeft. Je kan echter zelf ook functies maken die je later zelf oproept. Wanneer je zelf een functie maakt doe je dit om een bepaalde functionaliteit van je programma te groeperen.

Stel bijvoorbeeld dat je op meerder plaatsen in je programma een lampje wil laten knipperen om informatie over te brengen aan de gebruiker. De code om het lampje te doen knipperen kan je groeperen in een functie.

<pre>
<code class="language-cpp">

    void knipperLed13(){
        pinMode(13, OUTPUT);
        digitalWrite(13, HIGH);
        delay(500);
        digitalWrite(13, LOW);
        delay(500);
    }

</code>
</pre>



Je kan deze functie dan oproepen op andere plaatsten in je code. **Let wel op**: je moet ervoor zorgen dat de code die je functie definieert, zoals die hierboven. Voor de code staat waar de de functie oproept.


```cpp

        #include <Wire.h>
        #include <Dwenguino.h>

        void knipperLed13(){
            pinMode(13, OUTPUT);
            digitalWrite(13, HIGH);
            delay(500);
            digitalWrite(13, LOW);
            delay(500);
        }

        void setup()
        {
            initDwenguino();
            pinMode(SW_S, INPUT_PULLUP);
        }

        void loop()
        {
            // Knipper met led 13 wanneer SW_S is ingedrukt.
            if (digitalRead(SW_S) == LOW){
                knipperLed13();
            }
        }

```


<div class="dwengo-content sideinfo">
    <h2 class="title">Bibliotheken</h2>
    <div class="content">
        Zoals je al zag, kan je bovenaan je programma bibliotheken inladen aan de hand van een <code class="language-cpp">#include</code> commando. Door dit te doen, importeer je functies die door andere mensen geschreven zijn. Zo kan je ze gebruiken in je programma.
    </div>
</div>



