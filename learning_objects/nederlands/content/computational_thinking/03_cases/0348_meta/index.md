---
hruid: m_ct03_48
version: 3
language: nl
title: "Sentimentanalyse"
description: "Sentimentanalyse"
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
**Probleemstelling**<br>
Ontwikkel een AI-systeem dat reviews op sociale media classificeert volgens sentiment (positief, neutraal, negatief).  
</div>
</context>
<decomposition>
**Decompositie**<br>
<ul>
    <li>Verkennen van het probleem:
        <ul>
            <li>Wat is het sentiment van een tekst?
            <li>Welke technieken zijn er om het sentiment van een tekst te bepalen en wat zijn de voor- en nadelen van deze technieken?
            <li>Welke techniek is voor jou het meest geschikt? (Keuze maken tussen regelgebaseerd of datagebaseerd AI-systeem; hier kiezen we voor regelgebaseerd.)
        </ul>
    <li>Wat heb je nodig?
        <ul>
            <li>Sentimentwoordenboek in het Nederlands (lexicon).</li>
        </ul>
    <li>Hoe pak je het probleem concreet aan? Subtaken:
        <ul>
            <li>leren werken met het lexicon (Hoe vind je een woord en de sentimentscore van dat woord erin terug?);
            <li>een representatie kiezen voor de review zodat de computer ermee kan werken, en hiervoor een geschikt datatype kiezen (review voorverwerken: tokeniseren, hoofdletters en leestekens verwijderen, woorden representeren via hun woordenboekvorm en woordsoort (lemmatiseren en part-of-speech));
            <li>sentimentscore van elk woord bepalen door matching tussen de woorden en het sentimentwoordenboek;
            <li>sentiment van de review bepalen (Hoe bepaal je dit vertrekkend van de sentimentscores van de woorden?).</li>
        </ul>
    </li>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
<ul>
    <li>Het gebruik van een lexicon (woordenboek specifiek voor de taak) en tokeniseren, lemmatiseren en part-of-speech zijn technieken die veel worden toegepast in het domein van de taaltechnologie, bijvoorbeeld ook voor cyberpestdetectie, auteursherkenning, automatisch vertalen en tekst genereren.
    <li>Regelgebaseerde cyberpestdetectie en sentimentanalyse gebeuren via een gelijksoortig algoritme. Alleen het lexicon verschilt.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
<ul>
    <li>Bij een regelgebaseerd systeem wordt het sentiment van een woord aan een computer voorgesteld door een getal tussen -2 en 2.
    <li>Details van de reviews worden weggelaten, bijvoorbeeld het negeren van hoofdletters en leestekens. Tokeniseren reduceert de tekst tot de woorden die deze bevat. Lemmatiseren en part-of-speech herleiden deze woorden tot hun woordenboekvorm en woordsoort.
    <li>De voorverwerking laat toe om een datastructuur te gebruiken die geschikt is om efficiënt te zoeken.</li>
</ul>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
Een **algoritme** om het sentiment van een review te bepalen:<br>
<ul>
    <li>Maak een lijst van de woordenboekvormen van de woorden die in de review voorkomen, telkens met de woordsoort waarmee ze voorkomen. Negeer leestekens en hoofdletters.
    <li>Matching tussen de woorden in deze lijst en het sentimentwoordenboek. Zoek elk woord op in het lexicon. Hou daarbij rekening met de woordsoort. Sla de sentimentscore van elk woord op in een lijst.
    <li>Tel de sentimentscores in de lijst op. De som is de sentimentscore van de review.
    <li>Bepaal het sentiment van de review met een wiskundige uitdrukking (sentimentscore groter dan 0, gelijk aan 0, kleiner dan 0)</li>
</ul>
</algorithms>
<implementation>
**Programma**<br>
Deze activiteit kan zonder computer gebeuren. Je kan samen met de leerlingen een algoritme voor een regelgebaseerd systeem opstellen en het vervolgens unplugged uittesten. Wil je wel programmeren? Dat kan via de Python-notebooks van Dwengo.
</implementation>

