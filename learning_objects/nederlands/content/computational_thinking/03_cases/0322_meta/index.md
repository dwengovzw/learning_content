---
hruid: m_ct03_22
version: 3
language: nl
title: "Locked-in"
description: "Locked-in"
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
Bauby wordt volledig verlamd wakker in het ziekenhuis. Hij kan alleen nog knipperen met één oog. Hij vindt toch een manier om te communiceren en slaagt er zo zelfs in om een boek te schrijven. Analyseer vanuit de principes van computationeel denken hoe Bauby nog zou kunnen communiceren en een boek schrijven. Ga in op zijn methode en manieren om deze te verbeteren.
</context>
<decomposition>
**Decompositie**<br>
<ul>
    <li>Wat is er nog mogelijk? 
        <ul>
            <li>Bauby kan knipperen met één oog. 
	        <li>Bauby kan lezen.
	        <li>Helper kan praten, lezen en schrijven. 
        </ul>
    </li>
    <li>Hoe zou Bauby kunnen communiceren?
        <ul>
            <li>Woorden bestaan uit letters. Het knipperen met een oog zal moeten omgezet worden naar letters. Bv. één keer knipperen betekent ‘a’, 2 keer knipperen ‘b’ ... De helper moet alleen maar tellen hoeveel keer er wordt geknipperd en de bijbehorende letter opschrijven.</li>
        </ul>
    </li>	
    <li>Hoe zou Bauby een boek kunnen schrijven?
        <ul>
            <li>Op dezelfde manier, maar ook spaties, leestekens, cijfers, witruimtes ... toevoegen aan het alfabet.</li>
        </ul>
    </li>
    <li>Wat te doen als er per ongeluk een fout gemaakt wordt? Wat doen om een gok van de helper goed of af te keuren?
        <ul>
            <li>Er moet worden afgesproken hoe te communiceren in die gevallen.</li>
        </ul>
    </li>
    <li>Hoe kan het sneller? 
        <ul>
            <li>Moment van knipperen gebruiken i.p.v. het aantal keer.</li>
            <li>Eerst de veelvoorkomende letters vragen door de volgorde van de letters in het alfabet aan te passen.</li>
            <li>Binair zoeken garandeert dat elke letter wordt gevonden na opsomming van hoogstens 5 letters!</li>
            <li>Helper gokt een woord als hij vrij zeker is.</li>
            <li>Automatiseren met technologie.</li>
        </ul>
    </li>
</ul>
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
<ul>
    <li>Soms kan je halverwege een woord al raden wat het is. Als je ‘a-n-t-i-l’ hebt, zou het woord ‘antiloop’ een goede gok zijn. Dat is hetzelfde als de ‘woordsuggestie’ op een smartphone. Als de helper vrij zeker is van een gok, kan gokken tijd besparen.
    <li>Sommige letters komen meer voor dan andere. Door de eeuwen heen is frequentieanalyse gebruikt om geheime codes te kraken. Het kraken van codes en het raden van letters zijn vergelijkbare problemen. Bauby liet daarom de helper de letters voorlezen in volgorde van dalende frequentie (in de Franse taal).
    <li>Binair zoeken is een geschikte verdeel-en-heersstrategie om te zoeken tussen dingen met een bepaalde volgorde. Je stelt dan halveringsvragen (denk aan het spel 'Wie is het?').</li>
</ul>
</patternRecognition>
<abstraction>
**Abstractie**<br>
<ul>
    <li>Het aantal keer knipperen, een getal dus, is een encodering van een letter, leesteken ... (een andere voorstelling, de informatie wordt vervangen door iets anders).
    <li>Dus om te weten wat het snelste algoritme is, moet je de hoeveelheid letters bepalen die de helper moet overlopen. De tijdsduur zelf wordt genegeerd (abstractie). Je kan dit inschatten door het gemiddelde aantal opgesomde letters per letter in te schatten.</li>
</ul>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
<ul>
    <li>Het algoritme dat Bauby gebruikte: de helper las telkens het alfabet voor in de volgorde: 'e, s, a, r ... w'. Als de letter waar Bauby aan dacht, werd uitgesproken, knipperde hij met zijn oog. De helper schreef die letter op en begon dan opnieuw, letter voor letter.
    <li>Manieren om het proces te versnellen, bijvoorbeeld binair zoeken.</li>
</ul>
</algorithms>
<implementation>
**Programma**<br>
De mens komt eerst! We zouden binair zoeken kunnen toepassen of de computer gebruiken om het proces te versnellen. Maar houden we dan wel rekening met de juiste aspecten van het probleem?
<ul>
    <li>Wat als knipperen een grote inspanning was voor Bauby? Zijn oplossing hield in dat hij maar één keer per letter knipperde. Het verdeel-en-heersalgoritme zou vereisen dat hij vijf keer knippert. Zijn oplossing is gemakkelijk te begrijpen voor iedereen. De onze is complexer, en wie zal ze uitleggen aan bezoekers?
    <li>Stel dat we een systeem ontwerpen met de computer. Doet automatiseren niet meer kwaad dan goed? Er zouden geen helpers meer zijn die zorgen voor menselijke warmte.</li>
</ul>
</implementation>

