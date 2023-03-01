---
hruid: cb_chatbot4
version: 3
language: nl
title: "ChatGPT en co"
description: "ChatGPT en co"
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

# ChatGPT en co

## Toegankelijk
De gebruikersinterface van ChatGPT oogt eenvoudig en is van dezelfde aard als chatten in een app zoals WhatsApp of Signal. De gebruiksvriendelijkheid van ChatGPT heeft ervoor gezorgd dat het systeem toegang kreeg tot het grote publiek. <br>
De technologie is echter niet splinternieuw. ChatGPT is ontstaan uit GPT-3.5, een opvolger van GPT-3. GPT-3 bestaat al 2 jaar en tal van toepassingen om bv. gedichten en blogs te genereren (met GPT-3) staan al geruime tijd op het web. Aan de hand van ChatGPT ontdekte het grote publiek de opportuniteiten van deze AI-systemen die eigenlijk al geruime tijd in gebruik zijn, en tegelijkertijd kwamen de bezorgdheden naar boven. 

> Microsoft integreert ChatGPT in zijn zoekmachine Bing.

## Citizen science
Eigenlijk voert OpenAI momenteel een enorm burgerwetenschapsproject uit met ChatGPT. Het systeem wordt op een ongekend grote schaal getest vanaf week één van de lancering. Men spreekt van 1 miljoen gebruikers in de eerste week 1 en van 100 miljoen in januari. De ontwikkelaars bij OpenAI gebruiken de input van de gebruikers om het systeem te verbeteren. De leeftijdsgrens van 18 jaar, vooropgesteld door OpenAI, wordt niet gerespecteerd en sommigen maken zich dan ook *zorgen over het gebruik van de chatbot door minderjarigen*.

## Soortgelijke chatbots
ChatGPT is niet de enige in zijn soort. Een andere chatbot is ChatSonic waar je ook aan kunt vragen om beelden te genereren. Binnenkort komt Google met Bard, een broertje van ChatGPT. Bard zal wel beschikken over recente informatie omdat Bard het world wide web kan raadplegen.
Ook met de chatbot Claude wordt geëxperimenteerd. Deze werd ontwikkeld door ex-werknemers van OpenAI. En zo zijn/komen er ongetwijfeld nog.

## ChatGPT 
Om tot ChatGPT te komen heeft OpenAI eerst het groot taalmodel GPT-3 gefinetuned tot InstructGPT (of **GPT-3.5**). Dit om beter aan de verwachtingen van de gebruiker en de menselijke waarden te beantwoorden, en om de uitvoer meer waarheidsgetrouw te maken. <br>
Ze gebruikten daarvoor een techniek genaamd ***reinforcement learning from human feedback (RLHF)***, versterkend leren via menselijke feedback.
Tot slot werd een GPT-3.5 model waarvan de training gefinaliseerd werd begin 2022, nogmaals verbeterd om te komen tot ChatGPT.

**Hoe ging dit alles in zijn werk?**
- De oorspronkelijke dataset werd vermengd met conversaties die opgemaakt werden door mensen, weliswaar geïnspireerd door antwoorden die door het AI-model werden gegenereerd. Deze dataset werd dan omgevormd naar een *dialoogformaat*. Mensen hebben aangegeven of de gegenereerde antwoorden voldeden en hebben suggesties gedaan om de antwoorden beter te maken. 
- Daarna *rangschikten* mensen meerdere gegenereerde antwoorden op eenzelfde prompt van slechte naar goede kwaliteit. 
- Met deze data werd een model gemaakt dat met een *score* kan aangeven hoe goed een bepaald antwoord op een prompt is. Dat model geeft aan een gegenereerd antwoord een score. 
- Vervolgens wordt dat scoremodel gebruikt om het genereren van antwoorden op prompts te verbeteren. Via *versterkend leren*, reinforcement learning, werd ChatGPT getraind opdat het ‘het meest menselijke’ antwoord zou geven op prompts. Het model kreeg een beloning voor een goed antwoord en werd gestraft bij een slecht antwoord.
- Daarnaast heeft OpenAI er veel aan gedaan om te vermijden dat ChatGPT racistische of seksistische teksten, of teksten die aanzetten tot haat zou gaan genereren. Hiervoor heeft men echter *schaduwwerkers* gebruikt, in dit geval onderbetaalde Kenianen die getraumatiseerd raakten door wat ze te lezen kregen. (Bron: https://time.com/6247678/openai-chatgpt-kenya-workers/)

ChatGPT is minder krachtig  dan GPT-3, want GPT-3 kan ook nog andere dingen naast tekst genereren op basis van een prompt, bv. op basis van een afbeelding een classificatie doen.

ChatGPT heeft (vooralsnog) geen toegang tot het wereldwijde web en beschikt dus niet over de laatste informatie. OpenAI waarschuwt ervoor dat de antwoorden van ChatGPT niet betrouwbaar zijn en steeds kritisch moeten worden benaderd.

ChatGPT genereert tekst. ChatGPT verzint ook van alles. Men noemt dit **hallucineren**.

> Voorbeeld: ChatGPT schaakt tegen de schaakcomputer Stockfish. Na elke zet van ChatGPT wordt de nieuwe bordtoestand doorgegeven aan de schaakcomputer, die dan telkens de volgende zet berekent vertrekkende van de stukken op het bord.<br>
>![Schaakspel](https://user-images.githubusercontent.com/48352335/222217014-26aa20df-f29a-485c-a4b2-a4ef4259ab39.gif)<br>
> De dialoog tussen ChatGPT en de schaakcomputer: https://pastebin.com/X6kBRTa9
> Hieruit blijkt dat ChatGPT niet kan schaken; logisch, want het is een taalmodel. Zo doet hij bv. onmogelijke zetten en maakt stukken bij. De theorie van het schaakspel is veelvuldig te vinden op het world wide web, waardoor ChatGPT bij de eerste zetten de indruk wekt dat hij kan schaken, maar hij gaat algauw de mist in.   
> (Bron: https://www.reddit.com/r/AnarchyChess/comments/10ydnbb/i_placed_stockfish_white_against_chatgpt_black/) 


