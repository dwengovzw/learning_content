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
Zorg ervoor dat de terrasverlichting aan een villa, als het buiten donker is, automatisch geactiveerd wordt bij beweging, en dat je deze buitenverlichting ook kan inschakelen via een schakelaar in de keuken. <br>
(Voorkennis: De leerlingen kennen in- en uitvoerelementen van digitale systemen. Ze kunnen werken met waarheidstabellen.)
</div>
</context>
<decomposition>
Verkennen van het probleem. Wat heb je nodig? <br> 
Subtaken (**decompositie**):<br>
<ul>
    <li>Welke invoerelementen?</li>
        <ul> <li>Bewegingsdetector B (beweging: B  = 1)</li>
             <li>Lichtsensor S (donker: S = 0)</li>
             <li>Schakelaar K (ingedrukt: K = 1)</li>
        </ul>
    <li>Welke uitvoerelementen?</li>
        <ul>
            <li>Lamp L (brandt: L = 1)</li>
        </ul>
    <li>Het gevraagde weergeven d.m.v. een waarheidstabel. </li>
    <li>Een algoritme opstellen dat de verlichting aanstuurt.</li>
</ul>
</decomposition>
<patternRecognition>
**patroonherkenning**:<br>
* Soortgelijke problemen kennen een vaste manier van aanpak: het opstellen van een waarheidstabel en een algoritme. 
* Opzoek gaan naar patronen in de waarheidstabel, bv.<br>
![Waarheidstabel](waarheidstabelterraslamp1.png)  <br>
Bekijk in welke gevallen de lamp brandt (dat is aangegeven in het lichtgroen).<br>
Als K = 1 (donkergroen) dan zal de lamp branden (L = 1), ongeacht de waarden van B en S.<br>
Voor K = 0 is er nog maar één geval waarbij de lamp ook brandt, nl. als S = 0 én B = 1 (oranje). <br>
</patternRecognition>
<abstraction>
Het gevraagde wordt **abstract** weergegeven d.m.v. een waarheidstabel. De inputs staan in de eerste drie kolommen, de output in de laatste kolom.<br>
![Waarheidstabel](waarheidstabelterraslamp.png)  <br>
</abstraction>
<algorithms>
De oplossing van het probleem houdt de sturing van de verlichtingsinstallatie in a.d.h.v. een **algoritme** (hier verschillende oplossingen in de vorm van pseudocode of een flowchart).<br>
![Flowchart](flowchart.png)<br>
![Flowchart](flowchart2terraslamp.png)<br><br>
![Pseudocode](pseudocode1terraslamp.png)<br>
![Pseudocode](pseudocodewijterraslamp.png)
</algorithms>
<implementation>
Deze activiteit kan zonder computer gebeuren.
</implementation>


