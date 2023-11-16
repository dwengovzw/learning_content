---
hruid: un_ai4
version: 3
language: nl
title: "Deep learning"
description: "DL"
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

# Deep learning

Binnen het machinaal leren bekleedt ***deep learning (DL)*** een prominente plaats. DL heeft een revolutie veroorzaakt in het veld van ML door opmerkelijke resultaten te boeken op het vlak van spraak- en beeldherkenning, die vaardigheden zijn waarvan de computer de menselijke prestaties tot op vandaag moeilijk kan evenaren. DL speelt behalve in de spraakherkenning ook een grote rol in andere domeinen van taaltechnologie.

> **Voorbeeld:**<br>
> Stel dat men een spamfilter wilt trainen. Een spamfilter moet e-mails die spam zijn, leren onderscheiden van e-mails die geen spam zijn.
> Zo’n ML-systeem wordt getraind aan de hand van een zogenaamde gelabelde trainingset: een groot aantal e-mails waarbij vermeld wordt of ze spam zijn of niet. 
> Na de training heeft men een model ter beschikking om nieuwe e-mails te beoordelen als zijnde spam of geen spam (zie Figuur). Dit model zal niet perfect zijn. Er zullen nog steeds spam e-mails door de mazen van het net glippen en sommige e-mails zullen onjuist in het spampostvak terechtkomen.

<div class="alert alert-box alert-success">
    Hoe verloopt zo’n <b>training</b>?<br> 
    Bij het begin van de training kiest het algoritme <em>willekeurige waarden voor de parameters</em> van het systeem. Het is dus niet verwonderlijk dat het netwerk initieel niet goed presteert. Gedurende de training <em>past het algoritme de waarden van de parameters aan</em>, gebaseerd op de gelabelde voorbeelden, en verbeteren de resultaten. 
</div>

![spamfilter](https://user-images.githubusercontent.com/48352335/218816429-8a97d94c-df23-4236-9b01-c82486ee2ec3.png)
    <center>Spamfilter</center>
    
Er zijn dus deep learning-modellen voor taken zoals regressie en classificatie.<br>
De **convolutionele diepe neurale netwerken** zijn uitermate geschikt om objecten te herkennen.

### Convolutionele neurale netwerken

> De convolutie is een wiskundige bewerking die enkel gebruikmaakt van optellen en vermenigvuldigen. Het komt erop neer dat men aan een pixel een bepaald gewicht geeft en men daaraan gewogen waarden van de omliggende pixels toevoegt.

Met convoluties kan men op zoek gaan naar verschillende kenmerken in een afbeelding. Men kan er bv. verticale en horizontale lijnen mee detecteren, ruis
in een beeld mee verminderen of het contrast in een beeld verzachten. In elke laag van het convolutionele neurale netwerk wordt de representatie van de gegevens door de convoluties getransformeerd in een nieuwe representatie van de gegevens.

![Doel convoluties](embed/convolutiedoel.png "Doel convoluties")

In het leerpad [Deep learning - basis](https://dwengo.org/learning-path.html?hruid=kiks3_dl_basis&language=nl&te=true&source_page=%2Fkiks%2F&source_title=%20KIKS#kiks_inleiding;nl;3) van het project KIKS kan je experimenteren met convoluties. In het leerpad [Deep learning - gevorderd](https://dwengo.org/learning-path.html?hruid=kiks4_dl_gevorderd&language=nl&te=true&source_page=%2Fkiks%2F&source_title=%20KIKS#kiks_convolutie_bewerking;nl;3) van het project KIKS kan je je verdiepen in het achterliggende rekenwerk.

### Model voor objectherkenning vs generatief model

- Een **model voor objectherkenning**, een classificatiemodel dus, zal aan een bepaalde afbeelding een label toekennen, bv. hond. Een classificatiemodel dat een label voorspelt, zal kijken van welk label het het meest zeker is voor een gegeven afbeelding. <br>
- Een model dat afbeeldingen genereert, een **generatief model** dus, zal een afbeelding genereren die beantwoordt aan een gegeven label. Als zo’n model geleerd heeft wat de kenmerken zijn van een hond, dan kan het een afbeelding van een hond genereren die niet in de trainingset zit. Een generatief model zal kijken van welke afbeelding het het meest zeker is voor het gegeven label. 

> Achterliggende wiskunde: om een klasse te voorspellen wordt P(Y|X=x) berekend  en om iets te genereren P(X|Y=y). 
(https://en.wikipedia.org/wiki/Generative_model)

> **Voorbeelden** van generatieve modellen zijn DALL·E 2, dat afbeeldingen genereert, en ChatGPT, een groot taalmodel (*large language model*, LLM).

<div class="alert alert-box alert-warning">
    Murray Shanahan zegt dat we goed moeten beseffen wat een groot taalmodel doet.<br> 
    "Veronderstel dat we de volgende prompt geven aan een LLM: “The first person to walk on the moon was ”,  en stel dat het antwoordt met “Neil Armstrong”.<br>
    Wat vragen we hier eigenlijk? Het is belangrijk om in te zien dat we eigenlijk niet vragen wie de eerste persoon was die op de maan wandelde. De vraag die we echt stellen aan het model is de volgende vraag:  Gegeven de statistische verdeling van de woorden in de zeer uitgebreide publieke corpus van (Engelse) tekst, welke woorden volgen er het meest waarschijnlijk op de reeks “The first person to walk on the moon was ”? Een goed antwoord op deze vraag is “Neil Armstrong”.  (Bron: Talking About Large Language Models, Murray Shanahan, 2022)
    </div>
