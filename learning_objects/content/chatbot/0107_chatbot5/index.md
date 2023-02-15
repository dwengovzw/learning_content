---
hruid: cb_chatbot5
version: 3
language: nl
title: "In de klas"
description: "In de klas"
keywords: ["voorbeeld", "voorbeeld2"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-digitale-media-en-toepassingen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-stem-onderzoek', 
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-wiskunde-modelleren-en-heuristiek'
]
teacher_exclusive: true
---

# In de klas

Op het world wide web zijn tal van tips te vinden voor het didactisch aanwenden van ChatGPT in de klas. Hier zal je geen lange lijst vinden met de herhaling van wat al her en der  te lezen valt.

## Om te brainstormen
Wat echter opvalt, is dat vaak wordt voorbijgegaan aan het eigenlijke karakter van ChatGPT: het is een chatbot. Je kan er dus mee converseren en in discussie gaan. Je kan ChatGPT gebruiken als brainstormpartner. Bijvoorbeeld, een leerling kan eerst nadenken over argumenten om een bepaalde stelling te staven en tegenargumenten om hem te weerleggen. Nadien kan ChatGPT gevraagd worden naar extra argumenten en tegenargumenten. Zo kan een leerling zich beter voorbereiden op een klasdiscussie. Bovendien zal de leerling zelf nog op zoek moeten gaan naar betrouwbare bronnen en de antwoorden van de chatbot met een (grote) korrel zout moeten nemen. ChatGPT zal niet nalaten te ‘hallucineren’, het verzinnen van antwoorden en bronnen.       
Het zich pas in tweede instantie tot ChatGPT wenden voorkomt dat de leerling al in een bepaalde richting wordt gestuurd.

> **Voorbereiden van een klasdiscussie**
> Kies een stelling uit van de kaartenset van het project ‘AI in de Zorg’. 
> Voorbeeld:<br>
![image](https://user-images.githubusercontent.com/48352335/218336427-bc8cfc21-bb17-4da7-9816-116f70d0a507.png)
> Enkele leerlingen formuleren elk voor zich of ze al dan niet akkoord gaan met de stelling en waarom. De leerlingen vragen erna (individueel) aan ChatGPT wat de voor- en nadelen zijn van het zich laten wassen door een robot. Elke leerling reflecteert over de aspecten die ChatGPT heeft aangehaald. De leerling kan nadenken over argumenten en voorbeelden om te beamen of te weerleggen wat ChatGPT aanhaalt. Nadien volgt een discussie binnen deze groep leerlingen waarbij ze elkaar proberen te overtuigen van hun eigen standpunt. Omdat ChatGPT hen reeds confronteerde met elementen waar ze misschien zelf niet aan hadden gedacht, zijn ze beter voorbereid op deze discussie.  

## Om bias te illustreren
ChatGPT is (voorlopig nog) geschikt om bias in AI-systemen te illustreren.  

OpenAI geeft dat zelf ook aan.
![chatGPT55](https://user-images.githubusercontent.com/48352335/219005103-09e6a3ec-53a8-4fe8-bb97-9ee80e474461.png)

> Opdracht voor de leerlingen: Stel vragen en geef opdrachten aan ChatGPT en probeer hem te betrappen op het uitvergroten van vooroordelen aanwezig in onze maatschappij. 

Op die manier breng je je leerlingen nog wat mediawijsheid en kennis over AI bij. 

Zelf betrapten we ChatGPT met deze prompts op gender bias. 

![biasingenieur](https://user-images.githubusercontent.com/48352335/219005225-79d07e30-3542-4837-89a4-8fa19774cf23.png)

![biaswiskundeleerkracht](https://user-images.githubusercontent.com/48352335/219005375-3449a07f-666b-4cd8-99a1-e05879791cfa.png)

Toegegeven dat dit cherry picking is, veel andere prompts leidden tot een neutraal antwoord.

![biasverpleegkundige](https://user-images.githubusercontent.com/48352335/219005530-5d95c4af-0107-476b-9704-a9673d7749c6.png)

## Voor een wiskundeopdracht

![chatGPT3b](https://user-images.githubusercontent.com/48352335/219005727-49c083e7-d9d4-4e70-88d8-f9116903fb82.png)

Dit klinkt veelbelovend. Taalmodel wordt wel aan elkaar geschreven, maar goed. ChatGPT zegt  dat het uitvoeren van complexe berekeningen tot zijn mogelijkheden behoort.

We schotelden ChatGPT op 14 januari 2023 enkele eenvoudige wiskundeproblemen voor.

![chatGPT4](https://user-images.githubusercontent.com/48352335/219006272-e7133530-dada-41fc-bdc3-56d11edf657c.png)

![chatGPT8](https://user-images.githubusercontent.com/48352335/219006462-f785ffde-3a8d-43ad-9d62-b2820759f564.png)

![chatGPT5](https://user-images.githubusercontent.com/48352335/219008795-341ca7d6-3618-4df4-bb31-b9322e161412.png)

Dat lukt vrij goed. Maar …

![chatGPT10](https://user-images.githubusercontent.com/48352335/219007403-91ded600-e047-47ac-a67e-1f4789711e64.png)

ChatGPT slaagt er in heel overtuigend te klinken en tegelijkertijd je reinste onzin te verkopen.

> Opdracht voor de leerlingen: Stel een vraag aan ChatGPT over iets waar je zelf goed van op de hoogte bent. Slaag je erin ChatGPT te laten hallucineren?

Het was geheel te verwachten dat het geen goed idee is om ChatGPT wiskundige problemen voor te schotelen, aangezien het een taalmodel is. Daaruit concluderen dat ChatGPT dus enkel een bezorgdheid is voor taalleerkrachten, gaat volledig voorbij aan het feit dat er nog andere online systemen bestaan, zoals Wolfram Alpha, dat door de integratie van natural language processing (NLP) ook heel gebruiksvriendelijk is. 

![wolframparabool](https://user-images.githubusercontent.com/48352335/219007607-b1fae969-6397-4809-aaa7-062da8257b3b.png)

En op 9 februari 2023 stelden we nog eens dezelfde vraag:

![chatGPT57](https://user-images.githubusercontent.com/48352335/219008152-c699566e-267c-4400-96c9-1f8bc8bc3b34.png)

![chatGPT58](https://user-images.githubusercontent.com/48352335/219008277-9d2b013c-cbc1-471c-8442-1d0151b68556.png)

Handig is dat ChatGPT kan teruggrijpen naar eerdere elementen in de conversatie.

Op 15 februari 2023:
![chatGPT59](https://user-images.githubusercontent.com/48352335/219008359-9e83a2cc-00a4-48ca-ae35-1bd9eb4b57b3.png)

> Opdracht voor de leerlingen:
> Geef twee mogelijke antwoorden van ChatGPT op een vraag en laat ze vergelijken, omschrijven waar ze al dan niet mee akkoord gaan, en beargumenteren.
>  ![olympiadedemorgen](https://user-images.githubusercontent.com/48352335/219009371-3ba22ee8-0758-438c-a226-bc31fcb4e594.jpg)  (Bron: De morgen, februari 2023)
>  ![chatGPT61](https://user-images.githubusercontent.com/48352335/219009417-82648574-ad36-4b85-ba2d-58aef62e7066.png)
