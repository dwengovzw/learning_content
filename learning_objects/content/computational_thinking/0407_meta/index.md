---
hruid: m_ct_cases7
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
Stel gelabelde data uit de zorgsector voor op een manier die geschikt is om er beslissingen mee te nemen betreffende een diagnose of een behandeling.
</context>
<decomposition>
Subtaken (**decompositie**):
1. In de voorbeelden op zoek gaan naar een patroon (een gerichte gewortelde graaf, een binaire beslissingsboom).
2. Uit welke elementen is een beslissingsboom opgebouwd?
3. Wat is de werking van een beslissingsboom?
4. Hoe de mate van spreiding weergeven door een getal.
5. Welke berekeningen leiden tot de juiste splitsing?
6. Hoe geef je ja-neevragen vorm a.d.h.v. een logische (wiskundige) uitdrukkingen? 
7. Ontwerpen van een algoritme om een binaire beslissingsboom te construeren.
8. De implementatie van het algoritme in de computer.
9. De data voorverwerken tot het gewenste formaat.
</decomposition>
<patternRecognition>
De bestaande voorbeelden tonen dat zulke data vaak worden voorgesteld door een gerichte gewortelde graaf, meetal binair. M.a.w. een binaire beslissingsboom is geschikt om de data te representeren. (**patroonherkenning**)<br><br>
Een binaire beslissingsboom vertrekt uit een wortel en een ja-neevraag die een scheiding van de data oplevert in twee verzamelingen die zo weinig mogelijk spreiding over de categorieën vertonen. Dat gaat op een analoge manier verder met volgende ja-neevragen. De boom wordt zo opgebouwd met takken en knopen. Tot slot geven de bladeren van de beslissingsboom de mogelijke beslissingen.(**patroonherkenning**)
</patternRecognition>
<abstraction>
De beslissingsboom is een abstracte voorstelling van de oplossing in de vorm van een graaf. Het is een model voor de oplossing. (**abstractie**)<br>
Deze voorstelling is bovendien transparant.
</abstraction>
<algorithms>
**Algoritme** om binaire beslissingsboom op te stellen.<br>
1. Bekijk welke wortel de beste splitsing oplevert. Maak takken voor de mogelijke uitkomsten van de ja-neevraag.
2. Bekijk voor elke tak welke knoop het meest geschikt is voor de volgende splitsing. Maak takken voor de mogelijke uitkomsten van de ja-neevragen.  
3. Herhaal de vorige stap telkens opnieuw voor de nieuw aangemaakte takken.
4. Stop met de herhaling als de bekomen verzamelingen homogeen zijn, dus enkel elementen uit een en dezelfde klasse bevatten.
    
*Dit is een iteratief proces: om de wortel en de knopen te bepalen wordt telkens dezelfde techniek toegepast.*
</algorithms>
<implementation>
Voor het programmeren verwijzen we naar de notebooks van het project AI in de Zorg.
</implementation>

