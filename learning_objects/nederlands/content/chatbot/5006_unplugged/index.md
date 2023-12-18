---
hruid: cb5_unplugged6
version: 3
language: nl
title: "Werking lerende chatbots"
description: "Werking lerende chatbots"
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

# Hoe werkt een lerende chatbot?

De werking van lerende chatbots wordt [hier](https://dwengo.org/backend/api/learningObject/getWrapped?hruid=cb_chatbot3&version=3&language=nl) uitgelegd. Via *embeddings* wordt tekst omgezet naar vectoren. 

Onthoud: <br>
* Semantisch verwante teksten worden dicht bij elkaar in de vectorruimte geplaatst. Bijvoorbeeld, omdat de woorden ‘kat’ en ‘hond’ in teksten vaak samen voorkomen met het woord ‘dierenarts’, kan men de overeenkomstige drie vectoren dicht bij elkaar vinden in de vectorruimte.
* Ook vergelijkbare relaties tussen woorden zijn in de vectorruimte vaak terug te vinden. Vergelijkbare relaties tussen elementen kunnen voorgesteld worden door een gelijke positie tussen de elementen.

De lerende chatbot zal woorden die dicht bij elkaar liggen, gebruiken om zinnen mee te maken. 

*Voordat de leerlingen aan de oefeningen beginnen, kan je best deze werking eens met hen bespreken.* <br>
*Na de oefeningen kan je nog eens op de werking terugkomen. Je kan ook een spellingscorrector vermelden. Als bv. een woord in Word onderlijnd wordt met een rode krullijn, dan kan je suggesties opvragen om het woord te corrigeren. Kunnen leerlingen vertellen hoe het systeem die suggesties mogelijk bepaalt?* 

### Opdracht 1

*Deze opdracht gebruikt kenmerken van de strip 'Jommeke'.*<br>
*Misschien kennen je leerlingen 'Jommeke' niet.* <br>
* *Je kan dan bv. een of twee pagina's uit een Jommekestrip met de leerlingen lezen om ze te laten kennismaken met de personages.*
* *Of je kan polsen welke strips ze wel lezen en de oefening aanpassen aan de kenmerken van een andere strip.* 

Bekijk het eerste schema. Lees de tekst die ChatGPT schreef en die hoort bij het eerste schema.

![jommekeveld](https://github.com/dwengovzw/learning_content/assets/48352335/8daa9a5d-3886-4799-813e-10a64213fa2c)

![jommeke](https://github.com/dwengovzw/learning_content/assets/48352335/9bc4010f-459d-4010-96cb-a1ade5050ca0)

### Opdracht 2

Bekijk nu het tweede schema. Welke tekst zou ChatGPT kunnen schrijven bij dit schema? 

![emiliaveld](https://github.com/dwengovzw/learning_content/assets/48352335/25fcec34-9d31-4fc3-92c3-2835edec7f36)

[werkblad](embed/werkbladwieisemilia.pdf)

*Mogelijk antwoord:*<br>
*Emilia is een tekenfilm door tekenaar Kobe Devries. Ze heeft een zeehond en haar beste vriend is Arsène.* 


### Opdracht 3

Lees de woorden in het veld.

Leg de kaartjes in het veld. Hoe dichter woorden bij elkaar horen, hoe dichter je ze bij elkaar plaatst. Er zijn meerdere antwoorden goed. Misschien bedacht je wel een unieke oplossing voor dit probleem!

![veld](https://github.com/dwengovzw/learning_content/assets/48352335/953abce7-119a-4ca2-a7d2-382caccac749)

*Een voorbeeldoplossing (er zijn meerdere oplossingen):*<br>
![ingevuldveld](https://github.com/dwengovzw/learning_content/assets/48352335/dad2251d-ce91-4ea0-bad8-42f8e1bcd714)<br>


### Opdracht 4

*Deze opdracht gaat over de 'Suske en Wiske'-strips.*<br> 
*Misschien kennen je leerlingen 'Suske en Wiske' niet. Breng enkele 'Suske en Wiskes' mee, dan zien de leerlingen snel wat er niet klopt.*

Lees de tekst over Suske en Wiske.

![vectorensuskewiske](https://github.com/dwengovzw/learning_content/assets/48352335/5a054655-f848-490e-9b03-33bb2479562b)

Merk je iets vreemds op in deze tekst?

*Wiske heeft geen blauwe strik, maar een rode. Heeft Lambik wel een snor?*<br>
*Lerende chatbots durven dus heel wat te verzinnen!*
*Regelgebaseerde chatbots doen dat niet.*

