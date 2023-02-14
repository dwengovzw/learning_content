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
teacher_exclusive: false
---

# Machine learning en deep learning

Machine learning (ML) is een populair en succesvol onderdeel van de artificiële intelligentie. Bij machine learning gaat men vooral proefondervindelijk te werk, maar op een wiskundig onderbouwde manier, en gebruikmakend van principes uit de wiskundige statistiek (Chollet, 2018). Een machine learning-systeem verwerft met lerende algoritmes kennis uit data met de bedoeling uitkomsten te kunnen voorspellen betreffende nieuwe data. De nieuwe data moeten wel gelijkaardig zijn aan de aangeboden data. Deze voorspellingen worden gedaan met een bepaalde zekerheid. Zulke ML-modellen zullen dus nooit honderd procent accuraat zijn.

> Lerende algoritmes zijn algoritmes waarbij het ML-systeem zelf gaandeweg aanpassingen doet aan de aanwezige parameters tijdens het leerproces, om geleidelijk aan te komen tot betere prestaties. 

Een ML-systeem neemt zijn beslissingen dus niet op basis van vooraf in detail geprogrammeerde instructies.

Voorspellen betekent bijvoorbeeld dat er uit voorbije tendensen cijfers voor de toekomst gegenereerd worden of dat een object bij een bepaalde categorie (klasse genoemd) wordt ingedeeld. 

>In plaats van categorieën spreekt men in deze context eerder van klassen. 

>Het voorspellen gebaseerd op tendensen is een regressieprobleem. Het voorspellen van een klasse is een classificatieprobleem. Voorbeelden: de prijs van een appartement voorspellen of beslissen of een e-mail al dan niet spam is.

Binnen het machinaal leren bekleedt deep learning (DL) een prominente plaats (zie Figuur 1.1). DL heeft een revolutie veroorzaakt in het veld van ML door opmerkelijke resultaten te boeken op het vlak van spraak- en beeldherkenning, wat vaardigheden zijn waarvan de computer de menselijke prestaties tot op vandaag moeilijk kan evenaren. DL speelt behalve in de spraakherkenning ook een grote rol in andere domeinen van taaltechnologie.

Convolutionele neurale netwerken



> **Voorbeeld:**<br>
> Stel dat men een spamfilter wilt trainen. Een spamfilter moet e-mails die spam zijn leren onderscheiden van e-mails die geen spam zijn. Zo’n ML-systeem wordt getraind aan de hand van een zogenaamde gelabelde trainingset: een groot aantal e-mails waarbij vermeld wordt of ze spam zijn of niet. Na de training heeft men een model ter beschikking om nieuwe e-mails te beoordelen als zijnde spam of geen spam (zie Figuur 1.5). Dit model zal niet perfect zijn. Er zullen nog steeds spam e-mails door de mazen van het net glippen en sommige e-mails zullen onjuist in het spam postvak terechtkomen
Hoe verloopt zo’n training? Bij het begin van de training kiest het algoritme willekeurige waarden voor de parameters van het systeem. Het is dus niet verwonderlijk dat het netwerk initieel niet goed presteert. Gedurende de training past het In de figuren stellen de kruisjes spam voor en de bolletjes e-mails die geen spam zijn. algoritme de waarden van de parameters aan, gebaseerd op de gelabelde voorbeelden, en verbeteren de resultaten. 

Er zijn dus deep learning modellen voor taken zoals regressie en classificatie. Een model voor objectherkenning, een classificatiemodel dus, zal aan een bepaalde afbeelding een label toekennen, bv. hond. Een model dat afbeeldingen genereert, een **generatief model** dus, zal een afbeelding genereren die beantwoordt aan een gegeven label. Als zo’n model geleerd heeft wat de kenmerken zijn van een hond, dan kan die een afbeelding van een hond genereren die niet in de trainingsset zit.   
Een generatief model zal kijken van welke afbeelding het het meest zeker is voor het gegeven label. Een classificatiemodel dat een label voorspelt, zal kijken van welk label het het meest zeker is voor een gegeven afbeelding. 

> Achterliggende wiskunde: om een klasse te voorspellen wordt P(Y|X=x) berekend  en om iets te genereren P(X| Y=y). 
(https://en.wikipedia.org/wiki/Generative_model)

> Voorbeeld: 
Suppose we give an LLM the prompt “The first person to walk on the Moon was ”, and suppose it responds with “Neil Armstrong”. What are we really asking here? In an important sense, we are not really asking who was the first person to walk on the Moon. What we are really asking the model is the following question: Given the statistical distribution of words in the vast public corpus of (English) text, what words are most likely to follow the sequence “The first person to walk on the Moon was ”?  A good reply to this question is “Neil Armstrong.”  Bron: Talking About Large Language Models, Murray Shanahan

**Regressie en classificatie**<br>
Bij regressie is het de bedoeling dat het ML-model een kromme of een oppervlak bepaalt dat het best bij de gegeven punten past. Eens deze kromme of dit oppervlak gekend is, kan het model voorspellingen doen naar uitkomsten bij nieuwe data. Bv. uit het zeeniveau van de voorbije decennia in Oostende, het zeeniveau van de komende jaren afleiden. Figuur 6.1: Regressie. Figuur 6.2: Classificatie. Bij classificatie zijn er verschillende klassen waartoe de data kunnen behoren. Het is de bedoeling dat het ML-model van nieuwe data kan bepalen tot welke klasse ze behoren. Bv. van een foto kunnen zeggen of er al dan niet een huidmondje op staat.

**Supervised, unsupervised en reinforcement learning**<br>
Binnen ML onderscheidt men verschillende types van leren: supervised, unsupervised, en reinforcement learning.
 Bij supervised learning leert het systeem uit een dataset waarbij elk gegeven bestaat uit twee componenten: een input gekoppeld aan een label (de verwachte output). Het labelen van de voorbeelden gebeurt vaak manueel door mensen, men noemt dat annoteren. Het systeem voert een algoritme uit dat er geleidelijk aan voor zorgt dat het systeem focust op relevante patronen in de data. 
Bij unsupervised learning bevat de dataset geen labels. Het AI-systeem moet op zoek naar kenmerken bij de verschillende voorbeelden en moet ze zo, door het ontdekken van patronen, verdelen in klassen. Men kan het systeem bv. ongelabelde foto’s aanbieden van appels en peren. Het systeem gaat op zoek naar patronen om zo het onderscheid tussen de twee soorten fruit te kunnen maken (zie Figuur 6.3). 

Bij reinforcement learning streeft het AI-systeem naar een beloning. Om bv. goed te worden in een bepaalde videogame, gaat het AI-systeem het spel heel veel spelen en daaruit leren welke acties het beter vermijdt en welke het best onderneemt om te kunnen winnen. Zo werd Google DeepMind’s AlphaGo Zero in 2017 via reinforcement learning een topspeler in go, nog beter dan AlphaGo die de beste menselijke speler eerder al versloeg.


