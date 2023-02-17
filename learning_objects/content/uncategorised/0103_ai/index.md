---
hruid: un_ai3
version: 3
language: nl
title: "ML en DL"
description: "ML en DL"
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

# Machine learning en deep learning

## Machine learning
Machinaal leren (ML) is een populair en succesvol onderdeel van de artificiële intelligentie. Bij *machine learning* gaat men vooral proefondervindelijk te werk, maar op een wiskundig onderbouwde manier, en gebruikmakend van principes uit de wiskundige statistiek (Chollet, 2018). 

**Een machine learning-systeem verwerft met lerende algoritmes kennis uit data met de bedoeling uitkomsten te kunnen voorspellen betreffende nieuwe data.** 

- De nieuwe data moeten wel gelijkaardig zijn aan de aangeboden data. 
- Deze voorspellingen worden gedaan met een bepaalde zekerheid. Zulke ML-modellen zullen dus nooit honderd procent accuraat zijn.

<div class="alert alert-box alert-success">
    Lerende algoritmes zijn algoritmes waarbij het ML-systeem zelf gaandeweg aanpassingen doet aan de aanwezige parameters tijdens het leerproces, om geleidelijk aan te komen tot betere prestaties. 
</div>

> Een ML-systeem neemt zijn beslissingen dus niet op basis van vooraf in detail geprogrammeerde instructies. 

<div class="alert alert-box alert-success">
    Het voorspellen gebaseerd op tendensen is een <b>regressieprobleem</b>.<br> 
    Het voorspellen van een klasse is een <b>classificatieprobleem</b>. <br>
    Voorspellen betekent bijvoorbeeld dat er uit voorbije tendensen cijfers voor de toekomst gegenereerd worden (regressie) of dat een object bij een bepaalde categorie (klasse genoemd) wordt ingedeeld (classificatie).
</div>

> In plaats van categorieën spreekt men in deze context eerder van klassen.
 
> **Concrete voorbeelden van regressie:** <br>
> de prijs van een appartement voorspellen of beslissen (gebaseerd op de prijzen van apapartemenen die reeds verkocht zijn);<br>
> uit het zeeniveau van de voorbije decennia in Oostende, het zeeniveau van de komende jaren afleiden. <br>
> **Concrete voorbeelden van classificatie:** <br>
> bepalen of een e-mail al dan niet spam is; <br>
> van een foto kunnen zeggen of er al dan niet een huidmondje op staat.

