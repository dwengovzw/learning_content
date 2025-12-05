---
hruid: m_ct03_40
version: 3
language: nl
title: "Cases"
description: "Cases"
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
Stel gelabelde data uit de zorgsector voor door een beslissingsboom die kan helpen bij het stellen van een diagnose of het bepalen van een behandeling.
</context>
<decomposition>
**Decompositie**<br>
<ul>
    <li>In de voorbeelden op zoek gaan naar een patroon (een gerichte gewortelde graaf, een binaire beslissingsboom).</li>
    <li>Uit welke elementen is een beslissingsboom opgebouwd?</li>
    <li>Wat is de werking van een beslissingsboom?</li>
    <li>Hoe stel je een beslissingsboom op?
    <ul>
        <li>Hoe kan je de mate van spreiding weergeven door een getal?</li>
        <li>Welke berekeningen leiden tot de juiste splitsing?</li>
        <li>Hoe geef je een ja-neevraag vorm met een logische (wiskundige) uitdrukking?</li>
        <li>Ontwerpen van een algoritme om een binaire beslissingsboom te construeren.</li>
    </ul>
    <li>De implementatie van het algoritme in de computer.</li>
    <li>De data voorverwerken tot het gewenste formaat.</li>
</ul>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
<ul>
    <li>De reallife voorbeelden tonen dat zulke data vaak worden voorgesteld door een gerichte, gewortelde graaf (meestal binair). M.a.w. een binaire beslissingsboom is geschikt om de data te representeren.</li>
    <li>Een binaire beslissingsboom vertrekt uit een wortel en een ja-neevraag. Deze vraag levert een scheiding van de data op in twee verzamelingen die zo weinig mogelijk spreiding over de categorieën vertonen. Dit gaat op een analoge manier verder met telkens nieuwe ja-neevragen. De boom wordt zo opgebouwd met takken en knopen. Tot slot geven de bladeren van de beslissingsboom de mogelijke beslissingen.</li>
    <li>Herkennen dat het opsplitsen van data op basis van de gini-index telkens volgens hetzelfde patroon verloopt.</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
<ul>
    <li>In de beslissingsboom wordt geen rekening gehouden met irrelevante patiëntendata zoals naam, woonplaats...</li>
    <li>De beslissingsboom is een abstracte voorstelling van de oplossing in de vorm van een graaf. Het is een model voor de oplossing.</li>
    <li>Deze voorstelling is bovendien transparant.</li>
    <li>Abstractie komt ook voor:
    <ul>
        <li>als je de mate van spreiding weergeeft door een getal; en</li>
        <li>als je een ja-neevraag stelt met een wiskundige uitdrukking.</li>
    </ul>
</ul>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
Algoritme om binaire beslissingsboom op te stellen.<br>
<ol>
    <li>Bekijk welke wortel de beste splitsing oplevert. Maak takken voor de mogelijke uitkomsten van de ja-neevraag.</li>
    <li>Bekijk voor elke tak welke ja-neevraag het meest geschikt is voor de volgende splitsing. Maak takken voor de mogelijke uitkomsten van de ja-neevragen.</li>
    <li>Herhaal telkens de vorige stap voor de nieuw aangemaakte takken.</li>
    <li>Stop met de herhaling als de bekomen verzamelingen homogeen zijn, dus alleen elementen uit een en dezelfde klasse bevatten.</li>
</ol>
    
*Dit is een iteratief proces: om de wortel en de knopen te bepalen wordt telkens dezelfde techniek toegepast.*
</algorithms>
<implementation>
**Programma**
Deze activiteit kan met of zonder computer gebeuren.<br>
Voor het programmeren verwijzen we naar de notebooks van het project AI in de Zorg.
</implementation>

