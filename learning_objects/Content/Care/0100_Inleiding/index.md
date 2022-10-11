---
hruid: AIZ_Inleiding-v1
version: 3
language: nl
title: "Inleiding"
description: "Inleiding"
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

# Inleiding
Artificiële intelligentie vindt steeds meer haar weg naar de zorgsector. Logistieke diensten in ziekenhuizen kunnen voordeel halen uit artificiele
intelligentie, elektronische patiëntendossiers kunnen ermee beter benut worden, dokters wenden artificieel intelligente systemen aan
voor intakegesprekken of ter ondersteuning bij het stellen van een diagnose.

Het volgende voorbeeld illustreert hoe een artificieel intelligent systeem een arts kan helpen bij het bepalen van een therapie.
Kyphosis of ‘bolle rug’ is een afwijking aan de ruggengraat die zich manifesteert als een abnormale ronding van de bovenrug, zoals te zien op Figuur 1.<br>
Kyphosis kan op elke leeftijd voorkomen, maar uit zich vaak bij jongvolwassenen. De patiënt kan ervoor kiezen om te opereren, maar vaak is de aandoening nog steeds aanwezig na de operatie. De arts schat op voorhand in of een operatie aangewezen is of niet, en kan daarbij geholpen worden door een AI-systeem, bijvoorbeeld een
beslissingsboom.<br>
De beslissingsboom in Figuur 2 ‘voorspelt’ of een patiënt zal geholpen zijn door een operatie of niet. Deze beslissing gebeurt op
basis van verschillende patiëntenkenmerken, namelijk de leeftijd van de patiënt in maanden, het aantal wervels betrokken bij de operatie
en het nummer van de eerste wervel waarop geopereerd wordt.<br>
Deze patiëntenkenmerken worden voor een specifieke patiënt ingegeven in het AI-systeem en het systeem geeft aan aan de arts of een operatie voor die patiënt aangewezen is.

Zo’n beslissingsboom vormt een regelgebaseerd AI-systeem en is zeer transparant: het is duidelijk hoe het systeem tot zijn beslissing is
gekomen. Om de beslissingsboom te construeren werd een lerend AI-systeem aangewend: de beslissingsboom is gebaseerd op gelabelde
data, relevante patiëntenkenmerken gekoppeld aan het feit of de operatie resultaat opleverde of niet. In hoofdstuk 1 van de handleiding kan je meer
lezen over wat begrippen zoals regelgebaseerd, lerend en gelabeld inhouden.

In hoofdstuk 4 krijg je nog heel wat voorbeelden van beslissingsbomen uit de zorgsector te zien.

------

**Uitdaging**<br>
Stel gelabelde data uit de zorgsector op een manier voor die geschikt is om er beslissingen mee te nemen betreffende een diagnose of een behandeling.
Laat een computer jou daarbij helpen.