![Regressie](https://user-images.githubusercontent.com/48352335/218816712-9bd35fc3-2949-466e-bb4f-a94502781212.png)
<center>Regressie</center>

![classificatie](https://user-images.githubusercontent.com/48352335/218816762-3c171896-6129-4379-b6cc-ed4c986cb8cb.png)
<center>Classificatie</center>

## Deep learning
Binnen het machinaal leren bekleedt ***deep learning (DL)*** een prominente plaats. DL heeft een revolutie veroorzaakt in het veld van ML door opmerkelijke resultaten te boeken op het vlak van spraak- en beeldherkenning, wat vaardigheden zijn waarvan de computer de menselijke prestaties tot op vandaag moeilijk kan evenaren. DL speelt behalve in de spraakherkenning ook een grote rol in andere domeinen van taaltechnologie.

> **Voorbeeld:**<br>
> Stel dat men een spamfilter wilt trainen. Een spamfilter moet e-mails die spam zijn leren onderscheiden van e-mails die geen spam zijn.
> Zo’n ML-systeem wordt getraind aan de hand van een zogenaamde gelabelde trainingset: een groot aantal e-mails waarbij vermeld wordt of ze spam zijn of niet. 
> Na de training heeft men een model ter beschikking om nieuwe e-mails te beoordelen als zijnde spam of geen spam (zie Figuur). Dit model zal niet perfect zijn. Er zullen nog steeds spam e-mails door de mazen van het net glippen en sommige e-mails zullen onjuist in het spam postvak terechtkomen.

<div class="alert alert-box alert-success">
    Hoe verloopt zo’n <b>training</b>?<br> 
    Bij het begin van de training kiest het algoritme <em>willekeurige waarden voor de parameters</em> van het systeem. Het is dus niet verwonderlijk dat het netwerk initieel niet goed presteert. Gedurende de training <em>past het algoritme de waarden van de parameters aan</em>, gebaseerd op de gelabelde voorbeelden, en verbeteren de resultaten. 
</div>

![spamfilter](https://user-images.githubusercontent.com/48352335/218816429-8a97d94c-df23-4236-9b01-c82486ee2ec3.png)
    <center>Spamfilter</center>
    
Er zijn dus deep learning modellen voor taken zoals regressie en classificatie.<br>
De **convolutionele diepe neurale netwerken** zijn uitermate geschikt om objecten te herkennen.

> De convolutie is een wiskundige bewerking die enkel gebruikmaakt van optellen en vermenigvuldigen. Het komt erop neer dat men aan een pixel een bepaald gewicht geeft en men daaraan gewogen waarden van de omliggende pixels toevoegt.

Met convoluties kan men op zoek gaan naar verschillende kenmerken in een afbeelding. Men kan er bv. verticale en horizontale lijnen mee detecteren, ruis
in een beeld mee verminderen of het contrast in een beeld verzachten. In elke laag van het convolutionele neuraal netwerk wordt de representatie van de gegevens door de convoluties getransformeerd in een nieuwe representatie van de gegevens.

![image](https://user-images.githubusercontent.com/48352335/218817526-07143a54-056e-494d-9c35-d23894abe2a3.png)

### Model voor objectherkenning vs generatief model

- Een **model voor objectherkenning**, een classificatiemodel dus, zal aan een bepaalde afbeelding een label toekennen, bv. hond. Een classificatiemodel dat een label voorspelt, zal kijken van welk label het het meest zeker is voor een gegeven afbeelding. <br>
- Een model dat afbeeldingen genereert, een **generatief model** dus, zal een afbeelding genereren die beantwoordt aan een gegeven label. Als zo’n model geleerd heeft wat de kenmerken zijn van een hond, dan kan het een afbeelding van een hond genereren die niet in de trainingsset zit. Een generatief model zal kijken van welke afbeelding het het meest zeker is voor het gegeven label. 

> Achterliggende wiskunde: om een klasse te voorspellen wordt P(Y|X=x) berekend  en om iets te genereren P(X| Y=y). 
(https://en.wikipedia.org/wiki/Generative_model)

> **voorbeelden** van generatieve modellen zijn DALL·E 2, dat afbeeldingen genereert, en ChatGPT, een groot taalmodel (*large language model*, LLM).

<div class="alert alert-box alert-warning">
    Murray Shanahan zegt dat we goed moeten beseffen wat een groot taalmodel doet.<br> 
    "Veronderstel dat we de volgende prompt geven aan een LLM: “The first person to walk on the Moon was ”,  en stel dat het antwoordt met “Neil Armstrong”.<br>
    Wat vragen we hier eigenlijk? Het is belangrijk om in te zien dat we eigenlijk niet vragen wie de eerste persoon was die op de maan wandelde. De vraag die we echt stellen aan het model is de volgende vraag:  Gegeven de statistische verdeling van de woorden in de zeer uitgebreide publieke corpus van (Engelse) tekst, welke woorden volgen er het meest waarschijnlijk op de reeks “The first person to walk on the Moon was ”? Een goed antwoord op deze vraag is “Neil Armstrong.”  (Bron: Talking About Large Language Models, Murray Shanahan, 2022)
    </div>

## Supervised, unsupervised en reinforcement learning

Binnen ML onderscheidt men verschillende types van leren: supervised, unsupervised, en reinforcement learning.<br>
- Bij **supervised learning** leert het systeem uit een dataset waarbij elk gegeven bestaat uit twee componenten: een input gekoppeld aan een *label* (de verwachte output). Het labelen van de voorbeelden gebeurt vaak manueel door mensen, men noemt dat *annoteren*. Het systeem voert een algoritme uit dat er geleidelijk aan voor zorgt dat het systeem focust op relevante patronen in de data. 
- Bij **unsupervised learning** bevat de dataset *geen labels*. Het AI-systeem moet op zoek naar kenmerken bij de verschillende voorbeelden en moet ze zo, door het ontdekken van patronen, verdelen in klassen. Men kan het systeem bv. ongelabelde foto’s aanbieden van appels en peren. Het systeem gaat op zoek naar patronen om zo het onderscheid tussen de twee soorten fruit te kunnen maken (zie Figuur). 
![kenmerken](https://user-images.githubusercontent.com/48352335/218817259-180b1517-c345-403d-9db5-4360373c7ed8.png)
- Bij **reinforcement learning** streeft het AI-systeem naar een *beloning*. Om bv. goed te worden in een bepaalde videogame, gaat het AI-systeem het spel heel veel spelen en daaruit leren welke acties het beter vermijdt en welke het best onderneemt om te kunnen winnen. Zo werd Google DeepMind’s AlphaGo Zero in 2017 via reinforcement learning een topspeler in go, nog beter dan AlphaGo die de beste menselijke speler eerder al versloeg.
