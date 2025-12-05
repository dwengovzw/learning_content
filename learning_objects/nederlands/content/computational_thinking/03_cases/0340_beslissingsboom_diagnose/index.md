---
hruid: ct03_40
version: 3
language: nl
title: "Beslissingsboom medische diagnose (2,3)"
description: "Beslissingsboom"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
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
# Beslissingsboom voor medische diagnose

*In het project 'AI in de Zorg' gaan leerlingen samen met de leerkracht op zoek naar een middel om zorgverleners te helpen bij het stellen van een diagnose of het bepalen van een behandeling. Ze kunnen daarbij steunen op patiëntendata gegeven in een csv-bestand. Deze data zijn gelabeld en bevatten bijvoorbeeld patiëntenkenmerken, symptomen, en een aandoening.*  

**Uitdaging: Stel gelabelde data uit de zorgsector voor op een manier die geschikt is om er beslissingen mee te nemen betreffende een diagnose of een behandeling.**

**Doelgroep**: 2de graad - finaliteit doorstroom; 3de graad - dubbele finaliteit

**Vak:** 
* Wiskunde
* STEM 

**Voorkennis:**
* De leerlingen kunnen reële getallen ordenen.
* De leerlingen kennen tweedegraadsfuncties.
* De leerlingen kregen voorbeelden van beslissingsbomen te zien.

Een mogelijk verloop van de casestudy gaat als volgt:<br><br>

*Fase 1: kennismaking met beslissingsbomen en hun structuur*<br>
<ol>
    <li>Je geeft voobeelden van reallife beslissingsbomen of leerlingen zoeken er zelf op.
    <li>Patroonherkenning: de leerlingen herkennen de structuur uit de verschillende voorbeelden. Het is een gerichte graaf met bogen en knopen.
    <li>De leerlingen zien in dat je een beslissingsboom kan genereren op basis van een speidingsparameter en ja-neevragen.
    <li>De leerlingen vullen het schema met de basisconcepten in.</li>
</ol>

*Fase 2: wiskunde*<br>
<ol>
    <li>De leerlingen maken een taak over de spreidingsparameter.
    <li>De leerlingen maken een keuze voor de spreidingsparameter op basis van enkele criteria. Welke weerspiegelt het best de werkelijkheid? Welke is haalbaar rekening houdend met je voorkennis?
    <li>De leerlingen stellen een formule op voor de gini-index.
    <li>Oefeningen tonen dat je met logische uitdrukkingen (ongelijkheden) ja-neevragen kan representeren.</li>
</ol>

*Fase 3: algoritme*<br>
<ol>
    <li>De leerlingen schrijven het algoritme neer (in woorden).
    <li>De leerlingen testen het algoritme (manueel of plugged, beide kunnen) uit op een kleine dataset.</li>
</ol>

*Fase 4: Python*<br>
<ol>
    <li>De leerlingen voeren het algoritme in Python uit op een reallife dataset. Ze gebruiken een bestaande Python-module om hiervoor een programma te schrijven.
    <li>De leerlingen moeten de dataset voorverwerken (de data opkuisen en numeriek maken indien nodig).
    <li>De leerlingen vullen het schema met de basisconcepten verder in.</li>
</ol>
 
![ct-schema](@learning-object/m_ct03_40/nl/3)

Voor de uitwerking van dit project, zie het project 'AI in de Zorg'.
