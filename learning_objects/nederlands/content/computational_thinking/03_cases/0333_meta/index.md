---
hruid: m_ct03_33
version: 3
language: nl
title: "Terraslamp"
description: "Automatische terrasverlichting"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/ct-schema
available: true
target_ages: [12, 13, 14]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 1
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

<context>
Zorg ervoor dat de terrasverlichting aan een villa, als het buiten donker is, automatisch geactiveerd wordt bij beweging. Deze buitenverlichting kan ook ingeschakeld kan worden via een schakelaar binnen in de keuken. 
</div>
</context>
<decomposition>
Verkennen van het probleem. Wat heb je nodig? <br> 
Subtaken (**decompositie**):<br>
<ol>
    <li>Welke invoerelementen?</li>
        <ol> <li>Bewegingsdetector A (bij beweging is A  = 1)</li>
             <li>Lichtsensor B (donker B = 0)</li>
             <li>Schakelaar C (ingedrukt C = 1)</li>
        </ol>
    <li>Welke uitvoerelementen?</li>
        <ol>
            <li>Lamp L (brandt L = 1)</li>
        </ol>
    <li>Het gevraagde weergeven d.m.v. een waarheidstabel en Karnaugh-diagram. </li>
</ol>
</decomposition>
<patternRecognition>
Soortgelijke problemen kennen een vaste manier van aanpak: het opstellen van een waarheidstabel en het Karnaugh-diagram. (**patroonherkenning**)
</patternRecognition>
<abstraction>
Het gevraagde wordt **abstract** weergegeven d.m.v. een waarheidstabel en een Karnaugh-diagram.<br>
![Waarheidstabel](waarheidstabel.png)  <br>
![Karnaughdiagram](karnaugh.png)
</abstraction>
<algorithms>
De oplossing van het probleem houdt de sturing van de verlichtingsinstallatie in a.d.h.v. een **algoritme** (hier in een flowchart en in pseudocode).<br>
![Pseudocode](pseudocode1terraslamp.png)<br>
![Flowchart](flowchart.png)<br>
![Pseudocode](pseudocode2terraslamp.png)
</algorithms>
<implementation>
Deze activiteit kan zonder computer gebeuren.
</implementation>

