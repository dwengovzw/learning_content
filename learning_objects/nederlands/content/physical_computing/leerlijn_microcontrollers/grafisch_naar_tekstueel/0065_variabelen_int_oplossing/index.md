---
hruid: leerlijn_grafisch_naar_tekstueel_variabelen_int_oplossing
version: 1
language: nl
title: "Variabelen (int): oplossing"
description: "Hier zien we hoe een getalvariabele omgezet wordt naar tekstuele code."
keywords: ["programmeren", "blockly", "setup", "while", "loop", "microcontroller", "µC", "arduino", "dwenguino"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16]
difficulty: 3
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Voorwaardelijke herhaling (oplossing)

**Kijk terug naar te tekstuele voorstelling van de begrensde herhaling (for-lus). Herken je daar de variabele? Wat is het type en de naam van die variabele?**

De for-lus zag er als volgt uit.

<div class="dwengo-content">
    <pre>
<code class="language-cpp" data-filename="filename.cpp">

    for (int i = 0 ; i <= 10 ; i+=1) {
    }

</code>
    </pre>
</div>

In de lus gebruik je een variabele van het type <code class="language-cpp">int</code>, hier met de naam <code class="language-cpp">i</code>. Hier wordt de variabele gedeclareerd en toegekend in één lijn: <code class="language-cpp">int i = 0</code>. Op dezelfde lijn staat ook code om de variabele te lezen en die een andere waarde te geven. In de code <code class="language-cpp">i <= 10</code> wordt de waarde van de variabele <code class="language-cpp">i</code> gelezen en vergeleken met het getal <code class="language-cpp">10</code>. Net erna staat de code <code class="language-cpp">i+=1</code>. Deze code is een verkorte versie van <code class="language-cpp">i = i + 1</code> en zal ervoor zorgen dat de waarde van i met 1 verhoogd wordt.