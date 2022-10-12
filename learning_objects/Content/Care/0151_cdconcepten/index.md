---
hruid: aiz_cdconcepten-v1
version: 3
language: nl
title: "Basisconcepten"
description: "Basisconcepten"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
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
teacher_exclusive: false
---

# De basisconcepten van computationeel denken 

## Definities van de basisconcepten 

Computationeel denken steunt op vier basisconcepten: decompositie, abstractie, patroonherkenning en algoritmisch denken. Wat houden deze begrippen in? 

<ul><li><strong>Decompositie</strong></br>- Een probleem doordacht opsplitsen in goedgekozen deelproblemen, zodat elk deel afzonderlijk kan worden aangepakt, en een oplossing van het probleem gemakkelijker bekomen wordt.</li></ul> 
<ul><li><strong>Patroonherkenning</strong></br>- Achterhalen dat bepaalde aspecten van een probleem onderling gelijkenissen vertonen, waardoor het vereenvoudigd kan worden.<br>- Herkennen dat een probleem gelijkenissen vertoont met een eerder opgelost probleem.</li></ul> 
<ul><li><strong>Abstractie</strong></br>- Negeren van informatie die niet nodig is om een probleem op te lossen.<br>- Bepaalde details verbergen om in grote lijnen over een probleem te kunnen nadenken</li></ul> 

Bij het aanpakken van complexe problemen is er nood aan abstractie, omdat het redeneren vlotter verloopt zonder de ballast van irrelevante details. 

<ul><li><strong>Algoritmisch denken</strong></br>- Expliciteren van een reeks eenduidige instructies die stapsgewijs moeten worden uitgevoerd.<br>- Inzien dat deze reeks instructies en de volgorde ervan essentieel zijn om het gewenste resultaat op te leveren.</li></ul> 

## Centraal probleem vam 'AI in de Zorg 

*Stel gelabelde data uit de zorgsector op een manier voor die geschikt is om er beslissingen mee te nemen betreffende een diagnose of een behandeling."* 

Eenvoudige beslissingsbomen kunnen manueel worden opgemaakt, maar als er veel factoren zijn waarmee er rekening moet gehouden worden, dan vergt dat heel wat tijd. Het is dan handig om een computer in te zetten. In hoofdstuk 6 wordt concreet bekeken op welke manier de computer hiervoor kan worden gebruikt. Hoofdstuk 8 toont hoe je door de gevonden methode te implementeren in de computer een beslissingsboom automatisch genereert om tot een oplossing te komen voor het centraal probleem. 

> Om een beslissingsboom te bekomen die bruikbaar is voor een zorgverlener, zal je voldoende data moeten gebruiken om de beslissingsboom op te baseren. Dat zal dus met een computer moeten gebeuren. 

Hieronder wordt uit de doeken gedaan hoe de vier basisconcepten van computationeel denken daarbij aan bod kwamen. 

Je begint met **patroonherkenning** en **abstractie**: 

<ul><li>In de voorbeelden van hoofdstuk 4 zie je dat de data doorgaans voorgesteld worden met een gerichte, gewortelde graaf, meestal binair.</li></ul> 
<ul><li>Hoe de data worden voorgesteld vertoont een patroon. De data worden telkens op dezelfde manier geabstraheerd, nl. door een (binaire) beslissinsboom te gebruiken.<br>Ook de opbouw van zo'n binaire beslissingsboom vertoont bepaalde patronen.</li></ul> 
<ul><li>Uit de voorbeelden van hoofdstuk 4 leid je af dat een beslissingsboom vertrekt uit een wortel en een ja-neevraag die een scheiding van de data oplevert in twee verzamelingen die zo weinig mogelijk spreiding over de categorieën vertonen. A.d.h.v. een iteratief proces worden de knopen en de volgende ja-neevragen bepaald. De bladeren van de beslissingsboom geven de mogelijke beslissingen.</li></ul> 

**Decompositie** van dit probleem (en decompositie van de deelproblemen): 

<ul><li>In de voorbeelden van hoofdstuk 4 een **patroon** zoeken in hoe de data daar worden voorgesteld.</li></ul> 
<ul><li>Uit welke elementen wordt een beslissingsboom opgebouwd?<br>- Een beslissingsboom is een model voor de gezochte oplossing. Het is een <strong>abstracte</strong> voorstelling, de vorm is een graaf.<br>- Uit welke elementen is zo'n graaf opgebouwd?</li></ul> 
<ul><li>Hoe gaat zo'n beslissingsboom in zijn werk?<br>- Een beslissingsboom vertrekt uit een wortel en een ja-neevraag die een scheiding van de data oplevert in twee verzamelingen die zo weinig mogelijk spreiding over de categorieën vertonen. A.d.h.v. een iteratief proces worden de knopen en de volgende ja-neevragen bepaald. De bladeren van de beslissingsboom geven de mogelijke beslissingen.</li></ul> 
<ul><li>Om door een computer een binaire beslissingsboom te laten opmaken, is er een computerprogramma nodig. Je zal dus moeten werken met concepten die de computer begrijpt, zoals getallen en logische uitdrukkingen. Het computerprogramma wordt geschreven op basis van een algoritme.</li></ul> 
<ul><li>Welke berekeningen leiden tot de juiste splitsing?<br>- Bij elke splitsing wordt er gestreefd naar zo weinig mogelijk spreiding over de categorieën. Om de computer de mate van spreiding te laten herkennen, zal je de mate van spreiding De gini-index wordt gebruikt als maat voor de spreiding. weergeven met een getal. Hoe geef je dat weer door een getal?</li></ul> 

> De gini-index wordt gebruikt als maar voor de spreiding. 

<ul><li>Met welk <strong>algoritme</strong> kan een binaire beslissingsboom worden gecontrueerd?<br>- Het algoritme zal voor een binaire beslissingsboom de wortel moeten bepalen, de juiste knopen moeten kiezen en de geschikte ja-neevragen moeten vastleggen.<br>- Dat gebeurt via een iteratief proces. Bij elke splitsing is er hetzelfde patroon dat zich herhaalt.<br>- Hoe maakt een computer ja-neevragen? Dit zal gebeuren a.d.h.v. wiskundige uitdrukking waarvan wordt nagegaan of ze waar of niet waar zijn.</li></ul> 

> Deze wiskundige uitdrukkingen zullen worden opgebouwd a.d.h.v. de vergelijkingsoperatoren > en <. 

<ul><li>De implementatie van het algoritme in de computer.</li></ul> 
<ul><li>In welk formaat worden de data aangeleverd aan de computer?<br>- Voldoen de data aan dit formaat?<br>- Indien niet, hoe kan je de data dan voorverwerken?</li></ul> 

> Je zal gebruikmaken van een csv-bestand; csv staat voor 'comma separated values'. 

Je merkt dat de basisconcepten met elkaar verweven zijn.<br>
Figuur 5.1 vat samen hoe de vier basisconcepten van computationeel denken je op weg zetten om het centraal probleem over het construeren van beslissingsbomen aan te pakken. 

> Het vak ‘algoritme’ is nog niet ingevuld omdat het algoritme nog moet worden opgesteld in hoofdstuk 6. Figuur 6.31 geeft het aangevulde schema. 

![](embed/placeholder.png "Fig 5.1")
<figure>
    <figcaption align = "center"><b>Basisconcepten computationeel denken toegepast op het probleem van het opstellen van een binaire beslissingsboom.</b></figcaption>
</figure>