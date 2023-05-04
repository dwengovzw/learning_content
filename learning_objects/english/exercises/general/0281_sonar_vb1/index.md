---
hruid: g_sonar_vb1
version: 3
language: en
title: "Voorbeeld Sonar-sensor 1"
description: "Voorbeeld Sonar-sensor 1"
keywords: ["oefeningen", "sonar-sensor"]
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
estimated_time: 5
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---
## Sonar-sensor

OPGAVE 1

Voor je de sonar-sensor gaat gebruiken, moet je deze eerst testen. Schrijf een programma om de sonar-sensor uit te lezen.

***

Om de sonar-sensor uit te lezen (welke afstand de sonar-sensor meet), maak je gebruik van het lcd-scherm. Het blok van de sonar-sensor stelt gewoon een getal voor dat je kan laten verschijnen op het scherm. 

Hiervoor heb je de volgende blokken nodig:

![](embed/block_sonar.png "blok sonar-sensor")
![](embed/block_text.png "blok tekst")

Wanneer je deze blokken combineert, bekom je dit:

![](embed/combo_text_sonar.png "tekst + sonar-sensor")

Het getal van de sonar-sensor wordt door ![](embed/block_text.png "blok tekst") omgezet in gegevens die je op het lcd-scherm kunt doen verschijnen.

Met dit nieuwe tekst-blok kan je nu het bestaande *'tekst'-blok* van het lcd-scherm vervangen, waardoor je het onderstaande programma bekomt:

![blockly](@learning-object/sonar_m1a/nl/3)

***

Bij meer ingewikkelde programma's zal je echter snel merken dat het heel druk is om telkens het *'sonar-sensor'-blok* te gebruiken omdat dit vrij groot is. Om dit te verhelpen en het programma overzichtelijk te houden, zal je gebruik maken van **variabelen**.

Hiervoor heb je de volgende blokken nodig:

![](embed/block_variable.png "blok variabele")
![](embed/block_item.png "blok item")

Om de leesbaarheid van je programma te verbeteren, hernoem je de variabele 'item' best eerst naar iets beters. Omdat je hier afstand aan het meten bent, neem je bijvoorbeeld 'afstand'. Gebruik hiervoor het hulpmenu.

![](embed/rename_variable.png "hernoemen variabele")

Eens je dit gedaan hebt, combineer je het *'sonar-sensor'-blok* met ![](embed/block_variable.png):

![](embed/combo_variable_sonar.png "afstand")

Eens je een variabele hebt benoemd in een programma, kan je deze altijd oproepen m.b.v. ![](embed/block_item.png "blok item"). *Let er wel op dat je de juiste variabele opnoemt!*

Het eindresultaat voor het uitlezen van een sonar-sensor ziet er dan als volgt uit:

![blockly](@learning-object/sonar_m1b/nl/3)

<div class="alert alert-box alert-success">
Op het lcd-scherm verschijnen nu de waarden die de sonar-sensor teruggeeft. Indien dit niet werkt, moet je troubleshooten om het probleem te vinden.
<ul><li>Is het het juiste programma? (Check de code)</li></ul>
<ul><li>Is de sensor correct aangesloten? (Check de bedrading)</li></ul>
<ul><li>Werkt de sensor?</li></ul>
</div>