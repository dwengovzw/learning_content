---
hruid: leerlijn_basis_programmeren_commentaar
version: 1
language: nl
title: "Commentaar"
description: "Hier leer je hoe commentaar eruitziet in C++."
keywords: ["programmeren", "commentaar", "microcontroller", "µC", "arduino", "dwenguino"]
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

# Commentaar

In de voorbeelden die volgen, gebruiken we vaak commentaar om uitlegt te geven. Commentaar zijn stukken tekst in de code die niet uitgevoerd zullen worden. We kunnen er dus schrijven wat we willen zonder de computer in de war te brengen.

In C++ zijn er twee manieren om om commentaar te schrijven. De eerste manier noemen we **lijn-commentaar**. Met deze soort commentaar kunnen we ervoor zorgen dat, zoals de naam al aangeeft, één regel van ons programma niet wordt uitgevoerd. Lijn-commentaar begint met een <code class="language-cpp">//</code>.

<pre>
    <code class="language-cpp">// De computer zal deze lijn negeren tijdens het uitvoeren.</code>
</pre>

Een tweede soort commentaar noemen we **blok-commentaar**. Met blok-commentaar kunnen we ervoor zorgen dat meerdere lijnen van ons programma niet worden uitgevoerd. Blok commentaar staat tussen <code class="language-cpp">/\*</code> en <code class="language-cpp">\*/</code>

<pre>
    <code class="language-cpp">
/* 
    De computer zal deze lijnen
    negeren tijdens het 
    uitvoeren.
*/
    </code>
</pre>


