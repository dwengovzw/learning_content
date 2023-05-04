---
hruid: aiz_algoritmes
version: 3
language: nl
title: "Algoritmes"
description: "Algoritmes"
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
# Algoritmes
## Verdeel-en-heersalgoritme

Het algoritme dat je in hoofdstuk 6 zal gebruiken om een beslissingsboom te construeren voor een specifieke toepassing is een verdeel-en-heersalgoritme. Het idee van verdeel-en-heers is dat je om een probleem op te lossen, je het probleem omvormt naar een identiek probleem dat kleiner is. Dan pak je dat kleinere probleem op dezelfde manier aan door het ook om te vormen naar een een (bijna) identiek probleem dat nog kleiner is, Als je dit zo verder doet, wordt het probleem dat je effectief moet gaan oplossen zo klein dat de oplossing voor de hand ligt. 

> Door de eeuwen heen heeft men effectieve algoritmes weten op te stellen die een antwoord bieden op specifieke problemen, zoals sorteer- en zoekalgoritmes. Deze algoritmes vertonen bepaalde kenmerken, bv. verdeel-en-heers en gretig.<br>Via patroonherkenning kan men achterhalen of een bestaand algoritme geschikt is voor een nieuw op te lossen probleem.

Met een verdeel-en-heersalgoritme maak je een probleem eenvoudiger bij elke stap. 

*Voorbeeld*<br> 
Stel dat je een medische term wilt opzoeken in een woordenboek, bv. meningitis. In een woordenboek staan de woorden alfabetisch geordend. 

<ul><li>Je opent het woordenboek in de helft.</li></ul> 
<ul><li>Staan de woorden die beginnen met een 'm' in het eerste of tweede deel? Neem het juiste deel.</li></ul> 
<ul><li>Verdeel dat deel weer in twee.</li></ul> 
<ul><li>Staan de woorden die beginnen met een 'm' in het eerste of tweede deel? Neem opnieuw het juiste deel.</li></ul> 
<ul><li>Herhaal deze methode tot je bij de woorden met een 'm' aankomt.</li></ul> 

Er zijn ook wiskundige toepassingen. Het algoritme van Euclides is een verdeel-en-heersalgoritme om de grootste gemene deler van twee natuurlijke getallen te bepalen.<br> 
En er zijn ook praktische toepassingen. Om na het wassen dezelfde kousen weer bij elkaar te voegen, kan je ze eerst sorteren op kleur alvorens ze te matchen (Stock, 2017).

## Gulzig algoritme
Het algoritme dat je in hoofdstuk 6 zal gebruiken om een beslissingsboom te construeren heeft nog een bijzonder kenmerk. Het is een gulzig algoritme. Het zal bij elke stap voor het opbouwen van de beslissingsboom kiezen voor die splitsing die op dat moment zo optimaal mogelijk is, maar geen rekening houden met de stappen die erna nog komen. De gevoerde strategie is er een van ‘neem wat je nu kunt krijgen’ (Fack, 2007). Het algoritme is effectief, maar niet altijd het meest efficiënte. 

> Een gulzig algoritme wordt ook een gretig algoritme genoemd.