---
hruid: un_ai2
version: 3
language: nl
title: "Soorten AI"
description: "Soorten AI"
keywords: [""]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [12, 13, 14, 15, 16, 17, 18]
difficulty: 3
return_value: {
    callback_url: callback-url-example,
    callback_schema: {
        att: test,
        att2: test2
    }
}
content_location: example-location
estimated_time: 2
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: true
---

# Soorten AI

## Brede AI, smalle AI en AGI

Hoewel er ongetwijfeld spannende ontwikkelingen zijn op het vlak van AI, staat de kunstmatige intelligentie vooralsnog mijlenver af van menselijke intelligentie. Een mens kan behoorlijk veel bijleren uit een beperkt aantal voorbeelden, omdat hij ook zijn reeds opgedane kennis en vaardigheden benut. Een mens is bovendien zeer flexibel: we zijn in staat ons snel aan te passen aan veranderende omstandigheden en adequaat te reageren op onverwachte gebeurtenissen. Vandaag de dag kan een computer dat niet. Een AI-systeem is gericht op het invullen van een **bepaalde taak** en is maar goed in datgene waarvoor het ontworpen is.

<div class="alert alert-box alert-success">
    <strong>Brede AI, smalle (of enge) AI en AGI</strong><br> 
    Bij smalle AI (<em>narrow AI</em>) gaat het over AI-systemen die de specifieke taken doen waarvoor ze ontworpen werden, bv. een spamfilter. <br>
    Brede AI (<em>general AI</em>) betreft systemen die al meer diverse taken aankunnen, denk bv. aan wat men zich kan voorstellen bij een robotbutler. <br>
    Bij de zogenaamde <em>Artificial General Intelligence</em> (AGI) gaat het over computersystemen met dezelfde capaciteiten als een mens. We hebben vooralsnog niet de kennis om AGI-systemen te ontwerpen. 
</div>

AI zat lang op het niveau van de enge AI, maar momenteel situeren sommige toepassingen zich ergens tussen smalle en brede AI. 

## Kennis- en datagebaseerde systemen

Om AI in te zetten voor een bepaald probleem, wordt informatie over dat probleem aan de computer gegeven. Vervolgens verwerkt het AI-systeem deze informatie en komt er een *output*. 

Eerst moet zo’n AI-systeem ontwikkeld worden door het *programmeren van algoritmes* waarin expertenkennis vervat is, of a.d.h.v. lerende algoritmes (Steels et al., 2017): 

- **Kennisgebaseerde** (of regelgebaseerde) systemen, die met regels worden geprogrammeerd. Dit houdt in dat men de kennis van menselijke experts zoveel mogelijk in regels probeert te gieten. 
- **Datagebaseerde** (of lerende) systemen, die met lerende algoritmes worden geprogrammeerd en ook *machine learning*-systemen worden genoemd. Met statistische methodes worden patronen in relevante data opgespoord en dan gebruikt om nieuwe problemen op te lossen. 

> De chatbot ELIZA en lexicongebaseerde sentimentanalyse zijn voorbeelden van kennisgebaseerde systemen. Meer uitleg hierover vind je in de leerkrachtenhandleiding van het project 'Chatbot' dat gaat over taaltechnologie, meer bepaald in de hoofdstukken Chatbot en Sentimentanalyse. 

> Om het onderscheid te kunnen maken tussen appels en peren zou men kennisgebaseerd al volgt te werk kunnen gaan:<br>
> ![appelpeer](https://user-images.githubusercontent.com/48352335/222241824-c9c43bb2-9f61-4c9c-b02d-2f9afff7b66b.png)<br>
> ![grafiekappelpeer](https://user-images.githubusercontent.com/48352335/222241772-8a2a37b2-4168-4f1b-8bf9-ab6baf23bd1d.png)<br>
> ![aiappelpeer](https://user-images.githubusercontent.com/48352335/222241756-dc5a5c42-d1f6-4b53-8af6-fdf09d395b93.png)

> Gezichtsherkenning op Facebook en Google Translate zijn datagebaseerde systemen.

> Bij kennisgebaseerde systemen bestaat het algoritme uit expliciet geprogrammeerde regels. Men botst daarbij al snel op de grenzen van deze systemen. Voor een autonome wagen zou dat bijvoorbeeld betekenen dat men alle mogelijke scenario’s zou moeten kennen.

![AIMLDL](https://user-images.githubusercontent.com/48352335/218815994-b1befa16-019e-46a3-a29c-f611faeecfd3.png)
<center> Soorten AI</center>

Binnen de ML-systemen vind je de 'deep learning'-systemen.

-------------
#### Bronnen
Steels, L., Berendt, B., Pizurica, Van Dyck, D., A., & Vandewalle, J. (2017). *Artificiële intelligentie. Naar een vierde industriële revolutie?* Brussel: KVAB Standpunt 53.

