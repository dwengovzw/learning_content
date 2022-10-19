---
hruid: PN_InleidingSA-v1
version: 3
language: nl
title: "Inleiding"
description: "Inleiding"
keywords: ["voorbeeld", "voorbeeld2"]
educational_goals: [
    {source: Source, id: id}, 
    {source: Source2, id: id2}
]
copyright: Copyright by Jerro
licence: Licenced by Jerro
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
---

# Inleiding

Als onderzoekers aan de slag gaan met teksten op sociale media, gaan ze vaak op zoek naar informatie die expliciet en impliciet in die teksten staat. Door de opmars van de sociale media en het feit dat de posts vol staan met sentiment en opinies, ontstond spontaan de wetenschappelijke discipline van sentimentanalyse. Socialemediaposts dienen immers vooral om opinies en indrukken te delen. Het grondig analyseren van sociale media is dus eigenlijk onmogelijk zonder sentimentanalyse.  
Men gaat met behulp van computers op zoek naar gevoelens en opinies, meestal in content zoals klantenreviews, tweets en blogs, veelal op sociale media. 

![](embed/resto.png "Post Resto")
<sub>Bron: UGent - LT³</sub>

Naast expliciete opinies en gevoelens kan ook informatie uit een tekst worden gehaald die er niet letterlijk in staat. Is een klant tevreden over een bepaald product? Gaat de auteur van een tweet akkoord met een bepaalde politieke stellingname? 

In menselijke relaties en activiteiten spelen opinies een belangrijke rol, dus de sentimentanalyse beslaat een groot toepassingsgebied: gezondheid, toerisme, horeca, retail, sociale evenementen, financiële diensten, politieke verkiezingen... Door in te zetten op sentimentanalyse poogt men bijvoorbeeld een ranking van producten te maken, het succes van een film in te schatten, een verkiezingsuitslag of de evoluties op de beurs te voorspellen.

Automatische sentimentanalyse gebeurt met een artificieel intelligent systeem. Zo'n AI_systeem wordt ontwikkeld door het programmeren van algoritmes waarin expertenkennis vervat is (de kennisgebaseerde systemen) of a.d.h.v. lerende algoritmes (datagebaseerde systemen).  
Voor meer uitleg kan je terecht in hoofdstuk 1 van [chatbot](embed/Chatbot_handleiding_eerstedruk.pdf "chatbot handleiding").

Je gaat zelf aan de slag met notebooks voor de automatische detectie van het sentiment van online reviews. Om dit te kunnen doen, maak je in enkele voorbereidende notebooks eerst kennis met de gebruikte technieken. Fundamentele begrippen van machinaal leren komen bij sentimentanalyse aan bod.