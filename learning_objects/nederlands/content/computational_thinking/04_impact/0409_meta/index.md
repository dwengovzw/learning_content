---
hruid: m_ct04_09
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
Een fietspad constant goed verlichten kost veel energie. Door gebruik te maken van slimme verlichting is het mogelijk om enkel fel licht te gebruiken indien iemand in de buurt van de straatverlichting zijn.   
</div>
</context>
<decomposition>
**Decompositie**<br>
Het reguleren van fietspadverlichting kan worden opgesplitst in verschillende componenten, zoals het detecteren van beweging, het aanpassen van de helderheid van de verlichting en het beheren van energieverbruik. Hiervoor zullen onderdelen zoals een straatlamp en een bewegingssensor nodig zijn.
</decomposition>
<patternRecognition>
**Patroonherkenning**<br>
Het detecteren van beweging is een belangrijk deel van slimme fietspadverlichting, maar ook in een andere context kan deze detectie gebruikt worden. Denk maar aan verkeersdetectie om piekuren te weten te komen, of een beveiligingsalarm die een lamp doet branden indien er beweging is op een verdacht tijdstip. 
</patternRecognition>
<abstraction>
**Abstractie**<br>
We willen dat de straatlapen branden zodra iemand deze daadwerkelijk nodig heeft. Of de gebruiker een fiets, step of motor heeft, maakt ons in pricipe weinig uit. Daarom is het enkel noodzakelijk dat we de essentiële informatie over bewegingsdetectie behouden. Zodra de bewegingssenor iets opmerkt, kunnen we extra licht voorzien, zonder rekening te houden met irrelevante details over bijvoorbeeld specifieke individuen.<br>
</abstraction>
<algorithms>
**Algoritmisch denken**<br>
Voor dit voorbeeld kan een algoritme worden gebruikt om te bepalen wanneer de verlichting helderder moet worden op basis van de gedetecteerde beweging. Dit kan bijvoorbeeld een algoritme zijn dat de helderheid verhoogt wanneer beweging wordt gedetecteerd en deze na een bepaalde tijd weer verlaagt als er geen nieuwe beweging wordt gedetecteerd.
</algorithms>
<implementation>
... 
</implementation>

