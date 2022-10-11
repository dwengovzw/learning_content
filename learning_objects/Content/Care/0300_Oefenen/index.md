---
hruid: AIZ_Oefenen-v1
version: 3
language: nl
title: "Oefennotebooks"
description: "Oefennotebooks"
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

# Oefennotebooks
In het project 'AI in de Zorg' beschik je over enkels datasets met 'echte' data. 

Je kan dus aan de slag gaan met een oefeningenreeks waarbij er een beroep gedaan wordt op deze ‘echte’ data. Deze gegevens zijn opgeslagen in databestanden die vaak aanzienlijk zijn; er wordt gewerkt met csv-bestanden. Hierbij staat csv voor _comma separated values_.

Zo'n csv-bestand is eigenlijk een grote tabel waarin elke kolom bv. de waarden van een specifieke gezondheidsparameter bevat van een groot aantal patiënten. Eén bepaalde kolom bevat een ’label’, de klasse waartoe de patiënt behoort, bv. ‘komt terecht op de intensieve zorg’.

-------

De notebook ‘Hartaandoening’ bevat zo'n oefening. 

Hart- en vaatziekten vormen een belangrijke doodsoorzaak. Hartfalen bv. is een veelvoorkomende aandoening. De dataset heart.csv bevat waarden voor 11 parameters die gebruikt kunnen worden om een mogelijke hartziekte te voorspellen. Een hoge bloeddruk, diabetes, een verhoogde cholesterol zijn bv. gekende factoren die
het risico op een hartaandoening verhogen. Deze dataset is een combinatie van 5 datasets uit de VS en Europa en bevat waarden van 918 personen.

Je zal de tabel met de data inlezen en voorverwerken met functionaliteiten van de Python-modules pandas en NumPy. Je past dus toe wat je leerde in het onderdeel 'Dataframe' van dit leerpad. Eens je de gewenste parameters en het label hebt bekomen in een NumPy-array, verloopt alles op dezelfde manier als in de voorbeeldnotebook. Uiteindelijk wordt er een beslissingsboom gegenereerd op basis van de gegeven, grote dataset.

[![](embed/Knop.png "Knop")](https://kiks.ilabt.imec.be/jupyterhub/?id=3020 "Notebooks Sentimentanalyse")

-----

Gelijksoortige oefeningen kan je maken met de datasets titanic.csv, kyphosis.csv, heartca.csv, borstkanker.csv, en grieperig.csv. 
